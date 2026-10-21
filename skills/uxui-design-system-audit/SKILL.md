---
name: uxui-design-system-audit
description: Kiểm Design System của một sản phẩm - token màu/chữ/khoảng cách/bo góc/đổ bóng có đủ và đặt tên theo vai trò, component có variant và state, màn có dùng instance thay vì hard-code, icon một bộ, nhất quán giữa màn. Dùng khi chấm G3-2, G3-5, G4-2 hoặc khi hỏi giao diện có nhất quán và bàn giao được cho dev không.
---

# Design System audit

## Cần có (foundations)
| Nhóm | Phải có |
|---|---|
| Color roles | primary, on-primary, background, surface, text-primary, text-secondary, border, success, warning, error; thêm primary-text nếu chữ nhấn khác màu nút |
| Typography | Type scale có tên (display/title/body/label), cỡ và độ đậm; chữ nội dung ≥ 14 sp |
| Spacing & grid | Thang (ví dụ 4/8/12/16/24/32), lề màn, số cột |
| Shape | Bo góc theo cấp (sm/md/lg/xl) |
| Elevation | Số cấp đổ bóng hoặc quy tắc không dùng |
| Iconography | **Một** bộ icon, kích thước chuẩn, màu theo vai trò |
| Density | Quy tắc mật độ theo thiết bị |

## Component
- Mỗi component có tên theo quy ước (`Button/Primary`) và **variant theo state**: default, hover/pressed, focus, disabled, loading, error khi áp dụng.
- Component cốt lõi cho sản phẩm có danh mục, nút, ô nhập, thẻ, thanh điều hướng, chip, dialog/sheet, danh sách, trạng thái rỗng/lỗi.

## Quy trình
1. **Token:** liệt kê biến (Figma Variables hoặc style). Token đặt tên theo **vai trò** (`color/error`), không theo giá trị (`color/red-500`) hoặc màn. Đếm màu hex xuất hiện nhưng **không** là token (hard-code).
2. **Component:** đếm instance so với frame tự dựng cho cùng chức năng (nút, thẻ, nav); nêu chỗ detach hoặc vẽ lại.
3. **Nhất quán:** lấy mẫu 5 màn, so sánh radius, font, spacing, icon, màu nút chính. Một bộ icon? Một kiểu chip chọn? Một kiểu nút chính?
4. **Vai trò màu:** màu nhấn dùng cho vai trò gì; nếu dùng cho mọi vai trò (nền, thẻ, nút, viền, giá, badge) thì ghi là lỗi phân cấp.
5. **Tái sử dụng/bàn giao:** có bảng token → code (ThemeData/CSS variables) và component → widget? Tên có dùng được ở development?
6. **Kết luận:** G3-5 (naming/tokens tái sử dụng) và G4-2 (không hard-code tuỳ tiện).

## Đạt khi
- Mọi màu, cỡ chữ, khoảng cách trên màn chính truy được về token.
- Nút, thẻ, nav, chip, ô nhập là instance của component.
- Không màn nào có kiểu riêng (radius, icon, màu) khác style guide mà không giải trình.

## Lỗi hay gặp
- Style guide chỉ gồm logo, màu thương hiệu, font.
- Mỗi màn một kiểu màu, radius, icon.
- Emoji hoặc ký tự chữ làm icon; chữ trong nút gõ tay thay vì thuộc tính component.
