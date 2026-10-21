# Bản vẽ lại v2 trên Figma (sau phản biện)

Vẽ lại 13 màn theo [báo cáo A01–A15](01-bao-cao-do-tu-dong.md). **Bản cũ không bị xoá hay sửa** để đối chiếu; bản mới nằm cùng hàng, lệch phải 2000 px.

> Đây là **bản nháp của Claude chưa qua quyết định của bạn**. Bảng quyết định ở mục 4 của báo cáo vẫn do bạn điền; muốn bỏ điểm nào thì Reject và sửa lại Figma.

## Vị trí trong Figma (file PRM323)

| Việc | Ở đâu |
|---|---|
| 13 màn v2 (tên kết thúc bằng " v2") | Page 03, x = x cũ + 2000, cùng y. Tiêu đề "FINAL UI v2" ở (2040, 70) |
| Màn cũ | Page 03, x 40–1300, **giữ nguyên** |
| Bộ icon vector v2 (27 icon `Icon/…`) | Page 05, board "Components v2 · Icon library" |
| Component v2: Chip, NavBar, Card/Food, IconButton, Button/Secondary, Button/Text | Page 05, board "Components v2 · Components" |
| Token mới `color/v2-*` (5 biến) | Collection "FtaCode Design Tokens" |

13 màn: S01, S02, S03, S04, S05, S05-EMPTY, S05-VOUCHER-ERR, S06, S06-ERR, S07, S07-CASH, S08, S08-EMPTY. **Chưa nối prototype** cho v2 (prototype Page 06 và `npm test` vẫn chạy trên bản cũ).

## Mỗi lỗi được xử lý thế nào

| Mã | Thay đổi ở v2 |
|---|---|
| A01 quá cam | Nền màn `#FAF8F5` (kem trung tính), thẻ trắng viền `#E4DFD8`; cam chỉ còn ở nút chính duy nhất, trạng thái chọn và điểm nhấn nhỏ |
| A02 icon | Bỏ toàn bộ emoji; dùng một bộ 27 icon vector cùng nét, một màu |
| A03 giỏ + thanh toán lặp | S05 chỉ còn giỏ hàng, nút "Tiếp tục thanh toán"; chọn phương thức chỉ ở S06 |
| A04 vùng bấm | Nút icon, chip, nút +, nút −, dòng topping đều ≥ 48 dp |
| A05 chữ nhỏ | Mọi chữ ≥ 14 sp, trừ nhãn thanh dưới 12 sp (ngoại lệ D36) |
| A06 tương phản | Chữ cam dùng `primary-text` `#B45309`; đo không có chữ dưới 4,5:1 |
| A07 CTA S07 | Nút chính "Chỉ đường tới Kiosk"; "Về trang chủ" thành nút chữ |
| A08 chip | Một kiểu chip chọn ở mọi màn (nền kem nhạt, viền cam) |
| A09 S01 | Bỏ hero rỗng to và thẻ giống nút. **Chưa giải quyết:** vẫn còn dòng "Đăng nhập bằng email @fpt.edu.vn" (mâu thuẫn D12), bạn cần quyết định bỏ hay giữ |
| A10 QR | Mã QR minh hoạ 21×21 (không quét được, ghi chú trên khung) |
| A11 tên trạng thái | Thống nhất "Đang làm" ở S07, S08 |
| A12 ảnh món | Ô trung tính với icon theo loại (món ăn, đồ uống), không còn emoji. Chưa có ảnh món thật |
| A13 nội dung không kiểm chứng | Bỏ "256-bit", "hoàn tiền 5%". **Chưa giải quyết:** còn "Combo Giờ Vàng −15%", là khuyến mãi mô phỏng, cần ghi rõ là dữ liệu giả |
| A14 thanh trạng thái giả | Bỏ |
| A15 tên món | Thống nhất "Trà Đào Chanh Sả" |

## Số đo sau sửa (Figma Plugin API, 21/10/2026, chỉ đọc)

| Chỉ số | Bản cũ (báo cáo) | v2 |
|---|---|---|
| Ký tự emoji | xem báo cáo mục 1 | **0** |
| Chữ < 14 sp | xem báo cáo mục 2 | chỉ 4 nhãn thanh dưới 12 sp trên các màn có thanh dưới (ngoại lệ D36) |
| Chữ thiếu tương phản (4,5:1 / 3:1 chữ lớn) | xem báo cáo mục 2 | **0** |
| Nút, chip, nút icon < 48 dp (các instance component v2) | xem báo cáo mục 2 | **0** |

## Chưa làm / giới hạn

- **Chưa đo tỉ lệ màu cam bằng ảnh** và chưa xuất PNG v2 vào repo: gói Figma Starter hết hạn mức gọi MCP. Cần xuất 13 khung thủ công (Figma: chọn khung, Export, PNG 2x) vào `assets/figma/final-ui-v2/`, rồi chạy lại `tests/audit/measure.py` trỏ vào thư mục đó.
- Số đo trên chỉ phủ phần đã dựng bằng component v2 và chữ; thành phần tự vẽ (ô chọn topping, nút chính) lấy kích thước theo thiết kế, chưa đo riêng.
- Handoff Flutter (`handoff/flutter-handoff.md`) và prototype chưa cập nhật theo v2.
- Phải qua **AI khác** ([`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md)) rồi mới coi là phản biện đúng yêu cầu Lab 2.
