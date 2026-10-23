# Bộ câu hỏi khảo sát — Ăn uống trong giờ nghỉ giữa các slot

> Dùng cho P1 · UX Research. Thu thập qua Google Form, tạo tự động bằng script `ux/survey/tao-google-form.gs` (cách chạy ở cuối file).
> Nguyên tắc: hỏi **việc đã xảy ra**, không hỏi ý kiến về app đang thiết kế. Không thu họ tên, MSSV, email.

## Mục tiêu và đối tượng

| | |
|---|---|
| Mục tiêu | Trả lời RQ1–RQ5 (`ux/p1-research.md` mục 1.1) và kiểm giả định H1–H5 |
| Đối tượng | Sinh viên đang học trên trường |
| Số phản hồi mục tiêu | ≥ 30 |
| Thời gian làm | ~3 phút, 21 câu (2 câu không bắt buộc) |
| Phân phối | Nhóm lớp, nhóm khoá, nhóm ký túc xá — ghi lại kênh đã gửi |
| Ngoài phạm vi form | RQ6 (quầy, bếp) → hỏi trực tiếp nhân viên quầy |

## Câu hỏi

**Phần 0 · Đồng ý tham gia**
- **Q0.** *(bắt buộc, checkbox)* Khảo sát ẩn danh, chỉ dùng cho bài học môn PRM323. Bạn có thể dừng bất cứ lúc nào. → ☐ Tôi đồng ý tham gia

**Phần 1 · Về bạn**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q1 | Bạn là sinh viên năm mấy? | 1 lựa chọn | Năm 1 · Năm 2 · Năm 3 · Năm 4 trở lên | Phân nhóm |
| Q2 | Bạn đang ở đâu? | 1 lựa chọn | Ký túc xá · Nhà trọ gần trường · Nhà riêng / người thân · Khác | Phân nhóm P01/P02 |
| Q3 | Một ngày học bình thường bạn có mấy slot trên trường? | 1 lựa chọn | 1 · 2 · 3 · 4 trở lên | RQ1 |
| Q4 | Bạn dùng điện thoại gì? | 1 lựa chọn | Android · iPhone · Khác | Persona: thiết bị |

**Phần 2 · Giờ nghỉ giữa hai slot**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q5 | Giữa hai slot **gần nhất** của bạn có bao nhiêu phút nghỉ? | 1 lựa chọn | Dưới 10 phút · 10–15 phút · 16–20 phút · Trên 20 phút · Không nhớ | RQ1 · H1 |
| Q6 | Đi từ phòng này sang phòng học tiếp theo thường mất bao lâu? | 1 lựa chọn | Dưới 2 phút · 2–5 phút · Trên 5 phút | RQ1 |
| Q7 | Khi vừa đi vừa dùng điện thoại giữa các khu trong campus, bạn thường cầm máy thế nào? | 1 lựa chọn | Một tay · Hai tay · Không dùng khi đi bộ | Persona: thao tác một tay |
| Q8 | Lần gần nhất bạn mua đồ ăn/uống **ở trường** (căn tin, quầy, kiosk) là khi nào? | 1 lựa chọn, **rẽ nhánh** | Hôm nay · Trong tuần này · Trong tháng này · Lâu hơn · Chưa bao giờ → *chuyển tới Phần 4* | RQ2 |

**Phần 3 · Lần mua gần nhất ở trường**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q9 | Lần đó, từ lúc bắt đầu xếp hàng tới lúc cầm được món mất bao lâu? | 1 lựa chọn | Dưới 3 phút · 3–5 phút · 6–10 phút · Trên 10 phút · Không nhớ | RQ2 · H2 |
| Q10 | Trong **7 ngày qua**, bạn đã bao nhiêu lần định mua ở trường nhưng bỏ vì đông hoặc không kịp? | 1 lựa chọn | 0 · 1 · 2–3 · 4 lần trở lên | RQ2 · H2 |
| Q11 | Những lần bỏ mua đó, bạn đã làm gì? | Nhiều lựa chọn | Nhịn tới bữa sau · Mua ở ngoài cổng · Đặt app giao hàng · Ăn đồ mang theo · Không áp dụng · Khác | RQ2 |

**Phần 4 · Trước khi quyết định mua**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q12 | Lần gần nhất, **trước khi** đi mua, bạn đã biết những gì? | Nhiều lựa chọn | Quán mở hay đóng · Món nào còn · Giá · Phải chờ bao lâu · Không biết gì cả | RQ3 · H3 |
| Q13 | Mỗi thông tin dưới đây quan trọng thế nào khi bạn quyết định có đi mua hay không? | Lưới 1–5 | Hàng: Quán đang mở hay đóng · Món còn hay hết · Thời gian chờ · Tổng tiền phải trả · Khuyến mãi | RQ3 · H3 |

**Phần 5 · App và thanh toán**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q14 | Trong tháng qua bạn đã dùng app đặt đồ ăn nào? | Nhiều lựa chọn | GrabFood · ShopeeFood · beFood · Xanh SM Ngon · Không dùng · Khác | Đối thủ |
| Q15 | Lần gần nhất bạn cài một app mới là khi nào? | 1 lựa chọn | Trong tuần này · Trong tháng này · Vài tháng trước · Không nhớ | RQ4 · H4 |
| Q16 | Nếu quán ăn trong trường có app riêng để đặt trước, khả năng bạn cài là bao nhiêu? | Thang 1–5 | 1 = Chắc chắn không · 5 = Chắc chắn có | RQ4 · H4 |
| Q17 | Điều gì có thể khiến bạn **không** cài một app như vậy? | Nhiều lựa chọn | Phải đăng ký tài khoản · Tốn bộ nhớ · Ít khi mua ở trường · Đã có app khác · Lo về thanh toán · Không có lý do · Khác | RQ4 · H4 |
| Q18 | Khi mua đồ ăn ở trường, bạn thường trả bằng gì? | Nhiều lựa chọn | Tiền mặt · Chuyển khoản / QR ngân hàng · Ví điện tử (MoMo, ZaloPay…) · Thẻ | RQ5 |
| Q19 | Bạn đã từng bị **lỗi khi thanh toán online** lúc mua đồ ăn chưa? | 1 lựa chọn, **rẽ nhánh** | Có · Không → *chuyển tới Phần 7* | RQ5 · H5 |

**Phần 6 · Lần thanh toán lỗi gần nhất**

| # | Câu hỏi | Kiểu | Lựa chọn | Dùng cho |
|---|---|---|---|---|
| Q20 | Lần gần nhất bị lỗi, bạn đã làm gì? | 1 lựa chọn | Thử lại cách cũ · Đổi sang cách trả khác · Trả tiền mặt · Bỏ đơn · Khác | RQ5 · H5 |

**Phần 7 · Kết thúc**
- **Q21.** *(không bắt buộc, đoạn văn)* Kể ngắn lần gần nhất bạn không kịp ăn hoặc uống trong giờ nghỉ: chuyện gì xảy ra?
- **Q22.** *(không bắt buộc, câu ngắn)* Bạn có muốn nói chuyện thêm 5 phút không? Nếu có, để lại Zalo hoặc email. Thông tin này chỉ dùng để liên hệ phỏng vấn và sẽ xoá sau khi xong bài.

## Cách đọc kết quả

| Giả định | Đạt khi | Câu hỏi |
|---|---|---|
| H1 Giờ nghỉ ≤ 15 phút | ≥ 50% chọn "Dưới 10" hoặc "10–15 phút" | Q5 |
| H2 Hàng chờ làm bỏ mua | ≥ 40% có ít nhất 1 lần bỏ mua trong 7 ngày; thời gian chờ thường gặp ≥ 6 phút | Q9, Q10 |
| H3 Biết trước trạng thái quyết định việc mua | "Quán mở/đóng" và "Thời gian chờ" có điểm trung bình ≥ 4/5 | Q12, Q13 |
| H4 Chấp nhận cài app | ≥ 50% chọn 4–5; xem lý do từ chối phổ biến nhất | Q16, Q17 |
| H5 Lỗi thanh toán → trả tiền mặt | "Trả tiền mặt" hoặc "Đổi cách trả" là lựa chọn phổ biến nhất | Q20 |

- **Ngưỡng do nhóm đặt ra** để quyết định, không phải chuẩn thống kê.
- Sau khi có dữ liệu: đổi nhãn các ý được xác nhận từ **Assumed → Reported**, ghi số phản hồi và ngày vào `ux/p1-research.md`.
- So sánh nhóm ở KTX với nhóm ở trọ (Q2) để kiểm tra persona P01 và P02.

**Giới hạn cần ghi khi báo cáo:**
- Mẫu thuận tiện (bạn bè, nhóm lớp), không đại diện cho toàn trường.
- Câu hỏi tự khai, dễ sai do nhớ không chính xác.
- Q16 hỏi về ý định, không phải hành vi thật.

## Tạo Google Form (khoảng 2 phút)

1. Mở <https://script.google.com> bằng tài khoản Google của bạn → **New project**.
2. Xoá nội dung mẫu, dán toàn bộ file `ux/survey/tao-google-form.gs`.
3. Bấm **Run** (hàm `taoFormKhaoSat`). Lần đầu Google sẽ hỏi quyền tạo Form và Sheet trong Drive của bạn → **Allow**.
4. Mở **Execution log**: có 3 link — link gửi người làm khảo sát, link sửa form, link Google Sheet chứa câu trả lời.
5. Mở link sửa form, xem lại một lượt, rồi gửi link khảo sát vào nhóm lớp.

## Nạp dữ liệu thử vào Google Sheet (tuỳ chọn)

- Trong cùng project Apps Script: **+ → Script**, dán `ux/survey/nap-du-lieu-mo-phong.gs`, chọn hàm `napDuLieuMoPhong` → **Run**.
- Script tạo sheet `SIM_MoPhong` (20 phản hồi mô phỏng) và `PhanTich` (công thức H1–H5). Sheet câu trả lời thật của form **không bị đụng tới**.
- Khi có phản hồi thật: ở `PhanTich`, đổi ô B1 sang sheet câu trả lời của form là kết quả tự tính lại. Xoá `SIM_MoPhong` trước khi nộp hoặc chia sẻ.
