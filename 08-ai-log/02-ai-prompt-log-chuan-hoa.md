# AI Prompt Log (bản chuẩn hóa)

> **Đọc trước:** các prompt dưới đây được **viết lại theo khung chuẩn** (Vai trò, Nhiệm vụ, Bối cảnh, Ràng buộc, Định dạng đầu ra) từ những gì nhóm đã yêu cầu AI làm. Đây **không phải nguyên văn** cuộc trò chuyện. Prompt nguyên văn gửi Google Stitch và các prompt phản biện nằm ở [`ai-design-log.md`](01-ai-design-log.md); nếu thầy yêu cầu bản gốc thì dùng file đó.
> Mỗi bước ghi rõ: AI làm gì, nhóm quyết định gì, minh chứng ở đâu. Phần "Nhóm quyết định" là việc con người phải làm; AI không thay được.

**Dự án:** BreakBite · **Môn:** PRM323 Lab 2 · **Nhóm 2, SE1919**

## Khung prompt dùng chung

```text
[VAI TRÒ]      Bạn là <chuyên gia nào>.
[NHIỆM VỤ]     Hãy <làm gì, một việc cụ thể>.
[BỐI CẢNH]     Sản phẩm: app đặt món trước cho sinh viên có 15 phút giữa hai slot, nhận tại kiosk bằng mã QR.
               Persona chính: Minh Quân, 20 tuổi, một tay, mạng chập chờn. Địa điểm: Campus Quận 9 (kiosk tầng 2, tầng 4).
[RÀNG BUỘC]    Chuẩn 48 dp, chữ ≥ 14 sp, tương phản 4,5:1, một nút cam mỗi màn. Không bịa số liệu; điều chưa biết ghi "chưa biết".
[ĐỊNH DẠNG]    <bảng / danh sách đánh số / JSON>, mỗi phát hiện có mức nghiêm trọng và đề xuất sửa.
```

## Bảng tổng hợp

| # | Phase | Công cụ AI | Việc AI làm | Đầu ra chính |
|---|---|---|---|---|
| 1 | P0 | Claude | Phản biện problem statement | `01-P0-y-tuong/01-p0-problem-framing.md` |
| 2 | P1 | Claude | Giả lập 5 cuộc phỏng vấn và khảo sát mẫu | `02-P1-nghien-cuu/04-ai-persona-interviews.md`, `02-P1-nghien-cuu/khao-sat/` |
| 3 | P1 | Claude | Tổng hợp insight, nối tới quyết định thiết kế | `02-P1-nghien-cuu/01-p1-research.md`, `02-P1-nghien-cuu/02-research.md` |
| 4 | P2 | Claude | Dựng persona, user story, flow, wireframe | `03-P2-ux-design/01-persona.md`, `03-P2-ux-design/03-p2-ux-design.md`, `03-P2-ux-design/04-user-flow.md` |
| 5 | P3 | Google Stitch | Sinh 4 màn giao diện đầu tiên | `assets/stitch/`, `ai-design-log.md` mục 2 |
| 6 | P3 | Google Stitch | Ba vòng tinh chỉnh (tương phản, rỗng, lỗi thanh toán) | `ai-design-log.md` mục 3 |
| 7 | P3 | Gemini, Claude | Phản biện theo Nielsen, WCAG, persona | `ai-design-log.md` mục 4 |
| 8 | P3 | Claude | Dựng concept B, C; phản biện style guide | `assets/concepts/` |
| 9 | P4 | Claude (Figma, Playwright) | Đo bản cũ, vẽ lại bản v2 | `05-P4-ui-design/06-phan-bien-giao-dien/` |
| 10 | P4 | Claude (Figma) | Vẽ 30 màn khách, 15 màn người bán, 412 dp, prototype | `assets/figma/final-ui-v2/` |
| 11 | P4 | Claude (Figma) | Storyboard flow, wireframe xám, design system, ánh xạ pain point | `assets/figma/boards/` |
| 12 | P5 | Claude | Handoff Flutter, bộ skill chấm UX/UI, slide | `handoff/`, `skills/`, `07-trinh-bay/` |

---

## 1. P0: Phản biện problem statement

**Công cụ:** Claude. **Nhóm đưa vào:** problem statement bản đầu, bốn hướng giải pháp.

```text
[VAI TRÒ]    Bạn là mentor sản phẩm khó tính.
[NHIỆM VỤ]   Phản biện problem statement dưới đây theo bốn mặt: ai gặp vấn đề, khó gì, bối cảnh, hậu quả.
[BỐI CẢNH]   Đề bài: app đặt món cho căn tin trường. Statement hiện tại: "<dán>". Bốn hướng: A app đặt trước nhận tại quầy, B web đặt qua QR, C hàng chờ ảo và màn hình gọi số, D chatbot Zalo hoặc Messenger.
[RÀNG BUỘC]  Tách dữ kiện, giả thuyết và điều chưa biết. Không đề xuất giải pháp trong statement.
[ĐỊNH DẠNG]  Bảng: phát hiện | mức nghiêm trọng | đề xuất sửa. Sau đó viết lại statement dạng "How might we".
```

**AI trả về:** statement cũ chứa giải pháp; chỉ số chỉ đo tốc độ thao tác; nên chuyển sang web QR; thiếu giả định về năng lực bếp.
**Nhóm quyết định:** D18 Modify statement (thêm câu How might we); D19 Accept thêm chỉ số kết quả; D20 Reject web QR vì đề bắt buộc app mobile, giữ làm phương án dự phòng; D21 Accept thêm giả định.
**Minh chứng:** `ai-design-log.md` phụ lục C (Claude Opus 5.5, 19/10/2026), `01-P0-y-tuong/01-p0-problem-framing.md`.

## 2. P1: Phỏng vấn và khảo sát giả lập

**Công cụ:** Claude. Dữ liệu này **là giả lập**, dùng để thử bộ câu hỏi; không phải bằng chứng người dùng thật.

```text
[VAI TRÒ]    Bạn là người điều phối nghiên cứu người dùng.
[NHIỆM VỤ]   Giả lập 5 sinh viên (A1–A5) trả lời 10 câu hỏi phỏng vấn về giờ nghỉ, ăn uống, thanh toán, đặt món qua app.
[BỐI CẢNH]   Nhóm đối tượng: sinh viên có 3 slot mỗi ngày, nghỉ khoảng 15 phút. Mỗi người khác nhau về nơi ở, ngân sách, thiết bị.
[RÀNG BUỘC]  Ghi rõ "AI giả lập" ở đầu file. Có người không cần app và người mâu thuẫn với nhau. Không dùng số liệu như thể đã đo thật.
[ĐỊNH DẠNG]  Bản ghi từng người, rồi bảng mâu thuẫn, rồi giả thuyết cần kiểm chứng bằng khảo sát thật.
```

**Nhóm quyết định:** coi toàn bộ là dữ liệu thử form; viết bộ khảo sát thật (`02-P1-nghien-cuu/khao-sat/khao-sat-cau-hoi.md`); persona ghi nhãn *Assumed*.
**Minh chứng:** `02-P1-nghien-cuu/04-ai-persona-interviews.md`, `02-P1-nghien-cuu/khao-sat/`.

## 3. P1: Tổng hợp insight và nối tới quyết định

```text
[VAI TRÒ]    Bạn là chuyên gia tổng hợp nghiên cứu (affinity diagram).
[NHIỆM VỤ]   Gom các câu trả lời A1–A5 thành insight có mã INS-xx, mỗi insight nêu nguồn, mức tin cậy, quyết định thiết kế đi kèm.
[BỐI CẢNH]   Dữ liệu: <dán ai-persona-interviews.md>.
[RÀNG BUỘC]  Insight chỉ dựa vào câu trả lời có thật trong dữ liệu; đánh dấu insight chỉ có 1 nguồn là "thấp".
[ĐỊNH DẠNG]  Bảng: mã | insight | nguồn | tin cậy | quyết định thiết kế | màn hình.
```

**Ví dụ kết quả:** hàng chờ → hẹn giờ nhận; ngại phí ẩn → giá cộng dồn trên nút; không muốn đăng ký → không bắt đăng nhập (D12 từ chối ép đăng nhập).
**Minh chứng:** `02-P1-nghien-cuu/01-p1-research.md`, `02-P1-nghien-cuu/02-research.md`.

## 4. P2: Persona, user story, flow, wireframe

```text
[VAI TRÒ]    Bạn là UX designer.
[NHIỆM VỤ]   Từ insight INS-01…INS-xx, viết (1) một persona chính, hai persona phụ, một nhóm không nhắm tới, mỗi persona đủ 12 trường;
             (2) 12 user story có tiêu chí chấp nhận đo được; (3) ba flow chính có nhánh lỗi; (4) kiến trúc thông tin hai app.
[BỐI CẢNH]   <dán insight>. App khách và app người bán dùng chung hệ thiết kế.
[RÀNG BUỘC]  Mỗi trường persona ghi nguồn hoặc "Assumed". Flow F1 đặt xong dưới 35 giây, tối đa 8 chạm. Có nhánh lỗi mất mạng, hết món, huỷ.
[ĐỊNH DẠNG]  Markdown; flow dạng Mermaid; bảng truy vết Insight → Story → Flow → Màn.
```

**Nhóm quyết định:** chọn Minh Quân là persona chính; thêm app người bán vì màn khách hứa nhiều việc quầy phải làm được.
**Minh chứng:** `03-P2-ux-design/01-persona.md`, `03-P2-ux-design/03-p2-ux-design.md`, `03-P2-ux-design/04-user-flow.md`, `03-P2-ux-design/02-persona-mapping.xlsx`.

## 5. P3: Sinh giao diện đầu tiên bằng Google Stitch

**Công cụ:** Google Stitch. Prompt nguyên văn ở [`ai-design-log.md`](01-ai-design-log.md) mục 2.1; bản chuẩn hóa:

```text
[VAI TRÒ]    Bạn là Principal Mobile Product Designer.
[NHIỆM VỤ]   Thiết kế 4 màn của app "BreakBite": Trang chủ, Chi tiết món, Giỏ hàng, Theo dõi đơn.
[BỐI CẢNH]   Sinh viên có 15 phút nghỉ, nhận món tại kiosk bằng mã QR. Canvas 360 × 800 dp, Material Design 3.
[RÀNG BUỘC]  Nền kem #FFF5E5, cam #F69D39, chữ nâu #622B14, thẻ trắng. Font Nunito. Vùng bấm tối thiểu 48 dp. Giá cộng dồn trên nút chính.
[ĐỊNH DẠNG]  Bốn màn, cùng ngôn ngữ thị giác, có bottom navigation 4 tab.
```

**Nhóm quyết định:** nội dung brief `DESIGN.md` do nhóm viết trước khi mở Stitch (DP1–DP8); chọn dùng ảnh Stitch làm bản nháp, không dùng làm sản phẩm cuối.
**Minh chứng:** `assets/stitch/01–04`, `04-P3-ui-concept/01-DESIGN.md`.

## 6. P3: Ba vòng tinh chỉnh trên Stitch

| Vòng | Yêu cầu chuẩn hóa | Nhóm quyết định |
|---|---|---|
| 1 | "Tăng tương phản chữ nút, tách thứ bậc nút chính và nút phụ, giữ màu thương hiệu." | Modify: chữ nút đổi sang nâu #622B14 (5,23:1) |
| 2 | "Thêm trạng thái giỏ hàng trống và chặn lỗi thao tác: xoá món, mã sai." | Accept |
| 3 | "Thêm màn lỗi thanh toán: giữ giỏ hàng, thử lại hoặc trả tiền mặt." | Accept; trở thành flow F3 |

**Minh chứng:** `ai-design-log.md` mục 3 (ảnh trước và sau).

## 7. P3: AI phản biện giao diện

```text
[VAI TRÒ]    Bạn là chuyên gia đánh giá usability.
[NHIỆM VỤ]   Đánh giá 4 màn theo 10 heuristic của Nielsen và WCAG 2.1 AA; nêu tối thiểu 5 phát hiện, mỗi phát hiện gắn màn hình cụ thể.
[BỐI CẢNH]   Persona Minh Quân; ảnh các màn đính kèm.
[RÀNG BUỘC]  Chỉ nêu số đo khi tính được; nếu không chắc, ghi "cần đo lại".
[ĐỊNH DẠNG]  Bảng: màn | heuristic | mô tả | mức | đề xuất.
```

**Nhóm quyết định:** ghi Accept, Modify, Reject cho từng phát hiện (D01–D27, có 2 Reject). AI nêu một con số tương phản sai nên nhóm tự đo lại: chữ trắng trên cam chỉ 2,14:1.
**Minh chứng:** `ai-design-log.md` mục 4–5, `ai-evaluation-log.xlsx`.

## 8. P3: Concept B, C và phản biện style guide

```text
[VAI TRÒ]    Bạn là art director khó tính.
[NHIỆM VỤ]   Dựng hai hướng visual khác (B tối giản danh sách, C nền tối banner lớn) cho màn Trang chủ, cùng nội dung với hướng A.
[RÀNG BUỘC]  Cùng khung 360 × 800, cùng dữ liệu món. Sau đó kiểm cách chấm điểm so sánh có công bằng không.
[ĐỊNH DẠNG]  HTML từng hướng, bảng so sánh có tiêu chí và điểm.
```

**Nhóm quyết định:** chọn A, mượn khối trạng thái quán của B, loại C vì nền tối kém khi dùng ngoài nắng. Ghi rõ A là ảnh Stitch đã qua chỉnh, B và C dựng một lần.
**Minh chứng:** `assets/concepts/`, `04-P3-ui-concept/02-p3-ui-concept-style-guide.md`.

## 9. P4: Đo bản cũ và vẽ lại bản v2

**Công cụ:** Claude Code với Figma MCP, Playwright, Figma Plugin API.

```text
[VAI TRÒ]    Bạn là QA giao diện.
[NHIỆM VỤ]   Đo các màn hiện có: tỉ lệ pixel họ màu cam–be, số emoji, vùng bấm dưới 48 dp, tương phản chữ.
[RÀNG BUỘC]  Số đo phải tính bằng script (tests/audit/), không ước lượng bằng mắt.
[ĐỊNH DẠNG]  Báo cáo trước và sau; liệt kê điểm sai kèm vị trí.
```

**Kết quả đo:** họ cam–be 55,3% → 4,4%; emoji 98 → 0; vùng bấm dưới 48 dp 20/39 → 0/217.
**Nhóm quyết định:** lỗi chính là dùng một họ màu cho mọi vai trò, không phải nút cam quá lớn; chọn vẽ lại v2. Báo cáo đo do AI viết nên không độc lập; phản biện bằng AI khác chưa chạy (`05-P4-ui-design/06-phan-bien-giao-dien/02-prompt-cho-ai-khac.md`).
**Minh chứng:** `05-P4-ui-design/06-phan-bien-giao-dien/`, `tests/audit/`.

## 10. P4: Vẽ Final UI trong Figma

```text
[VAI TRÒ]    Bạn là UI designer thao tác Figma qua Plugin API.
[NHIỆM VỤ]   Dựng S01–S30 cho app khách và K01–K15 cho app người bán, mỗi màn có biến thể rỗng, lỗi, đang tải khi cần; dựng bản 412 dp bằng constraints; nối prototype.
[BỐI CẢNH]   Token trong Figma Variables "BreakBite Design Tokens"; component Chip, NavBar, Card/Food, IconButton, Button.
[RÀNG BUỘC]  Dùng instance và biến, không hard-code màu; không emoji, dùng bộ 27 icon; vùng bấm ≥ 48 dp; Back đúng; không màn mồ côi.
[ĐỊNH DẠNG]  Khung đặt tên "Sxx · Tên v2"; hotspot gắn liên kết; xuất PNG vào assets/figma/final-ui-v2/.
```

**Nhóm quyết định:** danh sách màn và quy tắc nội dung (tên món, giá, địa điểm Campus Q9 tầng 2, tầng 4) là dữ liệu mẫu do nhóm chốt.
**Minh chứng:** Figma Page 03, 06; `assets/figma/final-ui-v2/`; `tests/figma-proto/` (7/7 đồ thị flow đạt).

## 11. P4: Storyboard, wireframe, design system, ánh xạ pain point

```text
[VAI TRÒ]    Bạn là UX designer trình bày cho giảng viên.
[NHIỆM VỤ]   Vẽ lại Page 01, 02, 04, 05, 06: storyboard từng flow bằng ảnh màn thật, wireframe xám, bảng token, thư viện component, chỉ mục prototype; vẽ bảng ánh xạ pain point → màn hình.
[RÀNG BUỘC]  Mỗi mũi tên trong storyboard phải có liên kết thật trong prototype; không vẽ bước chưa tồn tại.
[ĐỊNH DẠNG]  Khung Figma `UF · …`, `WF v2 · …`, `DS v2`, `CMP v2`, `PT v2`, `MAP`; xuất ảnh vào assets/figma/boards/.
```

**Nhóm quyết định:** rà lại liên kết sai (voucher, lịch sử, huỷ đơn) và đặt lại 17 điểm bắt đầu cho khớp tên flow; duyệt danh sách pain point P1–P6.
**Minh chứng:** `03-P2-ux-design/05-anh-xa-painpoint-man-hinh.md`, `assets/figma/boards/`.

## 12. P5: Handoff, bộ skill chấm, slide

```text
[VAI TRÒ]    Bạn là design engineer bàn giao cho lập trình viên Flutter.
[NHIỆM VỤ]   Viết bảng token → ThemeData, bảng component → widget, và sáu mục đặc tả cho mỗi màn; tạo bộ skill chấm UX/UI theo Quality Gates G0–G5 và WCAG 2.2.
[RÀNG BUỘC]  Không viết code Flutter; ghi rõ rubric Quality Gates là tiêu chí nội bộ của môn, không phải chuẩn quốc tế.
[ĐỊNH DẠNG]  Markdown trong handoff/ và skills/; slide 33 trang theo thứ tự P0 → P5.
```

**Nhóm quyết định:** tự chấm sáu gate; **gate 5 chưa qua** vì chưa có usability test với người thật.
**Minh chứng:** `06-P5-kiem-thu-ban-giao/03-flutter-handoff.md`, `skills/`, `00-quy-trinh/03-quy-chuan-ux-ui.md`, `07-trinh-bay/`.

---

## Phần AI không làm thay nhóm

- Xác định vấn đề, chọn persona, chọn hướng visual và mọi quyết định Accept, Modify, Reject.
- Đo lại số liệu AI nêu (ví dụ tương phản 2,14:1).
- Khảo sát thật, usability test với người dùng, chạy Present trên prototype v2 và phản biện độc lập bằng AI khác: **còn lại, chưa làm**.
