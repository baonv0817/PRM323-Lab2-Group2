// Điều khiển prototype Figma bằng Playwright.
// Figma vẽ prototype bằng canvas nên không có nút DOM để bấm: ta tìm khung màn hình trên ảnh chụp
// rồi bấm theo toạ độ vùng bấm (hotspots.json, đọc từ Figma Page 06).
const { expect } = require('@playwright/test');
const { PNG } = require('pngjs');
const data = require('./hotspots.json');

const FILE = 'VnryhnE4z3159vHoKvx6jL';
const PAGE_ID = '1:263'; // Page 06 Prototype

function protoUrl(screen) {
  const id = data.frames[screen].nodeId;
  return `https://www.figma.com/proto/${FILE}/PRM323?page-id=${encodeURIComponent(PAGE_ID)}` +
    `&node-id=${id.replace(':', '-')}&starting-point-node-id=${encodeURIComponent(id)}` +
    `&scaling=${process.env.PROTO_SCALING || 'scale-down'}&hide-ui=1&hotspot-hints=0`; // tắt lớp cam gợi ý vùng bấm của Figma viewer
}

// Tìm hình chữ nhật của khung màn hình (khác màu nền viewer) trên ảnh chụp.
function detectFrame(buf, dpr) {
  const png = PNG.sync.read(buf);
  const { width, height, data: px } = png;
  const at = (x, y) => { const i = (y * width + x) * 4; return [px[i], px[i + 1], px[i + 2]]; };
  const bg = at(2, 2);
  const diff = (c) => Math.abs(c[0] - bg[0]) + Math.abs(c[1] - bg[1]) + Math.abs(c[2] - bg[2]) > 30;
  let x0 = width, x1 = -1, y0 = height, y1 = -1;
  for (let y = 0; y < height; y += 2) for (let x = 0; x < width; x += 2) {
    if (diff(at(x, y))) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
  }
  if (x1 < 0) throw new Error('Không thấy khung prototype trên ảnh chụp (viewer chưa tải xong?)');
  return { x: x0 / dpr, y: y0 / dpr, w: (x1 - x0 + 2) / dpr, h: (y1 - y0 + 2) / dpr };
}

async function waitForFrame(page, dpr, timeout = 45000) {
  const t0 = Date.now(); let last;
  while (Date.now() - t0 < timeout) {
    try {
      const r = detectFrame(await page.screenshot(), dpr);
      if (r.w > 200 && r.h > 400) return r;
    } catch (e) { last = e; }
    await page.waitForTimeout(700);
  }
  throw last || new Error('Prototype không hiện ra trong thời gian chờ');
}

// Mở prototype tại một màn hình bắt đầu.
async function openAt(page, screen) {
  const dpr = (await page.evaluate(() => window.devicePixelRatio)) || 1;
  // Thử lại vài lần nếu mạng chập chờn (ví dụ ERR_NAME_NOT_RESOLVED).
  for (let i = 1; ; i++) {
    try { await page.goto(protoUrl(screen), { waitUntil: 'domcontentloaded', timeout: 45000 }); break; }
    catch (e) { if (i >= 3) throw e; await page.waitForTimeout(3000 * i); }
  }
  await page.waitForTimeout(2500);
  const rect = await waitForFrame(page, dpr);
  return { page, rect, k: rect.w / data.frames[screen].width, dpr, screen };
}

// Bấm một vùng bấm theo tên.
async function tap(ctx, screen, name) {
  const hs = data.frames[screen].hotspots.find((h) => h.name === name);
  if (!hs) throw new Error(`Không có vùng bấm "${name}" ở ${screen}`);
  const x = ctx.rect.x + (hs.x + hs.w / 2) * ctx.k;
  const y = ctx.rect.y + (hs.y + hs.h / 2) * ctx.k;
  await ctx.page.mouse.click(x, y);
  ctx.screen = hs.dest || ctx.screen;
  await ctx.page.waitForTimeout(900); // chờ hiệu ứng chuyển cảnh
  return hs;
}

// So ảnh màn hình hiện tại với ảnh chuẩn (baseline) của bước này.
async function shot(ctx, name, opts = {}) {
  const clip = { x: Math.round(ctx.rect.x), y: Math.round(ctx.rect.y), width: Math.round(ctx.rect.w), height: Math.round(ctx.rect.h) };
  await expect(ctx.page).toHaveScreenshot(`${name}.png`, { clip, maxDiffPixelRatio: 0.04, animations: 'disabled', timeout: 20000, ...opts });
}

module.exports = { data, openAt, tap, shot, protoUrl };
