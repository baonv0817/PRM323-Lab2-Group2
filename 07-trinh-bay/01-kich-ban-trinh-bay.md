# Kịch bản trình bày (deck 33 slide theo quy trình P0 → P5)

Deck: `BreakBite_Lab2_Presentation.pptx`. Slide đi đúng thứ tự quy trình thiết kế; mỗi slide có nhãn phase ở góc trên phải và dòng "Minh chứng" ở chân slide.
Đầy đủ khoảng 20 phút. Nếu chỉ có 10 phút, trình bày các slide đánh dấu ★ và bỏ qua phần còn lại.

| # | Slide | Phase | Phút | |
|---|---|---|---|---|
| 1 | Bìa | | 0,3 | ★ |
| 2 | Quy trình P0 → P5 và gate | | 0,7 | ★ |
| 3 | Vấn đề cần giải quyết | P0 | 0,7 | ★ |
| 4 | Các hướng đã cân nhắc | P0 | 0,6 | |
| 5 | Giả định, rủi ro, phạm vi MVP | P0 | 0,6 | |
| 6 | Kế hoạch nghiên cứu | P1 | 0,5 | |
| 7 | Kết quả nghiên cứu hiện có | P1 | 0,7 | ★ |
| 8 | Insight → quyết định thiết kế | P1 | 0,7 | ★ |
| 9 | Persona | P2 | 0,6 | ★ |
| 10 | User story chính | P2 | 0,6 | |
| 11 | Kiến trúc thông tin | P2 | 0,6 | ★ |
| 12 | Ba flow chính | P2 | 1,0 | ★ |
| 13 | Wireframe và flow mở rộng | P2 | 0,5 | |
| 14 | Tạo giao diện với Google Stitch | P3 | 0,6 | |
| 15 | Ba hướng visual | P3 | 0,8 | ★ |
| 16 | AI phản biện và ba vòng tinh chỉnh | P3 | 0,8 | ★ |
| 17 | Quyết định Accept, Modify, Reject | P3 | 0,6 | ★ |
| 18 | App Style Guide | P3 | 0,6 | ★ |
| 19 | Phản biện giao diện và bản v2 | P4 | 0,8 | ★ |
| 20 | Final UI: luồng đặt món | P4 | 0,6 | ★ |
| 21 | Trạng thái hệ thống | P4 | 0,5 | ★ |
| 22 | Final UI: vòng đời đơn và tài khoản | P4 | 0,5 | |
| 23 | App người bán | P4 | 0,7 | ★ |
| 24 | Ánh xạ pain point → màn hình (1/2) | P4 | 0,6 | ★ |
| 25 | Ánh xạ pain point → màn hình (2/2) | P4 | 0,6 | ★ |
| 26 | Bản vẽ trong Figma, sáu page | P4 | 0,5 | |
| 27 | Component và responsive | P4 | 0,5 | |
| 28 | Prototype Figma | P4 | 0,4 | ★ |
| 29 | Accessibility | P5 | 0,6 | ★ |
| 30 | Kiểm thử | P5 | 0,6 | ★ |
| 31 | Bàn giao cho Flutter | P5 | 0,5 | ★ |
| 32 | Tự chấm theo Quality Gates | P5 | 0,6 | ★ |
| 33 | Tổng kết, cảm ơn | | 0,5 | ★ |

Demo Figma Present cộng thêm 5 phút (xem cuối file); chạy trên Page 06, chọn khung và bấm Present.

## Lời nói gợi ý theo phase

**P0 · Ideas (slide 3–5).** "Vấn đề: sinh viên chỉ có khoảng 15 phút giữa hai slot mà hàng chờ căn tin dồn đúng giờ nghỉ. Nhóm cân nhắc bốn hướng, chấm Impact nhân Feasibility, chọn app đặt trước vì gỡ được cả thời gian lẫn thông tin. AI đề xuất chuyển sang web QR, nhóm từ chối vì đề bắt buộc app mobile, nhưng giữ làm phương án dự phòng. Giả định chưa biết được xếp vào danh sách kiểm chứng ở P1."

**P1 · Research (slide 6–8).** "Kế hoạch có sáu câu hỏi nghiên cứu. Dữ liệu hiện có là phỏng vấn và khảo sát mô phỏng bằng AI, dùng để thử bộ câu hỏi, nên nhóm không coi là bằng chứng; khảo sát thật đang thu. Mỗi insight vẫn được nối tới một quyết định thiết kế, ví dụ hàng chờ dẫn tới hẹn giờ nhận."

**P2 · UX Design (slide 9–13).** "Persona chính là Minh Quân; hai persona phụ là Mỹ Linh và cô Hạnh, và một nhóm không nhắm tới. Mỗi user story có tiêu chí đo được. Kiến trúc thông tin có bốn tab cho khách và bốn tab cho người bán. Ba flow chính đều có nhánh lỗi; flow ba giữ giỏ hàng khi thanh toán lỗi. Bố cục được chốt bằng wireframe xám trước khi chọn màu."

**P3 · UI Concept (slide 14–18).** "Nhóm viết brief DESIGN.md trước, rồi dùng Google Stitch tạo bản nháp. Ba hướng visual được so sánh cùng nội dung: chọn A, mượn khối trạng thái quán của B, loại C vì nền tối kém ngoài nắng. AI phản biện bằng Nielsen và WCAG, nhóm quyết định Accept, Modify hoặc Reject; AI nêu một số sai nên nhóm tự đo lại. Kết quả là style guide có token màu, chữ, khoảng cách và component."

**P4 · UI Design (slide 19–28).** "Sau khi đo bản cũ bằng Playwright và Figma Plugin API, lỗi lớn nhất là cả màn dùng một họ cam–be cho mọi vai trò: 55% điểm ảnh, bản v2 còn 4%. Emoji về 0, vùng bấm dưới 48 dp từ 20 trên 39 về 0. Final UI gồm 30 màn khách và 15 màn người bán, mỗi màn có bản 360 và 412 dp. Prototype nối cả hai app. Bảng ánh xạ cho thấy mỗi pain point được giải bằng màn hình nào: hàng chờ bằng hẹn giờ và mã QR, phí ẩn bằng giá cộng dồn, lỗi thanh toán bằng giữ giỏ hàng, và người bán có đơn đã thanh toán sẵn."

**P5 · Validation (slide 29–32).** "Tương phản chữ nút là 5,23:1, vùng bấm từ 48 dp, chữ từ 14 sp. Playwright kiểm đồ thị flow và prototype; nhưng usability test với người thật mới ở mức kế hoạch. Handoff cho Flutter có bảng token và component sang widget và sáu mục cho mỗi màn. Nhóm tự chấm sáu gate của môn: gate 5 chưa qua vì chưa test với người."

**Tổng kết (slide 33).** "AI giúp nhanh và phản biện; nhóm xác định vấn đề, tự đo lại và quyết định. Việc còn lại là phản biện độc lập bằng AI khác, khảo sát thật, usability test và chạy Present trên prototype v2."

## Demo Figma Present (5 phút)

Địa điểm nhận trong demo: Kiosk Q9 · Tầng 2 (Campus Quận 9); kiosk tầng 4 và Nhà văn hóa sinh viên có ở màn Chọn Kiosk.

1. Mở Page 06, bấm Present ở một khung màn hình, rồi đổi flow trong menu. Có 17 điểm bắt đầu: F1–F13, đăng nhập, ba flow người bán.
2. **F1 (bắt đầu S02):** bấm combo → S04 → Thêm vào giỏ → S05 → Tiếp tục thanh toán → S06 → Xác nhận → màn đang tải tự chuyển → S07 mã nhận #A-204.
3. **F2 (bắt đầu S03):** S04 → Thêm vào giỏ → S05 → bấm ô mã giảm giá → S29 chọn mã → chọn mã BB20 đã hết hạn → S05 báo lỗi ngay tại ô mã.
4. **F3 (bắt đầu S06-ERR):** Tiền mặt tại Kiosk → S07-CASH → Huỷ đơn → hộp thoại xác nhận → S10 đơn đã huỷ.
5. **Người bán (K1 bắt đầu K01):** Đăng nhập → danh sách đơn → chọn đơn K03 → Nhận đơn → K04 đang chuẩn bị. **K2 (bắt đầu K05):** mã không đọc được → thu tiền mặt K06-CASH.
6. Back hoạt động, dialog ở S07 là overlay.

Trước khi trình bày: thử link Figma bằng cửa sổ chưa đăng nhập.

## Câu hỏi thầy có thể hỏi

Xem [`phan-bien-hoi-dap.md`](02-phan-bien-hoi-dap.md).
