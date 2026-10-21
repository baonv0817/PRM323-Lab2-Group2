# Quy chuẩn thiết kế UX/UI dùng để chấm

Tài liệu mô tả khung chấm UX/UI của dự án. Bộ skill thực hiện khung này nằm ở [`skills/`](../skills/).

## 1. Nguồn và mức độ chuẩn

| Nhóm | Nội dung | Nguồn | Bản chất |
|---|---|---|---|
| Quy trình và gate | Sáu phase P0–P5, sáu gate G0–G5, tiêu chí Critical, ngưỡng 80% | [Quality Gates PRM393](https://prm393-material.web.app/quality-gates), Guideline v1.0, 13/10/2026 | Rubric nội bộ của môn, không phải chuẩn quốc tế |
| Accessibility | Contrast 4.5:1 chữ thường, 3:1 chữ lớn và UI indicator; không chỉ dựa vào màu | W3C WCAG 2.2: 1.4.3, 1.4.11, 1.4.1 | Tiêu chuẩn quốc tế |
| Kích thước | Vùng chạm ≥ 48 dp | Material Design | Hướng dẫn của ngành |
| Kích thước | Chữ nội dung ≥ 14 sp | Chuẩn của môn | Rubric nội bộ |
| Heuristic | 10 heuristic của Nielsen | [NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/), Nielsen và Molich 1990, tinh chỉnh 1994 | Quy tắc kinh nghiệm (rules of thumb), không phải tiêu chuẩn |
| Màn hình | UI Simplicity Checklist 20 tiêu chí × 5 điểm | Tài liệu quy trình của dự án, tham khảo NN/g, Carbon, Material, Apple, Fiori, WCAG | Rubric của môn và dự án |
| Phương pháp | Khoảng 5 người cho mỗi nhóm trong test định tính; khung Discover → Define → Develop → Deliver | NN/g; Design Council | Hướng dẫn sư phạm, không bắt buộc |

Kết quả chấm vì vậy có nghĩa là "đạt yêu cầu của môn". Riêng phần contrast dựa trên tiêu chuẩn WCAG.

## 2. Sáu gate

| Gate | Phase | Tiêu chí Critical |
|---|---|---|
| G0 Problem Approval | P0 Idea Discovery | Problem statement đủ ai–vấn đề–bối cảnh–tác động; phân biệt dữ kiện/giả thuyết; kế hoạch kiểm chứng giả định |
| G1 Research Evidence | P1 UX Research | Nghiên cứu trực tiếp (hoặc giải trình); insight truy được về nguồn; cập nhật giả định P0 |
| G2 UX Design | P2 UX Design | Persona/JTBD có evidence; mọi tác vụ ưu tiên có flow đủ điểm đầu, cuối, lỗi; IA và wireframe low-fi cho MVP |
| G3 Visual Direction | P3 UI Concept | ≥ 2 visual direction; style guide đủ color roles, type, spacing, grid, density, states; contrast và vùng chạm và cỡ chữ đạt |
| G4 UI Design | P4 UI Design | Flow MVP đủ màn hi-fi và prototype đi hết tác vụ; dùng đúng style guide; đủ empty/loading/error/success/disabled |
| G5 Design Release | P5 Validation | Usability test với người đại diện (hoặc ngoại lệ); không còn blocker; findings theo task có retest; bàn giao đủ |

Mỗi gate có 6 tiêu chí; danh sách đầy đủ và cách kiểm nằm trong từng skill `uxui-gate-g*`.

## 3. Cách tính điểm

- Mỗi tiêu chí: `pass` = 1, `partial` = 0.5, `fail` = 0, `na` = bỏ khỏi mẫu (phải giải trình).
- ≥ 80% và mọi Critical đạt: **Đạt**. 70–79% và không Critical trượt: **Cần cải thiện**. < 70%: **Cần làm lại**. Có Critical trượt: **Chưa qua**, bất kể tổng điểm.
- Gate chỉ mở khi gate trước đã Approved. Việc "Approve gate" thuộc reviewer.
- UI Simplicity Checklist: màn chính cần ≥ 80/100 để đạt G4-5.

## 4. Bộ skill

| Skill | Dùng để |
|---|---|
| `uxui-quality-gates` | Điều phối chấm G0 → G5, tính điểm, viết báo cáo |
| `uxui-gate-g0-problem` … `uxui-gate-g5-validation` | Chấm từng gate |
| `uxui-accessibility-baseline` | Contrast, vùng chạm, cỡ chữ (kèm `contrast.py`) |
| `uxui-simplicity-checklist` | 20 tiêu chí cho từng màn và ba bài test phụ |
| `uxui-screen-state-coverage` | Ma trận màn × trạng thái, flow không ngõ cụt |
| `uxui-traceability` | Chuỗi Evidence → Insight → Need → Story → Flow → Screen → Test |
| `uxui-design-system-audit` | Token, component, nhất quán, hard-code |
| `uxui-heuristic-review` | Đánh giá heuristic Nielsen |

Cài đặt và cách dùng: [`skills/README.md`](../skills/README.md).

## 5. Giới hạn

- Bộ skill đề xuất kết quả; reviewer quyết định.
- Không thay phỏng vấn, quan sát, usability test với người thật.
- Số đo từ ảnh tĩnh có sai số; ưu tiên giá trị màu và kích thước lấy từ file thiết kế.
- Phần không có artefact được ghi là "không có", không suy đoán.
