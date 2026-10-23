# Kịch bản trình bày (deck 16 slide, khoảng 10 phút)

Deck: `BreakBite_Lab2_Presentation.pptx`. Mỗi slide ghi dòng "Minh chứng" ở chân slide để chỉ về file trong repo. Thời gian là gợi ý; demo Figma Present cộng thêm 5 phút.

| # | Slide | Thời gian | Ý chính |
|---|---|---|---|
| 1 | Bìa | 20 giây | Tên, nhóm, link |
| 2 | Vấn đề và người dùng | 50 giây | Problem statement, 4 điểm đau, persona Quân |
| 3 | Giải pháp | 40 giây | Đặt, trả trước, nhận bằng QR; 30 màn khách, 15 màn người bán |
| 4 | Nghiên cứu và quyết định | 50 giây | Insight nào dẫn tới quyết định nào; phần nào là dữ liệu mô phỏng |
| 5 | Kiến trúc thông tin | 40 giây | 4 tab khách, 4 tab người bán |
| 6 | Ba flow chính | 60 giây | F1, F2, F3 và nhánh lỗi |
| 7 | Thiết kế với AI | 50 giây | Stitch, phản biện, Accept/Modify/Reject |
| 8 | Phản biện giao diện và v2 | 50 giây | Số đo trước và sau |
| 9 | Final UI: luồng đặt món | 30 giây | S01–S08 |
| 10 | Final UI: vòng đời đơn | 30 giây | S09–S30 |
| 11 | App người bán | 40 giây | K01–K15 |
| 12 | Design system | 30 giây | Màu, chữ, icon, component |
| 13 | Accessibility và responsive | 30 giây | Số đo, 360 và 412 dp |
| 14 | Prototype và kiểm thử | 30 giây | Prototype v2, Playwright |
| 15 | Bàn giao và Quality Gates | 30 giây | Handoff Flutter, tự chấm G0–G5 |
| 16 | Tổng kết | 30 giây | AI giúp gì, nhóm phải làm gì, còn lại gì |

## Lời nói gợi ý

**Slide 2.** "Sinh viên có lịch học dày chỉ có khoảng 15 phút giữa hai slot, mà hàng chờ căn tin dồn đúng giờ nghỉ. Bốn điểm đau chính là hàng chờ, không biết trước quán còn món không, phí hiện ở bước cuối, và lỗi thanh toán làm mất giỏ. Persona chính là Minh Quân, hai mươi tuổi, cầm máy một tay khi đi bộ."
*Nếu bị hỏi cơ sở:* nói thẳng đây là proto-persona, dữ liệu phỏng vấn là mô phỏng AI, khảo sát thật đang thu.

**Slide 3.** "BreakBite có ba bước: đặt từ lớp, trả trước, ra Kiosk quét mã nhận món. App khách có 30 màn, app người bán có 15 màn. Mục tiêu là đặt xong dưới 35 giây, tối đa 8 chạm; trên prototype là 3 chạm từ Trang chủ tới Theo dõi đơn."

**Slide 4.** "Mỗi quyết định thiết kế nối về một insight. Ví dụ hàng chờ dẫn tới hẹn giờ nhận, ngại phí ẩn dẫn tới giá cộng dồn trên nút. Phỏng vấn và phản hồi đang có là mô phỏng để thử bộ câu hỏi, nên em không dùng chúng làm bằng chứng; khảo sát thật đang thu."

**Slide 5.** "App khách có bốn tab: Trang chủ, Thực đơn, Đơn hàng, Cá nhân. App người bán cũng có bốn tab: Đơn, Quét mã, Món, Quán."

**Slide 6.** "Flow 1 đặt nhanh, Flow 2 tuỳ chỉnh và mã giảm giá, Flow 3 là lỗi thanh toán: giỏ hàng vẫn được giữ và có thể thử lại hoặc trả tiền mặt."

**Slide 7.** "AI sinh giao diện ban đầu và phản biện, nhóm quyết định. Ví dụ Accept giá cộng dồn, Modify chữ nút sang màu nâu, Reject việc bắt buộc đăng nhập. AI nêu một con số tương phản sai nên nhóm tự đo lại: chữ trắng trên cam chỉ 2,14:1."

**Slide 8.** "Sau khi đo bản cũ, lỗi lớn nhất là cả màn dùng một họ cam–be cho mọi vai trò. Họ màu này chiếm 55% điểm ảnh, bản v2 còn 4%. Emoji về 0, vùng bấm dưới 48 dp từ 20 trên 39 về 0. Báo cáo đo do công cụ AI viết nên không độc lập; phản biện của AI khác nhóm chưa chạy."

**Slide 9–10.** "Bản v2 có ba nhóm màn: đặt món S01 đến S08, vòng đời đơn và tài khoản S09 đến S30, và mỗi màn có trạng thái rỗng, lỗi, đang tải."

**Slide 11.** "Màn khách đã hứa nhiều việc mà quầy phải làm được: nhận đơn, báo sẵn sàng, quét mã giao món, thu tiền mặt, báo hết món, thêm hoặc sửa món, từ chối đơn, hoàn tiền. Vì vậy có app người bán 15 màn, dùng chung hệ thiết kế."

**Slide 12–13.** "Màu, chữ, khoảng cách là token; component có variant theo trạng thái. Tương phản chữ nút nâu trên cam là 5,23:1, vùng bấm từ 48 dp, chữ nội dung từ 14 sp. Mỗi màn có bản 360 dp và 412 dp."

**Slide 14.** "Prototype v2 nối cả hai app. Playwright kiểm bản cũ 13 trên 13 test và đồ thị flow bản v2 7 trên 7. Kiểm thử tự động không thay usability test với người thật."

**Slide 15.** "Handoff cho Flutter gồm bảng token sang ThemeData, bảng component sang widget và sáu mục cho mỗi màn. Nhóm tự chấm theo sáu gate của môn; đây là rubric nội bộ, không phải chuẩn quốc tế. Gate 5 chưa qua vì chưa có usability test."

**Slide 16.** "AI giúp nhanh và phản biện; nhóm xác định vấn đề, tự đo lại và quyết định. Việc còn lại là phản biện độc lập bằng AI khác, khảo sát thật, usability test và chạy Present trên prototype v2."

## Demo Figma Present (5 phút)

1. Page 03, các khung " v2": chỉ ra S01–S08, rồi cuộn xuống app người bán (K01–K15).
2. **Flow 1:** S02 → bấm combo → S04 → Thêm vào giỏ → S05 → Tiếp tục thanh toán → S06 → Xác nhận → màn đang tải tự chuyển → S07.
3. **Flow 2:** S03 → S04 → S05 → bấm ô mã giảm giá (mã sai, S29) → nhập lại.
4. **Flow 3:** bắt đầu từ S06-ERR → Tiền mặt tại Kiosk → S07-CASH.
5. **Người bán:** K01 → K02 → K03 nhận đơn → K04 → K05 quét mã → K06 xác nhận giao.
6. Dialog huỷ đơn ở S07 (overlay) và Back hoạt động.

Trước khi trình bày: thử link Figma bằng cửa sổ chưa đăng nhập.

## Câu hỏi thầy có thể hỏi

Xem [`phan-bien-hoi-dap.md`](phan-bien-hoi-dap.md).
