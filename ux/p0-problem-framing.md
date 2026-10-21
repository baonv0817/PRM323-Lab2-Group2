# P0 · Problem Framing

> FtaCode Mobile · PRM323 Lab 2 · Gate G0 · Ngày lập: 19/10/2026

## 1. Problem statement

> **Sinh viên ở ký túc xá có lịch học dày thường không mua kịp đồ ăn trong giờ nghỉ ngắn giữa hai slot, khi hàng chờ ở căn tin dồn đúng giờ nghỉ chung, nên họ bỏ bữa hoặc vào lớp trễ.**

**How might we:** Làm sao để sinh viên có đồ ăn trong giờ nghỉ ngắn mà không phải xếp hàng?

| Chỉ số | Mục tiêu |
|---|---|
| Tác vụ | Đặt xong một đơn < 35 giây, ≤ 8 chạm (Flow 1, người đã dùng app) |
| Kết quả (giả thuyết, ngoài phạm vi Lab 2) | Giảm số lần sinh viên bỏ mua vì hàng chờ |

## 2. Các hướng đã cân nhắc

| Hướng | Impact | Feasibility | Điểm | Lý do |
|---|:---:|:---:|:---:|---|
| **A · App đặt trước, nhận tại quầy** | 5 | 4 | **20** | Gỡ cả pain point thời gian lẫn thông tin; khớp phạm vi Lab 2 (app mobile, handoff Flutter) |
| B · Web đặt món qua QR | 4 | 3 | 12 | Không cần cài app; nhưng không khớp yêu cầu app mobile 360 × 800 dp |
| C · Hàng chờ ảo + màn hình gọi số | 3 | 3 | 9 | Bớt đứng xếp hàng, nhưng không rút ngắn thời gian chờ món |
| D · Chatbot Zalo / Messenger | 2 | 2 | 4 | Khó tuỳ chỉnh topping và hiển thị trạng thái đơn |

**Chọn A.** Giữ B làm phương án dự phòng cho rủi ro "sinh viên ngại cài app" (R2).

## 3. Người dùng và stakeholder

| Nhóm | Ai | Phạm vi |
|---|---|---|
| Dùng trực tiếp | Sinh viên ở KTX, giờ nghỉ ngắn (P01, Primary) · sinh viên nhạy cảm về giá (P02, Secondary) | Trong phạm vi |
| Hỗ trợ | Nhân viên quầy (P03, Supporting) · chủ quán | App phía quầy ngoài phạm vi |
| Ngoài phạm vi | Sinh viên ít lên trường / mang cơm · giảng viên · cổng thanh toán | — |
| Dễ bị bỏ sót | Sinh viên không có tài khoản ngân hàng · sinh viên dùng trình đọc màn hình | Ghi vào backlog |

## 4. Giả định và rủi ro

Theo chuẩn của môn: **Fact** = Observed/Reported · **Hypothesis** = Inferred · **Unknown** = Assumed.

| ID | Nội dung | Loại | Kiểm bằng cách nào | Ưu tiên |
|---|---|---|---|---|
| H1 | Giờ nghỉ giữa hai slot ≤ 15 phút | Unknown | Khảo sát Google Form (Q5) | Cao |
| H2 | Hàng chờ giờ nghỉ làm sinh viên bỏ mua | Unknown | Khảo sát Google Form (Q9–Q10) | Cao |
| H3 | Biết trước trạng thái quán quyết định việc đặt | Hypothesis | Khảo sát Google Form (Q12–Q13) | Vừa |
| H4 | Sinh viên chấp nhận cài app riêng của quán | Unknown | Khảo sát Google Form (Q15–Q17) | Cao |
| H5 | Khi thanh toán lỗi, sinh viên muốn trả tiền mặt | Unknown | Phỏng vấn | Vừa |
| H6 | Quầy cần mã lớn + QR để trả món nhanh | Unknown | Hỏi nhân viên quầy | Vừa |
| H7 | Bếp làm kịp đơn đặt trước dồn vào giờ nghỉ | Unknown | Hỏi chủ quán | Cao |

| ID | Rủi ro | Cách giảm |
|---|---|---|
| R1 | Persona chưa kiểm chứng với người thật | Gắn nhãn Assumed; kế hoạch phỏng vấn ở P1 |
| R2 | Sinh viên ngại cài thêm app | Giữ hướng B (web đặt qua QR) làm phương án dự phòng |
| R3 | Bếp quá tải giờ nghỉ | Thời gian ước tính theo số đơn; quầy có thể tạm dừng nhận đơn |
| R4 | Thanh toán online lỗi khi mạng yếu | Flow 3: giữ giỏ hàng, cho trả tiền mặt |

## 5. Phạm vi MVP

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| App khách S01–S30 và app người bán K01–K13 · nhận tại quầy · QR / ví / tiền mặt · theo dõi đơn 4 bước · light theme · 360 × 800 dp, kiểm 412 dp | Giao hàng tận nơi · đăng nhập tích điểm · dark mode · thiết kế tablet · code Flutter |

## 6. AI phản biện và quyết định

Claude Opus 5.5, 19/10/2026. Prompt và câu trả lời nguyên văn: `ai/ai-design-log.md` Phụ lục C.

| Phát hiện | Quyết định |
|---|---|
| Problem statement cũ chứa giải pháp ("đặt trước và nhận tại quầy") | **D18 Modify:** chỉ mô tả vấn đề, thêm câu How might we |
| Chỉ số chỉ đo tốc độ thao tác, không đo vấn đề gốc | **D19 Accept:** thêm chỉ số kết quả (giả thuyết) |
| Nên cân nhắc chuyển sang web QR (hướng B) | **D20 Reject:** đề yêu cầu app mobile + handoff Flutter; giữ B làm dự phòng |
| Thiếu giả định về năng lực bếp | **D21 Accept:** thêm H7, R3 |
| "Căn tin đông giờ nghỉ" đang coi như sự thật | **D22 Accept:** xếp vào Unknown (gộp H2) |

## 7. Gate G0

| Điều kiện | Kết quả |
|---|:---:|
| **[C]** Problem statement đủ ai – vấn đề – bối cảnh – tác động | ✅ |
| **[C]** Phân biệt dữ kiện, giả thuyết, ý kiến | ✅ |
| ≥ 2 phương án ý tưởng đã cân nhắc | ✅ |
| Có nhóm người dùng và stakeholder | ✅ |
| Có phạm vi MVP, rủi ro, mục tiêu đo | ✅ |
| **[C]** Có kế hoạch kiểm chứng giả định ở P1 | ✅ |

**6/6 — đạt.**
