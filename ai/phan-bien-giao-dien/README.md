# Phản biện giao diện (trước khi ra Final UI)

| File | Nội dung |
|---|---|
| [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md) | Báo cáo lỗi A01–A15: số đo (Playwright, Figma API) và nhận xét bằng mắt |
| [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md) | Ảnh cần đính kèm và prompt cho AI khác |
| [`03-bao-cao-tong-hop.md`](03-bao-cao-tong-hop.md) | Quyết định, danh sách màn Final UI, hệ thiết kế v2, số đo sau sửa, việc còn lại |
| [`anh/`](anh/) | 13 ảnh chụp từ prototype Figma (21/10/2026) và ảnh tổng quan S01–S08 |

Mã đo: `tests/audit/` (`capture.js` chụp, `figma-audit.js` đọc Figma, `measure.py` tính tỉ lệ màu và vùng bấm).

Thứ tự: lấy phản biện AI khác và lưu nguyên văn vào `ai/ai-design-log.md` → đối chiếu với báo cáo đo → điền bảng quyết định → sửa Figma → chạy lại đo và `npm test` → xuất ảnh Final UI.
