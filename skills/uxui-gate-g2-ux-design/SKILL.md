---
name: uxui-gate-g2-ux-design
description: Chấm Gate G2 "UX Design Approval" (P2 UX Design & Interaction Architecture): persona/JTBD có evidence, user flow đủ điểm đầu-cuối-lỗi, IA và wireframe low-fi, liên kết Insight→Need→Story, walkthrough, trạng thái empty/loading/error. Dùng trước khi chọn ngôn ngữ hình ảnh.
---

# G2 · UX Design Approval (P2)

**Câu hỏi:** Người dùng sẽ hoàn thành tác vụ ra sao, trước khi có màu sắc và phong cách UI?

**Artefact:** Persona Set + Evidence Matrix + Prioritization · JTBD / Problem-to-Requirement Matrix · User Journey, IA/Sitemap, User Flow · Low-fi Wireframes cho luồng ưu tiên · Low-fi Clickable Prototype + Task Walkthrough Notes.

## Tiêu chí (C = Critical)

| # | Tiêu chí | Cách kiểm | Đạt khi |
|---|---|---|---|
| G2-1 **C** | **Persona/JTBD thể hiện nhóm hành vi khác nhau, truy xuất về research evidence** | Persona và Evidence Matrix | Persona khác nhau ở hành vi (không chỉ tên/tuổi/ảnh); mỗi trường quan trọng có nguồn hoặc nhãn Assumed |
| G2-2 **C** | **Mọi tác vụ ưu tiên có user flow** với điểm bắt đầu, kết thúc và trường hợp lỗi | Sơ đồ flow | 3–5 flow MVP, mỗi flow có start, end, ít nhất một nhánh lỗi/phục hồi, không ngõ cụt |
| G2-3 **C** | **IA và wireframe low-fi đủ cho luồng MVP** | IA/sitemap, wireframe | Mỗi màn trong flow có wireframe; IA cho biết màn nào cấp cao, màn con |
| G2-4 | **Quyết định chức năng liên kết Insight → Need → User Story** | Ma trận truy vết | Chọn ngẫu nhiên 3 story, truy ngược được tới insight |
| G2-5 | Có **walkthrough/kiểm thử prototype sơ bộ** và danh sách điểm cần chỉnh | Walkthrough notes | Có người đi thử (không chỉ tác giả), có danh sách chỉnh sửa |
| G2-6 | Đã xét **empty / loading / error / permission** trong luồng | Flow hoặc wireframe | Mỗi flow nêu các trạng thái này hoặc lý do không áp dụng |

## Kiểm bổ sung (dùng khi có file)
- **Flow ↔ screen:** màn nào không thuộc flow nào thì bỏ hoặc giải trình; flow nào nhắc màn không có wireframe là lỗi.
- **Số chạm đến đích** của flow chính so với mục tiêu đo lường ở P0.
- **Persona:** số lượng hợp lý (thường 3–5; Lab 2 tối thiểu 1 Primary); Primary và Secondary phân biệt rõ.

## Red flags
- Bắt đầu tô màu, làm icon trước khi user flow hoàn chỉnh.
- Nhiều persona giống nhau chỉ khác tên, tuổi, ảnh.
- Flow chỉ có "happy path".

**Chuyển tiếp:** chỉ chọn ngôn ngữ hình ảnh khi UX flow chính đã hợp lý và được reviewer chấp thuận. Dùng `uxui-traceability` để kiểm chuỗi truy vết.
