# Prompt cho AI khác phản biện giao diện

Mục đích theo đề Lab 2: **một AI khác với AI đã thiết kế** soi giao diện và tìm lỗi; sinh viên quyết định Accept / Modify / Reject, sửa Figma rồi mới ra Final UI. Nên dùng một công cụ khác với Claude (ví dụ Gemini hoặc ChatGPT có nhận ảnh).

## Cách làm

1. Mở công cụ AI khác, bắt đầu cuộc trò chuyện mới.
2. Đính kèm các ảnh trong [`anh/`](anh/): **S01 → S08**, cộng `S05-VOUCHER-ERR`, `S06-ERR`, `S07-CASH`. Có thể đính kèm thêm `_tong-quan-8-man.png`.
3. **Đừng đính kèm** [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md) trước, để AI kia không bị dẫn dắt; so sánh sau.
4. Dán nguyên văn prompt bên dưới.
5. **Lưu nguyên văn câu trả lời** (không sửa chữ) vào `08-ai-log/01-ai-design-log.md` thành một phụ lục mới (ví dụ "Phụ lục H"), ghi rõ tên công cụ, phiên bản và ngày.
6. Đối chiếu với báo cáo đo tự động: điểm trùng thì tin hơn; điểm chỉ một bên nêu thì kiểm lại; điểm AI khác nêu sai thì ghi Reject kèm lý do.

## Prompt (dán nguyên văn)

```text
Bạn là chuyên gia UI/UX khó tính, đóng vai người kiểm tra độc lập. Tôi đính kèm ảnh các màn hình của một app di động tên BreakBite (đặt món ăn trước, nhận tại quầy trong trường đại học), khung 360 × 800 dp. Đây là bài Lab 2 của một môn học; giao diện do AI sinh ra rồi được chỉnh, và tôi cần bạn tìm lỗi thật, không khen cho có.

BỐI CẢNH
- Người dùng chính: sinh viên 20 tuổi, chỉ có khoảng 15 phút giữa hai tiết học, cầm điện thoại một tay khi đi bộ.
- Mục tiêu: đặt xong một đơn dưới 35 giây, tối đa 8 chạm. Thanh toán lỗi không được làm mất giỏ hàng.
- Ràng buộc đã chọn: chủ đề sáng (light theme); chữ nội dung tối thiểu 14 sp; vùng chạm tối thiểu 48 × 48 dp; tương phản chữ tối thiểu 4,5:1 (3:1 cho chữ lớn); không bắt buộc đăng nhập.
- Màn hình đính kèm: S01 Onboarding, S02 Trang chủ, S03 Thực đơn, S04 Chi tiết món, S05 Giỏ hàng, S06 Thanh toán, S07 Theo dõi đơn, S08 Đơn hàng/Lịch sử, S05-VOUCHER-ERR (mã giảm giá sai), S06-ERR (lỗi thanh toán), S07-CASH (trả tiền mặt).

NHIỆM VỤ
Đánh giá theo 10 heuristic của Nielsen, WCAG 2.2 AA, và chất lượng thiết kế hình ảnh (thứ bậc, màu, icon, khoảng cách, nhất quán). Đặc biệt chú ý:
1. Việc dùng màu: màu có giúp mắt biết nhìn đâu trước không? Có quá một tông hay không? Mỗi màn có bao nhiêu thành phần tranh nhau sự chú ý?
2. Icon: có nhất quán một phong cách không? Icon có đúng nghĩa với chức năng không? Có icon nào gây hiểu nhầm hoặc thừa không?
3. Luồng và cấu trúc: có bước nào lặp, thừa, hoặc mâu thuẫn giữa các màn không?
4. Nội dung chữ: có thông tin nào nghe không đáng tin, thiếu căn cứ, hoặc đặt tên không thống nhất không?
5. Khả năng tiếp cận: chữ nhỏ, tương phản, vùng chạm, trạng thái chỉ dựa vào màu.

ĐỊNH DẠNG TRẢ LỜI (bắt buộc)
A. Bảng lỗi, sắp theo mức độ giảm dần, mỗi dòng gồm: Mã (L01, L02…) | Màn hình | Vấn đề (cụ thể, chỉ rõ chỗ nào trong ảnh) | Tiêu chí vi phạm (heuristic số mấy hoặc điều WCAG nào) | Mức (Cao / Vừa / Thấp) | Đề xuất sửa (một hai câu, không vẽ lại cả thiết kế).
B. Nhận xét riêng về màu sắc và icon (mỗi mục 5–8 dòng).
C. Ba điểm làm tốt thật sự (chỉ nêu nếu có căn cứ).
D. Những điều bạn KHÔNG thể kết luận chỉ từ ảnh tĩnh (ví dụ thời gian, tương tác, độ chính xác số đo pixel).
Nếu không chắc một điểm, ghi "chưa chắc" thay vì đoán. Không bịa số đo; nếu ước lượng thì nói là ước lượng.
```

## Gợi ý đọc kết quả

- AI nhìn ảnh tĩnh nên **ước lượng cỡ chữ và tương phản dễ sai**; số đo chính xác nằm ở báo cáo đo tự động.
- Nếu AI kia không nêu icon hoặc màu cam, hỏi thêm: *"Bạn đánh giá thế nào về việc dùng emoji làm icon và việc cả nền, thẻ, nút, viền đều cùng họ màu cam?"* và ghi cả câu hỏi thêm vào nhật ký.
