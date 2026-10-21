# Báo cáo tổng hợp: phản biện giao diện và thiết kế lại

FtaCode Mobile · Lab 2 PRM323 · 21/10/2026

> **Trạng thái:** bản nháp để bạn sửa và nộp. Cột "Quyết định" ở mục 4 là **đề xuất của Claude**; bạn phải đọc, đổi nếu không đồng ý, rồi mới coi là quyết định của nhóm. Phản biện **độc lập** (AI khác) **chưa có**; xem mục 6.

## 1. Mục đích

Theo đề Lab 2, giao diện phải được một AI khác soi lỗi, sinh viên quyết định Accept / Modify / Reject, rồi sửa trước khi ra Final UI. Báo cáo này ghi lại bước đã làm: đo lỗi bằng công cụ, vẽ lại giao diện, và kết quả đo sau khi vẽ.

## 2. Cách làm

| Bước | Công cụ | Kết quả |
|---|---|---|
| Chụp 13 màn từ prototype Figma thật | Playwright (`tests/audit/capture.js`) | [`anh/`](anh/) |
| Đo chữ, màu, tương phản, vùng bấm | Figma Plugin API + `measure.py` | [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md) |
| Vẽ lại 30 màn | Figma (bản sao PRM323 Copy) | [`03-ban-ve-lai-v2.md`](03-ban-ve-lai-v2.md) |
| Phản biện bởi AI khác | Chưa làm | [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md) |

Báo cáo đo do Claude viết, cũng là AI đã sửa Figma trước đó, nên **không độc lập**. Số đo thì khách quan và chạy lại được; phần nhận xét bằng mắt là của Claude.

## 3. Lỗi tìm được

| Mã | Lỗi | Đo được (bản cũ) | Mức |
|---|---|---|---|
| A01 | Giao diện quá cam | Cam đậm chỉ 5,9% điểm ảnh, nhưng khoảng 61% màn là một họ cam–be; không có màu trung tính | Cao |
| A02 | Icon lộn xộn | 98/366 chữ chứa emoji, 30 emoji khác nhau, 59 ký tự chữ dùng làm icon; "thời gian" dùng hai icon khác nhau | Cao |
| A03 | Giỏ hàng và thanh toán lặp | S05 và S06 đều chọn phương thức thanh toán; nút "Xác nhận thanh toán" đứng trước bước chọn | Cao |
| A04 | Vùng bấm nhỏ | 20/39 vùng bấm nhỏ hơn 48 dp | Cao |
| A05 | Chữ nhỏ | 86 dòng chữ dưới 14 sp; nhãn thanh dưới 10 sp | Cao |
| A06 | Tương phản | `#B45309` trên `#FFE8CC` chỉ 4,23:1, ở 8 chỗ | Vừa |
| A07–A15 | CTA S07 sai trọng tâm, chip chọn khác kiểu, onboarding rỗng, QR giả, tên trạng thái lệch, ảnh món là emoji, nội dung khó kiểm chứng, thanh trạng thái giả, tên món không thống nhất | Nhận xét bằng mắt | Vừa–Thấp |

Chi tiết và bằng chứng: [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md).

## 4. Quyết định (đề xuất, bạn sửa)

| Mã | Đề xuất | Lý do |
|---|---|---|
| A01 | Accept | Đo được; sửa bằng nền kem trung tính, thẻ trắng, cam chỉ cho một nút chính và trạng thái chọn |
| A02 | Accept | Emoji đổi theo thiết bị và không đổi được màu; thay bằng một bộ 27 icon vector |
| A03 | Accept | Đúng với quyết định D10 (tách giỏ hàng và thanh toán) |
| A04 | Accept | Vi phạm tiêu chí 48 dp mà nhóm tự đặt |
| A05 | Accept | Giữ ngoại lệ 12 sp cho nhãn thanh dưới theo D36 |
| A06 | Accept | Dùng chữ nâu hoặc `#B45309` trên nền không phải đào |
| A07 | Accept | Việc chính ở S07 là nhận món, nên "Chỉ đường" là nút chính |
| A08 | Accept | Một kiểu chip chọn ở mọi màn |
| A09 | **Modify** | Bỏ hero rỗng; dòng "Đăng nhập email @fpt.edu.vn" mâu thuẫn D12, **bạn cần quyết định bỏ hay giữ** |
| A10 | Accept | QR minh hoạ, có ghi chú là không quét được |
| A11 | Accept | Thống nhất "Đang làm" |
| A12 | **Modify** | Chưa có ảnh món thật; dùng ô trung tính với icon theo loại |
| A13 | **Modify** | Đã bỏ "256-bit" và "hoàn tiền 5%"; "Giảm 15%" còn lại là khuyến mãi mô phỏng, cần ghi rõ dữ liệu giả |
| A14 | Accept | Thanh trạng thái giả không có giá trị |
| A15 | Accept | Thống nhất "Trà Đào Chanh Sả" |

## 5. Kết quả sau khi vẽ lại (v2)

Đo bằng Figma Plugin API trên 30 màn v2 (13 màn lõi và biến thể, 17 màn mở rộng S09–S25).

| Chỉ số | Bản cũ | v2 |
|---|---|---|
| Ký tự emoji | 98/366 chữ | 0 |
| Chữ dưới 14 sp | 86 dòng ở 8 màn lõi | 0, ngoại trừ nhãn thanh dưới 12 sp (D36) |
| Chữ thiếu tương phản | 8 chỗ ở A06 | 0 (một cảnh báo giả ở S14 do lớp phủ tối) |
| Vùng bấm dưới 48 dp | 20/39 | 0 |
| Chữ tràn khỏi khung 360 × 800 | chưa đo | 0 |

Bản cũ vẫn nguyên trong Figma để đối chiếu; v2 nằm cùng hàng, lệch phải 2000 px.

## 6. Chưa làm và rủi ro

- **Chưa có phản biện độc lập.** Phải chạy [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md) với một AI khác, ghi nguyên văn vào `ai/ai-design-log.md`, rồi đối chiếu. Thiếu bước này thì chưa đáp ứng yêu cầu Lab 2.
- **Chưa đo tỉ lệ màu cam trên ảnh v2** và chưa xuất PNG v2 vào repo. Số "khoảng 61%" chỉ có cho bản cũ; chưa chứng minh bằng số rằng v2 bớt cam, chỉ có thiết kế và kiểm bằng mắt.
- Mới nhìn bằng mắt một số màn v2 (S02, S03, S04, S05, S07-CASH, S08, S11, S21, S23); các màn còn lại chỉ qua số đo.
- **Chưa nối prototype** cho v2; `npm test` và prototype Page 06 vẫn chạy trên bản cũ. Handoff Flutter chưa cập nhật.
- File Figma gốc chỉ có 13 màn lõi v2; **bản đủ 30 màn nằm ở bản sao** (PRM323 Copy), vì file gốc bị khoá hạn mức MCP.
- Nội dung S09–S25 là giả thuyết (Assumed), chưa có khảo sát hay test người dùng.
- Kiểm thử với người thật (G5) vẫn là việc phải làm; giao diện đẹp hơn chưa có nghĩa là dễ dùng hơn.

## 7. Việc tiếp theo, theo thứ tự

1. Chạy phản biện bằng AI khác, ghi nguyên văn vào `ai/ai-design-log.md` (Phụ lục mới).
2. Sửa cột "Quyết định" ở mục 4 theo ý bạn; quyết định A09 và A13.
3. Xuất 13 màn lõi v2 sang PNG, chạy lại `tests/audit/measure.py` để có số cam bản mới.
4. Nối prototype v2, sửa `hotspots.json`, chạy lại `npm test`.
5. Cập nhật handoff Flutter theo v2 rồi mới gọi là Final UI.

---

## 8. Phản biện UI (phần để nộp)

### 8.1 Phản biện của Claude (không độc lập)

Đã đo và nhận xét 15 lỗi (A01–A15, mục 3 và 4). Điểm chính: giao diện cũ **không sai ở độ lớn nút cam** (cam đậm chỉ 5,9%) mà sai ở chỗ **cả màn dùng một họ cam–be cho mọi vai trò**, trộn ba hệ icon, lặp bước chọn thanh toán giữa S05 và S06, và vi phạm hai tiêu chí nhóm tự đặt (vùng bấm 48 dp, chữ 14 sp). Bằng chứng: [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md).

### 8.2 Phản biện của AI khác (bắt buộc theo đề, **chưa có**)

| Mục | Điền khi có |
|---|---|
| Công cụ, phiên bản, ngày | |
| Nguyên văn câu trả lời | Ghi vào `ai/ai-design-log.md` thành phụ lục mới (ví dụ "Phụ lục H"), không sửa chữ |
| Điểm trùng với A01–A15 | |
| Điểm AI kia nêu mà Claude bỏ sót | |
| Điểm AI kia nêu sai (Reject, kèm lý do) | |

Cách làm: [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md). Điểm hai bên cùng nêu thì đáng tin hơn; điểm chỉ một bên nêu thì kiểm lại bằng số đo.

### 8.3 Quyết định cuối

Dùng bảng ở mục 4. Sau khi có 8.2, đổi cột "Quyết định" nếu AI kia đưa ra lý do tốt hơn, và ghi lại vào `ai/ai-design-log.md`.

## 9. Final UI

**Trạng thái:** v2 là **ứng viên Final UI**. Chỉ gọi là Final UI sau khi (1) có phản biện của AI khác, (2) bạn chốt A09 và A13, (3) xuất ảnh và đo lại màu cam.

### 9.1 Phạm vi

| Nhóm | Màn | Ghi chú |
|---|---|---|
| Lõi (Lab 2) | S01–S08 | 8 màn bắt buộc |
| Biến thể | S05-EMPTY, S05-VOUCHER-ERR, S06-ERR, S07-CASH, S08-EMPTY | Trạng thái rỗng và lỗi |
| Mở rộng (Phase 2) | S09–S25 | Backlog đã thiết kế, nhãn Assumed, không thuộc bài nộp Lab 2 |

Vị trí: Page 03 của bản sao Figma [PRM323 (Copy)](https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260), khung có hậu tố " v2", lệch phải 2000 px so với bản cũ.

### 9.2 Hệ thiết kế v2

| Thành phần | Quy tắc |
|---|---|
| Nền | `#FAF8F5`; thẻ trắng, viền `#E4DFD8` |
| Cam | `#F69D39` chỉ cho **một nút chính mỗi màn** và trạng thái đang chọn; chữ cam dùng `#B45309` |
| Chữ | Nâu `#622B14` cho nội dung, `#6B5F55` cho phụ; tối thiểu 14 sp, nhãn thanh dưới 12 sp (D36) |
| Icon | 27 icon vector một nét, một màu; không emoji |
| Vùng bấm | Tối thiểu 48 × 48 dp |
| Trạng thái | Luôn có chữ hoặc icon đi kèm màu (ví dụ "Đã áp dụng" có dấu tích, lỗi có icon) |
| Component | Chip, NavBar, Card/Food, IconButton, Button/Secondary, Button/Text (Page 05) |

### 9.3 Việc còn lại trước khi gọi là Final

1. Xuất PNG 2x của các màn lõi vào `assets/figma/final-ui-v2/`.
2. Chạy lại `tests/audit/measure.py` trên ảnh v2 và ghi số cam vào mục 5.
3. Nối prototype v2, cập nhật `hotspots.json`, chạy `npm test`.
4. Cập nhật `handoff/flutter-handoff.md` (token mới, component mới, mã màn S01–S25).
5. Kiểm thử với người dùng thật (G5); đến lúc đó mới có bằng chứng giao diện dễ dùng hơn.
