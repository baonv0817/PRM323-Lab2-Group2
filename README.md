# FtaCode Mobile — Đặt món trước, nhận tại quầy
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)

> **Ăn kịp trong giờ nghỉ, không phải xếp hàng.**

| | |
|---|---|
| **Nhóm** | Group 2 |
| **Thành viên** | Nguyễn Viết Bảo — SE183398 · Đỗ Hoàng Gia Bảo — SE193119 · Nguyễn Quốc Hoàng Pháp — SE190175 · Nguyễn Hoàng An — SE193905 · Nguyễn Thành Danh — SE193274 |
| **Lớp** | SE1919 |
| **Học kỳ** | Fall 2026 |
| **Tên repo** | `PRM323-Lab2-Group2` |
| **Cập nhật** | 21/10/2026 |
| **Figma** | [PRM323 (bản đầy đủ)](https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260) · [PRM323 (bản gốc)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) |

## 1. Đề tài

**FtaCode Mobile** là app đặt món trước cho quán trong trường: sinh viên đặt và trả tiền từ lớp, hẹn giờ, tới quầy lấy món theo mã, không xếp hàng trong giờ nghỉ chỉ khoảng 15 phút.

- **Persona chính:** Nguyễn Minh Quân, 20 tuổi, sinh viên năm 2 ở ký túc xá, có khoảng 15 phút giữa hai slot, dùng điện thoại một tay khi đi bộ.
- **Tiêu chí thành công:** đặt xong một đơn dưới 35 giây, tối đa 8 chạm từ Trang chủ.
- **Phạm vi:** 25 màn 360 × 800 dp (S01–S25) cùng các biến thể, 11 user flow có nhánh lỗi, Design System bằng Figma Variables, component có variant, prototype Figma. Không có mã nguồn Flutter (đề: `Coding: None`).

## 2. Link thiết kế

| Page Figma | Nội dung | Node |
|---|---|---|
| 01 User Flow | Sơ đồ 11 flow, mỗi flow có **Input → Output** | `1:6` |
| 02 Wireframe | Wireframe xám của toàn bộ màn và biến thể | `1:259` |
| 03 Final UI | 25 màn và biến thể. Bản cũ ở bên trái giữ để đối chiếu; **bản v2 (Final UI) lệch phải 2000 px**, tên khung có hậu tố " v2" | `1:260` |
| 04 Design System | Token màu, chữ, khoảng cách (Figma Variables) | `1:261` |
| 05 Components | Component set có variant (Button, TextField, Card/Food, NavBar, Dialog) và bộ v2 (Chip, NavBar, Card/Food, IconButton, Button) cùng 27 icon | `1:262` |
| 06 Prototype | Flow 1 bắt đầu tại S01, Flow 2 tại S03, Flow 3 tại S06 | `1:263` |

Link từng page: `https://www.figma.com/design/<file>/PRM323?node-id=<node, đổi : thành ->`, ví dụ page 03: `node-id=1-260`.

## 3. Cấu trúc thư mục

```
PRM323-Lab2-Group2/
├── README.md                     ← file này: điều hướng
├── ux/                           ← NGHIÊN CỨU & THIẾT KẾ TRẢI NGHIỆM (P0 → P2)
│   ├── p0-problem-framing.md     │  P0 · xác định vấn đề, giả định, MVP
│   ├── p1-research.md            │  P1 · nghiên cứu (khảo sát Google Form)
│   ├── p2-ux-design.md           │  P2 · user story, journey, độ phủ màn hình
│   ├── persona.md · persona-mapping.xlsx
│   ├── research.md · ai-interview-kit.md
│   ├── user-flow.md              │  IA + 11 flow (Input / Output)
│   ├── survey/                   │  câu hỏi khảo sát, script tạo Google Form, dữ liệu mô phỏng
│   ├── userflow/                 │  ảnh sơ đồ flow xuất từ Figma Page 01
│   └── wireframe/                │  ảnh wireframe xuất từ Figma Page 02
├── design/                       ← THIẾT KẾ GIAO DIỆN (P3 → P4)
│   ├── DESIGN.md                 │  design brief gửi AI + token
│   ├── p3-ui-concept-style-guide.md
│   ├── p4-detailed-ui-prototype.md
│   ├── screen-spec.md            │  đặc tả S01–S08
│   ├── screens-s09-s25.md        │  đặc tả S09–S25
│   └── design-decisions.md
├── ai/                           ← NHẬT KÝ AI & PHẢN BIỆN
│   ├── ai-design-log.md          │  prompt nguyên văn, vòng lặp, phản biện, quyết định D01–D42
│   ├── ai-evaluation-log.xlsx
│   ├── phan-bien-giao-dien/      │  phản biện giao diện trước Final UI: báo cáo đo, prompt cho AI khác, báo cáo tổng hợp
│   └── ai-persona-interviews.md  │  phỏng vấn mô phỏng
├── assets/                       ← ẢNH BẰNG CHỨNG
│   ├── stitch/                   │  ảnh Google Stitch ban đầu + 3 vòng trước/sau
│   ├── concepts/                 │  3 hướng visual cho P3
│   └── figma/
│       ├── final-ui/             │  S01–S08 và biến thể (bản cũ)
│       ├── final-ui-v2/          │  Final UI v2: 30 khung, ảnh 412 dp, ảnh tổng quan
│       ├── final-ui-s09-s25/     │  S09–S25 (bản cũ) và ảnh tổng quan
│       └── design-system/        │  token và component
├── handoff/
│   └── flutter-handoff.md        ← BÀN GIAO CHO LẬP TRÌNH VIÊN FLUTTER
├── tests/                        ← TEST TỰ ĐỘNG PROTOTYPE (Playwright, P4/P5)
│   ├── figma-proto/              │  test bấm prototype Figma + test đồ thị flow, ảnh chuẩn
│   ├── audit/                    │  chụp màn hình và đo lỗi thiết kế
│   └── README.md                 │  cách cài và chạy (có chế độ PROTO=v2)
├── slides/                       ← TRÌNH BÀY
│   ├── FtaCode_Lab2_Presentation.pptx   (38 trang)
│   └── kich-ban-*.md · phan-bien-hoi-dap.md
├── docs/                         ← QUY TRÌNH & THEO DÕI TIẾN ĐỘ
│   ├── quy-trinh/                │  quy trình UI/UX, hướng dẫn, bảng mẫu
│   ├── tien-do/                  │  TIEN-DO, checklist sửa
│   └── test-reports/             │  báo cáo test Playwright
└── archive/                      ← BẢN CŨ, giữ làm lịch sử
    ├── slides-cu/
    └── anh-cu-giong-stitch/
```

Thư mục nào có README riêng thì xem README đó để biết từng file là gì. Ảnh trong `assets/figma/` xuất từ Figma; ảnh flow và wireframe nằm trong `ux/` cạnh tài liệu nói về chúng.

## 4. Bàn giao theo quy trình (P0 → P5)

| Phase | Gate | Tài liệu | Tình trạng |
|---|---|---|---|
| P0 · Xác định vấn đề | G0 | [`ux/p0-problem-framing.md`](ux/p0-problem-framing.md) | ✅ 6/6 |
| P1 · Nghiên cứu | G1 | [`ux/p1-research.md`](ux/p1-research.md) · [`ux/survey/`](ux/survey/) | ⚠️ chưa có phản hồi khảo sát thật |
| P2 · UX Design | G2 | [`ux/p2-ux-design.md`](ux/p2-ux-design.md) · [`ux/persona.md`](ux/persona.md) · [`ux/user-flow.md`](ux/user-flow.md) | ⚠️ 5/6: chưa walkthrough với người thật |
| P3 · UI Concept & Style Guide | G3 | [`design/p3-ui-concept-style-guide.md`](design/p3-ui-concept-style-guide.md) · [`assets/concepts/`](assets/concepts/) | ✅ có bản 412 dp |
| P4 · UI chi tiết & Prototype | G4 | [`design/p4-detailed-ui-prototype.md`](design/p4-detailed-ui-prototype.md) | ⚠️ prototype v2 đã nối, chưa chạy Present |
| P5 · Kiểm thử & bàn giao | G5 | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) · [`tests/`](tests/) · [`docs/test-reports/`](docs/test-reports/) | ⚠️ có handoff và test tự động; chưa usability test với người |

Nhật ký AI: [`ai/ai-design-log.md`](ai/ai-design-log.md) · [`ai/ai-evaluation-log.xlsx`](ai/ai-evaluation-log.xlsx). Trình bày: [`slides/`](slides/).

## 5. Trạng thái (21/10/2026)

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| Final UI v2 | 32 khung trong Figma (25 màn và biến thể), có bản 412 dp; không emoji, vùng bấm ≥ 48 dp, chữ ≥ 14 sp; ảnh ở `assets/figma/final-ui-v2/` | [`ai/phan-bien-giao-dien/03-bao-cao-tong-hop.md`](ai/phan-bien-giao-dien/03-bao-cao-tong-hop.md) |
| Phản biện giao diện | Báo cáo đo A01–A15 và bảng quyết định; phản biện của AI khác chờ chạy | [`ai/phan-bien-giao-dien/`](ai/phan-bien-giao-dien/) |
| 11 flow | Đã vẽ, có Input/Output; Flow 1–3 đã nối prototype | `ux/user-flow.md` · `ux/userflow/` |
| Wireframe | Đủ các màn và biến thể | `ux/wireframe/` |
| Component | Bộ cũ 5 component set; bộ v2 thêm Chip, NavBar, Card/Food, IconButton, Button | Figma Page 05 |
| Màn 412 dp | Đã dựng cho S01–S08 và biến thể | `assets/figma/final-ui-v2/412/` |
| Nghiên cứu người dùng | Khảo sát Google Form đã soạn; kết quả hiện có là dữ liệu mô phỏng | `ux/survey/` |
| Test tự động prototype | Bản cũ 13/13 đạt (Playwright, 20/10); đồ thị flow v2 7/7 đạt | `tests/` · `docs/test-reports/playwright-prototype-2026-10-20.md` |
| Usability test với người thật | Chưa làm; có mẫu ghi kết quả | `docs/test-reports/usability-test-mau.md` |
| Code Flutter | Không có (đề không yêu cầu) | — |

Phỏng vấn SIM-A1…A5 và 20 phản hồi khảo sát SIM-S01…S20 do AI tạo để thử bộ câu hỏi và sheet phân tích; file kết quả đặt tên `…-MO-PHONG.xlsx`.

## 6. Công cụ AI đã dùng

| Công cụ | Dùng để | Vết lưu |
|---|---|---|
| **Google Stitch** | Sinh giao diện ban đầu từ `design/DESIGN.md` | `assets/stitch/` · `ai/ai-design-log.md` |
| **Gemini** | Phản biện UI theo 10 heuristics của Nielsen và WCAG | `ai/ai-design-log.md` |
| **Claude Opus 5.5** (Claude Code) | Phỏng vấn mô phỏng; các vòng phản biện (có nguyên văn); soạn và sửa tài liệu; khảo sát mô phỏng | `ai/ai-persona-interviews.md` · `ai/ai-design-log.md` Phụ lục A–G |
| **Claude Code + Figma MCP + Playwright** | Sửa và vẽ lại file Figma (màu, Variables, component, wireframe, sơ đồ flow, màn v2); viết và chạy test Playwright; đo lỗi thiết kế | `design/p4-detailed-ui-prototype.md` · `docs/tien-do/figma-fix-checklist.md` · `ai/phan-bien-giao-dien/` |
| **Claude / Antigravity** | Phân tích IA, kịch bản Flutter handoff, plugin Design System | `ux/`, `design/`, `handoff/` |

Mọi quyết định thiết kế ghi Accept / Modify / Reject trong `ai/ai-design-log.md`; sinh viên tự đo lại các con số AI đưa ra (ví dụ tương phản chữ trắng trên cam là 2,14:1).

## 7. Việc còn lại trước khi nộp

Danh sách đầy đủ: [`docs/tien-do/TIEN-DO.md`](docs/tien-do/TIEN-DO.md) và [`docs/tien-do/FIX-CHECKLIST.md`](docs/tien-do/FIX-CHECKLIST.md). Ưu tiên:

1. Chạy phản biện bằng AI khác ([`prompt`](ai/phan-bien-giao-dien/02-prompt-cho-ai-khac.md)), ghi nguyên văn vào `ai/ai-design-log.md`, chốt bảng quyết định.
2. Chạy Present cả 3 flow trên prototype v2 và cập nhật ảnh chuẩn Playwright.
3. Usability test 3–5 sinh viên ([`mẫu ghi kết quả`](docs/test-reports/usability-test-mau.md)).
4. Thu phản hồi khảo sát thật (Google Form) và viết lại mục kết quả ở P1.
5. Mở link Figma bằng tab ẩn danh để chắc quyền xem công khai.
