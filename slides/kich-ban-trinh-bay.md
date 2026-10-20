# Kịch bản trình bày Lab 2 — FtaCode Mobile

Gợi ý thời lượng theo hướng dẫn chấm: **10 phút slide + 5 phút demo + 5 phút hỏi đáp**. Mỗi slide khoảng 45–50 giây. Lời thoại chỉ là gợi ý, hãy nói bằng lời của bạn và chỉ khẳng định những gì bạn đã thật sự làm.

**Trước buổi chấm (bắt buộc):**
- Xong các mục trong `FIX-CHECKLIST.md`, nhất là đổi token màu trong Figma và chụp lại ảnh trước/sau.
- Mở link Figma và GitHub trong cửa sổ ẩn danh để chắc là người khác xem được.
- Đăng nhập Figma, bấm Present ở Page 06 và chạy thử cả 3 flow một lượt.
- Mở sẵn 4 tab: slide, Figma (Page 01), GitHub repo, `ai/ai-design-log.md`.

---

## Phần 1 — Trình bày slide (10 phút)

**Slide 01 · Tổng quan (40 giây)**
> "Em là [tên], MSSV [..]. Đề tài của em là FtaCode Mobile, app đặt món trước và nhận tại quầy Kiosk trong trường. Vấn đề em giải quyết: sinh viên chỉ có 15 phút giải lao nhưng xếp hàng căn tin mất 12–18 phút. Link GitHub và Figma ở cuối slide."

**Slide 02 · Persona (50 giây)**
> "Persona chính là Minh Quân, 20 tuổi, sinh viên năm 2. Bạn ấy đi bộ giữa các tòa nhà, cầm máy một tay, mạng chập chờn và hay dùng ngoài nắng. Từ đó em có ba yêu cầu thiết kế: nút chính ở nửa dưới màn hình, vùng chạm 48 dp, tương phản cao. Chỉ số thành công là đặt xong một đơn dưới 35 giây, tối đa 8 lần chạm, đếm theo Flow 1."

**Slide 03 · Kiến trúc thông tin (45 giây)**
> "App có 8 màn hình. SCR-01 là màn vào app. Thanh điều hướng dưới có 4 tab: Home, Menu, Theo dõi đơn, Lịch sử. Ba màn con là Chi tiết món, Giỏ hàng, Checkout. Màn lỗi thanh toán SCR-06-ERR là biến thể nên không tính là màn riêng. Em dùng bottom nav vì persona thao tác bằng ngón cái."

**Slide 04 · Ba user flow (50 giây)**
> "Flow 1 là luồng chính: từ Home chọn món, vào giỏ, thanh toán và nhận mã lấy đồ ở SCR-07. Flow 2 bắt đầu từ Menu, tuỳ chỉnh topping và nhập voucher; nếu mã sai thì báo rõ lý do. Flow 3 là luồng lỗi bắt buộc: thanh toán MoMo bị timeout thì app giữ nguyên giỏ hàng và cho chọn Thử lại hoặc chuyển sang trả tiền mặt."

**Slide 05 · Tạo UI bằng Stitch (50 giây)**
> "Em viết DESIGN.md trước, rồi dựa vào đó viết prompt cho Stitch. Prompt có đủ năm phần: persona, nhiệm vụ cho 4 màn hình, nền tảng 360×800 Material 3, ràng buộc 48 dp, và phong cách màu. Toàn văn prompt nằm trong ai-design-log mục 2.1. Đây là 4 màn Stitch sinh ra lần đầu."

**Slide 06 · Ba vòng tinh chỉnh và critique (60 giây)**
> "Mỗi vòng giải quyết một vấn đề khác nhau. Vòng 1 là nút CTA khó đọc và bị chìm. Vòng 2 là thiếu trạng thái giỏ trống và dễ xoá nhầm món. Vòng 3 là lỗi thanh toán thành ngõ cụt, mất cả giỏ hàng. Sau vòng 1 em đo lại thì chữ trắng trên nền cam chỉ đạt 2,14:1, vẫn chưa đạt, nên em sửa tiếp ở bước quyết định. Phần critique: em nhờ AI đánh giá theo 10 heuristic của Nielsen, WCAG và persona, được 5 phát hiện gắn với từng màn hình."

**Slide 07 · Quyết định thiết kế (50 giây)**
> "Em không nhận hết đề xuất của AI. Ví dụ AI đề xuất cho huỷ đơn bất kỳ lúc nào; em chỉ cho huỷ trong 60 giây đầu, vì sau đó bếp đã nấu và quán sẽ lỗ. Với chữ trên nút, em giữ màu cam thương hiệu cho nền nhưng đổi chữ sang nâu #622B14, đạt 5,23:1."
> *(Chỉ nhắc tới đề xuất bị từ chối nếu nó thật sự có trong log.)*

**Slide 08 · Wireframe → Final UI (45 giây)**
> "Đây là màn Chi tiết món và màn lỗi thanh toán, ở bản wireframe và bản cuối. Mỗi màn chỉ có một hành động chính ghim ở đáy. Các biến thể như giỏ trống, lỗi thanh toán và dialog được đặt ngay cạnh màn gốc ở Page 03."

**Slide 09 · Design system (45 giây)**
> "Token gồm màu, chữ Nunito, spacing theo lưới 4 dp, bo góc và elevation, đều là Figma Variables. Em có đủ 9 nhóm component với các state theo đề. Khi đổi một biến màu thì mọi màn hình dùng component đó tự cập nhật."

**Slide 10 · Accessibility (50 giây)**
> "Em phải nói thật là lần đo đầu em ghi sai: chữ trắng trên cam ghi 3,08 nhưng thực tế là 2,14, và em cũng tưởng chữ nút 14sp đậm được tính là chữ lớn. Theo WCAG thì chữ lớn phải từ khoảng 18,7px đậm. Em đã đo lại và đổi bốn token. Giờ chữ nút đạt 5,23, chữ phụ đạt 5,2, viền ô nhập đạt 3,93. Bố cục em đã kiểm ở 360 và 412 dp." *(chỉ vào ảnh)*

**Slide 11 · Prototype (20 giây, rồi chuyển sang demo)**
> "Em xin demo trực tiếp 3 flow trên Figma."

**Slide 12 · Handoff (để sau demo, 40 giây)**
> "Handoff có đủ 6 mục cho cả 8 màn: layout, component, state, tương tác, điều hướng và ràng buộc, kèm hai bảng ánh xạ token sang ThemeData và component sang widget. Điểm còn tồn tại là [..]."

---

## Phần 2 — Demo trực tiếp (5 phút)

Làm theo thứ tự trong hướng dẫn chấm.

1. **Mở Figma, cho thấy 6 page** (15 giây): 01 User Flow → 02 Wireframe → 03 Final UI → 04 Design System → 05 Components → 06 Prototype.
2. **Page 03: chỉ 8 màn khác nhau** (20 giây): SCR-01 → SCR-08, nói rõ giỏ trống, SCR-06-ERR và dialog là biến thể.
3. **Page 06: bấm Present, chạy từng flow:**

   **F1 — Đặt nhanh (khoảng 60 giây)**
   SCR-02 Home → bấm thẻ *Combo Tacos Bò Phô Mai* → SCR-04 tick topping (giá trên nút tự tăng) → *Thêm vào giỏ* → SCR-05 chọn giờ nhận → *Tiến hành thanh toán* → SCR-06 chọn *Tiền mặt tại quầy* → *Xác nhận* → **dialog overlay** → *Đồng ý* → **loading** → SCR-07 mã nhận đồ #A-204.
   Sau đó bấm **Back** để cho thấy quay về đúng màn trước.

   **F2 — Tuỳ chỉnh & voucher (khoảng 45 giây)**
   SCR-03 Menu → chọn món mì trộn → SCR-04 chọn mức cay và 2 topping → *Thêm vào giỏ* → SCR-05 nhập mã sai → **báo lỗi có icon và lý do** → nhập `FTASV20` → giảm giá thành công → thanh toán QR → SCR-07.

   **F3 — Lỗi thanh toán & phục hồi (khoảng 45 giây)**
   SCR-06 chọn MoMo → *Xác nhận thanh toán* → loading → **SCR-06-ERR** ("giỏ hàng vẫn được giữ") → bấm *Chuyển sang trả tiền mặt* → SCR-07. Nói thêm: nút *Thử lại* đưa về bước loading.

4. **Page 05 Components** (30 giây): chọn Button và cho xem các variant default, pressed, disabled, loading cùng Auto Layout. Mở bảng Variables, đổi thử một biến màu rồi hoàn tác.
5. **AI log** (30 giây): mở `ai/ai-design-log.md`, đi theo Vòng 1: prompt → ảnh trước/sau → kết quả đo lại → quyết định #06 → chỗ thay đổi trong Figma.
6. **GitHub** (20 giây): cho thấy cấu trúc repo, `design/screen-spec.md` và hai bảng ánh xạ trong `handoff/flutter-handoff.md`.

Nếu prototype hỏng giữa chừng: đừng sửa tại chỗ. Mở Page 03 và giải thích bằng frame, ghi lại lỗi để sửa sau.

---

## Phần 3 — Chuẩn bị hỏi đáp (5 phút)

| Câu thầy có thể hỏi | Ý trả lời |
|---|---|
| Persona cần gì mà em chọn kiểu điều hướng này? | Thao tác một tay khi di chuyển → bottom nav 4 tab trong vùng ngón cái, CTA ghim đáy. |
| Flow nào dễ lỗi nhất, phục hồi thế nào? | F3, vì phụ thuộc cổng thanh toán và mạng. Giỏ hàng được giữ, có 2 lối ra là Thử lại và Tiền mặt, nên không có ngõ cụt. |
| Đề xuất AI nào em từ chối hoặc sửa, vì sao? | Huỷ đơn bất kỳ lúc nào → chỉ cho huỷ trong 60 giây vì ràng buộc của bếp. Chữ trắng trên cam → đổi sang nâu vì đo chỉ 2,14:1. *(Nêu đề xuất bị từ chối chỉ khi có trong log.)* |
| Ba vòng lặp giải quyết ba vấn đề gì? | Tương phản và phân cấp CTA · thiếu empty state và dễ xoá nhầm · lỗi thanh toán là ngõ cụt. |
| Đổi primary color thì màn nào tự cập nhật? | Mọi màn dùng instance của Button, Navigation và badge, tức SCR-02 đến SCR-07. *(Demo đổi biến để chứng minh.)* |
| Làm sao biết 412 dp không vỡ layout? | Đổi frame sang 412, Auto Layout chọn Fill container, lề vẫn 16 dp. Chỉ vào ảnh 360/412. |
| Lập trình viên Flutter chưa biết dự án dựa vào đâu? | `handoff/flutter-handoff.md`: 6 mục mỗi màn và hai bảng ánh xạ; Figma chỉ để xem hình. |
| Sao số tương phản trong bản trước khác bây giờ? | Em đo sai và hiểu sai định nghĩa chữ lớn; đã đo lại bằng công thức WCAG và ghi lịch sử thay đổi ở DESIGN.md mục 2.5. |
| Sao ngày tạo Stitch trong log khác ngày commit? | Trả lời đúng sự thật về thời điểm bạn làm. Đừng đoán. |

Đề có nói có thể hỏi riêng 5 phút: đi qua một flow trong prototype và giải thích hai quyết định trong log. Hãy chuẩn bị sẵn F3, quyết định #04 (huỷ trong 60 giây) và quyết định #06 (đổi chữ sang nâu).
