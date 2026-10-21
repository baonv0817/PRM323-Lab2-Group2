# Cách tính điểm gate

## Một gate
- 6 tiêu chí; một số đánh dấu **Critical**.
- `pass` = 1 · `partial` = 0.5 · `fail` = 0 · `na` = bỏ khỏi mẫu (phải ghi lý do).
- `phần trăm = tổng điểm / số tiêu chí tính × 100`.
- Critical đạt chỉ khi `pass` (partial không đủ).

| Phần trăm | Không có Critical trượt | Có Critical trượt |
|---|---|---|
| ≥ 80 | Đạt | Chưa qua (Critical) |
| 70–79 | Cần cải thiện | Chưa qua (Critical) |
| < 70 | Cần làm lại | Cần làm lại |

Với 6 tiêu chí, 80% nghĩa là tối thiểu 5/6 tiêu chí `pass` (hoặc 4 pass + 2 partial = 83%).

## Điều kiện APPROVED đề xuất
1. ≥ 80% checklist của gate.
2. Không bỏ qua tiêu chí Critical nào.
3. Có link bằng chứng và tên người duyệt; reviewer bấm Approve.
4. Gate trước đã Approved.
5. Nếu bằng chứng đổi làm mất điều kiện đạt, approval bị thu hồi; gate sau rà lại.

## Script
`scripts/score_gate.py` đọc JSON và in kết luận:

```json
{
  "system": "Tên hệ thống",
  "gates": {
    "G0": {"previous_approved": true, "criteria": [
      {"id": "G0-1", "critical": true, "status": "pass", "evidence": "ux/p0-problem-framing.md mục 1"},
      {"id": "G0-2", "critical": true, "status": "partial", "evidence": "..."}
    ]}
  }
}
```

```bash
python scripts/score_gate.py audit.json
```

## UI Simplicity Checklist (G4, từng màn)
20 tiêu chí × 5 điểm = 100 điểm. Màn chính cần ≥ 80. Xem skill `uxui-simplicity-checklist`.
