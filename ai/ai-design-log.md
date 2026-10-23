# AI Design Log: Prompts, Iterations, Critique & Decisions

> **Ghi chú đổi tên (21/10/2026):** dự án tên cũ là FtaCode, đổi thành BreakBite. Tên trong file này đã được thay theo tên mới; prompt gốc gửi cho Google Stitch và Gemini dùng tên FtaCode, và dự án trên Google Stitch vẫn mang tên cũ.


> **Bản đọc nhanh:** [`ai-prompt-log-chuan-hoa.md`](ai-prompt-log-chuan-hoa.md) viết lại các bước theo khung prompt chuẩn (không phải nguyên văn); file này giữ nguyên văn.
>
> **Tài liệu:** `ai/ai-design-log.md`  
> **Dự án:** BreakBite App — Campus Quick Food Ordering  
> **Môn học:** PRM323 — Lab 2  

---

## 1. Khai báo công cụ AI (AI Disclosure)

Theo đúng quy định mục 5 của đề bài Lab 2, danh sách các công cụ AI được sử dụng trong suốt quá trình thiết kế giao diện được công bố minh bạch:

1. **Google Stitch (`stitch.withgoogle.com`):** Sử dụng để tạo bản phác thảo giao diện ban đầu (Generative UI) cho các màn hình chính dựa trên bản mô tả thiết kế `DESIGN.md`.
2. **Google Gemini (Advanced / Flash) & Claude:** Đóng vai trò Trợ lý AI Phản biện Độc lập (AI Critique Assistant), đánh giá giao diện dựa trên 10 Usability Heuristics của Jakob Nielsen và WCAG 2.1 AA.
3. **Antigravity AI Assistant:** Hỗ trợ cấu trúc tài liệu đặc tả, kiểm tra logic User Flows và sinh mã tự động hóa Figma.

---

## 2. Giai đoạn 1: Prompt sinh UI ban đầu trên Google Stitch (Initial UI Generation)

### 2.1 Câu Prompt nguyên văn (Verbatim Prompt)
Câu prompt dưới đây được thiết kế tỉ mỉ, đưa đầy đủ thông tin về Persona, Nhiệm vụ, Nền tảng di động, Ràng buộc và Phong cách thiết kế từ `DESIGN.md`:

```text
Act as a Principal Mobile Product Designer. Design a modern, appetizing mobile food ordering application named "BreakBite" tailored specifically for university students with short 15-minute breaks on campus.

Platform & Canvas:
- Mobile App UI, Screen resolution 360 x 800 dp (compact portrait layout).
- Follow Material Design 3 guidelines with comfortable thumb-zone reachability.

Primary Screens to Generate:
1. Home / Discovery Screen (SCR-02): Top app bar showing campus kiosk location "Kiosk Tòa Alpha", search bar with placeholder "Tìm Tacos, Mì trộn, Nước...", quick horizontal category pills ("Tất cả", "Tacos giòn", "Mì trộn cay", "Đồ uống"), promotional hero banner "Combo Giờ Vàng - Giảm 15%", and vertical list of food cards with appetizing images, cook time badge ("⚡ 3-5m"), price, and quick add (+) button. Bottom navigation bar with 4 tabs: Trang chủ, Thực đơn, Đơn hàng, Cá nhân.
2. Product Detail Screen (SCR-04): Large hero food image for "Combo Tacos Bò Phô Mai", price 39.000đ, preparation time "~4m", description, spice level selector (3 radio options: Không cay, Cay vừa, Siêu cay), topping checkboxes (Thêm Phô mai +8k, Trứng ốp la +5k), chef note input, and a sticky bottom bar with quantity counter (+/-) and a bold CTA button "Thêm vào giỏ hàng • 39.000đ".
3. Cart & Order Summary (SCR-05): List of selected items with quantity adjusters, Campus Pickup time selector dropdown ("Lấy ngay (~7m)" or "Hẹn giờ 09:20"), student voucher input field with "Áp dụng" button, cost summary breakdown, and bottom CTA button "Tiến hành thanh toán".
4. Pickup Status / Order Tracking (SCR-07): Large bold pickup pass token "#A-204", dynamic QR code for kiosk scanner, 4-step progress tracker (Đã nhận đơn -> Đang chuẩn bị -> Sẵn sàng -> Hoàn tất), and kiosk hotline button.

Design System & Aesthetics:
- Color Palette: Warm creamy background (#FFF5E5), Primary warm energetic orange (#F69D39), Deep espresso brown text for maximum contrast (#622B14), secondary golden yellow (#E0C375), crisp white surface cards (#FFFFFF).
- Typography: Rounded friendly modern sans-serif (Nunito style).
- Layout: Generous whitespace, clean card elevation, touch targets strictly minimum 48x48 dp.
```

### 2.2 Kết quả ban đầu từ Stitch (Initial Stitch Output)
* **Google Stitch Project ID:** `18314376874619200698` ("BreakBite - Campus Quick Food Ordering")
* **AI Model Engine:** Google Stitch with `GEMINI_3_8_FLASH`
* **Ngày tạo:** 15/10/2026. **[TODO: kiểm tra lại ngày trong Stitch — commit lưu ảnh Stitch đầu tiên có ngày 13/10/2026, vòng lặp có ngày 14/10/2026.]**
* **Đánh giá ban đầu:** AI sinh ra được bố cục màn hình chuẩn Mobile 360x800dp với màu sắc ấm áp, thẻ sản phẩm bắt mắt, tuân thủ Material Design 3 và Design Tokens từ `DESIGN.md`.
* **Minh chứng ảnh chụp:** Được lưu trữ đầy đủ tại thư mục:  
  * [`assets/stitch/01_initial_stitch_home.png`](../assets/stitch/01_initial_stitch_home.png)
  * [`assets/stitch/02_initial_stitch_detail.png`](../assets/stitch/02_initial_stitch_detail.png)
  * [`assets/stitch/03_initial_stitch_cart.png`](../assets/stitch/03_initial_stitch_cart.png)
  * [`assets/stitch/04_initial_stitch_tracking.png`](../assets/stitch/04_initial_stitch_tracking.png)
* **Dự án Google Stitch:** Project ID `18314376874619200698` ("BreakBite - Campus Quick Food Ordering", Mobile).
* **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/JeWtr0nQ6pD2cPzjUMqU6A/Untitled?node-id=1-6&t=kxQCPUOcwGKqvyJc-1) *(Bao gồm đầy đủ 6 Trang & 3 Flow Prototype tương tác)*

---

## 3. Giai đoạn 2: Ba vòng lặp tinh chỉnh có ý nghĩa (3 Meaningful AI Iterations)

Theo quy định nghiêm ngặt của đề bài, mỗi vòng lặp dưới đây đều nhắm vào một vấn đề UX cụ thể có tên gọi rõ ràng, tuyệt đối không yêu cầu "làm đẹp hơn" chung chung.

---

### Vòng lặp 1 (Iteration 1): Khắc phục độ tương phản thấp & Phân cấp thị giác nút CTA yếu
* **Tên vấn đề UX cụ thể:** *Low Contrast & Weak Visual Hierarchy on Primary Action Button*.
* **Phân tích vấn đề:** Ở phiên bản ban đầu, nút "Thêm vào giỏ hàng" và nút "Tiến hành thanh toán" sử dụng chữ màu trắng trên nền cam nhạt (#FFB366), tỷ lệ tương phản chỉ đạt $2.3:1$ (không đạt chuẩn WCAG AA). Ngoài ra, nút CTA bị chìm lẫn vào danh sách nội dung cuộn bên dưới thay vì ghim cố định ở đáy màn hình.
* **Prompt tinh chỉnh đưa vào AI:**
  ```text
  Iteration 1 Refinement:
  Fix low contrast and visual hierarchy on SCR-04 (Product Detail) and SCR-05 (Cart):
  1. Increase the primary orange button color to a rich saturated #F69D39 and use bold white text (Nunito Bold, 15sp) with an elevation drop shadow to ensure WCAG AA compliance.
  2. Pin the CTA button inside a sticky bottom navigation bar with a solid white background (#FFFFFF) and top border (#EEDBCA), ensuring it stays fixed above the fold while content scrolls behind it.
  3. Update dynamic price feedback directly on the button text: "Thêm vào giỏ hàng • 47.000đ".
  ```
* **Kết quả cải tiến:** Nút CTA được ghim đáy, giá tiền hiển thị động trên nút.
* **Kiểm tra lại sau vòng lặp (bổ sung):** Đo lại bằng công thức WCAG, chữ trắng trên `#F69D39` chỉ đạt **2,14:1**, vẫn **không đạt** 4,5:1. Vì vậy đề xuất "dùng chữ trắng trên `#F69D39`" của vòng này được ghi nhận là **CHỈNH SỬA (Modify)**: giữ nền cam thương hiệu nhưng đổi chữ trên nút sang nâu `#622B14` (5,23:1). Xem `design/DESIGN.md` mục 2.5 và quyết định #06 bên dưới.
* **⚠ Minh chứng cần chụp lại:** ảnh *trước* và *sau* của vòng này hiện là bản sao của ảnh Stitch ban đầu (trùng byte với file khác trong `assets/stitch/`), nên chưa cho thấy thay đổi. **[TODO: mở lịch sử phiên bản trong Stitch, chụp đúng màn hình trước và sau khi chạy prompt tinh chỉnh, ghi đè hai file bên dưới.]**
* **Minh chứng ảnh Before / After:**  
  * Ảnh trước (Before): [`assets/stitch/iteration1_before_cta_contrast.png`](../assets/stitch/iteration1_before_cta_contrast.png)  
  * Ảnh sau (After): [`assets/stitch/iteration1_after_cta_contrast.png`](../assets/stitch/iteration1_after_cta_contrast.png)

---

### Vòng lặp 2 (Iteration 2): Xử lý trạng thái rỗng và phòng ngừa lỗi thao tác trong Giỏ hàng
* **Tên vấn đề UX cụ thể:** *Missing Empty State & Lack of Error Prevention during Cart Operations*.
* **Phân tích vấn đề:** Phiên bản ban đầu của Stitch không có màn hình khi giỏ hàng trống (Empty State) khiến màn hình trắng trơn nếu người dùng xóa hết món. Ngoài ra, khi người dùng bấm giảm số lượng về 0 thì món ăn lập tức biến mất mà không có cảnh báo xác nhận, dễ gây xóa nhầm.
* **Prompt tinh chỉnh đưa vào AI:**
  ```text
  Iteration 2 Refinement:
  Address missing empty state and accidental item deletion in SCR-05 (Cart):
  1. Design an engaging Empty State variant: Display a friendly illustration of an empty lunch plate, clear headline "Giỏ hàng của bạn đang đói 🌮", supportive body text "Hãy chọn món ăn yêu thích để nạp năng lượng cho ca học tiếp theo nhé!", and a prominent Primary Button "Khám phá thực đơn ngay" navigating back to SCR-02.
  2. Implement an error prevention pattern: When quantity decreases from 1 to 0, trigger a confirmation micro-dialog "Bạn có chắc chắn muốn xóa món này khỏi giỏ hàng?" with distinct Cancel and Confirm Destructive buttons.
  ```
* **Kết quả cải tiến:** Giỏ hàng có trải nghiệm liền mạch, không bị rơi vào ngõ cụt; phòng ngừa triệt để việc sinh viên bấm nhầm nút trừ khi đang đi bộ.
* **⚠ Minh chứng cần chụp lại:** ảnh *trước* và *sau* của vòng này hiện là bản sao của ảnh Stitch ban đầu (trùng byte với file khác trong `assets/stitch/`), nên chưa cho thấy thay đổi. **[TODO: mở lịch sử phiên bản trong Stitch, chụp đúng màn hình trước và sau khi chạy prompt tinh chỉnh, ghi đè hai file bên dưới.]**
* **Minh chứng ảnh Before / After:**  
  * Ảnh trước (Before): [`assets/stitch/iteration2_before_empty_state.png`](../assets/stitch/iteration2_before_empty_state.png)  
  * Ảnh sau (After): [`assets/stitch/iteration2_after_empty_state.png`](../assets/stitch/iteration2_after_empty_state.png)

---

### Vòng lặp 3 (Iteration 3): Bổ sung màn hình phục hồi lỗi thanh toán (Error & Recovery Path)
* **Tên vấn đề UX cụ thể:** *Dead-end Error State during Network & Payment Failure (Flow 3)*.
* **Phân tích vấn đề:** Khi giả lập tình huống mất mạng hoặc ví MoMo/Ngân hàng bị timeout, phiên bản ban đầu chỉ hiển thị 1 thông báo toast màu đỏ "Thanh toán thất bại" rồi đưa người dùng về lại trang chủ và XÓA SẠCH giỏ hàng. Đây là lỗi UX nghiêm trọng (Dead-end) gây ức chế tột độ cho sinh viên.
* **Prompt tinh chỉnh đưa vào AI:**
  ```text
  Iteration 3 Refinement:
  Design a dedicated Error Recovery Screen (SCR-06-ERR) for Payment & Connectivity Failures:
  1. Do NOT discard user cart data. Show an empathetic headline "Chưa thể hoàn tất thanh toán" with plain language explanation: "Giao dịch qua ví điện tử tạm thời bị gián đoạn hoặc hết thời gian chờ (60s). Giỏ hàng của bạn vẫn được giữ nguyên."
  2. Provide two clear action paths:
     - Secondary Button: "Thử lại thanh toán online" (Retries gateway connection).
     - Primary Button: "Chuyển sang trả tiền mặt tại quầy Kiosk" (Instant conversion to Cash on Pickup so order is preserved and student can proceed immediately to class).
  ```
* **Kết quả cải tiến:** Đáp ứng 100% yêu cầu của Flow 3 (Error & Recovery Path), người dùng không bao giờ bị mất dữ liệu đặt món.
* **⚠ Minh chứng cần chụp lại:** ảnh *trước* và *sau* của vòng này hiện là bản sao của ảnh Stitch ban đầu (trùng byte với file khác trong `assets/stitch/`), nên chưa cho thấy thay đổi. **[TODO: mở lịch sử phiên bản trong Stitch, chụp đúng màn hình trước và sau khi chạy prompt tinh chỉnh, ghi đè hai file bên dưới.]**
* **Minh chứng ảnh Before / After:**  
  * Ảnh trước (Before): [`assets/stitch/iteration3_before_error_handling.png`](../assets/stitch/iteration3_before_error_handling.png)  
  * Ảnh sau (After): [`assets/stitch/iteration3_after_error_handling.png`](../assets/stitch/iteration3_after_error_handling.png)

---

## 4. Giai đoạn 3: Phản biện UX độc lập bằng AI (AI-based UX Critique)

Chúng tôi đã sử dụng Trợ lý AI đóng vai trò Chuyên gia đánh giá Heuristic độc lập với câu lệnh kiểm thử:
> *"Hãy đánh giá nghiêm khắc toàn bộ thiết kế giao diện của BreakBite dựa trên 10 Usability Heuristics của Jakob Nielsen, tiêu chuẩn tiếp cận WCAG 2.1 và đặc điểm của Persona sinh viên bận rộn."*

> Bản trả lời đầy đủ của lần critique này không được lưu; các mục dưới đây là bản tóm tắt. Vòng critique bổ sung có nguyên văn đầy đủ ở **Phụ lục A**.

### 5 Phát hiện phản biện cụ thể gắn với từng màn hình:

1. **Phát hiện 1 (Màn hình SCR-02 - Heuristic #1: Visibility of system status):**
   * *Đánh giá của AI:* Màn hình chính hiển thị tên quán nhưng không hiển thị trạng thái quầy Kiosk đang "Mở cửa" hay "Đang tạm dừng nhận đơn vì quá tải". Sinh viên có thể chọn món xong xuôi mới phát hiện quầy đóng cửa.
2. **Phát hiện 2 (Màn hình SCR-04 - Heuristic #6: Recognition rather than recall):**
   * *Đánh giá của AI:* Khi chọn các loại topping có tính phí (ví dụ: Trứng non +8k), số tiền không tự động cộng dồn vào giá nút bấm bên dưới, buộc sinh viên phải tự làm phép tính cộng trong đầu.
3. **Phát hiện 3 (Màn hình SCR-05 - Heuristic #9: Help users recognize & recover from errors):**
   * *Đánh giá của AI:* Ô nhập mã giảm giá khi nhập sai mã chỉ đổi viền sang màu đỏ mà không có câu thông báo nguyên nhân cụ thể (ví dụ: "Mã đã hết hạn" hay "Mã chỉ áp dụng cho đơn trên 50k").
4. **Phát hiện 4 (Màn hình SCR-07 - Heuristic #3: User control and freedom):**
   * *Đánh giá của AI:* Màn hình theo dõi đơn hàng không có nút Hủy đơn nhanh hoặc chỉnh sửa trong vòng 60 giây đầu sau khi đặt. Nếu sinh viên lỡ tay bấm nhầm địa điểm Kiosk thì không có cách nào can thiệp.
5. **Phát hiện 5 (Màn hình SCR-03 - WCAG 2.5.5: Target Size):**
   * *Đánh giá của AI:* Các icon lọc danh mục ở góc nhỏ chỉ có kích thước $20 \times 20\text{ dp}$, quá nhỏ để sinh viên vừa đi bộ vừa bấm chính xác.

---

## 5. Giai đoạn 4: Bảng quyết định của sinh viên (Decision Record)

Theo đúng quy định của rubric: Mỗi quyết định đều ghi rõ Chấp nhận (Accept), Chỉnh sửa (Modify) hoặc Từ chối (Reject) kèm lý do gắn với Persona, Heuristic hoặc Ràng buộc kỹ thuật thực tế:

| # | Đề xuất từ bản AI Critique | Quyết định của nhóm | Lý do & Lập luận giải thích chi tiết |
| :---: | :--- | :---: | :--- |
| **01** | Bổ sung Banner trạng thái Kiosk (Mở cửa / Đóng cửa) tại `SCR-02`. | **CHẤP NHẬN (Accept)** | **Căn cứ Heuristic #1:** Rất cần thiết. Tránh việc sinh viên tốn thời gian chọn món khi quầy bếp đang quá tải. Đã bổ sung badge "🟢 Kiosk Tòa Alpha: Đang nhận món (Lấy trong 5-7p)". |
| **02** | Cộng dồn giá tiền động trực tiếp lên nút CTA `SCR-04`. | **CHẤP NHẬN (Accept)** | **Căn cứ Heuristic #6 & Persona:** Sinh viên có ngân sách giới hạn cần biết chính xác mình sẽ trả bao nhiêu tiền ngay khi tích chọn topping phô mai/trứng. |
| **03** | Thêm nhãn lỗi giải thích rõ lý do không dùng được mã voucher tại `SCR-05`. | **CHẤP NHẬN (Accept)** | **Căn cứ Heuristic #9 & WCAG 1.4.1:** Không dùng màu đỏ đơn thuần. Đã thêm icon `(!)` và text cảnh báo cụ thể: *"Mã FTASV20 chỉ áp dụng cho đơn từ 40.000đ"*. |
| **04** | Cho phép hủy đơn hàng vô điều kiện bất kỳ lúc nào tại `SCR-07`. | **CHỈNH SỬA (Modify)** | **Căn cứ Ràng buộc Nghiệp vụ Kiosk:** Nếu khách hủy đơn khi bếp đã làm xong thức ăn nóng thì quán sẽ bị tổn thất chi phí. Nhóm quyết định: **Chỉ cho phép hủy trong vòng 60 giây đầu tiên** (khi bếp chưa bấm "Bắt đầu nấu") kèm popup cảnh báo xác nhận. |
| **05** | Tăng kích thước icon lọc danh mục lên $48 \times 48\text{ dp}$ tại `SCR-03`. | **CHẤP NHẬN (Accept)** | **Căn cứ WCAG 2.5.5 & Công thái học:** Đảm bảo toàn bộ touch target đạt chuẩn $48\text{ dp}$ để sinh viên thao tác bằng 1 tay khi đang di chuyển. |
| **06** | (Kiểm tra lại sau Vòng 1) Dùng chữ trắng trên nút cam `#F69D39` để đạt WCAG AA. | **CHỈNH SỬA (Modify)** | **Căn cứ WCAG 1.4.3 & Persona dùng ngoài nắng:** đo lại chỉ 2,14:1. Giữ màu cam thương hiệu cho nền nút, đổi chữ sang nâu `#622B14` (5,23:1); thêm token `color-primary-text` `#B45309` cho chữ cam trên nền sáng. |
| **07** | (Phản biện persona, Phụ lục B5) Bỏ các con số không có nguồn (12–18 phút, giờ cao điểm). | **CHẤP NHẬN (Accept)** | Không có dữ liệu thật chống lưng; ghi lại thành giả thuyết cần đo. |
| **08** | (B5) Persona dùng iPhone nhưng thiết kế theo Android 360 dp. | **CHẤP NHẬN (Accept)** | Nhân vật đau nhất (A1, A5) dùng Android; khung 360 × 800 dp của đề là Android. Đổi thiết bị persona sang Android tầm trung. |
| **09** | (B5) Thêm rào cản "không muốn cài thêm app" (A3). | **CHỈNH SỬA (Modify)** | Ghi thành rủi ro sản phẩm, không đổi hướng: nhóm mục tiêu (A1, A5) không phản đối app; hướng web đặt qua QR là phương án dự phòng. Thêm pain point "không muốn đăng ký để xem menu". |
| **10** | (Phụ lục A #4) Tách Giỏ hàng và Thanh toán thành 2 màn. | **CHẤP NHẬN (Accept)** | Heuristic #8 + IA đã định nghĩa SCR-05 và SCR-06 riêng; Figma Page 03 đã có 2 frame riêng. Cần xuất lại ảnh `assets/figma/`. |
| **11** | (Phụ lục A #6) Ẩn mã lỗi kỹ thuật "#PAY_402". | **CHỈNH SỬA (Modify)** | Giữ mã trong dòng chữ nhỏ "Mã tham chiếu" để nhân viên quầy tra cứu khi cần, nhưng câu chính dùng ngôn ngữ thường (heuristic #9). |
| **12** | (Phụ lục A #9) Thêm đăng nhập bằng email sinh viên để tích điểm. | **TỪ CHỐI (Reject)** | Đi ngược insight từ phỏng vấn: A1, A3 nói sẽ bỏ app nếu bắt đăng ký trước. Mục tiêu dưới 35 giây không cho phép thêm bước đăng nhập. Ngoài phạm vi Lab 2. |
| **13** | (Phụ lục A #5) Vùng chạm 48 dp cho nút +/- và tách khỏi CTA. | **CHẤP NHẬN (Accept)** | WCAG 2.5.5 + persona thao tác một tay. |
| **14** | (Phụ lục A #1) Thay ô ảnh giữ chỗ ở Home bằng ảnh món thật. | **CHẤP NHẬN (Accept)** | Heuristic #2, #6: persona chọn món bằng mắt khi vội. |
| **15** | (Phụ lục A #3) Nâng chữ phụ lên tối thiểu 14 sp. | **CHẤP NHẬN (Accept)** | Chuẩn C4 của môn và rubric Lab 2 yêu cầu chữ nội dung ≥ 14 sp; persona P02 phải phóng to chữ nhỏ. Dòng nào không cần thì bỏ thay vì thu nhỏ. |
| **16** | (Phụ lục A #7) Thống nhất nhãn nút ở màn lỗi thanh toán. | **CHỈNH SỬA (Modify)** | Heuristic #4. Dùng một bộ nhãn cho Figma, flow và handoff: "Thử lại thanh toán" và "Trả tiền mặt tại quầy" (đúng hai lối thoát của Flow 3), bỏ nhãn "Thử lại bằng phương thức khác" vì mơ hồ. |
| **17** | (Phụ lục A #8) Thống nhất mã nhận đồ mẫu. | **CHẤP NHẬN (Accept)** | Heuristic #4. Dùng "#A-204" như trong màn hình Stitch/Figma và sửa tài liệu flow theo. |
| **18** | (Phản biện P0, C01) Problem statement đang chứa giải pháp "đặt trước và nhận tại quầy". | **CHỈNH SỬA (Modify)** | Câu cũ khoá luôn hướng giải pháp. Viết lại chỉ mô tả vấn đề, thêm câu "How might we". |
| **19** | (P0-C02) Thêm chỉ số đo kết quả, không chỉ tốc độ thao tác. | **CHẤP NHẬN (Accept)** | Chỉ số 35 giây không đo được vấn đề gốc (bỏ bữa). Ghi là giả thuyết, ngoài phạm vi Lab 2. |
| **20** | (P0-C03) Chuyển sang hướng web đặt qua QR. | **TỪ CHỐI (Reject)** | Ràng buộc thật: đề Lab 2 yêu cầu app mobile 360 × 800 dp + handoff Flutter. Giữ web làm phương án dự phòng cho rủi ro "ngại cài app". |
| **21** | (P0-C04) Thêm giả định về năng lực bếp. | **CHẤP NHẬN (Accept)** | Nếu bếp không kịp thì đặt trước vô nghĩa. Thêm H7, R3. |
| **22** | (P0-C05) "Căn tin đông giờ nghỉ" chưa có quan sát. | **CHẤP NHẬN (Accept)** | Xếp vào Unknown, gộp vào H2. |
| **23** | (Phản biện P1, C01) Chưa có dữ liệu người thật. | **CHẤP NHẬN (Accept)** | Đúng theo Chuẩn chung C3. Không bịa dữ liệu; ghi ngoại lệ Lab 2, kế hoạch và trạng thái "chưa thực hiện". |
| **24** | (P1-C02) Flow 3 dựa trên một nguồn giả lập. | **CHỈNH SỬA (Modify)** | Giữ Flow 3 vì đề bắt buộc ≥ 1 flow lỗi/phục hồi và thanh toán QR có giới hạn thời gian; hạ tin cậy INS-06, thêm RQ5. |
| **25** | (P1-C03) Bảng đối thủ gán nguồn giả lập như thử thật. | **CHẤP NHẬN (Accept)** | Ghi rõ nguồn là giả lập trong `ux/research.md` mục 1.2. |
| **26** | (P1-C04) Thiên lệch vòng tròn khi cùng AI vừa đóng vai người dùng vừa hỗ trợ thiết kế. | **CHẤP NHẬN (Accept)** | Ghi vào giới hạn; không dùng giả lập để xác nhận thiết kế. |
| **27** | (P1-C05) Câu hỏi dẫn dắt trong bộ phỏng vấn giả lập. | **CHẤP NHẬN (Accept)** | Câu hỏi giả định sẵn giải pháp; kịch bản cho người thật đã sửa. |
| **28** | (Phản biện P2, C01) Xác nhận hai lần ở bước thanh toán. | **CHỈNH SỬA (Modify)** | Giữ dialog vì đơn chỉ huỷ được trong 60 giây (Nielsen #5, ràng buộc P03); bù 1 chạm bằng giờ nhận mặc định "Lấy ngay". |
| **29** | (P2-C02) Hành vi sau "Thêm vào giỏ" chưa chốt. | **CHẤP NHẬN (Accept)** | Chuyển thẳng tới Giỏ hàng + snackbar "Thêm món khác"; ít chạm nhất cho P01. |
| **30** | (P2-C04) Thiếu trạng thái món hết hàng. | **CHẤP NHẬN (Accept)** | Gỡ pain point "còn món không" của P01; thêm US04, biến thể Card "Tạm hết". |
| **31** | (P2-C05) Đơn tiền mặt có thể bị bỏ. | **CHỈNH SỬA (Modify)** | Giữ lối thoát tiền mặt; S07 hiện badge "Trả tại quầy"; thêm giả định H8. |
| **32** | (P2-C03) Chỉ số thành công chưa rõ đối tượng. | **CHẤP NHẬN (Accept)** | Ghi rõ áp dụng cho người đã dùng app; S01 có Bỏ qua. |
| **33** | (P3) Chọn concept visual cho Trang chủ (A Stitch / B tối giản / C tối). | **CHỈNH SỬA (Modify)** | Chọn A (ảnh món, thương hiệu, light theme), mượn từ B khối trạng thái quán và banner nhỏ để thấy ≥ 3 món (P3-C03). |
| **34** | (P3) Concept C nền tối, banner lớn. | **TỪ CHỐI (Reject)** | Đọc kém ngoài nắng (P01), banner chiếm chỗ món, đề chỉ bắt buộc light theme. |
| **35** | (P3-C01) So sánh concept thiếu công bằng. | **CHẤP NHẬN (Accept)** | Ghi rõ nguồn từng concept; B và C cùng nội dung, cùng khung 360 × 800. |
| **36** | (P3-C02) Chữ 12 sp trong thang chữ. | **CHỈNH SỬA (Modify)** | Chỉ dùng cho nhãn tab có icon; cấm dùng cho nội dung. |
| **37** | (P3-C04) Chưa quy định ảnh món. | **CHẤP NHẬN (Accept)** | Ảnh 1:1, nền kem, fallback tên món khi lỗi (handoff mục 4). |
| **38** | (Phản biện P4, C02) Thông tin trang trí trên thẻ món. | **CHỈNH SỬA (Modify)** | Bỏ sao đánh giá; giữ giá gạch chỉ khi có khuyến mãi thật (P02 cần thấy giảm giá). |
| **39** | (P4-C03) Lời giải thích ở S06-ERR quá dài. | **CHẤP NHẬN (Accept)** | Rút còn 2 dòng: nguyên nhân + "Giỏ hàng của bạn vẫn được giữ". |
| **40** | (P4-C04) Figma thiếu biến thể trạng thái. | **CHẤP NHẬN (Accept)** | Critical của G4: thêm Loading (S02, S03, S07), Card Tạm hết, badge quán đóng, lỗi mã. |
| **41** | (P4-C05) Prototype dễ hỏng khi demo. | **CHẤP NHẬN (Accept)** | Màn loading không có hotspot; Back của S07 nối về S02. |
| **42** | (P4-C01) Điểm checklist chấm trên ảnh Stitch. | **CHẤP NHẬN (Accept)** | Giữ làm mức nền; chấm lại 4 màn chính trên Figma sau khi sửa. |

> Đề xuất "bản đồ 3D theo dõi đơn" trên slide cũ không có trong log, nên không đưa vào bảng.

---

## Phụ lục G: Phản biện P4 (UI chi tiết & prototype)

- **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 20/10/2026

**Prompt (nguyên văn):**
```text
Đây là ảnh các màn hiện có, ma trận trạng thái, đặc tả prototype và điểm UI checklist của tôi: [đính kèm mục 1–7].
Hãy: (1) chỉ ra tiêu chí checklist nào tôi chấm quá dễ hoặc quá khó; (2) trạng thái nào còn thiếu trong Figma;
(3) tương tác nào trong prototype dễ hỏng khi demo; (4) điều gì ngăn tôi qua Gate G4.
```

**Câu trả lời của AI (nguyên văn):**
1. **P4-C01 — Chấm trên ảnh Stitch, không phải Figma (vừa).** Điểm checklist hiện chỉ là mức nền. Gate G4 yêu cầu các màn chính đạt ≥ 80 trên bản cuối, nên phải chấm lại sau khi sửa Figma.
2. **P4-C02 — Home quá nhiều thông tin trang trí (vừa).** Sao đánh giá, giá gạch, banner flash không giúp tác vụ "đặt nhanh"; bài test Bớt cho thấy bỏ đi không mất thông tin.
3. **P4-C03 — S06-ERR lời giải thích dài (thấp).** Persona đang vội; câu quan trọng nhất ("giỏ hàng vẫn được giữ") bị chìm giữa các đoạn chữ.
4. **P4-C04 — Thiếu biến thể trạng thái trong Figma (cao).** Đặc tả có đủ, nhưng Figma chỉ có Empty, Error, Success. Thiếu Loading là trượt Critical "có empty/loading/error/success/disabled phù hợp" của G4.
5. **P4-C05 — Dễ hỏng khi demo (vừa).** Chuyển cảnh loading → kết quả dùng "After delay" dễ bị bấm nhầm khi đang chờ. Ngoài ra Back từ S07 phải nối về S02, nếu không sẽ quay lại màn thanh toán.
6. **Điều chặn G4:** QA01 (tương phản), QA04 (thiếu Loading), QA05 (chưa chạy thử prototype).

Quyết định: dòng 38–42 ở bảng mục 5.

---

## Phụ lục F: Concept & phản biện P3

Concept A là ảnh Stitch thật; concept B và C do Claude dựng bằng HTML ngày 20/10/2026 (`assets/concepts/`).

- **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 20/10/2026
- **Đầu vào:** 3 ảnh concept, bảng so sánh mục 1, style guide mục 3.

**Prompt (nguyên văn):**
```text
Đóng vai art director khó tính. Đây là 3 hướng visual cho màn Trang chủ của app đặt món cho sinh viên (persona: 15 phút nghỉ,
một tay, dùng ngoài nắng) và style guide tôi chọn: [đính kèm]. Hãy kiểm tra: (1) cách chấm điểm so sánh có công bằng không;
(2) style guide có đủ color roles, type scale, spacing, grid, density, component states chưa; (3) chỗ nào mâu thuẫn với chuẩn
14 sp / 48 dp / 4,5:1; (4) rủi ro khi dựng lên Figma.
```

**Câu trả lời của AI (nguyên văn):**
1. **P3-C01 — So sánh thiếu công bằng (vừa).** A là ảnh Stitch thật đã qua vòng chỉnh, còn B và C là mockup HTML dựng trong một lần. Ngoài ra A được cộng điểm "nhận diện thương hiệu", tiêu chí này tự nhiên có lợi cho phương án đang có. *Đề xuất:* ghi rõ chênh lệch này, và cho B, C cùng nội dung, cùng kích thước để so cho đúng.
2. **P3-C02 — Mâu thuẫn chữ 12 sp (vừa).** `type-label-small` 12 sp vẫn nằm trong thang chữ; nếu dùng cho nội dung sẽ trái chuẩn 14 sp. *Đề xuất:* chỉ cho dùng ở nhãn tab có icon, ghi rõ.
3. **P3-C03 — Banner ưu đãi của A đẩy món xuống (vừa).** Trên 360 × 800, A chỉ thấy khoảng 2,5 thẻ món trước khi phải cuộn, trong khi B thấy 4.
4. **P3-C04 — Ảnh món chưa có quy định (thấp).** Thẻ có ảnh nhưng chưa quy định tỉ lệ, nền ảnh, và ảnh thay thế khi tải lỗi. *Đề xuất:* ảnh 1:1, nền `#FFF5E5`, khi lỗi hiện tên món trên khối màu.
5. **P3-C05 — Thiếu kiểm nội dung dài (vừa).** Chưa có bằng chứng concept chịu được tên món dài và màn 412 dp — đây là một điều kiện của G3.

Quyết định: dòng 33–37 ở bảng mục 5.

---

## Phụ lục E: Phản biện P2 (flow & walkthrough)

- **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 20/10/2026

**Prompt (nguyên văn):**
```text
Đây là IA và 3 user flow (Mermaid) của tôi, kèm screen-spec và handoff: [dán]. Persona chính: SV ở KTX, 15 phút nghỉ, một tay, mạng chập chờn.
Hãy tìm: (1) ngõ cụt hoặc màn không ai tới được; (2) bước thừa so với chỉ số "≤ 8 chạm, < 35 giây";
(3) nhánh lỗi còn thiếu (mất mạng, nhập sai, hết hàng, huỷ); (4) Back dẫn về đâu ở từng màn; (5) hành vi nào dev sẽ phải hỏi lại.
```

**Câu trả lời của AI (nguyên văn):**
1. **Không có ngõ cụt; mọi màn đều thuộc ít nhất một flow** (mục 5). Back từ S07 về S02 là đúng, tránh trả tiền hai lần.
2. **P2-C01 — Bước thừa (vừa):** F1 có nút "Xác nhận" ở S06 rồi lại dialog "Đồng ý". Hai bước làm cùng một việc. *Đề xuất:* bỏ một trong hai, hoặc đặt "Lấy ngay" làm mặc định để bù 1 chạm.
3. **P2-C02 — Hành vi chưa chốt (vừa):** sau "Thêm vào giỏ" ở S04, handoff ghi hai khả năng. *Đề xuất:* chọn một và ghi rõ.
4. **P2-C04 — Thiếu nhánh "hết hàng" (cao):** chưa có trạng thái món hết ở S03/S04, và "Đặt lại" ở S08 có thể chứa món đã hết. Đây cũng là pain point "còn món không" của P01 chưa được gỡ.
5. **P2-C05 — Rủi ro tiền mặt (vừa):** lối thoát "Trả tiền mặt" ở F3 tạo đơn chưa thanh toán. Nếu khách không tới, bếp lỗ (liên quan H7).
6. **P2-C03 — Chỉ số chưa rõ đối tượng (thấp):** người mở app lần đầu phải qua S01, nên "≤ 8 chạm từ Trang chủ" chỉ đúng với người đã dùng.

Quyết định: dòng 28–32 ở bảng mục 5.

---

## Phụ lục D: Phản biện P1 (UX research)

- **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 19/10/2026
- **Đầu vào:** mục 1–7 ở trên, `ux/research.md`, `ai/ai-persona-interviews.md`.

**Prompt (nguyên văn):**
```text
Đây là research plan, evidence log, affinity map, insight và journey của tôi: [dán]. Hãy chỉ ra:
(1) thiên lệch trong cách chọn người và cách đặt câu hỏi; (2) insight nào chỉ có 1 người nói mà tôi đang coi là xu hướng;
(3) kết luận nào không truy về được ghi chép nguồn; (4) điều tôi cần hỏi thêm; (5) tôi có đạt điều kiện Critical của Gate G1 không.
```

**Câu trả lời của AI (nguyên văn):**

1. **P1-C01 — Không có dữ liệu người thật (cao).** Mọi insight về hành vi đều dựa trên SIM-A1…A5. Theo C3, đó không phải dữ liệu nghiên cứu. Điều kiện Critical đầu tiên của G1 chỉ đạt được theo nhánh "giải trình hợp lý". Phần giải trình phải nói rõ vì sao chưa làm và kế hoạch làm, không chỉ ghi "hạn chế".
2. **P1-C02 — Một nguồn mà dẫn tới cả một flow (cao).** INS-06 (mất giỏ hàng khi lỗi thanh toán) chỉ có SIM-A5, nhưng Flow 3 và màn SCR-06-ERR được xây dựa nhiều vào đó.
3. **P1-C03 — Gán nhầm nguồn trong bảng đối thủ (vừa).** Ô "không giao được vào tòa nhà/lab" của GrabFood/ShopeeFood trong `ux/research.md` mục 1.2 lấy từ nhân vật giả lập, nhưng đặt trong bảng đối thủ trông như kết quả thử app thật.
4. **P1-C04 — Thiên lệch vòng tròn (vừa).** Nhân vật giả lập được tạo sau khi sản phẩm đã có, bởi cùng hệ AI hỗ trợ thiết kế, nên chúng dễ "kể" đúng những vấn đề mà thiết kế đã giải quyết.
5. **P1-C05 — Câu hỏi dẫn dắt trong kit cũ (thấp).** Câu 8 của bộ phỏng vấn giả lập ("Nếu có app cho đặt trước…") giả định sẵn giải pháp. Kịch bản cho người thật ở mục 2.1 đã tránh được lỗi này.
6. **Cần hỏi thêm:** RQ1, RQ2 và RQ4 quan trọng nhất, vì nếu sai thì ý tưởng mất giá trị.

Quyết định: dòng 23–27 ở bảng mục 5.

---

## Phụ lục C: Phản biện P0 (problem framing)

- **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 19/10/2026
- **Đầu vào:** problem statement cũ (`ux/persona.md` mục 4), Idea Board, Assumption Log ở trên.

**Prompt (nguyên văn):**
```text
Đóng vai giảng viên UX khó tính. Đây là problem statement, các hướng ý tưởng và danh sách giả định của tôi: [dán mục 1, 4 và problem statement cũ].
Kiểm tra: (1) đủ ai – vấn đề – bối cảnh – hậu quả chưa; (2) chỗ nào tôi lẫn giả định với sự thật;
(3) chỗ nào là giải pháp trá hình; (4) cách chấm điểm ý tưởng có thiên vị không; (5) giả định lớn nào còn thiếu;
(6) 3 câu hỏi tôi cần đi hỏi người dùng thật.
```

**Câu trả lời của AI (nguyên văn):**

1. **P0-C01 — Giải pháp trá hình (cao).** Problem statement cũ ghi "cần đặt trước và nhận món ngay tại quầy". Đó là giải pháp, không phải vấn đề. Nếu giữ như vậy thì các hướng B, C, D bị loại ngay từ câu đầu, nên Idea Board chỉ còn là hình thức. *Đề xuất:* chỉ mô tả vấn đề, đưa giải pháp sang câu "How might we".
2. **P0-C02 — Hậu quả chưa đo được (vừa).** "Bỏ bữa hoặc vào lớp trễ" là hậu quả đúng, nhưng chỉ số thành công lại đo tốc độ thao tác app (35 giây), không đo việc giảm bỏ bữa. *Đề xuất:* thêm một chỉ số về kết quả, kể cả khi chưa đo được trong Lab 2.
3. **P0-C03 — Chấm điểm thiên về đề bài (vừa).** Feasibility của IDEA-A cao chủ yếu vì "khớp yêu cầu Lab 2", không phải vì phù hợp người dùng. Trong khi đó insight A3 (ngại cài app) lại nghiêng về IDEA-B. *Đề xuất:* nói rõ ràng buộc đề bài là một tiêu chí riêng, và cân nhắc chuyển sang IDEA-B.
4. **P0-C04 — Thiếu giả định về phía cung (cao).** Danh sách chỉ có giả định về sinh viên. Chưa có giả định nào về việc bếp có làm kịp nhiều đơn đặt trước dồn vào cùng giờ nghỉ hay không. Nếu bếp không kịp, đặt trước cũng không giúp được gì.
5. **P0-C05 — Lẫn dữ kiện và giả định (thấp).** "Căn tin đông vào giờ nghỉ" đang được nói như sự thật, nhưng chưa có quan sát nào. *Đề xuất:* xếp vào Unknown cho tới khi bấm giờ thực tế.
6. **3 câu hỏi cần hỏi người thật:** số phút nghỉ thật và việc làm trong lúc đó · số lần bỏ mua vì đông trong tuần qua · có chịu cài app riêng không, vì sao.

Quyết định: dòng 18–22 ở bảng mục 5.

---

## Phụ lục A: AI critique bổ sung (nguyên văn)

> Bản trả lời đầy đủ của lần critique đầu (Gemini, mục 4) **không được lưu lại**, chỉ còn bản tóm tắt 5 phát hiện. Để có bản nguyên văn theo yêu cầu đề, nhóm chạy thêm một vòng critique.
> **Công cụ:** Claude Opus 5.5 (Anthropic), trong Claude Code · **Ngày:** 17/10/2026 · **Đầu vào:** các ảnh trong `assets/stitch/` (độ phân giải thấp, ≤ 512 px) và các file `ux/persona.md`, `design/DESIGN.md`.

**Prompt:**
```text
Đóng vai chuyên gia UX khó tính. Đánh giá các màn hình BreakBite trong assets/stitch/ theo 10 heuristic của Nielsen,
WCAG 2.1 và persona trong ux/persona.md (sinh viên ở KTX, giờ nghỉ 15 phút, thao tác một tay, mạng chập chờn).
Mỗi phát hiện phải gắn với một màn hình cụ thể, nêu heuristic hoặc tiêu chí, mức độ nghiêm trọng (cao/vừa/thấp) và đề xuất sửa.
Nêu cả điểm làm tốt. Không khen chung chung.
```

**Câu trả lời của AI:**

*Lưu ý trước: ảnh ở độ phân giải thấp nên kích thước chữ và vùng chạm chỉ ước lượng bằng mắt; cần đo lại trong Figma.*

1. **SCR-02 Home — ảnh món là ô giữ chỗ màu tím (cao).** Heuristic #2 (khớp với thế giới thật), #6 (nhận diện). Persona chọn món nhanh bằng mắt; ô trống buộc phải đọc tên. *Đề xuất:* dùng ảnh món thật của quán.
2. **Mọi màn — chữ trắng trên nút cam (cao).** WCAG 1.4.3: tỷ lệ 2,14:1, không đạt 4,5:1. Persona hay dùng ngoài nắng. *Đề xuất:* chữ nút màu nâu đậm, hoặc nền nút đậm hơn.
3. **SCR-02, SCR-05 — chữ phụ rất nhỏ (vừa).** Các dòng như "Chuẩn bị theo giờ nghỉ", nhãn phí, nhãn tab nhìn dưới 14 sp. Đề yêu cầu chữ nội dung ≥ 14 sp. *Đề xuất:* nâng lên 14 sp hoặc bỏ bớt chữ không cần.
4. **SCR-05 — Giỏ hàng gộp luôn phương thức thanh toán (vừa).** Heuristic #8 (tối giản): màn quá dài, phải cuộn mới thấy tổng tiền và nút. Ảnh "giỏ hàng" và "checkout" trong repo đang là cùng một file. *Đề xuất:* tách Giỏ hàng (SCR-05) và Thanh toán (SCR-06) đúng như IA.
5. **SCR-04 — nút tăng giảm số lượng nhỏ (vừa).** WCAG 2.5.5 / Material: nút +/- nhìn khoảng 24–28 dp, đặt sát nút CTA, dễ bấm nhầm khi cầm một tay. *Đề xuất:* vùng chạm 48 dp, tách stepper khỏi CTA.
6. **SCR-06-ERR — lộ mã lỗi kỹ thuật "#PAY_402" (thấp).** Heuristic #9: thông báo lỗi nên dùng ngôn ngữ thường. Điểm tốt: màn này giữ giỏ hàng và đưa ra lối thoát rõ ràng. *Đề xuất:* ẩn mã lỗi vào mục "chi tiết", giữ câu giải thích.
7. **SCR-06-ERR — nhãn nút không khớp tài liệu (thấp).** Heuristic #4 (nhất quán): ảnh ghi "Thử lại bằng phương thức khác / Quay lại giỏ hàng", còn flow ghi "Thử lại online / Chuyển tiền mặt". *Đề xuất:* thống nhất một bộ nhãn trong Figma, flow và handoff.
8. **SCR-07 Theo dõi đơn — mã nhận đồ không khớp (thấp).** Heuristic #4: ảnh ghi "#A-204", flow ghi "#A-204". *Đề xuất:* dùng một mã mẫu thống nhất.
9. **SCR-02 — đề xuất thêm đăng nhập bằng email sinh viên để tích điểm thưởng (gợi ý mở rộng).** Heuristic #7 (linh hoạt, hiệu quả): giữ chân người dùng quay lại.
10. **Điểm làm tốt:** badge "Sẵn sàng (5–7 phút)" trên Home đáp ứng heuristic #1; giá động trên nút CTA ở SCR-04 (#6); empty state có thông điệp và một hành động (#9); tiến trình 4 bước có cả icon và chữ (WCAG 1.4.1).

---

## Phụ lục B: Phỏng vấn AI để xây persona

Toàn văn (prompt, 5 hồ sơ, 5 buổi phỏng vấn, tổng hợp, phản biện persona) nằm ở [`ai/ai-persona-interviews.md`](./ai-persona-interviews.md). Công cụ: Claude Opus 5.5 · Ngày: 17/10/2026. Quyết định rút ra: dòng 07–09 ở bảng mục 5.
