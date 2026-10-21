---
name: uxui-traceability
description: Kiểm chuỗi truy vết quyết định thiết kế Evidence → Insight → Persona/Need → User Story → Flow → Screen → Test Case, phát hiện mắt xích đứt, quyết định không có căn cứ, persona/story/màn mồ côi. Dùng khi chấm G1, G2, G4, G5 hoặc khi cần bảo vệ quyết định thiết kế.
---

# Traceability

**Chuỗi mẫu:** Evidence ID → Insight ID → Persona/Need → User Story → Flow → Screen → Test Case.
Mã định danh khuyến nghị: `E` evidence · `INS` insight · `P` persona · `US` story · `F` flow · `S` screen · `T` test. Một số dự án dùng thêm `D` cho quyết định thiết kế.

## Quy trình
1. **Thu bảng/ma trận truy vết** của dự án (nếu có); nếu không, dựng từ tài liệu: persona, insight, story, flow, màn, test.
2. **Kiểm tiến** (từ evidence đi xuống): mỗi insight quan trọng dẫn tới ít nhất một need/persona, story, flow, màn, test? Ghi insight "treo" (không dẫn tới thiết kế).
3. **Kiểm lùi** (từ màn đi lên): chọn ngẫu nhiên 5 màn hoặc quyết định thiết kế; truy ngược về story, need, insight, evidence. Ghi màn/quyết định **không có căn cứ**.
4. **Kiểm mồ côi:** persona không có story; story không có flow; flow không có màn; màn không thuộc flow; test không gắn story.
5. **Kiểm nhãn bằng chứng:** mắt xích nào dựa trên giả định (Assumed) mà không ghi nhãn là lỗi; mắt xích Assumed có ghi nhãn là chấp nhận được nhưng không tính là bằng chứng ở G1.
6. **Báo cáo** theo mẫu:

| Mắt xích | Số mục | Có liên kết | Đứt | Ví dụ đứt |
|---|---|---|---|---|
| Evidence → Insight | | | | |
| Insight → Need/Persona | | | | |
| Need → Story | | | | |
| Story → Flow | | | | |
| Flow → Screen | | | | |
| Screen → Test | | | | |

## Gắn vào gate
- G1-2: insight truy được về evidence.
- G2-4: quyết định chức năng nối Insight → Need → Story.
- G4-6: traceability flow → screen.
- G5-3: test case gắn task và findings.
