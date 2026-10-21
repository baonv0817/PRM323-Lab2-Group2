---
name: uxui-simplicity-checklist
description: Chấm UI Simplicity Checklist 20 tiêu chí × 5 điểm cho từng màn hình (text, màu, mật độ và khoảng trắng, thứ bậc thị giác, nhất quán và accessibility) kèm 3 bài test phụ 5-second, grayscale, reduction. Màn chính cần ≥ 80/100 để qua G4. Dùng khi chấm chất lượng giao diện từng màn.
---

# UI Simplicity Checklist (dùng cho từng màn ở P3–P4)

20 tiêu chí × 5 điểm = 100 điểm. Mục tiêu màn chính **≥ 80**. Chấm theo thang 0 (không đạt) · 2.5 (đạt một phần) · 5 (đạt); ghi lý do cho mọi điểm dưới 5.

| Nhóm | # | Tiêu chí | Gợi ý kiểm |
|---|---|---|---|
| **A. Text & Content** (NN/g) | 1 | Tiêu đề và nhãn ngắn, dễ quét | Nhãn ≤ 3–4 từ; tiêu đề nói được việc của màn |
| | 2 | Không có đoạn giải thích dài thừa | Đoạn > 2 dòng nên bị hỏi "có cần không" |
| | 3 | Thông tin ít dùng chuyển vào chi tiết | Thông tin phụ có thu gọn/chuyển màn không |
| | 4 | Không lặp nội dung ở nhiều card | Cùng một giá/tên/trạng thái xuất hiện > 1 lần? |
| **B. Color Discipline** (Carbon, Material, Apple) | 5 | Một màu nhấn chủ đạo + bảng trung tính | Đếm số màu nhấn; có thang xám/trung tính không |
| | 6 | Không dùng màu khác nhau chỉ để trang trí card | Mỗi màu có vai trò gì |
| | 7 | Success/warning/error nhất quán | Cùng ngữ nghĩa cùng màu ở mọi màn |
| | 8 | Màu không phải cách duy nhất báo trạng thái | Kèm icon/chữ; thử thang xám |
| **C. Density & Whitespace** (Fiori, Carbon) | 9 | Mật độ hợp tác vụ và thiết bị | Số thành phần chính trên 1 màn; có cần cuộn để thấy việc chính? |
| | 10 | Khoảng cách theo spacing scale | Khoảng cách là bội của đơn vị (4/8 dp) |
| | 11 | Nhóm mục liên quan, không chia quá nhiều card | Card lồng card, mỗi mục một card |
| | 12 | Vùng chạm ≥ 48 dp, chữ ≥ 14 sp | Dùng `uxui-accessibility-baseline` |
| **D. Visual Hierarchy** (Apple, NN/g) | 13 | Nội dung quan trọng nhận ra ngay | 5-second test |
| | 14 | **Một** hành động chính nổi bật | Đếm nút nhấn mạnh cao nhất |
| | 15 | Các cấp chữ phân biệt rõ | Ít nhất 3 cấp: tiêu đề, nội dung, phụ |
| | 16 | Các phần có thứ tự, không tranh nhau | Thứ tự đọc; không hai khối cùng "hét" |
| **E. Consistency & Accessibility** (WCAG 2.2) | 17 | Component, font, spacing, icon nhất quán | So với style guide; một bộ icon |
| | 18 | Tương phản 4.5:1 / 3:1 | Dùng `contrast.py` |
| | 19 | Điều khiển có chỉ báo trạng thái rõ | Default, pressed, selected, disabled, focus |
| | 20 | Loading, empty, success, error rõ ràng | Có màn/ô cho các trạng thái |

## Ba bài test phụ (ghi kết quả, không cộng điểm)
- **5-second test:** nhìn 5 giây có nói được chức năng và hành động chính không.
- **Grayscale test:** xem ở thang xám để phát hiện phụ thuộc màu.
- **Reduction test:** bỏ chữ, card, màu trang trí mà không mất thông tin thì phần bỏ là thừa.

## Đầu ra mỗi màn
| Màn | A (20) | B (20) | C (20) | D (20) | E (20) | Tổng | Tiêu chí trượt | Việc sửa |
|---|---|---|---|---|---|---|---|---|

Kết luận gate G4-5: tất cả màn chính ≥ 80 → `pass`; một số màn 70–79 → `partial`; có màn < 70 → `fail`.

## Lưu ý
- Chấm trên ảnh/Figma thật của màn, không chấm trên mô tả.
- Ưu tiên bằng chứng đo được cho tiêu chí 12 và 18; không ước lượng bằng mắt.
- Một lỗi có thể trừ ở nhiều tiêu chí (ví dụ chữ nhỏ vừa trượt 12 vừa trượt 18); ghi rõ để không trừ lặp quá mức.
