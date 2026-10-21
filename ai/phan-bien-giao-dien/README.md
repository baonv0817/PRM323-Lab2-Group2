# Phản biện giao diện (trước khi ra Final UI)

Bước theo đề Lab 2: AI tìm lỗi giao diện, sinh viên quyết định, sửa Figma, rồi mới có Final UI.

| File | Nội dung |
|---|---|
| [`01-bao-cao-do-tu-dong.md`](01-bao-cao-do-tu-dong.md) | Báo cáo lỗi bằng số đo (Playwright + Figma API) và nhận xét bằng mắt; bảng quyết định để bạn điền. **Do Claude viết, không độc lập** |
| [`02-prompt-cho-ai-khac.md`](02-prompt-cho-ai-khac.md) | Bộ ảnh cần đính kèm và prompt dán nguyên văn cho **một AI khác** (Gemini, ChatGPT…) |
| [`anh/`](anh/) | 13 ảnh màn hình chụp từ prototype Figma ngày 21/10/2026 và ảnh tổng quan 8 màn lõi |

Mã đo: `tests/audit/` (`capture.js` chụp, `figma-audit.js` đọc Figma, `measure.py` tính tỉ lệ màu và vùng bấm).

**Thứ tự đề xuất:** (1) lấy phản biện của AI khác và lưu nguyên văn vào `ai/ai-design-log.md` → (2) đối chiếu với báo cáo đo → (3) điền bảng quyết định → (4) sửa Figma → (5) chạy lại đo và `npm test` → (6) xuất ảnh Final UI.
