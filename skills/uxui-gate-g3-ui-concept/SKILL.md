---
name: uxui-gate-g3-ui-concept
description: Chấm Gate G3 "Visual Direction Approval" (P3 UI Concept & App Style Guide): ≥2 visual direction, style guide có color roles/type/spacing/grid/density/states, contrast WCAG AA và vùng chạm 48dp, thứ bậc thị giác, component naming/tokens, kiểm trên thiết bị chủ đạo. Dùng trước khi nhân rộng thành nhiều màn hi-fi.
---

# G3 · Visual Direction Approval (P3)

**Câu hỏi:** Ứng dụng sẽ trông như thế nào và quy tắc nào giữ nó nhất quán?

**Artefact:** Concept Exploration Board (≥ 2 phương án) + Decision Rationale · Approved Visual Direction / 2–3 key screens · App Style Guide (foundations, tokens, component states) · UI Component Starter Library / Figma styles · Accessibility Baseline & Contrast Evidence.

## Tiêu chí (C = Critical)

| # | Tiêu chí | Cách kiểm | Đạt khi |
|---|---|---|---|
| G3-1 **C** | **≥ 2 visual direction để so sánh**, chọn concept có lý do dựa trên persona/task | Concept board, rationale | ≥ 2 hướng khác biệt thật trên **cùng một key screen**; lý do chọn nêu persona/task, không chỉ "đẹp hơn" |
| G3-2 **C** | **App Style Guide có color roles, type scale, spacing, grid, density, component states** | Style guide, trang Design System | Đủ 6 nhóm; không chỉ logo, màu thương hiệu, font |
| G3-3 **C** | **Contrast chữ thường ≥ 4.5:1; chữ lớn và UI indicator thiết yếu ≥ 3:1; vùng chạm ≥ 48×48 dp; chữ nội dung ≥ 14 sp** | `uxui-accessibility-baseline` | Có số đo cho từng cặp màu chính; không cặp nào dưới ngưỡng; ngoại lệ có giải trình |
| G3-4 | Key screens thể hiện **thứ bậc thị giác, ít chữ thừa, màu nhấn có vai trò** | Chấm nhanh bằng `uxui-simplicity-checklist` nhóm A, B, D | Mỗi màn có một hành động chính nổi bật; màu nhấn có vai trò rõ |
| G3-5 | **Component naming / tokens có thể tái sử dụng** ở P4 và development | `uxui-design-system-audit` | Token đặt tên theo vai trò (không theo màu); component có tên và variant nhất quán |
| G3-6 | Đã duyệt concept trên **kích thước thiết bị chủ đạo và nội dung dài** | Ảnh kiểm 360/412 dp, tên dài | Có ảnh ở ít nhất hai chiều rộng và một case nội dung dài |

## Red flags
- Mỗi màn một kiểu màu, radius, icon.
- App Style Guide chỉ gồm logo, màu thương hiệu và font.
- Màu nhấn dùng cho mọi vai trò (nền, thẻ, nút, viền, giá, badge).

**Chuyển tiếp:** không phát triển toàn bộ hi-fi trước khi concept và foundation được duyệt.
