// Mã đo chạy trong Figma (Plugin API, ví dụ qua use_figma của Figma MCP hoặc plugin console), CHỈ ĐỌC, không sửa gì.
// Trên Page 06: liệt kê emoji/ký tự dùng làm icon, chữ < 14 px, và tỉ lệ tương phản WCAG của từng chữ
// so với lớp tô nằm trên cùng phía sau nó. Kết quả ngày 20/10/2026 nằm ở 05-P4-ui-design/06-phan-bien-giao-dien/01-bao-cao-do-tu-dong.md.
const page = await figma.getNodeByIdAsync('1:263'); await figma.setCurrentPageAsync(page);
const cols = await figma.variables.getLocalVariableCollectionsAsync();
const V = {}; for (const c of cols) for (const id of c.variableIds) { const v = await figma.variables.getVariableByIdAsync(id); V[v.id] = v.valuesByMode[c.modes[0].modeId]; }
const resolve = (p) => { if (!p || p.type !== 'SOLID' || p.visible === false) return null; const bv = p.boundVariables && p.boundVariables.color; const c = bv ? V[bv.id] : p.color; if (!c || typeof c !== 'object' || !('r' in c)) return null; return { r: c.r, g: c.g, b: c.b, a: p.opacity ?? 1 }; };
const lum = (c) => { const f = (x) => x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
const ratio = (a, b) => { const A = lum(a), B = lum(b); return (Math.max(A, B) + 0.05) / (Math.min(A, B) + 0.05); };
const EMO = /\p{Extended_Pictographic}/u;
const frames = page.children.filter(c => c.type === 'FRAME' && /^S\d/.test(c.name) && !/DIALOG/.test(c.name));
const emoji = [], tiny = {}, low = [];
for (const f of frames) {
  const code = f.name.split(' ·')[0]; const all = f.findAll(() => true);
  const shapes = all.filter(n => n.type !== 'TEXT' && 'fills' in n && n.visible !== false && n.opacity === 1 && n.absoluteBoundingBox && Array.isArray(n.fills) && resolve(n.fills.find(p => p.type === 'SOLID' && p.visible !== false)));
  for (const t of all.filter(n => n.type === 'TEXT' && n.visible !== false)) {
    if (/^(09:41|📶 🔋 100%)$/.test(t.characters)) continue;
    const b = t.absoluteBoundingBox, size = t.fontSize === figma.mixed ? 0 : t.fontSize, txt = t.characters.replace(/\s+/g, ' ');
    if (EMO.test(txt)) emoji.push([code, txt.slice(0, 30), size]);
    if (size && size < 14 && !EMO.test(txt)) (tiny[code] = tiny[code] || []).push(size + ':' + txt.slice(0, 18));
    const cx = b.x + b.width / 2, cy = b.y + b.height / 2; let bg = null;
    for (const s of shapes) { const sb = s.absoluteBoundingBox; if (cx >= sb.x && cx <= sb.x + sb.width && cy >= sb.y && cy <= sb.y + sb.height) { const r = resolve(s.fills.find(p => p.type === 'SOLID' && p.visible !== false)); if (r && r.a >= 0.99) bg = r; } }
    const seg = t.getStyledTextSegments(['fills', 'fontWeight'])[0]; const fg = resolve(seg.fills.find(p => p.type === 'SOLID'));
    if (bg && fg && !EMO.test(txt)) { const r = ratio(fg, bg); const large = size >= 24 || ((seg.fontWeight || 400) >= 700 && size >= 18.66); if (r < (large ? 3 : 4.5)) low.push([code, txt.slice(0, 26), size, Math.round(r * 100) / 100]); }
  }
}
return { emojiTextNodes: emoji.length, emoji, tinyPerFrame: Object.fromEntries(Object.entries(tiny).map(([k, v]) => [k, v.length])), lowContrast: low };
