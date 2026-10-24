// Kiểm đồ thị flow từ hotspots.json (không mở trình duyệt, chạy trong vài giây).
const { test, expect } = require('@playwright/test');
// PROTO=v2 kiểm prototype Final UI v2 (hotspots-v2.json); mặc định kiểm bản cũ (hotspots.json)
const V2 = process.env.PROTO === 'v2';
const data = require(V2 ? './hotspots-v2.json' : './hotspots.json');

const frames = Object.keys(data.frames);
// cạnh: [từ, đến, số chạm]; 'timeout' tự chuyển (0 chạm); 'close' không đi đâu
const edges = [];
for (const [from, f] of Object.entries(data.frames))
  for (const h of f.hotspots) if (h.dest) edges.push([from, h.dest, h.trigger === 'timeout' ? 0 : 1]);

function reach(starts) {
  const seen = new Set(starts), q = [...starts];
  while (q.length) { const u = q.shift(); for (const [a, b] of edges) if (a === u && !seen.has(b)) { seen.add(b); q.push(b); } }
  return seen;
}
function taps(from, to) { // đường ngắn nhất theo số chạm (0-1 BFS đơn giản)
  const dist = Object.fromEntries(frames.map((f) => [f, Infinity])); dist[from] = 0;
  for (let i = 0; i < frames.length; i++) for (const [a, b, w] of edges) if (dist[a] + w < dist[b]) dist[b] = dist[a] + w;
  return dist[to];
}

test('không có màn hình cụt: mọi màn đều có đường đi tiếp', () => {
  const dead = frames.filter((f) => !edges.some(([a]) => a === f) && !data.frames[f].hotspots.some((h) => h.type === 'back'));
  expect(dead, `Màn không có lối ra: ${dead.join(', ')}`).toEqual([]);
});

// Màn đã biết là chưa có lối vào trong prototype. Khi nối xong thì xoá khỏi danh sách (test sẽ nhắc).
const KNOWN_UNREACHABLE = V2 ? {} : {
  'S08-EMPTY': 'Trạng thái "chưa có đơn" của S08: chưa có liên kết nào dẫn tới, chỉ xem được bằng cách mở trực tiếp.',
};

test('không có màn mồ côi ngoài danh sách đã biết', () => {
  const seen = reach(Object.values(data.startingPoints));
  const orphan = frames.filter((f) => !seen.has(f));
  const unexpected = orphan.filter((f) => !(f in KNOWN_UNREACHABLE));
  for (const f of orphan.filter((f) => f in KNOWN_UNREACHABLE)) {
    test.info().annotations.push({ type: 'đã biết', description: `${f}: ${KNOWN_UNREACHABLE[f]}` });
    console.log(`⚠ ${f} chưa có lối vào — ${KNOWN_UNREACHABLE[f]}`);
  }
  expect(unexpected, `Màn không tới được: ${unexpected.join(', ')}`).toEqual([]);
});

test('danh sách "đã biết" không lỗi thời: các màn trong đó vẫn thật sự không có lối vào', () => {
  const seen = reach(Object.values(data.startingPoints));
  const fixed = Object.keys(KNOWN_UNREACHABLE).filter((f) => seen.has(f));
  expect(fixed, `Đã có lối vào, hãy xoá khỏi KNOWN_UNREACHABLE: ${fixed.join(', ')}`).toEqual([]);
});

test('mọi liên kết trỏ tới một màn có thật', () => {
  const bad = edges.filter(([, b]) => !frames.includes(b));
  expect(bad).toEqual([]);
});

// Đặt đơn thật phải thêm món (S02 → "+" → S02-ADDED → Xem giỏ), qua giỏ hàng, chọn phương thức và xác nhận ở cổng thanh toán.
// Đường tắt bằng biểu tượng giỏ trên Trang chủ hoặc xem lại đơn cũ (S02 → S08 → S07) không tính là đặt đơn.
const ORDER_PATH = V2 ? ['S02', 'S02-ADDED', 'S05', 'S06', 'S06-LOADING', 'S06-GATEWAY', 'S07'] : null;
const orderTaps = (from) => taps(from, 'S06') + taps('S06', 'S07');
function pathTaps(path) {
  return path.slice(1).reduce((sum, to, i) => {
    const e = edges.filter(([a, b]) => a === path[i] && b === to);
    return sum + (e.length ? Math.min(...e.map((x) => x[2])) : Infinity);
  }, 0);
}

test('F1: đặt đơn từ Trang chủ tới Theo dõi đơn (qua thêm món, giỏ, thanh toán, cổng) ≤ 8 chạm (tiêu chí thành công)', () => {
  if (V2) {
    const n = pathTaps(ORDER_PATH);
    console.log(`Đặt đơn ${ORDER_PATH.join(' → ')} = ${n} chạm (Loading tự chuyển, không tính)`);
    expect(Number.isFinite(n), 'đường đặt đơn có liên kết đứt').toBe(true);
    expect(n).toBeGreaterThanOrEqual(5);
    expect(n).toBeLessThanOrEqual(8);
    return;
  }
  const n = orderTaps('S02');
  console.log(`Đặt đơn S02 → S06 → S07 = ${n} chạm; tính cả S01 = ${n + taps('S01', 'S02')} chạm; (đường xem lại đơn cũ S02 → S08 → S07 = ${taps('S02', 'S07')} chạm, không phải đặt đơn)`);
  expect(n).toBeLessThanOrEqual(8);
});

test('v2: nút "+" thêm vào giỏ không nhảy thẳng vào giỏ hàng', () => {
  if (!V2) return;
  const plus = data.frames['S02'].hotspots.filter((h) => h.w === 48 && h.h === 48 && h.x === 283);
  expect(plus.length).toBeGreaterThan(0);
  for (const h of plus) expect(h.dest).toBe('S02-ADDED');
});

test('v2: chọn được 4 phương thức thanh toán, tiền mặt đi thẳng tới đơn trả tại quầy', () => {
  if (!V2) return;
  const keys = ['S06', 'S06-VNPAY', 'S06-CARD', 'S06-CASH'];
  for (const a of keys) for (const b of keys) if (a !== b) expect(edges.some(([x, y]) => x === a && y === b), `${a} → ${b}`).toBe(true);
  expect(edges.some(([x, y]) => x === 'S06-CASH' && y === 'S07-CASH')).toBe(true);
  for (const k of ['S06', 'S06-VNPAY', 'S06-CARD']) expect(edges.some(([x, y]) => x === k && y === 'S06-LOADING')).toBe(true);
});

test('v2: cổng thanh toán có hai kết quả, thành công tới Theo dõi đơn, từ chối tới màn lỗi giữ giỏ', () => {
  if (!V2) return;
  const out = edges.filter(([a]) => a === 'S06-GATEWAY').map(([, b]) => b);
  expect(out).toContain('S07');
  expect(out).toContain('S06-ERR');
  expect(edges.some(([a, b]) => a === 'S06-LOADING' && b === 'S06-GATEWAY')).toBe(true);
});

test('F2: từ Thực đơn tới Thanh toán ≤ 8 chạm', () => {
  expect(taps('S03', 'S06')).toBeLessThanOrEqual(8);
});

test('F3: từ lỗi thanh toán có lối phục hồi tới đơn đã tạo và về giỏ hàng', () => {
  const out = edges.filter(([a]) => a === 'S06-ERR').map(([, b]) => b);
  expect(out).toContain('S07-CASH');
  expect(out).toContain('S05');
});
