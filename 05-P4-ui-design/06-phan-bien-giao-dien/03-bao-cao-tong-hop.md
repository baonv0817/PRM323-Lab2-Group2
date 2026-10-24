# Báo cáo phản biện giao diện và Final UI

BreakBite · Lab 2 PRM323 · 21/10/2026

## 1. Quy trình

Theo đề Lab 2: AI tìm lỗi giao diện, sinh viên quyết định Accept / Modify / Reject, sửa Figma, rồi ra Final UI.

| Bước | Công cụ | Kết quả |
|---|---|---|
| Chụp 13 màn từ prototype Figma | Playwright (`tests/audit/capture.js`) | [`anh/`](anh/) |
| Đo chữ, màu, tương phản, vùng bấm | Figma Plugin API, `tests/audit/measure.py` | [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md) |
| Phản biện bởi AI khác | Gemini hoặc ChatGPT | [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md) |
| Vẽ lại Final UI v2 | Figma | Page 03 |

Kiểm thử flow bằng Playwright: [`06-P5-kiem-thu-ban-giao/01-playwright-prototype-2026-10-20.md`](../../06-P5-kiem-thu-ban-giao/01-playwright-prototype-2026-10-20.md).

## 2. Lỗi tìm được

| Mã | Lỗi | Số đo (bản cũ) | Mức |
|---|---|---|---|
| A01 | Giao diện quá cam | Cam đậm 5,9% điểm ảnh; khoảng 61% màn là một họ cam–be; không có màu trung tính | Cao |
| A02 | Icon lộn xộn | 98/366 chữ chứa emoji, 30 emoji khác nhau, 59 ký tự chữ dùng làm icon; "thời gian" có hai icon | Cao |
| A03 | Giỏ hàng và thanh toán lặp | S05 và S06 đều chọn phương thức thanh toán | Cao |
| A04 | Vùng bấm nhỏ | 20/39 vùng bấm dưới 48 dp | Cao |
| A05 | Chữ nhỏ | 86 dòng chữ dưới 14 sp; nhãn thanh dưới 10 sp | Cao |
| A06 | Tương phản | `#B45309` trên `#FFE8CC` đạt 4,23:1, ở 8 chỗ | Vừa |
| A07 | S07 | CTA chính sai: "Về trang chủ" là nút cam đặc | Vừa |
| A08 | S02, S03 | Chip đang chọn khác kiểu | Vừa |
| A09 | S01 | Hero rỗng chiếm 1/3 màn; thẻ tính năng trông như nút; link đăng nhập email mâu thuẫn D12 | Vừa |
| A10 | S07 | QR chỉ là ba ô vuông | Thấp |
| A11 | S07, S08 | "Đang chế biến" và "Đang làm" lẫn nhau | Vừa |
| A12 | S02–S05 | Ảnh món là emoji | Vừa |
| A13 | S06, S02 | "256-bit", "hoàn tiền 5%", "giảm 15%" không có nguồn | Vừa |
| A14 | Mọi màn | Thanh trạng thái giả có emoji | Thấp |
| A15 | S03, S05, S07 | Tên "Trà Đào Chanh Sả" không thống nhất | Thấp |

Chi tiết và bằng chứng: [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md).

## 3. Quyết định

| Mã | Quyết định | Lý do |
|---|---|---|
| A01 | Accept | Nền kem trung tính, thẻ trắng, cam chỉ cho một nút chính và trạng thái chọn |
| A02 | Accept | Thay emoji bằng bộ 27 icon vector một nét |
| A03 | Accept | Đúng D10: tách giỏ hàng và thanh toán |
| A04 | Accept | Tiêu chí 48 dp nhóm tự đặt |
| A05 | Accept | Giữ ngoại lệ 12 sp cho nhãn thanh dưới theo D36 |
| A06 | Accept | Chữ cam dùng `#B45309` trên nền kem hoặc trắng |
| A07 | Accept | Nút chính S07 là "Chỉ đường tới Kiosk" |
| A08 | Accept | Một kiểu chip chọn ở mọi màn |
| A09 | Modify | Bỏ hero rỗng; giữ link đăng nhập hay bỏ do nhóm chốt |
| A10 | Accept | QR minh hoạ 21 × 21 |
| A11 | Accept | Thống nhất "Đang làm" |
| A12 | Modify | Ô trung tính với icon theo loại món, chờ ảnh món thật |
| A13 | Modify | Bỏ "256-bit" và "hoàn tiền 5%"; khuyến mãi −15% giữ như dữ liệu mẫu |
| A14 | Accept | Bỏ thanh trạng thái giả |
| A15 | Accept | Thống nhất "Trà Đào Chanh Sả" |

### Phản biện của AI khác

| Mục | Nội dung |
|---|---|
| Công cụ, phiên bản, ngày | |
| Nguyên văn câu trả lời | Ghi vào `08-ai-log/01-ai-design-log.md` thành phụ lục mới (ví dụ "Phụ lục H") |
| Điểm trùng với A01–A15 | |
| Điểm bổ sung | |
| Điểm bị Reject, kèm lý do | |

## 4. Final UI

Page 03 của Figma [PRM323](https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260). Bản cũ nằm ở x 40–1300 để đối chiếu; bản v2 là Final UI, lệch phải 2000 px, tên khung có hậu tố " v2".

| Nhóm | Màn |
|---|---|
| Đặt món | S01 Onboarding · S02 Trang chủ · S03 Thực đơn · S04 Chi tiết món · S05 Giỏ hàng · S06 Thanh toán · S07 Theo dõi đơn · S08 Đơn hàng |
| Trạng thái | S05-EMPTY · S05-VOUCHER-ERR · S06-ERR · S07-CASH · S08-EMPTY |
| Sửa và huỷ đơn | S09 Sửa đơn · S10 Đơn đã huỷ |
| Lịch sử | S11 Lịch sử tuần/tháng · S12 Chi tiết đơn |
| Yêu thích | S13 Món yêu thích · S14 Đặt lại nhanh |
| Cá nhân | S15 Cá nhân · S16 Hồ sơ sinh viên · S17 Phương thức thanh toán · S18 Cài đặt thông báo |
| Thông báo và nhận món | S19 Thông báo · S20 Nhận món (mã QR) |
| Quán đóng, món hết | S21 Trang chủ khi quán đóng · S22 Món hết, gợi ý thay thế |
| Sau khi nhận món | S23 Đánh giá món · S24 Báo sự cố |
| Hẹn giờ | S25 Hẹn giờ theo slot |
| Bổ sung | S26 Đăng nhập · S26-OTP · S27 Chọn Kiosk · S28 Kết quả tìm kiếm · S28-EMPTY · S29 Mã giảm giá · S30 Mất kết nối · S02-LOADING |
| App người bán | K01 Đăng nhập · K02 Danh sách đơn · K02-EMPTY · K03 Chi tiết đơn · K04 Đang chuẩn bị · K05 Quét mã · K05-ERR · K06 Xác nhận giao · K06-CASH · K08 Quản lý món · K09 Hết món · K10 Quán · K11 Thống kê ca · K12 Từ chối đơn · K13 Sự cố · K14 Thêm món mới · K14-ERR · K15 Sửa món ([`05-P4-ui-design/03-kitchen-app.md`](../03-kitchen-app.md)) |

S02 và S21 có chuông thông báo dẫn tới S19. S23 dùng thang số 1–5 thay cho mặt cười.

### Hệ thiết kế v2

| Thành phần | Quy tắc |
|---|---|
| Nền | `#FAF8F5`; thẻ trắng, viền `#E4DFD8` |
| Cam | `#F69D39` cho một nút chính mỗi màn và trạng thái đang chọn; chữ cam `#B45309` |
| Chữ | Nâu `#622B14` cho nội dung, `#6B5F55` cho phụ; tối thiểu 14 sp, nhãn thanh dưới 12 sp |
| Icon | 27 icon vector một nét, một màu, Page 05 |
| Vùng bấm | Tối thiểu 48 × 48 dp |
| Trạng thái | Màu luôn đi kèm chữ hoặc icon |
| Component | Chip, NavBar, Card/Food, IconButton, Button/Secondary, Button/Text (Page 05) |

### Số đo sau khi vẽ lại

Ảnh v2 xuất từ Figma: [`assets/figma/final-ui-v2/`](../../assets/figma/final-ui-v2/) (tổng quan: `contact-sheet-s01-s08.png`, `contact-sheet-s09-s25.png`). Đo bằng `python tests/audit/measure.py v2` và Figma Plugin API trên 114 khung (58 ở 360 dp, 56 ở 412 dp).

| Chỉ số | Bản cũ | v2 |
|---|---|---|
| Cam đậm (trung bình S01–S08) | 5,9% | 4,3% |
| Họ cam–be (nền, thẻ đào, chip đào) | 55,3% | 4,4% (nền chuyển sang `#FAF8F5`, thẻ trắng) |
| Ký tự emoji | 98/366 chữ | 0 |
| Chữ dưới 14 sp | 86 dòng ở 8 màn | 0, trừ nhãn thanh dưới 12 sp |
| Chữ thiếu tương phản | 8 chỗ | 0 |
| Vùng bấm dưới 48 dp | 20/39 | 0/262 |
| Chữ tràn khỏi khung 360 × 800 | — | 0 |

### Prototype và màn 412 dp

- Prototype v2 nối ngay trên Page 03: hơn 260 vùng bấm giữa 64 khung (gồm S06-LOADING, S02-LOADING, K02-EMPTY, S02-ADDED, S03-ADDED tự chuyển; S06-GATEWAY là cổng thanh toán mô phỏng; S07-DIALOG, K12 dạng overlay), 19 điểm bắt đầu gồm cả luồng người bán. Vùng bấm đọc ra `tests/figma-proto/hotspots-v2.json`.
- Kiểm đồ thị flow v2: `PROTO=v2 npx playwright test graph.spec.js` đạt 10/10 (không màn cụt, không màn mồ côi, đặt đơn S02 → S02-ADDED → S05 → S06 → cổng thanh toán → S07 mất 5 chạm, F3 có lối về S07-CASH và S05).
- 56 khung có bản 412 dp (" v2 · 412", dùng constraints), gồm toàn bộ màn khách và người bán trừ hai dialog. Ảnh S02, S05, S06, S07 ở `assets/figma/final-ui-v2/412/`.

## 5. Quyết định phạm vi mới

| Mã | Quyết định | Lý do |
|---|---|---|
| D43 | Thêm app người bán K01–K15 và S26–S30 vào phạm vi (trước đây app phía quầy nằm ngoài phạm vi ở P0) | Đơn của khách cần quầy nhận, làm, giao; các màn S07, S20, S21, S22, S24 đã dựa vào thao tác phía quầy |

## 6. Việc còn lại

1. Chạy phản biện bằng AI khác, ghi nguyên văn vào `08-ai-log/01-ai-design-log.md`, rồi điền bảng ở mục 3.
2. Chạy Present trong Figma cho từng flow v2 và cập nhật ảnh chuẩn Playwright (`flows.spec.js`) cho prototype v2.
3. Usability test với 3–5 sinh viên, ghi vào [`06-P5-kiem-thu-ban-giao/02-usability-test-mau.md`](../../06-P5-kiem-thu-ban-giao/02-usability-test-mau.md).
