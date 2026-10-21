---
name: uxui-screen-state-coverage
description: Kiểm Screen/State Coverage Matrix - mỗi màn có đủ các trạng thái default, focus, disabled, error, loading, empty, success, permission (hoặc lý do không áp dụng) và mỗi flow có đủ màn, nhánh lỗi, không ngõ cụt. Dùng khi chấm G2 và G4 hoặc khi hỏi UI có chỉ có happy path không.
---

# Screen / State Coverage

## Trạng thái cần xét
`default` · `focus/pressed` · `disabled` · `error` · `loading` · `empty` · `success` · `permission` (camera, vị trí, thông báo) · `offline/mất mạng` · `nội dung dài/dữ liệu lớn`.

## Quy trình
1. **Liệt kê màn** (từ Figma hoặc danh sách màn) và **flow MVP**.
2. **Lập ma trận**: hàng = màn, cột = trạng thái. Mỗi ô: tên màn/khung có trạng thái đó, hoặc `n/a` kèm lý do ngắn (ví dụ "màn tĩnh, không tải dữ liệu").
3. **Kiểm theo loại màn:**
   - Màn danh sách/lưới: loading (skeleton), empty, error, lọc không ra kết quả.
   - Màn biểu mẫu: lỗi từng ô, disabled nút khi chưa hợp lệ, loading khi gửi, success.
   - Màn thanh toán/giao dịch: loading, lỗi và **phục hồi không mất dữ liệu**, thành công.
   - Màn dùng camera/vị trí/thông báo: permission bị từ chối.
   - Màn theo dõi trạng thái: từng bước của quy trình.
4. **Kiểm flow:**
   - Có điểm bắt đầu và kết thúc rõ.
   - Mỗi flow có ít nhất một nhánh lỗi/phục hồi.
   - Không màn cụt (không lối ra) và không màn mồ côi (không lối vào).
   - Nút Back và huỷ luôn dẫn về nơi hợp lý.
5. **Báo cáo:** tỉ lệ ô có màn/(ô áp dụng); danh sách ô thiếu xếp theo mức ảnh hưởng (thiếu lỗi thanh toán nặng hơn thiếu skeleton).

## Đạt G4-3 khi
- Mỗi màn chính có đủ error/empty/loading/success phù hợp loại màn; không chỉ happy path.
- Mọi ô `n/a` có lý do.

## Mẫu ma trận
| Màn | default | loading | empty | error | success | disabled | permission | ghi chú |
|---|---|---|---|---|---|---|---|---|
