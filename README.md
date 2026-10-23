# BreakBite — Đặt món trước, nhận tại quầy
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)


| | |
|---|---|
| **Nhóm** | Group 2 |
| **Thành viên** | Nguyễn Viết Bảo — SE183398 · Đỗ Hoàng Gia Bảo — SE193119 · Nguyễn Quốc Hoàng Pháp — SE190175 · Nguyễn Hoàng An — SE193905 · Nguyễn Thành Danh — SE193274 |
| **Lớp** | SE1919 |
| **Học kỳ** | Fall 2026 |
| **Tên repo** | `PRM323-Lab2-Group2` |
| **Cập nhật** | 21/10/2026 |
| **Figma** | [PRM323](https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260) |



## 1. Đề tài

**BreakBite** là app đặt món trước cho quán trong trường: sinh viên đặt và trả tiền từ lớp, hẹn giờ, tới quầy lấy món theo mã, không xếp hàng trong giờ nghỉ chỉ khoảng 15 phút.

- **Persona chính:** Nguyễn Minh Quân, 20 tuổi, sinh viên năm 2 học cả ngày trên campus, chỉ có 15 phút giữa hai slot, dùng điện thoại một tay khi đi bộ.
- **Điểm nhận món:** Campus Quận 9 (kiosk tầng 2 và tầng 4) và Nhà văn hóa sinh viên (tầng 1); tên quầy, giờ mở và thời gian chờ là dữ liệu mẫu.
- **Tiêu chí thành công:** đặt xong một đơn dưới 35 giây, tối đa 8 chạm từ Trang chủ.
- **Phạm vi:** app khách 30 màn 360 × 800 dp (S01–S30) và app người bán 15 màn (K01–K15) cùng các biến thể, user flow có nhánh lỗi, Design System bằng Figma Variables, component có variant, prototype Figma. Không có mã nguồn Flutter (đề: `Coding: None`).

## 2. Link thiết kế

| Page Figma | Nội dung | Node |
|---|---|---|
| 01 User Flow | Sơ đồ flow F1–F11, mỗi flow có **Input → Output** | `1:6` |
| 02 Wireframe | Wireframe xám của toàn bộ màn và biến thể | `1:259` |
| 03 Final UI | Bản cũ ở bên trái giữ để đối chiếu; **bản v2 (Final UI) lệch phải 2000 px**, tên khung có hậu tố " v2"; bản 412 dp lệch thêm 2400 px (" v2 · 412"); app người bán ở phía dưới (y ≥ 11000) | `1:260` |
| 04 Design System | Token màu, chữ, khoảng cách (Figma Variables) | `1:261` |
| 05 Components | Component set có variant (Button, TextField, Card/Food, NavBar, Dialog) và bộ v2 (Chip, NavBar, Card/Food, IconButton, Button) cùng 27 icon | `1:262` |
| 06 Prototype | Bản chạy được bằng Present: 58 màn nối liên kết, 17 điểm bắt đầu (F1–F13, đăng nhập, người bán), kèm bảng chỉ mục | `1:263` |



## 3. Cấu trúc thư mục

Mỗi thư mục đánh số là một bước của quy trình; file trong thư mục cũng đánh số theo thứ tự đọc. Thư mục nào có `README.md` thì xem để biết từng file là gì.

```
PRM323-Lab2-Group2/
├── README.md                        
├── 00-quy-trinh/                      ← QUY TRÌNH, QUY CHUẨN, TIẾN ĐỘ
│   ├── 01-QUY-TRINH-UIUX.md           │  quy trình P0 → P5 và cổng G0 → G5
│   ├── 02-BANG-MAU.md                 │  bố cục từng bảng trong quy trình
│   ├── 03-quy-chuan-ux-ui.md          │  quy chuẩn UX/UI dùng để chấm
├── 01-P0-y-tuong/                     ← P0 · xác định vấn đề (G0)
│   └── 01-p0-problem-framing.md
├── 02-P1-nghien-cuu/                  ← P1 · nghiên cứu người dùng (G1)
│   ├── 01-p1-research.md · 02-research.md · 03-ai-interview-kit.md · 04-ai-persona-interviews.md
│   └── khao-sat/                      │  câu hỏi, script Google Form, dữ liệu mô phỏng
├── 03-P2-ux-design/                   ← P2 · persona, flow, ánh xạ pain point (G2)
│   ├── 01-persona.md · 02-persona-mapping.xlsx · 03-p2-ux-design.md
│   ├── 04-user-flow.md · 05-anh-xa-painpoint-man-hinh.md
│   └── anh/                           │  sơ đồ flow và IA xuất từ Figma
├── 04-P3-ui-concept/                  ← P3 · brief, concept, style guide (G3)
│   ├── 01-DESIGN.md
│   └── 02-p3-ui-concept-style-guide.md
├── 05-P4-ui-design/                   ← P4 · giao diện chi tiết và prototype (G4)
│   ├── 01-screen-spec.md · 02-screens-s09-s30.md · 03-kitchen-app.md
│   ├── 04-p4-detailed-ui-prototype.md · 05-design-decisions.md
│   └── 06-phan-bien-giao-dien/        │  báo cáo đo, prompt cho AI khác, báo cáo tổng hợp
├── 06-P5-kiem-thu-ban-giao/           ← P5 · kiểm thử và bàn giao (G5)
│   ├── 01-playwright-prototype-2026-10-20.md · 02-usability-test-mau.md
│   └── 03-flutter-handoff.md
├── 07-trinh-bay/                      ← SLIDE, KỊCH BẢN, CÂU HỎI PHẢN BIỆN
├── 08-ai-log/                         ← NHẬT KÝ AI (nguyên văn, bản chuẩn hóa, bảng đánh giá)
├── assets/                            ← ẢNH BẰNG CHỨNG
│   ├── stitch/ · concepts/            │  ảnh Stitch, các hướng visual
│   └── figma/                         │  final-ui-v2 (S01–S30, K01–K15, 412 dp), boards, design-system, bản cũ
├── tests/                             ← TEST TỰ ĐỘNG PROTOTYPE (Playwright) và đo lỗi thiết kế
└── skills/                            ← BỘ SKILL CHẤM UX/UI THEO QUALITY GATES G0–G5
```

## 4. Bàn giao theo quy trình (P0 → P5)

| Phase | Gate | Tài liệu | Tình trạng |
|---|---|---|---|
| P0 · Xác định vấn đề | G0 | [`01-P0-y-tuong/01-p0-problem-framing.md`](01-P0-y-tuong/01-p0-problem-framing.md) | ✅ 6/6 |
| P1 · Nghiên cứu | G1 | [`02-P1-nghien-cuu/01-p1-research.md`](02-P1-nghien-cuu/01-p1-research.md) · [`02-P1-nghien-cuu/khao-sat/`](02-P1-nghien-cuu/khao-sat/) | ✅ 6/6 |
| P2 · UX Design | G2 | [`03-P2-ux-design/03-p2-ux-design.md`](03-P2-ux-design/03-p2-ux-design.md) · [`03-P2-ux-design/01-persona.md`](03-P2-ux-design/01-persona.md) · [`03-P2-ux-design/04-user-flow.md`](03-P2-ux-design/04-user-flow.md) | ✅ 6/6 |
| P3 · UI Concept & Style Guide | G3 | [`04-P3-ui-concept/02-p3-ui-concept-style-guide.md`](04-P3-ui-concept/02-p3-ui-concept-style-guide.md) · [`assets/concepts/`](assets/concepts/) | ✅ có bản 412 dp |
| P4 · UI chi tiết & Prototype | G4 | [`05-P4-ui-design/04-p4-detailed-ui-prototype.md`](05-P4-ui-design/04-p4-detailed-ui-prototype.md) | ✅ 6/6 |
| P5 · Kiểm thử & bàn giao | G5 | [`06-P5-kiem-thu-ban-giao/03-flutter-handoff.md`](06-P5-kiem-thu-ban-giao/03-flutter-handoff.md) · [`tests/`](tests/) · [`06-P5-kiem-thu-ban-giao/`](06-P5-kiem-thu-ban-giao/) | ⚠️ có handoff và test tự động; chưa usability test với người |

Nhật ký AI: [`08-ai-log/01-ai-design-log.md`](08-ai-log/01-ai-design-log.md) · [`08-ai-log/03-ai-evaluation-log.xlsx`](08-ai-log/03-ai-evaluation-log.xlsx). Trình bày: [`07-trinh-bay/`](07-trinh-bay/).

## 5. Trạng thái (21/10/2026)

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| Final UI v2 | 58 khung 360 dp (30 màn khách, 15 màn người bán và biến thể) và 56 khung 412 dp; không emoji, vùng bấm ≥ 48 dp, chữ ≥ 14 sp; ảnh ở `assets/figma/final-ui-v2/` | [`05-P4-ui-design/06-phan-bien-giao-dien/03-bao-cao-tong-hop.md`](05-P4-ui-design/06-phan-bien-giao-dien/03-bao-cao-tong-hop.md) |
| Phản biện giao diện | Báo cáo đo A01–A15 và bảng quyết định; phản biện của AI khác chờ chạy | [`05-P4-ui-design/06-phan-bien-giao-dien/`](05-P4-ui-design/06-phan-bien-giao-dien/) |
| Flow | F1–F11 đã vẽ, có Input/Output; Flow 1–3 đã nối prototype | `03-P2-ux-design/04-user-flow.md` · `03-P2-ux-design/anh/` · Figma Page 01 |
| Wireframe | Đủ các màn và biến thể, bản xám trên Figma | Figma Page 02 · `assets/figma/boards/wireframe-s01-s30.png` |
| Component | Bộ cũ 5 component set; bộ v2 thêm Chip, NavBar, Card/Food, IconButton, Button | Figma Page 05 |
| Màn 412 dp | Đã dựng cho toàn bộ màn (trừ hai dialog) | Figma Page 03 (" v2 · 412"); ảnh mẫu ở `assets/figma/final-ui-v2/412/` |
| Nghiên cứu người dùng | Khảo sát Google Form đã soạn; kết quả hiện có là dữ liệu mô phỏng | `02-P1-nghien-cuu/khao-sat/` |
| Test tự động prototype | Bản cũ 13/13 đạt (Playwright, 20/10); đồ thị flow v2 7/7 đạt | `tests/` · `06-P5-kiem-thu-ban-giao/01-playwright-prototype-2026-10-20.md` |
| Usability test với người thật | Chưa làm; có mẫu ghi kết quả | `06-P5-kiem-thu-ban-giao/02-usability-test-mau.md` |
| Code Flutter | Không có (đề không yêu cầu) | — |



## 6. Công cụ AI đã dùng

| Công cụ | Dùng để | Vết lưu |
|---|---|---|
| **Google Stitch** | Sinh giao diện ban đầu từ `04-P3-ui-concept/01-DESIGN.md` | `assets/stitch/` · `08-ai-log/01-ai-design-log.md` |
| **Gemini** | Phản biện UI theo 10 heuristics của Nielsen và WCAG | `08-ai-log/01-ai-design-log.md` |
| **Claude Opus 5.5** (Claude Code) | Phỏng vấn mô phỏng; các vòng phản biện (có nguyên văn); soạn và sửa tài liệu; khảo sát mô phỏng | `02-P1-nghien-cuu/04-ai-persona-interviews.md` · `08-ai-log/01-ai-design-log.md` Phụ lục A–G |
| **Claude Code + Figma MCP + Playwright** | Sửa và vẽ lại file Figma (màu, Variables, component, wireframe, sơ đồ flow, màn v2); viết và chạy test Playwright; đo lỗi thiết kế | `05-P4-ui-design/04-p4-detailed-ui-prototype.md` · `05-P4-ui-design/06-phan-bien-giao-dien/` |
| **Claude / Antigravity** | Phân tích IA, kịch bản Flutter handoff, plugin Design System | `03-P2-ux-design/`, `05-P4-ui-design/`, `06-P5-kiem-thu-ban-giao/` |

Mọi quyết định thiết kế ghi Accept / Modify / Reject trong `08-ai-log/01-ai-design-log.md`; sinh viên tự đo lại các con số AI đưa ra (ví dụ tương phản chữ trắng trên cam là 2,14:1).

