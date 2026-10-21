---
name: uxui-quality-gates
description: Chấm toàn bộ UX/UI của một hệ thống theo sáu Quality Gate G0–G5 (Problem, Research, UX Design, UI Concept, UI Design, Validation/Handoff) của PRM393/PRM323. Dùng khi người dùng muốn "chấm UX/UI", "review thiết kế", "kiểm gate", hoặc hỏi thiết kế đã đủ điều kiện sang phase sau chưa.
---

# Chấm UX/UI theo Quality Gates (orchestrator)

Bộ skill này chấm một hệ thống theo quy trình chuẩn hoá thiết kế sản phẩm số của môn PRM393/PRM323:
Ideas → UX Research → UX Design → UI Concept → UI Design → Validation, mỗi phase một gate G0–G5.
Nguồn: https://prm393-material.web.app/quality-gates (Guideline v1.0, 13/10/2026). Ngưỡng 80% và thang điểm là rubric nội bộ của môn, không phải chuẩn quốc tế.

## Quy tắc lõi
- AI hỗ trợ brainstorm, gom insight, wireframe, gợi ý style; **không thay** phỏng vấn người dùng, quan sát, usability test, hay quyết định phê duyệt.
- Phần nào không có bằng chứng phải gắn nhãn **giả định (Assumed)**. Khi chấm, không tính giả định là bằng chứng.
- Chỉ chấm điều quan sát được trong artefact hoặc link bằng chứng. Không suy đoán, không bịa số đo.

## Thang điểm (Chuẩn chung)
| Kết quả gate | Điều kiện |
|---|---|
| **Đạt (APPROVED đề xuất)** | ≥ 80% checklist **và** mọi tiêu chí Critical đạt, gate trước đã đạt |
| **Cần cải thiện** | 70–79%, không Critical nào trượt |
| **Cần làm lại** | < 70% |
| **Chưa qua (Critical)** | Có tiêu chí Critical trượt, bất kể tổng điểm |

Mỗi tiêu chí: `pass` = 1, `partial` = 0.5, `fail` = 0, `na` = loại khỏi mẫu (cần giải trình). Critical chỉ tính đạt khi `pass`.
Gate chỉ mở khi gate trước đã Approved; nếu bằng chứng gate trước bị thay đổi làm mất điều kiện đạt thì gate sau phải rà lại.
Ngưỡng accessibility chung: contrast chữ 4.5:1, chữ lớn và UI indicator 3:1, vùng chạm 48 dp, chữ nội dung 14 sp.

## Quy trình
1. **Xác định phạm vi và bằng chứng.** Hỏi người dùng: tên hệ thống, phase đang ở, link Figma/prototype/repo, thư mục tài liệu (research, persona, flow, style guide, test). Nếu thiếu thì ghi rõ "không có artefact" ở gate tương ứng chứ không đoán.
2. **Chọn gate cần chấm.** Mặc định chấm G0 → G5 theo thứ tự; dừng báo cáo "bị chặn" ở gate đầu tiên chưa qua. Nếu người dùng chỉ hỏi một phase, chỉ chạy skill phase đó (kèm kiểm gate trước).
3. **Chạy skill từng gate:**
   - G0 → `uxui-gate-g0-problem`
   - G1 → `uxui-gate-g1-research`
   - G2 → `uxui-gate-g2-ux-design`
   - G3 → `uxui-gate-g3-ui-concept` (dùng `uxui-accessibility-baseline`, `uxui-design-system-audit`)
   - G4 → `uxui-gate-g4-ui-design` (dùng `uxui-simplicity-checklist`, `uxui-screen-state-coverage`, `uxui-accessibility-baseline`)
   - G5 → `uxui-gate-g5-validation`
   - Xuyên suốt: `uxui-traceability` (chuỗi Evidence → Insight → Persona/Need → Story → Flow → Screen → Test).
4. **Tính điểm** bằng `scripts/score_gate.py` (xem `references/scoring.md`) hoặc tính tay theo bảng trên.
5. **Viết báo cáo** theo `references/report-template.md`: bảng tiêu chí từng gate, bằng chứng, red flags, hành động sửa có người phụ trách và hạn.

## Đầu ra bắt buộc
- Bảng mỗi gate: tiêu chí, Critical?, kết quả (pass/partial/fail), **bằng chứng cụ thể** (đường dẫn, tên màn, số đo), nhận xét.
- Tổng % và kết luận gate theo thang trên.
- Danh sách **Needs Revision**: lỗi, người chịu trách nhiệm, hạn hoàn thành; sau sửa chỉ chấm lại gate đó trừ khi thay đổi ảnh hưởng upstream.
- Mục "Không đánh giá được" cho những gì cần người thật (usability test, phỏng vấn) hoặc truy cập công cụ mà ta không có.

## Trách nhiệm
Students làm artefact và tự kiểm; reviewer/giảng viên phê duyệt; end user kiểm chứng nhu cầu; development xác nhận khả thi ở G5. Skill này **đề xuất** kết quả chấm; việc "Approve gate" thuộc reviewer.
