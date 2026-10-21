// Chụp từng màn hình của prototype Figma (đúng thứ người dùng thấy) để phân tích và đưa cho AI khác phản biện.
// Chạy: node audit/capture.js   (cần mạng; ≈ 3 phút)
const { chromium } = require('@playwright/test');
const fs = require('fs');
const path = require('path');
process.env.PROTO_SCALING = process.env.PROTO_SCALING || 'contain'; // phóng khung lên để ảnh rõ hơn
const { openAt } = require('../figma-proto/helpers');

const SCREENS = ['S01', 'S02', 'S03', 'S04', 'S05', 'S05-EMPTY', 'S05-VOUCHER-ERR', 'S06', 'S06-ERR', 'S07', 'S07-CASH', 'S08', 'S08-EMPTY'];
const OUT = path.join(__dirname, '..', '..', 'ai', 'phan-bien-giao-dien', 'anh');

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const ctx = await browser.newContext({ viewport: { width: 760, height: 1640 }, deviceScaleFactor: 1, locale: 'vi-VN' });
  for (const s of SCREENS) {
    const page = await ctx.newPage();
    try {
      const c = await openAt(page, s);
      await page.waitForTimeout(1500);
      const clip = { x: Math.round(c.rect.x), y: Math.round(c.rect.y), width: Math.round(c.rect.w), height: Math.round(c.rect.h) };
      await page.screenshot({ path: path.join(OUT, `${s}.png`), clip });
      console.log('ok', s, clip.width + 'x' + clip.height);
    } catch (e) { console.log('FAIL', s, e.message.split('\n')[0]); }
    await page.close();
  }
  await browser.close();
})();
