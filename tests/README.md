# Test tự động prototype Figma (Playwright)

Bước kiểm thử bổ sung ở P4/P5: Playwright mở **prototype Figma thật** (Page 06), bấm theo từng flow và so ảnh từng bước với ảnh chuẩn; thêm một nhóm test đồ thị flow chạy trong vài giây.

> **Không thay usability test với người thật** (G5). Test này chỉ chứng minh prototype *đi đúng đường đã thiết kế*; nó không biết người dùng có hiểu, có làm nhanh hay có vướng không.

## Cài và chạy

Cần Node 20+ và Microsoft Edge (hoặc Chrome) cài sẵn. Không phải tải trình duyệt riêng.

```bash
cd tests
npm install
npm test                 # chạy tất cả (≈ 3 phút; phần bấm prototype cần mạng)
npm run test:graph       # chỉ test đồ thị flow, vài giây, không cần mạng
npm run test:flows       # chỉ bấm prototype Figma
npm run report           # mở báo cáo HTML của lần chạy gần nhất
```

Dùng Chrome thay Edge: đổi `channel: 'msedge'` thành `'chrome'` trong `playwright.config.js`.

## Hai nhóm test

| File | Làm gì | Kiểm cái gì |
|---|---|---|
| `figma-proto/flows.spec.js` | Mở prototype, bấm theo toạ độ vùng bấm, chụp và so với `__screenshots__/` | F1 (2 đường), F2, F3 (2 nhánh), dialog huỷ đơn: mỗi bước phải ra **đúng màn hình**. Bấm sai chỗ hoặc liên kết đổi thì ảnh lệch và test hỏng |
| `figma-proto/graph.spec.js` | Đọc `hotspots.json`, dựng đồ thị màn hình | Không màn cụt; không màn mồ côi (trừ danh sách đã biết); liên kết trỏ đúng màn; đặt đơn ≤ 8 chạm; F3 có lối phục hồi |

## Dữ liệu và ảnh chuẩn

- `figma-proto/hotspots.json`: toạ độ và đích của 40 vùng bấm, **đọc từ Figma Page 06 bằng Figma Plugin API** (20/10/2026). Figma vẽ prototype bằng canvas nên không có nút DOM để bấm; helper tìm khung màn hình trên ảnh chụp rồi bấm theo toạ độ.
- `figma-proto/__screenshots__/`: 20 ảnh chuẩn, mỗi ảnh là một bước của một flow. Tổng quan: [`flow-baselines.png`](flow-baselines.png).
- Link prototype dùng `hotspot-hints=0`; thiếu tham số này viewer vẽ khối cam đè lên màn hình.

## Khi sửa Figma

1. Nếu đổi vùng bấm hoặc liên kết: đọc lại toạ độ và cập nhật `hotspots.json`.
2. `npm run test:flows` → ảnh nào lệch sẽ nằm trong `test-results/` (kèm ảnh khác biệt).
3. Nếu lệch là **chủ ý**: `npm run update`, rồi **mở xem từng ảnh mới** (đúng màn, không khối lạ) trước khi commit. Chạy `update` mà không xem thì test đạt nhưng không chứng minh gì.

## Dùng với Playwright agent CLI (khám phá)

Khi muốn nhờ agent tự đi thử prototype thay vì viết script:

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills -g    # cài skill vào thư mục home, không thêm gì vào repo
```

Rồi nhờ agent: "Dùng playwright-cli mở prototype Figma của BreakBite và đi Flow 1". Vì Figma vẽ bằng canvas, snapshot của CLI không thấy nút; agent phải bấm theo toạ độ trong `hotspots.json`. Script trong thư mục này vẫn là bằng chứng lặp lại được.

## Đo lỗi thiết kế (`audit/`)

Ngoài test flow, `audit/` phục vụ bước phản biện giao diện: `capture.js` chụp từng màn từ prototype, `figma-audit.js` đọc chữ/màu từ Figma, `measure.py` tính tỉ lệ màu và vùng bấm. Kết quả và cách dùng: [`../ai/phan-bien-giao-dien/`](../ai/phan-bien-giao-dien/).

## Prototype v2

`figma-proto/hotspots-v2.json` là vùng bấm của prototype Final UI v2 (Page 03, 58 khung gồm app người bán, đọc từ Figma Plugin API). Kiểm đồ thị flow v2:

```bash
PROTO=v2 npx playwright test graph.spec.js          # bash
$env:PROTO='v2'; npx playwright test graph.spec.js  # PowerShell
python audit/measure.py v2                          # tỉ lệ màu và vùng bấm trên ảnh v2
```

## Giới hạn

- Bấm prototype bằng trình duyệt (`flows.spec.js`) mới chạy trên bản cũ F1–F3 và dialog huỷ; bản v2 mới kiểm đồ thị flow.
- Không đo thời gian dưới 35 giây; số chạm tính từ đồ thị liên kết.
- Không kiểm màn loading ở giữa (S06-LOADING tự chuyển sau 1,2 giây); test chỉ kiểm màn đích.
- Phụ thuộc mạng và giao diện viewer của Figma; viewer đổi giao diện có thể làm ảnh chuẩn lệch.
