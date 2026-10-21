---
name: uxui-gate-g5-validation
description: Chấm Gate G5 "Design Release Approval" (P5 Usability Validation & Developer Handoff): usability test với người đại diện, không còn blocker, findings theo task có retest, gói bàn giao đủ, acceptance criteria và xác nhận của reviewer/dev. Dùng trước khi bàn giao thiết kế cho development.
---

# G5 · Design Release Approval (P5)

**Câu hỏi:** Người dùng có làm xong việc không, và dev có triển khai đúng được không?

**Artefact:** Test Plan & Participant/Task Log · Usability Findings & Severity-based Issue List · Design Revision & Retest Evidence · Dev Handoff Package + Accessibility/QA Notes · Design Release Record (known limitations, owners, sign-off).

## Tiêu chí (C = Critical)

| # | Tiêu chí | Cách kiểm | Đạt khi |
|---|---|---|---|
| G5-1 **C** | **Có usability test với người dùng đại diện**, hoặc lý do ngoại lệ được ghi lại | Test plan, log người tham gia | Có người thật thuộc nhóm mục tiêu thực hiện task **không được hướng dẫn từng bước**; nếu không, có đoạn ngoại lệ ký tên |
| G5-2 **C** | **Không còn blocker nghiêm trọng** trong task MVP; major có hướng xử lý | Issue list | Không P0 mở; mỗi P1 có hướng xử lý và chủ sở hữu |
| G5-3 **C** | **Findings theo task, bằng chứng, ưu tiên sửa, retest lỗi trọng yếu** | Findings, retest | Mỗi task có tỉ lệ hoàn thành, thời gian, số chạm, nguyên nhân lỗi; lỗi P0/P1 đã sửa và retest |
| G5-4 **C** | **Bàn giao đủ flow, screens, states, components, tokens, assets, interaction spec** | Handoff package | Mỗi màn có layout, component, state, tương tác, điều hướng, ràng buộc; có bảng token → code và component → widget |
| G5-5 | Có **acceptance criteria, hạn chế tồn đọng, người chịu trách nhiệm** | Release record | Danh sách tồn đọng có owner |
| G5-6 | **Reviewer/dev xác nhận** đủ rõ để triển khai | Xác nhận bằng văn bản | Có tên và ngày; dev không phải hỏi lại cơ bản |

## Phân loại issue
P0 blocker (không hoàn thành được task) · P1 major (hoàn thành nhưng vướng nhiều) · P2 minor (góp ý).

## Lưu ý
- Mức tối thiểu gợi ý: khoảng 5 người mỗi nhóm mục tiêu chính cho một vòng định tính; retest nếu có blocker.
- Kiểm thử tự động prototype và người trong nhóm xem thử **không phải** usability test.
- Nếu chưa test với người thật: G5-1, G5-3 là `fail` (hoặc `partial` nếu có kế hoạch và lý do ngoại lệ hợp lý), gate không qua.

## Red flags
- "Đã test" nhưng chỉ cho bạn bè xem rồi nhận lời khen.
- Dev phải hỏi lại kích thước, hành vi nút, component, trạng thái lỗi.

**Chuyển tiếp:** release cho development; vòng lặp tiếp tục khi có phản hồi từ bản build thực.
