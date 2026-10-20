# Kịch bản trình bày theo bộ Google Slides (12 slide)

Bám theo bộ slide trên Google Slides của bạn (bản tải ngày 17/10/2026).
Thời lượng: **10 phút slide → 5 phút demo → 5 phút hỏi đáp**.

> **Đọc phần 0 trước.** Bộ slide hiện có nhiều chỗ khác repo GitHub và file Figma. Thầy chấm theo repo và Figma, nên phải sửa slide cho khớp trước khi trình bày. Lời thoại ở phần 1 đã viết theo nội dung **đúng của repo**.

---

## Phần 0 — Sửa trên Google Slides trước khi trình bày (khoảng 20 phút)

| Slide | Đang ghi | Vấn đề | Sửa thành |
|---|---|---|---|
| 01 | "PRM393 — LAB 2" | Mã môn là **PRM323** | "PRM323 — LAB 2". Thêm họ tên, MSSV, link GitHub và link Figma |
| 02 | Minh Anh · nghỉ 20 phút · dưới 45 giây | Repo ghi **Nguyễn Minh Quân · 15 phút · dưới 35 giây, tối đa 8 chạm** | Đổi theo repo. Ghi đầy đủ "Thói quen: dùng điện thoại **một tay** khi di chuyển" (đang bị cụt) |
| 03 | SCR-07 Theo dõi đơn nằm ở hàng "cấp con" | Repo coi SCR-07 là tab cấp cao (tab 3) | Chuyển SCR-07 lên hàng cấp cao cùng 02, 03, 08. Hàng cấp con còn 04, 05, 06 |
| 04 | L1 "Onboarding → Giỏ hàng", L3 "Tùy chọn món: Trang chủ → Khám phá món" | Không khớp repo và Figma Page 01. L1 dừng ở giỏ hàng là chưa tới đích; L3 không có đích rõ ràng | Dùng 3 flow trong repo (bảng ngay dưới đây) |
| 05 | Chỉ có 4 dòng tóm tắt dưới tiêu đề "Prompt nguyên văn" | Hướng dẫn chấm yêu cầu prompt **nguyên văn** | Dán một đoạn trích nguyên văn trong ngoặc kép, ghi "Toàn văn: ai-design-log.md mục 2.1" |
| 06 | Không có ảnh trước/sau | Rubric yêu cầu có ảnh trước/sau | Chèn 3 cặp ảnh **sau khi đã chụp lại thật** (ảnh hiện trong repo bị trùng nhau) |
| 07 | "Tăng tương phản… Đạt WCAG 2.1 AA (5.2:1)" | Chữ trắng trên `#F69D39` chỉ đạt **2,14:1**. Con số 5,2:1 chỉ đúng khi chữ nút là nâu `#622B14` | Ghi "Chỉnh sửa: giữ nền cam, đổi chữ nút sang nâu #622B14 → 5,23:1" và đổi Figma cho khớp. Cột "Từ chối – bản đồ 3D": chỉ giữ nếu thật sự có trong log, và thêm vào `ai/ai-design-log.md` |
| 09 | "0% giá trị gán cứng", "24+ biến thể", "Instance liên kết Variables" | Mình chưa kiểm được vì Figma bắt đăng nhập. Thầy có thể bảo bạn đổi một biến ngay tại chỗ | Chỉ giữ các con số đã tự đếm và kiểm trong Figma |
| 10 | "Văn bản chính 7.4:1", "CTA chuẩn ≥ 3.0:1 đạt 5.2:1", "8/8 màn không tràn" | Chữ chính thật là **10,37:1**. Chữ nút 14–15sp đậm không phải "chữ lớn" nên ngưỡng là **4,5:1**, không phải 3:1. "8/8 màn" cần ảnh làm minh chứng | Ghi: chữ chính 10,37:1 · chữ nút 5,23:1 (ngưỡng 4,5:1) · chữ phụ 5,2:1 · viền ô nhập 3,93:1 (ngưỡng 3:1). Chèn ảnh 360/412 dp |

**Bảng 3 flow để dán vào slide 04** (khớp `ux/user-flow.md`):

| Flow | Start → End | Nhánh thay thế / lỗi | Màn hình |
|---|---|---|---|
| F1 Đặt nhanh, nhận tại quầy | Home (02) → Theo dõi đơn (07) | Dialog xác nhận → loading → mã nhận đồ | 02, 04, 05, 06, 07 |
| F2 Tuỳ chỉnh món & voucher | Menu (03) → Theo dõi đơn (07) | Mã voucher sai → báo lỗi kèm lý do → nhập lại | 03, 04, 05, 06, 07 |
| F3 Lỗi thanh toán & phục hồi | Checkout (06) → Theo dõi đơn (07) | MoMo timeout → Thử lại **hoặc** chuyển tiền mặt; giỏ hàng được giữ | 05, 06, 06-ERR, 07 |

---

## Phần 1 — Lời thoại theo từng slide (10 phút)

**Slide 01 · Thiết Kế UI/UX Có Hỗ Trợ AI (40 giây)**
> "Em là [tên], MSSV [..]. Đề tài là FtaCode Mobile, app đặt đồ ăn nhanh trong khuôn viên trường. Bài có 8 màn hình trên Figma, 3 luồng tương tác và bản đặc tả handoff cho Flutter. Link repo và Figma ở dưới."

**Slide 02 · Vấn đề & Chân dung người dùng (60 giây)**
> "Persona chính là Minh Quân, 20 tuổi, sinh viên năm 2. Giữa hai ca học bạn ấy chỉ có 15 phút, mà xếp hàng ở căn tin đã mất gần hết thời gian đó. Bạn ấy vừa đi vừa cầm máy một tay, mạng chập chờn, hay dùng ngoài nắng. Mục tiêu là đặt trước rồi ghé quầy lấy luôn. Tiêu chí thành công: đặt xong một đơn dưới 35 giây, tối đa 8 lần chạm từ Trang chủ."
>
> *Nếu bị hỏi "cơ sở đâu":* trả lời theo `phan-bien-hoi-dap.md` mục B1 — nói rõ đây là persona giả định, hoặc nêu kết quả khảo sát nếu bạn đã làm.

**Slide 03 · Kiến trúc thông tin (50 giây)**
> "App có 8 màn hình độc lập, chia 2 tầng. Onboarding là màn vào app, chỉ hiện lần đầu. Tầng cấp cao là 4 tab dưới đáy: Trang chủ, Thực đơn, Theo dõi đơn, Lịch sử. Tầng cấp con là Chi tiết món, Giỏ hàng và Thanh toán. Giỏ trống và lỗi thanh toán là biến thể trạng thái, không tính là màn riêng. Em dùng bottom navigation vì persona thao tác bằng ngón cái."

**Slide 04 · Ba luồng người dùng (60 giây)**
> "Luồng 1 là luồng chính: từ Trang chủ chọn combo, thêm topping, vào giỏ, chọn giờ nhận, thanh toán, rồi nhận mã lấy đồ ở màn Theo dõi đơn. Luồng 2 bắt đầu từ Thực đơn: tuỳ chỉnh mức cay và topping, nhập voucher; nếu mã sai thì app báo rõ lý do để nhập lại. Luồng 3 là luồng lỗi bắt buộc: thanh toán MoMo bị timeout thì app giữ nguyên giỏ hàng và cho hai lối ra là Thử lại hoặc chuyển sang tiền mặt tại quầy. Không có ngõ cụt."

**Slide 05 · Khởi tạo UI với Google Stitch (50 giây)**
> "Em viết DESIGN.md trước để chốt màu, chữ và quy tắc component, rồi mới viết prompt. Prompt có đủ năm phần: ngữ cảnh persona, nhiệm vụ cho 4 màn hình, nền tảng 360×800 Material 3, ràng buộc vùng chạm 48 dp, và phong cách màu ấm. Đây là màn Home Stitch sinh ra lần đầu. Toàn văn prompt nằm trong ai-design-log mục 2.1."

**Slide 06 · Ba vòng lặp AI & Phản biện UX (70 giây)**
> "Mỗi vòng giải quyết một vấn đề có tên, không phải yêu cầu 'làm đẹp hơn'. Vòng 1: nút CTA khó đọc và bị chìm, em ghim nút xuống đáy và hiện giá động. Vòng 2: thiếu màn giỏ trống và dễ xoá nhầm, em thêm empty state và dialog xác nhận xoá. Vòng 3: lỗi thanh toán thành ngõ cụt, mất giỏ hàng, em thêm màn phục hồi. *(chỉ vào ảnh trước/sau)* Sau đó em nhờ AI phản biện theo 10 heuristic của Nielsen, WCAG và persona. Được 5 phát hiện, mỗi phát hiện gắn với một màn hình, ví dụ màn Home thiếu trạng thái quầy mở hay đóng, vi phạm heuristic số 1."

**Slide 07 · Quyết định thiết kế trọng tâm (60 giây)**
> "Em không nhận hết đề xuất của AI. Chấp nhận: thêm thông báo lỗi thanh toán và giữ giỏ hàng, theo heuristic số 9. Chỉnh sửa: AI đề xuất chữ trắng trên nút cam, nhưng em đo lại chỉ đạt 2,14:1, nên em giữ nền cam thương hiệu và đổi chữ sang nâu, đạt 5,23:1. Cũng chỉnh sửa: AI muốn cho huỷ đơn bất kỳ lúc nào; em chỉ cho huỷ trong 60 giây đầu vì sau đó bếp đã nấu."
> *(Chỉ nói câu sau nếu thật sự có trong log:)* "Từ chối: bản đồ 3D theo dõi đơn, vì sinh viên nhận đồ ngay tại quầy nên tiến trình 4 bước là đủ."

**Slide 08 · Từ wireframe đến giao diện cuối (45 giây)**
> "Ở Page 02 em chốt bố cục 8 màn bằng khung xám trước, để sửa luồng mà không bị màu làm phân tâm. Ở Page 03 mỗi màn chỉ có một nút hành động chính. Các biến thể giỏ trống và lỗi mạng được đặt ngay cạnh màn gốc. Nhãn tiếng Việt và Auto Layout thống nhất trên mọi màn."

**Slide 09 · Hệ thống thiết kế & Component (50 giây)**
> "Em có 5 nhóm token: màu, chữ, khoảng cách, bo góc, độ nổi, đều là Figma Variables. Ở Page 05 em có 5 component set có variant: Button, TextField, Card món, NavBar, Dialog, mỗi cái có các state như default, pressed, disabled, loading, error. Màu trên màn hình đã gắn vào biến, nên đổi một token thì màu cả app cập nhật. Phần còn thiếu em nói thật: các màn chưa thay bằng instance của component."
> *(Chỉ đọc con số "24+" và "0%" nếu đã tự kiểm.)*

**Slide 10 · Khả năng truy cập & đáp ứng (60 giây)**
> "Em kiểm bằng công thức WCAG chứ không nhìn bằng mắt. Chữ chính nâu trên nền kem đạt 10,37:1. Chữ trên nút đạt 5,23:1. Lần đầu em ghi sai: em tưởng chữ nút 14sp đậm là chữ lớn nên chỉ cần 3:1, nhưng WCAG yêu cầu chữ đậm phải từ khoảng 18,7px. Vì vậy em đổi màu chữ nút và ghi lịch sử thay đổi trong DESIGN.md. Vùng chạm tối thiểu 48 dp, chữ nội dung từ 14sp. Bố cục em kiểm ở 360 và 412 dp." *(chỉ vào ảnh)*

**Slide 11 · Nguyên mẫu tương tác (15 giây → chuyển sang demo)**
> "Prototype có 3 điểm bắt đầu riêng, dialog overlay, chuyển cảnh loading sang kết quả và nút Back. Em xin demo trực tiếp."

**Slide 12 · Bàn giao Flutter & Tổng kết (40 giây, nói sau demo)**
> "Handoff có đủ 6 mục cho cả 8 màn: layout, component, state, tương tác, điều hướng và ràng buộc UI, kèm hai bảng ánh xạ token sang ThemeData và component sang widget. Điều em rút ra là không tin con số của AI mà phải tự đo lại. Hạn chế: persona chưa được kiểm chứng với nhiều người dùng thật. Em xin nhận câu hỏi."

---

## Phần 2 — Flow demo trên Figma (5 phút)

Chuẩn bị: đăng nhập Figma, mở sẵn file và tab GitHub, phóng to màn hình. Chạy thử toàn bộ một lần trước buổi chấm.

| # | Làm gì | Nói gì | Thời gian |
|---|---|---|---|
| 1 | Mở sidebar, lần lượt bấm 6 page | "File có đúng 6 page theo thứ tự đề." | 15 giây |
| 2 | Page 03, chỉ từng frame SCR-01 → SCR-08 | "8 màn khác nhau. Giỏ trống, lỗi thanh toán và dialog là biến thể." | 20 giây |
| 3 | Page 06 → **Present** → chọn flow **F1** | Đi theo: Home → thẻ Combo Tacos → tick topping (*"giá trên nút tự cộng"*) → Thêm vào giỏ → chọn giờ nhận → Tiến hành thanh toán → Tiền mặt → Xác nhận → **dialog overlay** → Đồng ý → **loading** → mã #A-204 | 70 giây |
| 4 | Bấm **Back** | "Back về đúng màn trước, không có ngõ cụt." | 10 giây |
| 5 | Chọn flow **F2** | Thực đơn → món mì → chọn mức cay và topping → giỏ → nhập mã sai (*"báo lỗi có icon và lý do"*) → nhập `FTASV20` → giảm giá → thanh toán | 45 giây |
| 6 | Chọn flow **F3** | Checkout → MoMo → loading → **màn lỗi** (*"giỏ hàng vẫn được giữ"*) → Chuyển tiền mặt → Theo dõi đơn | 45 giây |
| 7 | Thoát Present → Page 05, chọn Button | Cho xem variant default / pressed / disabled / loading và Auto Layout | 25 giây |
| 8 | Mở Variables, đổi `color-primary` → xem Page 03 → Ctrl+Z | "Đổi một biến, mọi màn dùng instance tự đổi." | 25 giây |
| 9 | Mở `ai/ai-design-log.md` trên GitHub | Đi theo Vòng 1: prompt → ảnh trước/sau → đo lại 2,14:1 → quyết định #06 → chữ nâu trong Figma | 30 giây |
| 10 | Mở `handoff/flutter-handoff.md` | Chỉ hai bảng ánh xạ và 6 mục của một màn | 15 giây |

Tên nút trong bảng lấy theo `ux/user-flow.md`. Nếu trong Figma tên khác thì sửa bảng này cho đúng.

**Nếu bị lỗi khi demo:**
- **Prototype đứng:** thoát Present, giải thích bằng frame ở Page 03. Không sửa tại chỗ.
- **Đổi biến mà có màn không đổi màu:** nói thật là màn đó còn màu gán cứng và em sẽ gán lại vào biến. Đừng chống chế. Tốt nhất là kiểm việc này trước buổi chấm.

---

## Phần 3 — Hỏi đáp

Xem file `phan-bien-hoi-dap.md`. Ba câu bộ slide này dễ bị hỏi nhất:

1. **"Slide ghi 5,2:1 / 7,4:1, em đo bằng gì?"** → Bằng công thức WCAG (hoặc WebAIM Contrast Checker). Nêu số đúng và kể chuyện đã sửa.
2. **"Từ chối bản đồ 3D — AI đề xuất ở đâu?"** → Phải chỉ ra được trong log. Không có thì đừng đưa lên slide.
3. **"0% giá trị gán cứng — chứng minh đi."** → Demo đổi biến (bước 8). Không chắc chắn thì bỏ con số này khỏi slide.
