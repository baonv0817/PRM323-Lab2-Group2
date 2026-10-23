# UX Analysis: Persona & Problem Statement

> **Tài liệu:** `03-P2-ux-design/01-persona.md`
> **Dự án:** BreakBite App — Campus Quick Food Ordering
> **Môn học:** PRM323 — Lab 2
> **Chuẩn áp dụng:** [Persona Guideline của môn](https://prm393-material.web.app/persona-guideline) — 12 trường lõi, nhãn bằng chứng, số lượng persona theo phạm vi.
> **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6)

---

## 0. Cơ sở, số lượng và nhãn bằng chứng

**Nhãn bằng chứng** (theo guideline mục 4):

| Nhãn | Nghĩa trong bài này |
|---|---|
| **Observed** | Quan sát được: số liệu thị trường từ nguồn công khai (`02-P1-nghien-cuu/02-research.md` mục 1) |
| **Reported** | Người thật tự kể lại — **hiện chưa có** |
| **Inferred** | Nhóm suy luận từ pattern trong các nguồn trên (ghi rõ lý do) |
| **Assumed** | Chưa có bằng chứng từ người thật. Bao gồm mọi ý từ **5 nhân vật giả lập bằng AI** (mã A1–A5, `02-P1-nghien-cuu/04-ai-persona-interviews.md`) |

**Số lượng:** 1 Primary + 1 Secondary + 1 Supporting. BreakBite là ứng dụng nhỏ với một tác vụ chính (đặt món và lấy tại quầy), nên dùng mức 2–3 persona của guideline. Ba persona khác nhau ở **hành vi và ràng buộc**, không chỉ ở tên hay tuổi:

| | P01 Quân (Primary) | P02 Linh (Secondary) | P03 Cô Hạnh (Supporting) |
|---|---|---|---|
| Vai trò | Sinh viên ở KTX, giờ nghỉ ngắn | Sinh viên ở trọ, nhạy cảm về giá | Nhân viên quầy Kiosk |
| Ràng buộc chính | Thời gian (15 phút) | Ngân sách (~40.000đ/ngày) | Đông khách giờ nghỉ, phải xử lý đơn nhanh |
| Hành vi quyết định | Bỏ mua khi thấy hàng dài | Bỏ app nếu có phí ẩn | Gọi số, kiểm tra chuyển khoản bằng tay |

**Trạng thái chung:** tất cả là **proto-persona**. Chưa có phỏng vấn người thật (guideline khuyến nghị 6–12 buổi cho lớp học). Kế hoạch kiểm chứng ở `02-P1-nghien-cuu/02-research.md` mục 7.

---

## 1. P01 — Nguyễn Minh Quân (Primary)

| # | Trường | Nội dung | Nhãn & nguồn |
|---|---|---|---|
| 1 | **Identity & Archetype** | 20 tuổi, sinh viên năm 2 Kỹ thuật phần mềm, ở ký túc xá. *Archetype: "Người chạy giữa hai slot".* | Assumed — A1 |
| 2 | **Persona Priority** | **Primary** — nhóm đau nhất và mua ở trường thường xuyên nhất | Inferred — affinity map (A1, A5) |
| 3 | **Usage Context** | Mở app trên hành lang hoặc khi đi bộ giữa các khu trong campus, cầm máy một tay, mạng trong campus chập chờn, hay dùng ngoài nắng | Assumed — A1, A5 |
| 4 | **Goals** | (1) Có đồ ăn trong giờ nghỉ mà không trễ lớp. (2) Biết chắc món đã xong trước khi xuống quầy. (3) Biết đúng số tiền phải trả ngay từ đầu. | Assumed — A1, A5 |
| 5 | **Job to Be Done** | "Khi chỉ có 15 phút giữa hai slot, tôi muốn đặt trước và ghé quầy lấy ngay, để ăn kịp mà không phải xếp hàng." | Inferred |
| 6 | **Current Behaviors** | Bỏ bữa sáng, mua bù lúc giải lao. Thấy hàng dài thì bỏ mua. Từng đặt GrabFood nhưng phải ra cổng nhận. Trả bằng QR ngân hàng. | Assumed — A1 |
| 7 | **Pain Points** | (1) Hàng chờ đúng giờ nghỉ chung → bỏ bữa hoặc vào lớp trễ. (2) Không biết quán còn mở, còn món, bao lâu xong. (3) Nút nhỏ hoặc ở trên cao, khó bấm khi đi bộ. | Assumed — A1, A5 |
| 8 | **Motivations** | Tiết kiệm thời gian; giữ điểm chuyên cần; không muốn nhịn đói tới trưa. | Assumed — A1 |
| 9 | **Constraints** | 15 phút nghỉ, trong đó khoảng 5 phút đi bộ. Một tay. Mạng yếu. Không muốn đăng ký tài khoản chỉ để xem menu. | Assumed — A1, A3 |
| 10 | **Key Scenarios** | **S1:** Cuối slot 1, Quân mở app trên đường ra hành lang, chọn combo, hẹn giờ nhận 09:20, thanh toán QR, đi thẳng tới quầy lấy món theo mã. **S2:** Thanh toán bị timeout vì mạng yếu; app giữ giỏ hàng, Quân chọn trả tiền mặt tại quầy. | Inferred — Flow 1, Flow 3 |
| 11 | **Success Criteria** | Đặt xong một đơn **dưới 35 giây, tối đa 8 lần chạm** từ Trang chủ (Flow 1). | Assumed — chưa đo |
| 12 | **Evidence & Status** | Proto-persona. Nguồn: A1, A5 (giả lập AI). Câu hỏi mở: giờ nghỉ thật là bao nhiêu? Hàng chờ thật bao lâu? | — |

**Bắt buộc của Lab 2:** tuổi 20 · vai trò sinh viên · thiết bị Android tầm trung (ví dụ Samsung Galaxy A), màn hình 360–412 dp, thao tác một tay · accessibility: cần tương phản cao khi dùng ngoài nắng, vùng chạm ≥ 48 dp, trạng thái không chỉ thể hiện bằng màu.

---

## 2. P02 — Trần Mỹ Linh (Secondary)

| # | Trường | Nội dung | Nhãn & nguồn |
|---|---|---|---|
| 1 | Identity & Archetype | 19 tuổi, năm 1 Thiết kế đồ hoạ, ở trọ, đi xe buýt. *Archetype: "Người đếm từng nghìn".* | Assumed — A2 |
| 2 | Persona Priority | **Secondary** — dùng cùng luồng đặt món nhưng quyết định dựa trên giá | Inferred |
| 3 | Usage Context | Ngồi ở hành lang giữa hai slot buổi sáng, dùng hai tay, iPhone cũ, ví MoMo | Assumed — A2 |
| 4 | Goals | (1) Ăn trong ngân sách ~40.000đ/ngày. (2) Thấy tổng tiền thật trước khi đặt. | Assumed — A2 |
| 5 | Job to Be Done | "Khi đói giữa buổi sáng, tôi muốn biết chính xác món nào vừa túi tiền, để không bị bất ngờ ở bước thanh toán." | Inferred |
| 6 | Current Behaviors | Ít dùng app giao hàng vì phí. Ngại chen lấn ở căn tin nên đôi khi bỏ ăn. | Assumed — A2 |
| 7 | Pain Points | (1) Phí ship và phí dịch vụ cộng vào cao hơn cả món. (2) Tổng tiền chỉ hiện ở bước cuối. | Assumed — A2 |
| 8 | Motivations | Tiết kiệm; thích combo hoặc giảm giá sinh viên. | Assumed — A2 |
| 9 | Constraints | Ngân sách thấp; chữ nhỏ phải phóng to. | Assumed — A2 |
| 10 | Key Scenarios | Linh lướt Thực đơn, lọc combo dưới 40.000đ, nhập mã sinh viên, thấy giá giảm ngay trên nút rồi mới đặt. | Inferred — Flow 2 |
| 11 | Success Criteria | Thấy tổng tiền cuối cùng (sau giảm giá) **trước bước chọn phương thức thanh toán**, không có phí phát sinh sau đó. | Assumed |
| 12 | Evidence & Status | Proto-persona. Nguồn: A2. Câu hỏi mở: sinh viên có thật sự bỏ app vì vài nghìn phí không? | — |

---

## 3. P03 — Cô Hạnh (Supporting)

| # | Trường | Nội dung | Nhãn & nguồn |
|---|---|---|---|
| 1 | Identity & Archetype | Khoảng 40 tuổi, nhân viên quầy Kiosk BreakBite. *Archetype: "Người giữ nhịp quầy".* | Assumed |
| 2 | Persona Priority | **Supporting** — không dùng app khách, nhưng quyết định món có sẵn đúng giờ hay không | Inferred |
| 3 | Usage Context | Đứng quầy giờ nghỉ chung, vừa nấu vừa trả món, xem đơn trên màn hình quán | Assumed |
| 4 | Goals | (1) Biết trước số đơn và giờ nhận để chuẩn bị. (2) Trả đúng món cho đúng người. | Assumed |
| 5 | Job to Be Done | "Khi nhiều sinh viên tới cùng lúc, tôi muốn biết đơn nào đã trả tiền và đơn nào tới giờ lấy, để trả món nhanh mà không nhầm." | Inferred |
| 6 | Current Behaviors | Gọi số; kiểm tra chuyển khoản bằng tay khi khách đưa màn hình. | Assumed |
| 7 | Pain Points | (1) Khách đứng chờ kiểm tra chuyển khoản (A1 kể lại). (2) Khách huỷ đơn khi món đã nấu. | Assumed — A1 · Inferred |
| 8 | Motivations | Bán được nhiều trong giờ nghỉ; ít sai sót. | Assumed |
| 9 | Constraints | Ít thời gian nhìn điện thoại; tay bận. | Assumed |
| 10 | Key Scenarios | Khách đưa mã nhận đồ (số lớn + QR); cô Hạnh quét hoặc đọc số, đối chiếu, trả món. | Inferred — SCR-07 |
| 11 | Success Criteria | Trả một món cho khách đã đặt trước **trong khoảng 30 giây** kể từ khi khách tới quầy. | Assumed |
| 12 | Evidence & Status | Proto-persona, **chưa có nguồn từ nhân viên thật**. Ảnh hưởng tới thiết kế: mã nhận đồ cỡ lớn + QR (quyết định 02), chỉ cho huỷ trong 60 giây (quyết định 04). App phía quầy nằm ngoài phạm vi Lab 2. | — |

---

## 4. Câu phát biểu vấn đề

> **"Sinh viên ở ký túc xá có lịch học dày thường không mua kịp đồ ăn trong giờ nghỉ ngắn giữa hai slot, khi hàng chờ ở căn tin dồn đúng giờ nghỉ chung, nên họ bỏ bữa hoặc vào lớp trễ."**

> **Cơ hội (How might we):** Làm sao để sinh viên có đồ ăn trong giờ nghỉ ngắn mà không phải xếp hàng?

> *Sửa ngày 19/10/2026 theo quyết định D18: bản cũ ghi "cần đặt trước và nhận món tại quầy", tức là đưa giải pháp vào problem statement. Chi tiết ở `01-P0-y-tuong/01-p0-problem-framing.md`.*

## 5. Tiêu chí thành công đo được (Primary)

> **"Sinh viên chọn món, thêm topping và đặt đơn thành công trong dưới 35 giây, tối đa 8 lần chạm từ Trang chủ"** — đếm theo Flow 1 trong `03-P2-ux-design/04-user-flow.md`: thẻ món → topping → Thêm vào giỏ → giờ nhận → Tiến hành thanh toán → phương thức → Xác nhận → Đồng ý trong dialog. Cách đo: cho 3–5 người chạy Flow 1 trên prototype và bấm giờ (`02-P1-nghien-cuu/02-research.md` mục 7).

> *Áp dụng cho người **đã dùng app** (bỏ qua S01 Onboarding). Giờ nhận mặc định "Lấy ngay" nên đường ngắn nhất là 7 chạm (D28, D32).*

> *Ghi chú sửa đổi: bản trước ghi "tối đa 4 bước chạm", không khớp với số thao tác thực tế của Flow 1 nên đã đếm lại.*
