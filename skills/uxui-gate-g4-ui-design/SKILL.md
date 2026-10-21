---
name: uxui-gate-g4-ui-design
description: Chấm Gate G4 "UI Design Approval" (P4 Detailed UI Design & Prototyping): flow MVP có đủ màn hi-fi và prototype đi hết tác vụ, dùng đúng style guide/component, đủ state, responsive, UI Simplicity ≥80, UI QA log và traceability. Dùng khi cần kiểm chất lượng giao diện chi tiết và prototype.
---

# G4 · UI Design Approval (P4)

**Câu hỏi:** Mọi luồng ưu tiên đã đủ màn hình, state, responsive và nhất quán chưa?

**Artefact:** Hi-fi Screens & Responsive Variants · Component Library + interaction & state specs · Clickable High-fidelity Prototype · Screen/State Coverage Matrix · UI QA Checklist + Design Change Log.

## Tiêu chí (C = Critical)

| # | Tiêu chí | Cách kiểm | Đạt khi |
|---|---|---|---|
| G4-1 **C** | **Mọi user flow MVP có đủ màn hi-fi và prototype đi hết tác vụ** | Mở prototype, chạy từng flow từ điểm bắt đầu | Mỗi flow đi tới đích; có nhánh lỗi/phục hồi; không màn cụt, không màn mồ côi; Back hoạt động |
| G4-2 **C** | **Dùng đúng App Style Guide / component, không hard-code tuỳ tiện** | `uxui-design-system-audit` | Màu, chữ, khoảng cách gắn token/variable; màn dùng instance của component; không detach hàng loạt |
| G4-3 **C** | **Đủ empty / loading / error / success / disabled**, không chỉ happy path | `uxui-screen-state-coverage` | Ma trận màn × state; mỗi ô có màn hoặc lý do không áp dụng |
| G4-4 | **Responsive variant** và kiểm với nội dung thực tế | Ảnh 360/412 (hoặc theo dự án), tên dài, số lớn | Có variant hoặc hành vi co giãn rõ; không tràn, không cuộn ngang ngoài ý muốn |
| G4-5 | **Màn chính ≥ 80 điểm UI Simplicity Checklist** | `uxui-simplicity-checklist` cho từng màn chính | Mỗi màn chính ≥ 80/100; nêu tiêu chí trượt |
| G4-6 | Có **UI QA log, traceability flow → screen, danh sách tồn đọng** | Change log, QA log | Có log ghi thay đổi và lỗi còn lại; mỗi flow nối tới màn |

## Cách kiểm prototype
1. Liệt kê flow và điểm bắt đầu; chạy lần lượt, ghi **số chạm** và màn cụt.
2. Với prototype Figma có thể dùng tự động hoá (ví dụ Playwright bấm theo toạ độ vùng bấm) để chứng minh lặp lại được; kết quả này **không thay** usability test.
3. Kiểm vùng bấm: mọi điều khiển tương tác ≥ 48×48 dp.

## Red flags
- UI nhiều màu và card trang trí vì AI sinh tự do.
- Prototype chỉ điều hướng giữa trang chính, không hoàn thành được task.
- Chỉ có màn "đẹp", thiếu màn lỗi/rỗng/tải.

**Chuyển tiếp:** sang testing khi prototype đại diện đủ chức năng để người dùng thực hiện nhiệm vụ.
