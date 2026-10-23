# Ánh xạ pain point → màn hình

Mỗi pain point của người dùng được giải bằng một quyết định thiết kế và các màn hình cụ thể. Bản vẽ nằm ở Figma Page 01 (khung `MAP · Pain point → Màn hình`), ảnh ở `assets/figma/boards/pain-point-map.png`, trang trình bày ở slide 24–25.

Nguồn pain point: `ux/persona.md` và `ux/research.md`. Dữ liệu persona là giả định, chờ khảo sát thật.

| Mã | Pain point | Gặp ở | Quyết định thiết kế | Màn hình giải quyết |
|---|---|---|---|---|
| P1 | Hàng chờ đúng giờ nghỉ | Minh Quân, Mỹ Linh | Đặt từ lớp, hẹn giờ nhận, nhận bằng mã QR, không xếp hàng | S02 Trang chủ, S25 Hẹn giờ theo slot, S07 Theo dõi đơn, S20 Nhận món (QR) |
| P2 | Không biết quán còn mở, còn món, bao lâu xong | Minh Quân | Trạng thái quán và món hiện ngay, gợi ý món thay, giờ dự kiến sẵn sàng | S21 Quán đóng, S22 Món hết, S05 Giỏ hàng, S19 Thông báo |
| P3 | Ngại phí ẩn, tổng tiền chỉ hiện ở bước cuối | Mỹ Linh | Giá cộng dồn trên nút, tổng chi tiết từ giỏ, mã giảm giá rõ ràng | S04 Chi tiết món, S05 Giỏ hàng, S29 Chọn mã giảm giá, S06 Thanh toán |
| P4 | Lỗi thanh toán làm mất giỏ hàng | Flow F3, giả định chưa kiểm chứng | Giữ giỏ hàng, thử lại hoặc trả tiền mặt tại Kiosk, báo mất kết nối | S06-ERR, S07-CASH, S30 Mất kết nối, S05 Giỏ hàng |
| P5 | Nút nhỏ, khó bấm một tay khi đi bộ | Minh Quân | Vùng bấm từ 48 dp, nút chính ở đáy màn, một nút cam mỗi màn | S02, S04, S05, S08 |
| P6 | Người bán: khách đứng chờ kiểm tra chuyển khoản, huỷ khi món đã nấu | Cô Hạnh | Đơn đã thanh toán hiện sẵn, quét QR giao món, hộp thoại từ chối đơn | K02 Danh sách đơn, K03 Chi tiết đơn, K05 Quét mã, K12 Từ chối đơn |

Cách kiểm chứng: mỗi hàng chạy được trên prototype Page 06 bằng các flow F1–F13 và K1–K3; vùng bấm và tương phản đo ở `tests/audit/`.
