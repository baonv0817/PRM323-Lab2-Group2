# Tiến độ theo quy trình — FtaCode Mobile

Cập nhật: 20/10/2026. Đối chiếu repo `PRM323-Lab2-Group2` (bản cục bộ, **chưa push**) với 45 bước trong `QUY-TRINH-DE-HIEU.md`.

**Ký hiệu**
- ✅ **Xong**
- 🟡 **Có nhưng chưa đạt** — thiếu một phần, hoặc chưa kiểm được
- ❌ **Chưa làm**
- 🔵 **Bổ sung sau** — tài liệu viết lại ngày 19/10 để chuẩn hoá theo quy trình, đã ghi rõ điều này trong file

Cột "Ai làm tiếp": **Bạn** = cần tài khoản Figma/Stitch/GitHub hoặc người thật · **Mình** = làm được trong repo.

---

## Tổng quan

| Chặng | Phase · Gate | Tình trạng |
|---|---|---|
| 0 · Chuẩn bị | — | 🟡 thiếu tên repo đúng chuẩn, tên/MSSV |
| 1 · Xác định vấn đề | P0 · G0 | ✅ đạt 6/6 (🔵) |
| 2 · Hỏi người dùng | P1 · G1 | 🟡 đạt có điều kiện — chưa có người thật |
| 3 · Persona, luồng, wireframe | P2 · G2 | ✅ 5/6, đủ Critical (🔵) — còn bạn tự đi lại flow trên Figma |
| 4 · UI bằng AI + phản biện | P3 · G3 | 🟡 có 3 concept + style guide (🔵); **chưa qua** vì Figma chưa đổi màu, chưa kiểm nội dung dài |
| 5 · Giao diện cuối + prototype | P4 · G4 | ❌ chưa qua — đủ tài liệu (🔵), nhưng Figma thiếu Loading, chưa chạy prototype, màu chưa sửa |
| 6 · Thử, bàn giao, bảo vệ | P5 · G5 | 🟡 handoff xong, chưa usability test |

---

## Chặng 0 — Chuẩn bị

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 1 | Đề tài cụ thể, thầy duyệt | 🟡 | Đề tài rõ; chưa ghi ngày duyệt | Bạn |
| 2 | Repo của nhóm | ✅ | Tên `PRM323-Lab2-Group2` | — |
| 3 | Figma 6 page đúng thứ tự | 🟡 | Đủ 6 page; file tên "Untitled" | Bạn |
| 4 | File AI log | ✅ | `ai/ai-design-log.md` | — |
| 5 | Commit đều | 🟡 | Repo này mới chỉ có 1 commit khởi tạo (lịch sử cũ nằm ở repo `prm393-lab2`); cần commit đều từ nay | Bạn |

## Chặng 1 — Xác định vấn đề (P0)

| # | Bước | Tình trạng | File |
|---|---|---|---|
| 6 | 2–3 hướng giải pháp | ✅ 🔵 | `ux/p0-problem-framing.md` mục 2 (4 hướng) |
| 7 | Chọn hướng có lý do (Impact × Feasibility) | ✅ 🔵 | mục 2 |
| 8 | Problem statement 1 câu | ✅ 🔵 | mục 1 (đã bỏ giải pháp trá hình, D18) |
| 9 | Giả định Fact / Hypothesis / Unknown | ✅ 🔵 | mục 4 (F1–F2, H1–H7, R1–R4) |
| 10 | Sơ đồ người liên quan | ✅ 🔵 | mục 3 · `ux/research.md` 5.1 |
| 11 | AI phản biện + quyết định | ✅ 🔵 | mục 6 (D18–D22) · nguyên văn ở `ai/ai-design-log.md` Phụ lục C |

## Chặng 2 — Hỏi người dùng (P1)

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 12 | Kế hoạch nghiên cứu | ✅ 🔵 | `ux/p1-research.md` mục 1 (RQ1–RQ6, consent) | — |
| 13 | Câu hỏi về hành vi đã xảy ra | ✅ 🔵 | mục 2.1 | — |
| 14 | **Hỏi 5–6 người thật** | ❌ | Mới có 5 nhân vật **mô phỏng AI** | **Bạn** |
| 15 | Quan sát hàng chờ | ❌ | Có phiếu quan sát, chưa đi đo | **Bạn** |
| 16 | Khảo sát Google Form | 🟡 | Form + sheet phân tích sẵn, đã chạy thử bằng dữ liệu mô phỏng; đang thu phản hồi thật | Bạn |
| 17 | Gom ý (affinity) | ✅ | `ux/research.md` mục 3 (từ dữ liệu mô phỏng) | — |
| 18 | Gắn nhãn bằng chứng | ✅ | SIM-A1…A5 · SIM-S01…S20 mô phỏng | — |
| 19 | AI tổng hợp | ✅ | `ai/ai-persona-interviews.md` B3 | — |
| 20 | AI phản biện nghiên cứu | ✅ 🔵 | `ux/p1-research.md` mục 7 (D23–D27) | — |

## Chặng 3 — Persona, luồng, wireframe (P2)

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 21 | Persona 12 trường + 4 mục Lab 2 | ✅ | `ux/persona.md` (P01, P02, P03) | — |
| 22 | Chỉ số thành công đo được | ✅ | < 35 giây, ≤ 8 chạm (đếm lại theo Flow 1) | — |
| 23 | Coverage matrix + bảng truy vết | ✅ | `ux/persona-mapping.xlsx` | — |
| 24 | User story | ✅ 🔵 | US01–US12 (`ux/p2-ux-design.md` mục 3) | — |
| 25 | ≥ 8 màn hình (IA) | ✅ | `ux/user-flow.md` mục 1 | — |
| 26 | ≥ 3 luồng, có nhánh lỗi | ✅ | F1–F3 (Mermaid) | — |
| 27 | Bảng luồng → màn hình | 🟡 | Có trong repo; **Figma Page 01 ghi mã màn khác repo** | Bạn |
| 28 | AI phản biện persona và flow | ✅ 🔵 | Persona (B5) + flow (`ux/p2-ux-design.md` mục 8, D28–D32) | — |
| 29 | Wireframe (Figma Page 02) | ✅ | Có | — |
| 30 | Đi thử luồng trên wireframe | 🟡 | Walkthrough do AI (mục 7); bảng đi thử ở mục 7 chờ bạn đi lại trên Figma | **Bạn** |

## Chặng 4 — UI bằng AI + phản biện (P3)

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 31 | DESIGN.md trước Stitch + nguyên tắc gắn persona | ✅ | Commit 12/10, trước Stitch; token sửa 17/10; DP1–DP8 | — |
| 32 | ≥ 2 hướng visual trên 1 màn | ✅ 🔵 | A Stitch + B, C do Claude dựng (`design/p3-ui-concept-style-guide.md`) | — |
| 33 | Prompt Stitch nguyên văn + ảnh | ✅ | `ai/ai-design-log.md` mục 2 · `assets/stitch/01–04` | — |
| 34 | 3 vòng lặp có ảnh trước/sau | 🟡 | Prompt có; **ảnh trước/sau bị trùng file** | **Bạn** |
| 35 | AI critique ≥ 5 phát hiện, nguyên văn | ✅ | Gemini (tóm tắt) + Claude (nguyên văn, Phụ lục A) | — |
| 36 | Bảng quyết định (có Reject) | ✅ | D01–D27, 2 Reject · `ai/ai-evaluation-log.xlsx` | — |
| 37 | Token bằng Variables (Page 04) | 🟡 | Page có; **chưa đổi màu theo DESIGN.md mục 2.5** | **Bạn** |
| 38 | 9 component + đủ state (Page 05) | 🟡 | Page có; chưa kiểm được variant/instance | Bạn |

## Chặng 5 — Giao diện cuối + prototype (P4)

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 39 | ≥ 8 màn Final UI dùng instance | 🟡 | Page 03 có 8 màn + biến thể; chưa áp quyết định D06, D13–D16 | **Bạn** |
| 40 | Kiểm 360 / 412 dp | ❌ | Chưa có ảnh | **Bạn** |
| 41 | Prototype 3 flow, overlay, loading, Back | 🟡 | Page 06 có; chưa chạy thử được (cần đăng nhập) | **Bạn** |
| 42 | UI checklist 20 tiêu chí, 3 bài test | 🟡 🔵 | Mức nền trên ảnh Stitch (S02 55 · S04 70 · S05 65 · S07 85 · S06-ERR 75); chấm lại trên Figma (D42) | Bạn |
| 42b | `design-decisions.md`, `screen-spec.md` | ✅ | Có, số tương phản đã sửa | — |
| 42c | Xuất PNG từ Figma vào `assets/figma/final-ui/` | 🟡 | Đã xuất từ file Figma PRM323 ngày 20/10 (1×); S03, S04, S05-EMPTY, S06-ERR là ảnh chụp độ phân giải thấp; bản sao Stitch cũ chuyển vào `archive/anh-cu-giong-stitch/` | **Bạn** (xuất 2×) |

## Chặng 6 — Thử, bàn giao, bảo vệ (P5)

| # | Bước | Tình trạng | Ghi chú | Ai làm tiếp |
|---|---|---|---|---|
| 43 | **Usability test 3–5 người** | ❌ | **Critical của G5** (hoặc ghi lý do ngoại lệ) | **Bạn** |
| 44 | Handoff 6 mục/màn + 2 bảng mapping | ✅ | `handoff/flutter-handoff.md` | — |
| 45a | README đủ | 🟡 | Thiếu họ tên, MSSV | Bạn |
| 45b | Link mở được ở cửa sổ ẩn danh | ❓ | Chưa kiểm | Bạn |
| 45c | Slide + kịch bản + câu hỏi phản biện | ✅ | `slides/FtaCode_Lab2_Presentation.pptx` (38 trang) · `kich-ban-*.md` · `phan-bien-hoi-dap.md` | — |
| 45d | Push lên GitHub | ❌ | 13 commit đang ở máy, chưa push | Bạn quyết |

---

## Việc còn lại theo thứ tự ưu tiên

**Bạn phải tự làm** (cần tài khoản hoặc người thật):
1. Sửa Figma: đổi token màu theo `FIX-CHECKLIST.md`, áp D06, D13–D16; sửa mã màn Page 01; đổi tên file.
2. Stitch: tạo **2 hướng visual** cho màn Home (bước 32); chụp lại ảnh trước/sau 3 vòng (bước 34).
3. Gửi **khảo sát Google Form, ≥ 30 sinh viên** (bước 14, `ux/survey/`) và **3–5 người thử Flow 1** (bước 43). Mỗi việc khoảng 1 giờ, gỡ được 2 điều kiện Critical.
4. Xuất PNG từ Figma, chụp 360/412 dp, chèn vào các khung trong slide.
5. Đổi tên repo, điền tên + MSSV, kiểm link ẩn danh, rồi push.

**Mình làm được ngay trong repo:**
- Chuẩn hoá P2: user story, AI phản biện flow, mẫu ghi walkthrough, tự kiểm G2 (bước 24, 28, 30).
- Chấm UI checklist 20 tiêu chí trên ảnh Stitch (bước 42).
- Viết sẵn mẫu ghi kết quả usability test (bước 43) để bạn chỉ điền số.
