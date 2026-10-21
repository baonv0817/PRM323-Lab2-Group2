---
name: uxui-heuristic-review
description: Đánh giá heuristic một giao diện theo 10 heuristic của Nielsen cộng kiểm nhanh luồng chính, ghi lỗi theo mức nghiêm trọng (Cao/Vừa/Thấp) kèm vị trí cụ thể và đề xuất sửa ngắn. Dùng ở P2 (walkthrough) và P4 (design QA) hoặc khi người dùng yêu cầu "tìm lỗi UX/UI" của một màn hay một flow.
---

# Heuristic review (Nielsen)

Nguồn: Nielsen Norman Group, "10 Usability Heuristics for User Interface Design" (https://www.nngroup.com/articles/ten-usability-heuristics/). Jakob Nielsen và Rolf Molich đề xuất năm 1990, Nielsen tinh chỉnh năm 1994; NN/g gọi đây là **quy tắc kinh nghiệm (rules of thumb)**, không phải tiêu chuẩn hay guideline cụ thể. Tên tiếng Anh chính thức xem cột dưới.

## 10 heuristic và cách hỏi
| # | Heuristic | Câu hỏi khi xem màn |
|---|---|---|
| 1 | Hiển thị trạng thái hệ thống (Visibility of System Status) | Người dùng có biết đang ở đâu, đang chờ gì, thao tác đã thành công chưa? |
| 2 | Khớp thế giới thực (Match Between the System and the Real World) | Từ ngữ, icon, thứ tự có khớp ngôn ngữ người dùng? |
| 3 | Kiểm soát và tự do (User Control and Freedom) | Có huỷ, Back, hoàn tác? Có lối thoát khỏi nhầm lẫn? |
| 4 | Nhất quán và chuẩn (Consistency and Standards) | Cùng việc có cùng cách làm, cùng tên, cùng icon? |
| 5 | Ngăn lỗi (Error Prevention) | Có chặn thao tác dễ sai, xác nhận hành động phá huỷ? |
| 6 | Nhận ra hơn nhớ lại (Recognition Rather than Recall) | Thông tin cần thiết có hiện ngay, không bắt nhớ giữa các màn? |
| 7 | Linh hoạt và hiệu quả (Flexibility and Efficiency of Use) | Đường tắt cho người quen (đặt lại, yêu thích)? |
| 8 | Tối giản thẩm mỹ (Aesthetic and Minimalist Design) | Có thông tin thừa cạnh tranh sự chú ý? |
| 9 | Giúp nhận biết, chẩn đoán, phục hồi lỗi (Help Users Recognize, Diagnose, and Recover from Errors) | Thông báo lỗi nói rõ chuyện gì và làm gì tiếp, không mất dữ liệu? |
| 10 | Trợ giúp và tài liệu (Help and Documentation) | Có chỗ hỏi/liên hệ khi kẹt? |

## Quy trình
1. Chọn tác vụ chính và chạy từ điểm bắt đầu; ghi từng bước, màn, số chạm.
2. Với mỗi màn, đi qua 10 heuristic; chỉ ghi lỗi **có thật** và chỉ rõ chỗ nào trong màn.
3. Phân mức: **Cao** (chặn hoặc gây sai nghiêm trọng, mất dữ liệu, không hoàn thành được task), **Vừa** (làm chậm, gây nhầm), **Thấp** (thẩm mỹ, góp ý).
4. Cộng kiểm accessibility nhanh bằng `uxui-accessibility-baseline` và kiểm đủ trạng thái bằng `uxui-screen-state-coverage`.
5. Kiểm tính nhất quán giữa các màn (cùng thành phần, cùng nhãn, cùng icon, tên món/trạng thái thống nhất).

## Đầu ra
| Mã | Màn | Vấn đề (cụ thể) | Heuristic số | Mức | Đề xuất sửa (1–2 câu) |
|---|---|---|---|---|---|

Cuối báo cáo: ba điểm làm tốt thật sự (nếu có căn cứ) và những điều **không** kết luận được từ ảnh tĩnh (thời gian, tương tác, số đo pixel).

## Lưu ý
- Không bịa số đo; nếu ước lượng thì nói là ước lượng.
- Một AI không thay được người dùng thật; kết quả này là giả thuyết cần kiểm bằng usability test (G5).
- Khi hai người chấm khác nhau, điểm cả hai cùng nêu đáng tin hơn; điểm chỉ một bên nêu thì kiểm lại bằng số đo.
