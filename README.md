# FtaCode Mobile — Đặt món trước, nhận tại quầy
### PRM323 — Lab 2: Thiết kế UI/UX có hỗ trợ AI (Google Stitch → Figma)

> **Ăn kịp trong giờ nghỉ, không phải xếp hàng.**

| | |
|---|---|
| **Nhóm** | Group 2 |
| **Thành viên** | Nguyễn Viết Bảo — SE183398 *(lấy từ tên file trong thư mục môn học; xác nhận lại)* · `[Điền các thành viên còn lại]` |
| **Lớp** | `[Điền mã lớp]` |
| **Học kỳ** | Fall 2026 |
| **Tên repo** | `PRM323-Lab2-Group2` |
| **Cập nhật** | 20/10/2026 |
| **Figma** | [PRM323](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) *(quyền xem công khai chưa kiểm lại; mở bằng tab ẩn danh trước khi nộp)* |

## 1. Đề tài

**FtaCode Mobile** là app đặt món trước cho quán trong trường: sinh viên đặt và trả tiền từ lớp, hẹn giờ, tới quầy lấy món theo mã, không xếp hàng trong giờ nghỉ chỉ khoảng 15 phút.

- **Persona chính (proto-persona, giả định chưa kiểm chứng):** Nguyễn Minh Quân, 20 tuổi, sinh viên năm 2 ở ký túc xá, có ~15 phút giữa hai slot, dùng điện thoại một tay khi đi bộ.
- **Tiêu chí thành công (mục tiêu kiểm thử, chưa phải kết quả):** đặt xong một đơn dưới 35 giây, tối đa 8 chạm từ Trang chủ.
- **Phạm vi Lab 2:** 8 màn 360 × 800 dp, 3 user flow có nhánh lỗi, Design System bằng Figma Variables, component có variant, prototype Figma. **Không có mã nguồn Flutter** (đề: `Coding: None`).
- **Ngoài phạm vi (backlog):** 17 màn và 8 flow mở rộng đã thiết kế sẵn, xem [`design/extended-screens.md`](design/extended-screens.md). Không tính vào bài nộp.

## 2. Link thiết kế

| Page Figma | Nội dung | Node |
|---|---|---|
| 01 User Flow | Sơ đồ 3 flow bắt buộc + 8 flow mở rộng, mỗi flow có **Input → Output** | `1:6` |
| 02 Wireframe | Wireframe xám của toàn bộ màn, biến thể và màn mở rộng | `1:259` |
| 03 Final UI | 8 màn hi-fi + 7 biến thể; 17 màn mở rộng ở cuối trang | `1:260` |
| 04 Design System | Token màu, chữ, khoảng cách (Figma Variables) | `1:261` |
| 05 Components | 5 component set có variant (Button, TextField, Card/Food, NavBar, Dialog) | `1:262` |
| 06 Prototype | 3 điểm bắt đầu: Flow 1 tại S01, Flow 2 tại S03, Flow 3 tại S06 | `1:263` |

Link từng page: `https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=<node, đổi : thành ->`, ví dụ page 03: `node-id=1-260`.

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
│   ├── survey/                   │  câu hỏi khảo sát, script tạo Google Form, dữ liệu MÔ PHỎNG
│   ├── userflow/                 │  ảnh sơ đồ flow xuất từ Figma Page 01
│   └── wireframe/                │  ảnh wireframe xuất từ Figma Page 02
├── design/                       ← THIẾT KẾ GIAO DIỆN (P3 → P4)
│   ├── DESIGN.md                 │  design brief gửi AI + token
│   ├── p3-ui-concept-style-guide.md
│   ├── p4-detailed-ui-prototype.md
│   ├── screen-spec.md · design-decisions.md
│   └── extended-screens.md       │  backlog: màn S09–S25
├── ai/                           ← NHẬT KÝ AI & PHẢN BIỆN
│   ├── ai-design-log.md          │  prompt nguyên văn, vòng lặp, phản biện, quyết định D01–D42
│   ├── ai-evaluation-log.xlsx
│   └── ai-persona-interviews.md  │  phỏng vấn mô phỏng (Assumed)
├── assets/                       ← ẢNH BẰNG CHỨNG
│   ├── stitch/                   │  ảnh Google Stitch ban đầu + 3 vòng trước/sau
│   ├── concepts/                 │  3 hướng visual cho P3
│   └── figma/
│       ├── final-ui/             │  8 màn lõi + 7 biến thể
│       ├── final-ui-phase2/      │  17 màn mở rộng + ảnh tổng quan
│       └── design-system/        │  token và component
├── handoff/
│   └── flutter-handoff.md        ← BÀN GIAO CHO LẬP TRÌNH VIÊN FLUTTER
├── tests/                        ← TEST TỰ ĐỘNG PROTOTYPE (Playwright, P4/P5)
│   ├── figma-proto/              │  test bấm prototype Figma + test đồ thị flow, ảnh chuẩn
│   └── README.md                 │  cách cài và chạy
├── slides/                       ← TRÌNH BÀY
│   ├── FtaCode_Lab2_Presentation.pptx   (38 trang, bản hiện hành)
│   └── kich-ban-*.md · phan-bien-hoi-dap.md
├── docs/                         ← QUY TRÌNH & THEO DÕI TIẾN ĐỘ (không phải sản phẩm nộp)
│   ├── quy-trinh/                │  quy trình UI/UX, hướng dẫn, bảng mẫu
│   ├── tien-do/                  │  TIEN-DO, checklist sửa
│   └── test-reports/             │  báo cáo test Playwright
└── archive/                      ← BẢN CŨ, giữ làm lịch sử
    ├── slides-cu/
    └── anh-cu-giong-stitch/
```

**Quy tắc:** thư mục nào có README riêng thì xem README đó để biết từng file là gì. Ảnh trong `assets/figma/` là xuất từ Figma; ảnh flow và wireframe nằm trong `ux/` cạnh tài liệu nói về chúng.

## 4. Bàn giao theo quy trình (P0 → P5)

| Phase | Gate | Tài liệu | Tình trạng |
|---|---|---|---|
| P0 · Xác định vấn đề | G0 | [`ux/p0-problem-framing.md`](ux/p0-problem-framing.md) | ✅ 6/6 |
| P1 · Nghiên cứu | G1 | [`ux/p1-research.md`](ux/p1-research.md) · [`ux/survey/`](ux/survey/) | ⚠️ có điều kiện: chưa có phản hồi khảo sát thật |
| P2 · UX Design | G2 | [`ux/p2-ux-design.md`](ux/p2-ux-design.md) · [`ux/persona.md`](ux/persona.md) · [`ux/user-flow.md`](ux/user-flow.md) | ⚠️ 5/6: chưa walkthrough với người thật |
| P3 · UI Concept & Style Guide | G3 | [`design/p3-ui-concept-style-guide.md`](design/p3-ui-concept-style-guide.md) · [`assets/concepts/`](assets/concepts/) | ❌ chưa qua: còn nút −/+ 48 dp, chữ ≥ 14 sp, màn 412 dp |
| P4 · UI chi tiết & Prototype | G4 | [`design/p4-detailed-ui-prototype.md`](design/p4-detailed-ui-prototype.md) | ❌ chưa qua: chưa chạy thử Present, màn chưa dùng instance |
| P5 · Kiểm thử & bàn giao | G5 | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) · [`tests/`](tests/) · [`docs/test-reports/`](docs/test-reports/) | ⚠️ có handoff và test tự động prototype (13/13 đạt); chưa usability test với người |

Nhật ký AI: [`ai/ai-design-log.md`](ai/ai-design-log.md) · [`ai/ai-evaluation-log.xlsx`](ai/ai-evaluation-log.xlsx). Trình bày: [`slides/`](slides/).

## 5. Trạng thái thực tế (20/10/2026)

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| 8 màn lõi + 7 biến thể trong Figma | Đã dựng, màu đã gắn Figma Variables | `assets/figma/final-ui/` |
| 3 flow bắt buộc | Đã vẽ, có Input/Output, đã nối prototype | `ux/user-flow.md` · `ux/userflow/` |
| Wireframe | Đủ 8 màn lõi và biến thể | `ux/wireframe/` |
| Component | 5 component set có variant; **màn chưa thay bằng instance** | `assets/figma/design-system/` |
| Màn 412 dp | **Chưa dựng** | — |
| Nghiên cứu người dùng | Khảo sát Google Form đã soạn; **kết quả hiện có là mô phỏng** (nhãn Assumed) | `ux/survey/` |
| Test tự động prototype | 13/13 đạt (Playwright, 20/10); còn 2 điểm lệch giữa prototype và tài liệu | `tests/` · `docs/test-reports/playwright-prototype-2026-10-20.md` |
| Usability test với người thật | **Chưa làm** | — |
| Màn mở rộng S09–S25 | Đã thiết kế, **backlog**, chưa nối prototype | `design/extended-screens.md` |
| Code Flutter | Không có (đề không yêu cầu) | — |

**Về dữ liệu mô phỏng:** phỏng vấn SIM-A1…A5 và 20 phản hồi khảo sát SIM-S01…S20 do AI tạo để thử bộ câu hỏi và sheet phân tích. Chúng **không phải bằng chứng nghiên cứu**; file kết quả được đặt tên `…-MO-PHONG.xlsx` để không bị nhầm.

## 6. Công cụ AI đã dùng

| Công cụ | Dùng để | Vết lưu |
|---|---|---|
| **Google Stitch** | Sinh giao diện ban đầu từ `design/DESIGN.md` | `assets/stitch/` · `ai/ai-design-log.md` |
| **Gemini** | Phản biện UI theo 10 heuristics của Nielsen và WCAG | `ai/ai-design-log.md` |
| **Claude Opus 5.5** (Claude Code) | Phỏng vấn mô phỏng; các vòng phản biện (có nguyên văn); soạn và sửa tài liệu; khảo sát mô phỏng | `ai/ai-persona-interviews.md` · `ai/ai-design-log.md` Phụ lục A–G |
| **Claude Code + Figma MCP + Playwright** | Sửa file Figma: màu, Variables, component set, wireframe, sơ đồ flow, biến thể màn; viết và chạy test Playwright trên prototype | `design/p4-detailed-ui-prototype.md` · `docs/tien-do/figma-fix-checklist.md` |
| **Claude / Antigravity** | Phân tích IA, kịch bản Flutter handoff, plugin Design System | `ux/`, `design/`, `handoff/` |

Mọi quyết định thiết kế đều ghi Accept / Modify / Reject trong `ai/ai-design-log.md`; sinh viên tự đo lại các con số AI đưa ra (ví dụ tương phản chữ trắng trên cam là 2,14:1, không phải mức AI nêu).

## 7. Việc còn lại trước khi nộp

Danh sách đầy đủ: [`docs/tien-do/TIEN-DO.md`](docs/tien-do/TIEN-DO.md) và [`docs/tien-do/FIX-CHECKLIST.md`](docs/tien-do/FIX-CHECKLIST.md). Ưu tiên:

1. Thu phản hồi khảo sát **thật** (Google Form) và viết lại mục kết quả ở P1.
2. Figma: nút −/+ 48 dp, chữ nội dung ≥ 14 sp, thay nút/thẻ/nav bằng instance, dựng màn 412 dp, chạy Present cả 3 flow.
3. Chụp ảnh Stitch trước/sau từ lịch sử Stitch; xuất ảnh Figma 2×.
4. Điền họ tên và MSSV các thành viên, mã lớp.
5. Mở link Figma bằng tab ẩn danh để chắc quyền xem công khai.
