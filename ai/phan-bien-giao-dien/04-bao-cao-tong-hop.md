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
