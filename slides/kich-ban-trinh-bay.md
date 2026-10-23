# Kịch bản trình bày (deck 30 slide theo quy trình P0 → P5)

Deck: `BreakBite_Lab2_Presentation.pptx`. Slide đi đúng thứ tự quy trình thiết kế; mỗi slide có nhãn phase ở góc trên phải và dòng "Minh chứng" ở chân slide.
Đầy đủ khoảng 18 phút. Nếu chỉ có 10 phút, trình bày các slide đánh dấu ★ và bỏ qua phần còn lại.

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
| 24 | Component và responsive | P4 | 0,5 | |
| 25 | Prototype Figma | P4 | 0,4 | ★ |
| 26 | Accessibility | P5 | 0,6 | ★ |
| 27 | Kiểm thử | P5 | 0,6 | ★ |
| 28 | Bàn giao cho Flutter | P5 | 0,5 | ★ |
| 29 | Tự chấm theo Quality Gates | P5 | 0,6 | ★ |
| 30 | Tổng kết, cảm ơn | | 0,5 | ★ |

Demo Figma Present cộng thêm 5 phút (xem cuối file).

## Lời nói gợi ý theo phase

**P0 · Ideas (slide 3–5).** "Vấn đề: sinh viên chỉ có khoảng 15 phút giữa hai slot mà hàng chờ căn tin dồn đúng giờ nghỉ. Nhóm cân nhắc bốn hướng, chấm Impact nhân Feasibility, chọn app đặt trước vì gỡ được cả thời gian lẫn thông tin. AI đề xuất chuyển sang web QR, nhóm từ chối vì đề bắt buộc app mobile, nhưng giữ làm phương án dự phòng. Giả định chưa biết được xếp vào danh sách kiểm chứng ở P1."

**P1 · Research (slide 6–8).** "Kế hoạch có sáu câu hỏi nghiên cứu. Dữ liệu hiện có là phỏng vấn và khảo sát mô phỏng bằng AI, dùng để thử bộ câu hỏi, nên nhóm không coi là bằng chứng; khảo sát thật đang thu. Mỗi insight vẫn được nối tới một quyết định thiết kế, ví dụ hàng chờ dẫn tới hẹn giờ nhận."

**P2 · UX Design (slide 9–13).** "Persona chính là Minh Quân; hai persona phụ là Mỹ Linh và cô Hạnh, và một nhóm không nhắm tới. Mỗi user story có tiêu chí đo được. Kiến trúc thông tin có bốn tab cho khách và bốn tab cho người bán. Ba flow chính đều có nhánh lỗi; flow ba giữ giỏ hàng khi thanh toán lỗi. Bố cục được chốt bằng wireframe xám trước khi chọn màu."

**P3 · UI Concept (slide 14–18).** "Nhóm viết brief DESIGN.md trước, rồi dùng Google Stitch tạo bản nháp. Ba hướng visual được so sánh cùng nội dung: chọn A, mượn khối trạng thái quán của B, loại C vì nền tối kém ngoài nắng. AI phản biện bằng Nielsen và WCAG, nhóm quyết định Accept, Modify hoặc Reject; AI nêu một số sai nên nhóm tự đo lại. Kết quả là style guide có token màu, chữ, khoảng cách và component."

**P4 · UI Design (slide 19–25).** "Sau khi đo bản cũ bằng Playwright và Figma Plugin API, lỗi lớn nhất là cả màn dùng một họ cam–be cho mọi vai trò: 55% điểm ảnh, bản v2 còn 4%. Emoji về 0, vùng bấm dưới 48 dp từ 20 trên 39 về 0. Final UI gồm 30 màn khách và 15 màn người bán, mỗi màn có bản 360 và 412 dp. Prototype nối cả hai app."

**P5 · Validation (slide 26–29).** "Tương phản chữ nút là 5,23:1, vùng bấm từ 48 dp, chữ từ 14 sp. Playwright kiểm đồ thị flow và prototype; nhưng usability test với người thật mới ở mức kế hoạch. Handoff cho Flutter có bảng token và component sang widget và sáu mục cho mỗi màn. Nhóm tự chấm sáu gate của môn: gate 5 chưa qua vì chưa test với người."

**Tổng kết (slide 30).** "AI giúp nhanh và phản biện; nhóm xác định vấn đề, tự đo lại và quyết định. Việc còn lại là phản biện độc lập bằng AI khác, khảo sát thật, usability test và chạy Present trên prototype v2."

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
