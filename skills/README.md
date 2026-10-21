# Bộ skill chấm UX/UI theo Quality Gates

Chấm UX/UI của một hệ thống theo quy trình P0–P5 và các gate G0–G5 của môn PRM393/PRM323
(nguồn: https://prm393-material.web.app/quality-gates, Guideline v1.0 ngày 13/10/2026).
Giải thích chuẩn và nguồn: [`docs/quy-chuan-ux-ui.md`](../docs/quy-chuan-ux-ui.md).
Ngưỡng 80%, thang điểm và mức tối thiểu là rubric nội bộ của môn, không phải chuẩn quốc tế.

## Gồm 13 skill

| Skill | Dùng để |
|---|---|
| `uxui-quality-gates` | Điều phối: chấm G0 → G5, tính điểm, viết báo cáo (kèm `score_gate.py` và mẫu báo cáo) |
| `uxui-gate-g0-problem` | G0 · Problem Approval |
| `uxui-gate-g1-research` | G1 · Research Evidence Approval |
| `uxui-gate-g2-ux-design` | G2 · UX Design Approval |
| `uxui-gate-g3-ui-concept` | G3 · Visual Direction Approval |
| `uxui-gate-g4-ui-design` | G4 · UI Design Approval |
| `uxui-gate-g5-validation` | G5 · Design Release Approval |
| `uxui-accessibility-baseline` | Contrast 4.5:1 / 3:1, vùng chạm 48 dp, chữ 14 sp (kèm `contrast.py`) |
| `uxui-simplicity-checklist` | UI Simplicity Checklist 20 tiêu chí cho từng màn, ngưỡng 80/100 |
| `uxui-screen-state-coverage` | Ma trận màn × trạng thái, kiểm flow không ngõ cụt |
| `uxui-traceability` | Chuỗi Evidence → Insight → Need → Story → Flow → Screen → Test |
| `uxui-design-system-audit` | Token, component, nhất quán, hard-code |
| `uxui-heuristic-review` | Đánh giá heuristic Nielsen, ghi lỗi theo mức |

## Cài đặt (Claude Code)

Sao chép các thư mục `uxui-*` trong thư mục `skills/` vào `~/.claude/skills/` (dùng cho mọi dự án) hoặc `<dự án>/.claude/skills/` (chỉ dự án đó).

```powershell
# Windows PowerShell, cài cho mọi dự án
Copy-Item -Recurse -Force .\skills\uxui-* "$env:USERPROFILE\.claude\skills\"
```

```bash
# macOS/Linux
cp -r skills/uxui-* ~/.claude/skills/
```

Khởi động lại phiên Claude Code; skill xuất hiện trong danh sách và được gọi theo mô tả hoặc theo tên (`/uxui-quality-gates`).

## Cách dùng

1. Mở thư mục dự án cần chấm (chứa tài liệu research, persona, flow, style guide, test, handoff) hoặc đưa link Figma/prototype.
2. Nói: *"Chấm UX/UI của hệ thống này theo uxui-quality-gates"*, hoặc từng phần:
   - *"Chấm G3 cho hệ thống này"*
   - *"Chấm UI Simplicity cho S02 và S05"*
   - *"Kiểm contrast các cặp màu trong style guide"*
   - *"Tìm lỗi heuristic của flow đặt món"*
3. Skill đọc bằng chứng thật, chấm từng tiêu chí (pass / partial / fail, có trích dẫn), tính % và kết luận gate, rồi liệt kê việc cần sửa.
4. Chạy script:
   ```bash
   python skills/uxui-quality-gates/scripts/score_gate.py skills/examples/audit-mau.json
   python skills/uxui-accessibility-baseline/scripts/contrast.py "#622B14" "#F69D39"
   ```

## Thang điểm

| Kết quả | Điều kiện |
|---|---|
| Đạt | ≥ 80% và mọi Critical đạt, gate trước đã đạt |
| Cần cải thiện | 70–79%, không Critical trượt |
| Cần làm lại | < 70% |
| Chưa qua (Critical) | Có Critical trượt, bất kể tổng điểm |

## Giới hạn
- Skill đề xuất kết quả; việc "Approve gate" thuộc reviewer/giảng viên.
- Không thay phỏng vấn, quan sát, usability test với người thật.
- Số đo từ ảnh tĩnh có sai số; ưu tiên giá trị màu và kích thước lấy từ file thiết kế.
- Chấm đúng bằng chứng có thật; phần không có artefact được ghi là "không có", không đoán.
