---
name: uxui-gate-g0-problem
description: Chấm Gate G0 "Problem Approval" (P0 Idea Discovery & Problem Framing) cho một hệ thống: problem statement, phân biệt dữ kiện/giả thuyết, phương án ý tưởng, nhóm người dùng, MVP và kế hoạch kiểm chứng. Dùng khi người dùng muốn kiểm tra vấn đề đã rõ chưa trước khi nghiên cứu.
---

# G0 · Problem Approval (P0)

**Câu hỏi của gate:** Đang giải quyết vấn đề gì, cho ai và vì sao đáng giải quyết? Chưa vẽ UI chi tiết ở phase này.

**Artefact cần có:** Idea backlog/Idea Board · Problem Statement + Opportunity Brief (1 trang) · Stakeholder & User Group Map sơ bộ · Assumption/Risk Log và MVP Scope.

## Tiêu chí (C = Critical)

| # | Tiêu chí | Cách kiểm | Đạt khi |
|---|---|---|---|
| G0-1 **C** | Problem statement xác định cụ thể **ai – vấn đề – bối cảnh – tác động** | Đọc statement; tìm đủ 4 phần | Cả 4 phần có, không chứa giải pháp ("app giúp…") trá hình |
| G0-2 **C** | Phân biệt **dữ kiện, giả thuyết, ý kiến chủ quan** | Tìm bảng Fact/Hypothesis/Unknown hoặc nhãn tương đương | Mỗi giả định quan trọng có nhãn; dữ kiện có nguồn |
| G0-3 | Có **≥ 2 phương án ý tưởng** được cân nhắc | Idea backlog | ≥ 2 hướng, có lý do chọn (Impact × Feasibility hoặc tương đương) |
| G0-4 | Có **nhóm người dùng mục tiêu và stakeholder** sơ bộ | User/Stakeholder map | Nêu nhóm chính, nhóm phụ, ai ra quyết định |
| G0-5 | Có **phạm vi MVP, giới hạn, rủi ro, mục tiêu đo lường** sơ bộ | MVP scope, risk log | Có phần "trong/ngoài phạm vi" và ít nhất một chỉ số đo được |
| G0-6 **C** | Có **kế hoạch học hỏi/kiểm chứng** giả định lớn ở P1 | Research backlog | Mỗi giả định lớn gắn phương pháp kiểm chứng |

## Red flags
- "App này hay" nhưng không có vấn đề người dùng rõ ràng.
- Đã tạo 20 màn hình trước khi hiểu ai sẽ dùng.
- Problem statement là mô tả tính năng.

## Cách chấm
Với mỗi tiêu chí: trích dẫn câu/đoạn làm bằng chứng và đường dẫn; nếu không tìm thấy thì `fail`, nếu có nhưng thiếu một phần (ví dụ có bối cảnh nhưng không có tác động) thì `partial`. Tính điểm bằng `uxui-quality-gates`.
Nếu đọc được nhiều ý tưởng nhưng không có lý do chọn, G0-3 là `partial`.

**Chuyển tiếp:** chỉ sang nghiên cứu khi vấn đề và giả định đã rõ.
