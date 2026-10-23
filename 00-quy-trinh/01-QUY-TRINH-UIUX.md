# Quy trình thiết kế UI/UX — theo PRM393 UI/UX Material

Tổng hợp từ toàn bộ [prm393-material.web.app](https://prm393-material.web.app/) (v1.0, 10/2026): trang chủ và Chuẩn chung, [Quy trình & Quality Gates](https://prm393-material.web.app/quality-gates.html), [Persona Guideline](https://prm393-material.web.app/persona-guideline.html), [UI Checklist](https://prm393-material.web.app/ui-checklist.html), [Lab 2 · Trình bày](https://prm393-material.web.app/lab2-presentation.html). Cột **"BreakBite hiện tại"** là đánh giá của repo này tại ngày 17/10/2026.

Ký hiệu: ✅ có · ⚠️ có một phần hoặc chưa kiểm chứng · ❌ chưa có · **[C]** điều kiện **Critical** (chưa đạt thì gate bị chặn dù tổng điểm cao).

---

## 0. Bức tranh tổng thể

```
P0 Ideas → P1 UX Research → P2 UX Design → P3 UI Concept → P4 UI Design → P5 Validation
   G0          G1               G2              G3              G4             G5
└──────── Analyze ────────┘   └ Generate → Critique → Refine ┘  └ Prototype ┘  └ Handoff ┘   (6 bước của Lab 2)
```

- Khung dựa trên Double Diamond của Design Council (Discover → Define → Develop → Deliver). Nghiên cứu và test tham khảo NN/g, tương phản theo WCAG 2.2.
- **Quy tắc lõi:** AI được dùng để brainstorm, gom insight, tạo wireframe và gợi ý style. AI **không thay** phỏng vấn, quan sát, usability test hay quyết định phê duyệt. Phần nào chưa có bằng chứng phải gắn nhãn giả định.
- **Lab 2** là bài cá nhân, thời gian ngắn: P1 được làm ở mức tối thiểu, nhưng **mọi nội dung chưa có bằng chứng phải gắn nhãn Assumed**. Đồ án nhóm hoặc capstone phải đi đủ cả 6 gate.

### Quy tắc qua gate
- Đạt **≥ 80%** checklist của gate **và** không thiếu điều kiện Critical nào.
- Có link bằng chứng và tên người duyệt; gate trước phải đã được duyệt.
- Nếu sửa làm mất điều kiện đạt, gate bị thu hồi và các gate sau phải rà lại.
- Không đạt thì ghi lỗi, người chịu trách nhiệm, hạn sửa, rồi đánh giá lại chính gate đó.

---

## 1. Chuẩn chung (áp dụng cho mọi tài liệu)

| Mã | Quy ước |
|---|---|
| **C1 · Thang điểm** | ≥ 80 Đạt · 70–79 Cần cải thiện · < 70 Cần làm lại. Critical chưa đạt thì kết quả là chưa đạt. Checklist chỉ để tự kiểm; điểm Lab 2 chấm theo rubric 100 điểm của đề (45 quy trình + 55 sản phẩm) |
| **C2 · Bằng chứng** | **Observed** quan sát trực tiếp, có mã nguồn (E01…) · **Reported** người tham gia tự kể · **Inferred** suy luận từ pattern, có lý do · **Assumed** chưa có bằng chứng. Trong Assumption Log: Fact = Observed/Reported, Hypothesis = Inferred, Unknown = Assumed |
| **C3 · Dùng AI** | Ghi nguyên văn mọi prompt, lưu ảnh kết quả. Mỗi vòng lặp nhắm **một vấn đề có tên**, khác các vòng khác. Mỗi đề xuất quan trọng: Accept / Modify / Reject kèm lý do gắn persona, heuristic hoặc ràng buộc. **Persona do AI sinh ra không phải dữ liệu nghiên cứu** |
| **C4 · Accessibility** | Chữ thường ≥ 4,5:1; chữ lớn và thành phần điều khiển ≥ 3:1 (WCAG 2.2 AA). Vùng chạm ≥ 48 × 48 dp, chữ nội dung ≥ 14 sp. Không truyền thông tin chỉ bằng màu. Kiểm ở 360 và 412 dp; mô tả thay đổi từ 600 dp |
| **C5 · Số persona** | Lab 2: tối thiểu 1 Primary đủ 12 trường lõi; bắt buộc tuổi, vai trò, thói quen thiết bị, nhu cầu accessibility. Đồ án nhóm: thường 3–5 |
| **C6 · Cách đếm** | **Màn hình** là một đích điều hướng riêng; dialog, bottom sheet, biến thể trạng thái không tính. **Flow** có điểm bắt đầu, mục tiêu, kết thúc, happy path và ≥ 1 nhánh thay thế. Mỗi màn liên quan cần đủ state default, loading, empty, error, success |
| **C7 · Mã định danh** | **E01** bằng chứng · **P01** persona · **F01** flow · **S01** màn hình · **I01** vòng lặp AI · **D01** quyết định · **T01** test case. Chuỗi truy vết: **E → Insight → P/Need → User story → F → S → T**. Mọi màn hình phải thuộc ≥ 1 flow |
| **C8 · Link nộp** | Figma ai có link đều xem được; GitHub giảng viên truy cập được; kiểm bằng cửa sổ ẩn danh. Link Figma không mở được thì các tiêu chí dựa trên Figma bị 0 điểm |

---

## 2. Sáu phase, deliverable và gate

### P0 · Idea Discovery & Problem Framing → **G0 Problem Approval**
**Câu hỏi:** Giải quyết vấn đề gì, cho ai, vì sao đáng giải quyết? *(Chưa vẽ UI chi tiết.)*

**Hoạt động:** brainwriting 6-3-5 hoặc silent ideation · viết problem statement (ai, khó khăn gì, bối cảnh, hậu quả) · stakeholder map, assumption mapping (Facts / Hypotheses / Unknowns) · ưu tiên ý tưởng theo Impact × Feasibility, chọn phạm vi MVP.

**Deliverable:** Idea Board · Problem Statement + Opportunity Brief (1 trang) · Stakeholder & User Group Map · Assumption/Risk Log và MVP Scope.

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Problem statement cụ thể: ai – vấn đề – bối cảnh – tác động | ✅ đã sửa bỏ giải pháp trá hình (D18) |
| **[C]** Phân biệt dữ kiện, giả thuyết, ý kiến | ✅ nhãn bằng chứng + backlog H1–H6 (`02-P1-nghien-cuu/02-research.md` mục 6) |
| Có ≥ 2 phương án ý tưởng được cân nhắc | ✅ 4 hướng + chấm điểm (`01-P0-y-tuong/01-p0-problem-framing.md` mục 2) |
| Có nhóm người dùng mục tiêu và stakeholder | ✅ `02-P1-nghien-cuu/02-research.md` mục 5.1 |
| Có phạm vi MVP, giới hạn, rủi ro, mục tiêu đo | ✅ `01-P0-y-tuong/01-p0-problem-framing.md` mục 4–5 |
| **[C]** Có kế hoạch kiểm chứng giả định ở P1 | ✅ `02-P1-nghien-cuu/02-research.md` mục 7 |

**Red flags:** "App này hay" mà không có vấn đề người dùng rõ ràng · làm 20 màn hình trước khi biết ai dùng.

### P1 · UX Research → **G1 Research Evidence Approval**
**Câu hỏi:** Người dùng thật làm gì, đau ở đâu, bằng chứng nào?

**Hoạt động:** Research Plan (câu hỏi nghiên cứu, người tham gia, phương pháp, protocol, consent) · phỏng vấn/quan sát · phân tích đối thủ và workaround hiện tại · affinity mapping, insight có mức tin cậy.

**Deliverable:** Research Plan + Protocol · ghi chép phỏng vấn/quan sát (evidence log) · Affinity Map + Insight Statements gắn bằng chứng · current-state journey / task analysis · hồ sơ tuyển chọn và consent.

**Mức đề xuất:** khoảng 5 người cho mỗi nhóm chính (Persona Guideline: 6–12 buổi cho lớp học).

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Nghiên cứu trực tiếp với người dùng phù hợp, **hoặc giải trình hợp lý** khi chưa thể | ⚠️ đạt theo nhánh giải trình: kế hoạch, protocol, consent đầy đủ, trạng thái "chưa thực hiện" (`02-P1-nghien-cuu/01-p1-research.md` mục 1, 8) |
| **[C]** Insight quan trọng liên kết tới ghi chép nguồn | ✅ INS-01…06 có mã E…/SIM… và mức tin cậy (`02-P1-nghien-cuu/01-p1-research.md` mục 2–3) |
| Ghi rõ phương pháp, mẫu, giới hạn, thiên lệch | ✅ `02-P1-nghien-cuu/02-research.md` mục 8, `02-P1-nghien-cuu/04-ai-persona-interviews.md` |
| Có Affinity Map / Task Analysis | ✅ affinity + current-state journey (`02-P1-nghien-cuu/01-p1-research.md` mục 4) |
| **[C]** Đã kiểm và cập nhật giả định trọng yếu từ P0 | ✅ bảng cập nhật H1–H7 (`02-P1-nghien-cuu/01-p1-research.md` mục 5) |
| Kết luận nhu cầu ưu tiên và câu hỏi còn mở | ✅ cơ hội (mục 1.2) + Open questions trong persona |

**Red flags:** persona hoàn toàn do ChatGPT bịa mà không gắn evidence · chỉ khảo sát bạn cùng lớp mà không nêu giới hạn.

### P2 · UX Design & Interaction Architecture → **G2 UX Design Approval**
**Câu hỏi:** Người dùng hoàn thành tác vụ thế nào, **trước khi** có màu và phong cách?

**Hoạt động:** gom nhóm hành vi thành persona (Primary/Secondary) · JTBD / Goal–Pain–Need, journey hiện tại và tương lai, user stories có ưu tiên · IA, sitemap, user flow, edge case · wireframe low-fi → prototype cơ bản → walkthrough.

**Deliverable:** Persona Set + Evidence Matrix · JTBD / Problem-to-Requirement Matrix · Journey, IA/Sitemap, User Flow · wireframe low-fi · prototype low-fi + ghi chú walkthrough.

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Persona/JTBD khác nhau về hành vi và truy về evidence | ✅ P01–P03, JTBD, nhãn (`03-P2-ux-design/01-persona.md`, `03-P2-ux-design/02-persona-mapping.xlsx`) |
| **[C]** Mọi tác vụ ưu tiên có flow rõ bắt đầu, kết thúc, lỗi | ✅ F1–F3 (`03-P2-ux-design/04-user-flow.md`) |
| **[C]** Có IA và wireframe low-fi cho các luồng MVP | ✅ IA trong user-flow; Figma Page 02 |
| Quyết định chức năng nối Insight → Need → **User Story** | ✅ problem-to-requirement matrix + US01–US12 (`03-P2-ux-design/03-p2-ux-design.md` mục 2–3) |
| Có walkthrough / test prototype sơ bộ | ⚠️ walkthrough chuyên gia do AI (`03-P2-ux-design/03-p2-ux-design.md` mục 7); bạn cần tự đi lại trên Figma |
| Đã xét empty/loading/error/permission | ✅ có trong handoff và biến thể Figma |

**Red flags:** tô màu, làm icon trước khi flow xong · nhiều persona giống nhau chỉ khác tên, tuổi, ảnh.

### P3 · UI Concept & App Style Guide → **G3 Visual Direction Approval**
**Câu hỏi:** App trông thế nào và quy tắc nào giữ nó nhất quán? *(Bước Generate → Critique → Refine của Lab 2.)*

**Hoạt động:** moodboard có nguồn; **2–3 hướng visual khác nhau trên cùng một key screen** · đánh giá readability, hierarchy, brand fit, phù hợp persona; chọn 1 · định nghĩa token (color roles, typography, spacing, grid, radius, elevation, icon, density) · component nền tảng + state; kiểm contrast và responsive.

**Deliverable:** Concept Exploration Board (≥ 2 phương án) + lý do chọn · Visual Direction được duyệt / 2–3 key screen · App Style Guide · thư viện component / Figma styles · bằng chứng accessibility và contrast.

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Có **≥ 2 visual direction** để so sánh; chọn có lý do dựa trên persona/task | ✅ 3 concept + chấm điểm (`04-P3-ui-concept/02-p3-ui-concept-style-guide.md` mục 1) |
| **[C]** Style Guide có color roles, type scale, spacing, grid, density, component states | ✅ `04-P3-ui-concept/01-DESIGN.md`, Figma Page 04/05 (chưa có mục grid/density riêng) |
| **[C]** Contrast 4,5:1 / 3:1; vùng chạm ≥ 48 dp; chữ ≥ 14 sp | ⚠️ đã sửa token trong tài liệu; **Figma chưa đổi** |
| Key screens có thứ bậc, ít chữ thừa, màu nhấn có vai trò | ⚠️ critique phát hiện chữ phụ nhỏ (Phụ lục A #3) |
| Có naming component / token tái sử dụng được | ✅ |
| Đã duyệt concept trên thiết bị chủ đạo và nội dung dài | ❌ cần kiểm trong Figma (412 dp, tên món dài) |

**Red flags:** mỗi màn một kiểu màu, radius, icon · Style Guide chỉ có logo, màu và font.

### P4 · Detailed UI Design & Prototyping → **G4 UI Design Approval**
**Câu hỏi:** Mọi luồng ưu tiên đã đủ màn hình, state, responsive và nhất quán chưa?

**Hoạt động:** hi-fi theo flow đã duyệt, dùng shared component · state default, focus, disabled, error, loading, empty, success, permission · responsive và nội dung thật · clickable prototype, review heuristic, visual density, design QA.

**Deliverable:** hi-fi screens + responsive variant · Component Library + spec state/tương tác · prototype hi-fi · Screen/State Coverage Matrix · UI QA Checklist + Design Change Log.

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Mọi flow MVP có đủ màn hi-fi và prototype đi hết tác vụ | ⚠️ Figma Page 03/06 có; chưa chạy thử được (Figma bắt đăng nhập) |
| **[C]** Màn hình dùng đúng Style Guide/component, không hard-code | ⚠️ chưa kiểm được Variables/instance |
| **[C]** Có đủ empty/loading/error/success/disabled | ✅ biến thể trong Figma + handoff |
| Có responsive variant và nội dung thật | ⚠️ có mô tả 360/412/600 dp; thiếu ảnh 412 dp |
| Màn chính đạt **≥ 80 điểm UI Simplicity Checklist** | ❌ mức nền trên Stitch: S02 55 · S04 70 · S05 65 · S06-ERR 75 (`05-P4-ui-design/04-p4-detailed-ui-prototype.md` mục 4) |
| Có UI QA log, traceability flow → screen, tồn đọng | ✅ coverage matrix, change log, QA log (`05-P4-ui-design/04-p4-detailed-ui-prototype.md` mục 2, 6, 7) |

**Red flags:** UI nhiều màu và card trang trí vì AI sinh tự do · prototype chỉ chuyển trang, không làm hết được task.

### P5 · Usability Validation & Developer Handoff → **G5 Design Release Approval**
**Câu hỏi:** Người dùng có làm xong việc không, và dev có triển khai đúng được không?

**Hoạt động:** Usability Test Plan (mục tiêu, task, tiêu chí thành công, đối tượng) · cho người dùng làm task **không hướng dẫn từng bước**; ghi success, thời gian, chỗ vướng, lỗi · phân loại P0 blocker / P1 major / P2 minor, sửa và test lại · bàn giao Figma inspect, token, spec component, tương tác, copy, asset, responsive, acceptance criteria.

**Kiểm thử tự động prototype (bước bổ sung):** dùng Playwright mở prototype Figma, bấm theo từng flow và so ảnh từng bước với ảnh chuẩn; kiểm đồ thị flow (không màn cụt, không màn mồ côi, số chạm tới đích). Mã ở `tests/`, báo cáo ở `docs/test-reports/`. Bước này **không thay** usability test với người thật.

**Deliverable:** Test Plan & log người tham gia/task · Usability Findings + Issue List theo mức độ · bằng chứng sửa và retest · gói Handoff + ghi chú accessibility/QA · Release Record.

| Gate check | BreakBite hiện tại |
|---|---|
| **[C]** Có usability test với người đại diện, hoặc lý do ngoại lệ được ghi | ❌ chưa test; đã có kế hoạch (`02-P1-nghien-cuu/02-research.md` mục 7) |
| **[C]** Không còn blocker trong tác vụ MVP | ⚠️ chưa test nên chưa biết |
| **[C]** Có findings theo task, ưu tiên sửa, retest | ❌ |
| **[C]** Bàn giao đủ flow, screen, state, component, token, asset, interaction spec | ✅ `06-P5-kiem-thu-ban-giao/03-flutter-handoff.md` (6 mục/màn + 2 bảng mapping) |
| Có acceptance criteria, tồn đọng, người chịu trách nhiệm | ⚠️ có tiêu chí thành công; chưa có danh sách tồn đọng chính thức |
| Reviewer/dev xác nhận đủ rõ để triển khai | ❌ |

**Red flags:** "đã test" nhưng chỉ cho bạn bè xem rồi nhận lời khen · dev phải hỏi lại kích thước, hành vi nút, component, trạng thái lỗi.

---

## 3. Persona Guideline (dùng ở P1–P2)

- **12 trường lõi:** Identity & Archetype · Persona Priority · Usage Context · Goals (2–3) · Job to Be Done · Current Behaviors · Pain Points (2–3) · Motivations · Constraints · Key Scenarios (1–2) · Success Criteria · Evidence & Status. Gọn trong khoảng một trang A4; transcript để ở phụ lục.
- **Số lượng:** app nhỏ 2–3 · đồ án thường 3–5 · hệ thống nhiều nhóm 4–6 · Lab 2 tối thiểu 1 Primary.
- **Workshop 100 phút:** Frame (10') → List người & tình huống (15') → Brainwriting im lặng (15') → Affinity (20') → Chọn segment (15') → Viết proto-persona (15') → Chọn nghiên cứu tiếp (10') → kiểm chứng và sửa.
- **Đầu ra workshop:** Stakeholder/User Map · Affinity Board có nguồn · Persona Coverage Matrix · 3–5 proto-persona · Assumption & Research Backlog · ≥ 1 scenario cho mỗi Primary.
- **Dùng AI để tổng hợp:** chỉ dựa trên ghi chú do người dùng cung cấp (mỗi đoạn có ID); thiếu thì ghi UNKNOWN/ASSUMPTION; không bịa quote, số liệu; trả về Evidence matrix → Candidate segments → Persona drafts → Open questions.
- **Rubric 10 tiêu chí × 10 điểm:** phạm vi · user map + nhóm dễ bỏ sót · số persona hợp lý · khác biệt thật · đủ 12 trường · nhu cầu theo kết quả (không ngụy trang tính năng) · có bằng chứng hoặc nhãn giả định · có affinity · scenario + success criteria · ≥ 1 quyết định UI và cách kiểm chứng nối với persona.
- **Nộp:** Milestone A (Discovery) và Milestone B (Validation & Design, gồm **ma trận Persona → Need → UI Decision → Test**).

BreakBite: ✅ 12 trường, 3 persona, user map, coverage matrix, backlog, scenario, ma trận Excel · ⚠️ toàn bộ nhãn Assumed · ❌ chưa có ảnh workshop/affinity board.

---

## 4. UI Simplicity Checklist (dùng cho **từng màn hình** ở P3–P4)

20 tiêu chí × 5 điểm, thang C1.

| Nhóm | Tiêu chí |
|---|---|
| **A. Text & Content** (NN/g) | 1 Tiêu đề và nhãn ngắn, dễ quét · 2 Không có đoạn giải thích dài thừa · 3 Thông tin ít dùng chuyển vào chi tiết · 4 Không lặp nội dung ở nhiều card |
| **B. Color Discipline** (Carbon, Material, Apple) | 5 Một màu nhấn chủ đạo + bảng trung tính · 6 Không dùng màu khác nhau chỉ để trang trí card · 7 Success/warning/error nhất quán · 8 Màu không phải cách duy nhất báo trạng thái |
| **C. Density & Whitespace** (Fiori, Carbon) | 9 Mật độ hợp tác vụ và thiết bị · 10 Khoảng cách theo spacing scale · 11 Nhóm mục liên quan, không chia quá nhiều card · 12 Vùng chạm ≥ 48 dp, chữ ≥ 14 sp |
| **D. Visual Hierarchy** (Apple, NN/g) | 13 Nội dung quan trọng nhận ra ngay · 14 Một hành động chính nổi bật · 15 Các cấp chữ phân biệt rõ · 16 Các phần có thứ tự, không tranh nhau |
| **E. Consistency & Accessibility** (WCAG 2.2) | 17 Component, font, spacing, icon nhất quán · 18 Tương phản 4,5:1 / 3:1 · 19 Điều khiển có chỉ báo trạng thái rõ · 20 Loading, empty, success, error rõ ràng |

**3 bài test thêm:** **5-second test** (nhìn 5 giây có nói được chức năng và hành động chính không) · **Grayscale test** (xem ở thang xám, phát hiện phụ thuộc màu) · **Reduction test** (bỏ chữ, card, màu trang trí mà không mất thông tin).

BreakBite: ❌ chưa chấm màn nào. Dự đoán trượt ở tiêu chí 12 và 18 cho tới khi Figma đổi màu chữ nút và tăng cỡ chữ phụ.

---

## 5. Bảo vệ Lab 2 (P5)

- **Thời lượng đề xuất:** 10 phút slide (10–12 slide) · 5 phút demo · 5 phút hỏi đáp.
- **12 slide:** Overview · Problem & Persona · IA · 3 Flows · AI Generation · AI Iterations & Critique · Design Decisions · Wireframe → Final · Design System · Accessibility/Responsive · Live Prototype · Handoff/Summary. Mỗi slide phải trỏ tới minh chứng.
- **Demo 7 bước:** 6 page đúng thứ tự → chỉ 8 màn khác nhau → chạy 3 flow (có lỗi/phục hồi, Back, không ngõ cụt) → dialog overlay + loading → result → Components, Variables → một vòng AI log từ prompt tới thay đổi trong Figma → GitHub (spec + 2 bảng mapping).
- **Tác phong:** không dùng ảnh minh hoạ giả làm bằng chứng · thử link bằng cửa sổ chưa đăng nhập · repo tên `prm323-lab2-<student-id>`.

Kịch bản đã soạn: `07-trinh-bay/kich-ban-theo-google-slides.md`, câu hỏi phản biện: `07-trinh-bay/02-phan-bien-hoi-dap.md`.

---

## 6. Việc cần làm để BreakBite qua đủ gate (theo mức ưu tiên)

| # | Việc | Gate | Critical? | Ai làm được |
|---|---|---|---|---|
| 1 | Đổi token màu trong Figma (chữ nút nâu, chữ phụ, viền ô nhập), xuất lại PNG | G3, G4 | ✅ | Bạn (Figma) |
| 2 | Tạo **2 hướng visual** trên một key screen (ví dụ Home), so sánh và ghi lý do chọn | G3 | ✅ | Bạn (Stitch) + mình viết bảng so sánh |
| 3 | Khảo sát Google Form ≥ 30 sinh viên (`02-P1-nghien-cuu/khao-sat/`), đổi nhãn Assumed → Reported | G1 | ✅ (hoặc giữ giải trình) | Bạn |
| 4 | Usability test Flow 1 với 3–5 người, ghi thời gian, số chạm, lỗi | G5 | ✅ (hoặc ghi lý do ngoại lệ) | Bạn |
| 4b | Chạy test Playwright trên prototype (`tests/`) sau mỗi lần sửa Figma | G4, G5 | — | Đã làm lần đầu 20/10 (13/13 đạt); chạy lại sau khi sửa Figma |
| 5 | Chụp lại ảnh trước/sau 3 vòng Stitch | Rubric Lab 2 | — | Bạn |
| 6 | Viết user stories, nối Insight → Need → Story → Flow | G2 | — | Mình làm được |
| 7 | Đổi mã định danh theo C7 (E01, P01, F01, S01, I01, D01, T01) | C7 | — | Mình làm được |
| 8 | Chấm UI Simplicity Checklist cho 8 màn + 3 bài test thêm | G4 | — | Mình chấm được trên ảnh, bạn xác nhận trong Figma |
| 9 | Ghi lại ≥ 2 hướng ý tưởng ban đầu đã cân nhắc, MVP scope | G0 | — | Mình làm được |
