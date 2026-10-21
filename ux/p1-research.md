# P1 · UX Research

> BreakBite · PRM323 Lab 2 · Gate G1 · Ngày lập: 19/10/2026
> Dữ liệu người dùng hiện có là **phỏng vấn mô phỏng bằng AI** (mã SIM-A1…A5). Theo chuẩn của môn, đây không phải bằng chứng nghiên cứu: mọi ý từ nguồn này gắn nhãn **Assumed**.
> Phương pháp nghiên cứu chính là **khảo sát Google Form** (`ux/survey/`). Form đã chạy thử bằng dữ liệu mô phỏng; đang thu phản hồi thật.

## 1. Kế hoạch nghiên cứu

### 1.1 Câu hỏi nghiên cứu

| RQ | Câu hỏi | Kiểm giả định | Phương pháp | Trạng thái |
|---|---|---|---|---|
| RQ1 | Giữa hai slot có bao nhiêu phút, làm gì trong lúc đó? | H1 | Khảo sát Google Form (Q3, Q5–Q7) | Chưa làm |
| RQ2 | Hàng chờ giờ nghỉ dài bao lâu, có làm bỏ mua không? | H2 | Khảo sát Google Form (Q8–Q11) | Chưa làm |
| RQ3 | Cần biết gì trước khi quyết định mua? | H3 | Khảo sát Google Form (Q12–Q13) | Chưa làm |
| RQ4 | Có chịu cài app riêng của quán không? | H4 | Khảo sát Google Form (Q15–Q17) | Chưa làm |
| RQ5 | Lần thanh toán lỗi gần nhất đã xử lý thế nào? | H5 | Khảo sát Google Form (Q18–Q20) | Chưa làm |
| RQ6 | Quầy trả món thế nào, có kịp đơn dồn giờ nghỉ không? | H6, H7 | Hỏi trực tiếp nhân viên quầy | Chưa làm |
| — | Tạo giả thuyết về người dùng | — | Phỏng vấn mô phỏng AI (5 nhân vật) | ✅ 17/10/2026 |

**Người tham gia dự kiến:**
- Khảo sát online: ≥ 30 sinh viên, gửi qua nhóm lớp, nhóm khoá, nhóm ký túc xá. Câu Q2 (nơi ở) dùng để tách nhóm P01 / P02.
- 1 nhân viên quầy cho RQ6.
- Mẫu thuận tiện, không đại diện cho toàn trường.

**Đồng ý tham gia:** câu đầu tiên của form là xác nhận đồng ý; khảo sát ẩn danh (không thu họ tên, MSSV, email); có thể dừng bất cứ lúc nào. Liên hệ (Zalo/email) để phỏng vấn thêm là không bắt buộc và xoá sau khi xong bài.

### 1.2 Bộ câu hỏi khảo sát

Đầy đủ 22 câu, rẽ nhánh và ngưỡng đọc kết quả cho H1–H5: `ux/survey/khao-sat-cau-hoi.md`. Form được tạo bằng script `ux/survey/tao-google-form.gs`.

| Phần | Nội dung | RQ |
|---|---|---|
| 0–1 | Đồng ý; năm học, nơi ở, số slot/ngày, loại điện thoại | Phân nhóm |
| 2 | Số phút nghỉ giữa hai slot gần nhất, thời gian di chuyển, cách cầm máy | RQ1 |
| 3 | Lần mua gần nhất: thời gian chờ, số lần bỏ mua trong 7 ngày, làm gì thay thế | RQ2 |
| 4 | Đã biết gì trước khi mua; mức quan trọng của từng thông tin (1–5) | RQ3 |
| 5 | App đặt đồ ăn đang dùng; lần cài app gần nhất; khả năng cài, lý do không cài; cách trả tiền | RQ4, RQ5 |
| 6 | Lần thanh toán lỗi gần nhất đã xử lý thế nào (chỉ hiện nếu từng bị lỗi) | RQ5 |
| 7 | Kể lại một lần không kịp ăn (không bắt buộc) | Bổ sung định tính |

Nguyên tắc: hỏi về **lần gần nhất / 7 ngày qua**, không hỏi "bạn có muốn app…". Chỉ Q16 hỏi ý định và được ghi là giới hạn.

## 2. Bằng chứng

| Mã | Nguồn | Nội dung |
|---|---|---|
| SIM-A1…A5 | `ai/ai-persona-interviews.md` | 5 sinh viên mô phỏng — chỉ để tạo giả thuyết |
| SIM-S01…S20 | `ux/survey/ket-qua-khao-sat-MO-PHONG.xlsx` | 20 phản hồi khảo sát **mô phỏng** — chỉ để thử form và sheet phân tích |

### 2.1 Kết quả khảo sát thử (dữ liệu mô phỏng)

> ⚠️ AI tạo 20 phản hồi ngày 20/10/2026 **theo hướng ủng hộ giả định của nhóm**, nên các con số dưới đây không chứng minh được gì. Nhãn vẫn là **Assumed**. Mục đích: kiểm tra form, ngưỡng và sheet phân tích trước khi gửi khảo sát thật.

| Giả định | Kết quả (n = 20) | Ngưỡng | Kết luận thử |
|---|---|---|:---:|
| H1 Giờ nghỉ ≤ 15 phút | 65% | ≥ 50% | Đạt |
| H2 Bỏ mua ≥ 1 lần / 7 ngày | 61% (11/18 người từng mua) | ≥ 40% | Đạt |
| H2 Chờ ≥ 6 phút | 61% | ≥ 50% | Đạt |
| H3 Mức quan trọng: quán mở/đóng · thời gian chờ | 4,35 · 4,50 / 5 | ≥ 4 | Đạt |
| H4 Chọn 4–5 khả năng cài app | 55% (TB 3,5) | ≥ 50% | Đạt sát ngưỡng |
| H5 Lỗi thanh toán → tiền mặt / đổi cách trả | 67% (6/9) | ≥ 50% | Đạt |

**Những điểm đáng chú ý nếu khảo sát thật cho ra kết quả tương tự:**
- Không ai biết trước "phải chờ bao lâu" (0/20), và 35% không biết gì trước khi đi mua. Điều này củng cố khối trạng thái quán ở S02.
- Lý do không cài app phổ biến nhất là **phải đăng ký tài khoản** (9/20), nên cần đăng nhập nhanh hoặc cho xem menu mà không cần tài khoản.
- Nhóm ở nhà riêng gần như không cài app (0/4 chọn 4–5), trong khi KTX là 67% và trọ là 71%. Persona chính nên giữ là P01.
- 65% cầm máy một tay khi đi bộ, nên đặt nút chính ở nửa dưới màn hình.

## 3. Insight

Bảng gom ý (affinity) đầy đủ: `ux/research.md` mục 3.

| Mã | Insight | Nguồn | Tin cậy |
|---|---|---|---|
| INS-01 | Hàng chờ dồn đúng giờ nghỉ làm sinh viên bỏ mua hoặc vào lớp trễ | SIM-A1, A2, A5 | Thấp |
| INS-02 | Trước khi đi mua, sinh viên muốn biết quán mở/đóng, còn món, bao lâu xong | SIM-A1, A3, A4, A5 | Thấp |
| INS-03 | App giao hàng không giao vào được tòa nhà hay phòng lab | SIM-A1, A5 | Thấp |
| INS-04 | Sinh viên ngại phí phát sinh, muốn thấy tổng tiền sớm | SIM-A1, A2 | Thấp |
| INS-05 | Không muốn đăng ký hay cài thêm app chỉ để mua ở trường | SIM-A1, A3 | Thấp |
| INS-06 | Thanh toán lỗi mà mất giỏ hàng gây bực bội | SIM-A5 (1 nguồn) | Thấp |

**Mâu thuẫn:** SIM-A3, A4 ít ăn ở trường nên không cần app; SIM-A4 muốn trả tiền mặt, SIM-A1, A5 ưu tiên QR/ví.

## 4. Hành trình hiện tại — P01 mua đồ ăn trong giờ nghỉ

| Giai đoạn | Hết slot | Đi tới căn tin | Xếp hàng | Gọi món, trả tiền | Chờ món | Về lớp |
|---|---|---|---|---|---|---|
| Nỗi đau | Không biết tình trạng quán | Đi rồi mới biết đông / đóng | Chờ lâu nhất | Chờ quầy kiểm chuyển khoản | Không biết bao lâu xong | Vào lớp muộn |
| Cơ hội | Xem trạng thái trước | Đặt trước từ lớp | Không phải xếp hàng | Thanh toán trong app | Tiến trình đơn + giờ hẹn | Lấy theo mã |

Nhãn: **Assumed** (nguồn SIM-A1, A2, A5). Thời gian từng giai đoạn chưa đo.

## 5. Cập nhật giả định từ P0

| ID | Sau P1 | Ghi chú |
|---|---|---|
| H1, H2, H5, H6, H7 | Vẫn Unknown | Chưa có bằng chứng thật; khảo sát thử (SIM-S) không tính là bằng chứng |
| H3 | Hypothesis | 4/5 nhân vật mô phỏng nhắc tới |
| H4 | Unknown, rủi ro tăng | SIM-A3 phản đối rõ |

## 6. Kết luận

**Nhu cầu ưu tiên chuyển sang P2:**
1. Có đồ ăn mà không xếp hàng (INS-01).
2. Biết trước trạng thái quán, còn món, thời gian chờ (INS-02).
3. Thấy tổng tiền sớm (INS-04).
4. Không mất đơn khi thanh toán lỗi (INS-06).

**Giới hạn:**
- Chưa phỏng vấn hay quan sát người thật.
- Người dùng mô phỏng thường nông và dễ đồng thuận hơn người thật ([tổng hợp NN/g](https://radar.zurb.com/article/nielsen-norman-synthetic-users-were-too-shallow-to-be-useful-against-three-real-studies)).
- Cùng hệ AI vừa đóng vai người dùng vừa hỗ trợ thiết kế, nên dễ thiên lệch về những gì thiết kế đã có.

## 7. AI phản biện và quyết định

Claude Opus 5.5, 19/10/2026. Nguyên văn: `ai/ai-design-log.md` Phụ lục D.

| Phát hiện | Quyết định |
|---|---|
| Mọi insight hành vi đến từ dữ liệu mô phỏng | **D23 Accept:** không bịa dữ liệu; ghi ngoại lệ Lab 2 và kế hoạch phỏng vấn |
| Flow 3 dựa trên insight chỉ có 1 nguồn | **D24 Modify:** giữ Flow 3 (đề bắt buộc flow lỗi), hạ tin cậy INS-06, thêm RQ5 |
| Thiên lệch vòng tròn | **D26 Accept:** ghi vào giới hạn |
| Câu hỏi dẫn dắt trong bộ phỏng vấn mô phỏng | **D27 Accept:** kịch bản người thật chỉ hỏi việc đã xảy ra |

## 8. Gate G1

| Điều kiện | Kết quả |
|---|:---:|
| **[C]** Nghiên cứu với người dùng phù hợp, hoặc giải trình khi chưa thể | ⚠️ Đạt theo nhánh giải trình (mục 1, 6) |
| **[C]** Insight liên kết tới ghi chép nguồn | ✅ |
| Ghi rõ phương pháp, mẫu, giới hạn, thiên lệch | ✅ |
| Có affinity map / task analysis | ✅ |
| **[C]** Đã kiểm và cập nhật giả định từ P0 | ✅ |
| Có kết luận nhu cầu ưu tiên và câu hỏi còn mở | ✅ |

**6/6 có điều kiện** — chờ reviewer chấp nhận giải trình, hoặc bổ sung kết quả khảo sát thật (≥ 30 phản hồi) theo mục 1.2.
