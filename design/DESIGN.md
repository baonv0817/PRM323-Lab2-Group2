# Design Brief & Token System

> **Tài liệu:** `design/DESIGN.md`  
> **Dự án:** BreakBite App — Campus Quick Food Ordering  
> **Môn học:** PRM323 — Lab 2  
> **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) *(Bao gồm đầy đủ 6 Trang & 3 Flow Prototype tương tác)*  
> **Mục đích:** Bản mô tả thiết kế quy chuẩn định nghĩa toàn bộ Tokens (Màu sắc, Typography, Spacing, Bo góc, Elevation) và quy tắc Component làm tài liệu cơ sở gửi cho Google Stitch và thiết lập Figma Variables.

---

## 1. Phong cách thiết kế & Giọng điệu thương hiệu (Design Tone & Aesthetics)

* **Tên ứng dụng:** BreakBite (Trực thuộc hệ sinh thái ẩm thực nhanh BreakBite).
* **Định vị & Cảm xúc:** Trẻ trung, tràn đầy năng lượng, ấm áp và thân thiện với đời sống sinh viên năng động.
* **Nguyên tắc thẩm mỹ (Visual Principles):**
  1. **Ấm cúng & Kích thích vị giác:** Sử dụng tông màu cam ấm `#F69D39` kết hợp màu nâu cacao trầm `#622B14` và nền kem sữa `#FFF5E5`.
  2. **Rõ ràng & Tối giản (Clutter-free):** Bố cục thẻ (Card-based layout) với khoảng trắng thoáng đãng, phân cấp thị giác mạch lạc giúp sinh viên quét nhanh món ăn trong 3 giây.
  3. **Công thái học di động (Mobile Ergonomics):** Mọi nút bấm tương tác chính đều tập trung ở nửa dưới màn hình (Thumb zone), kích thước chạm tối thiểu đạt chuẩn $48 \times 48\text{ dp}$.

---

> Concept đã chọn, color roles, grid, density, component states và naming: xem `design/p3-ui-concept-style-guide.md`.

## 1A. Nguyên tắc thiết kế gắn với persona

Mỗi nguyên tắc xuất phát từ nhu cầu của một persona (`ux/persona.md`) và dựa trên một chuẩn thiết kế có tên. Ánh xạ đầy đủ persona → nhu cầu → nguyên tắc → quyết định UI → màn hình → cách kiểm chứng nằm trong `ux/persona-mapping.xlsx` (sheet *Mapping*).

| ID | Nguyên tắc | Nội dung | Phục vụ nhu cầu | Persona | Căn cứ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DP1** | Nhanh trước tiên | Mỗi bước phải rút ngắn đường tới đơn đã đặt; một hành động chính mỗi màn, ghim ở đáy. | N1 | P01 | Nielsen #7 Flexibility & efficiency; Fitts's law |
| **DP2** | Thấy trước khi quyết định | Trạng thái quán, thời gian chờ và tiến trình đơn luôn hiển thị trước khi người dùng phải chọn. | N2 | P01 | Nielsen #1 Visibility of system status |
| **DP3** | Một tay, vùng ngón cái | Điều hướng và nút chính nằm ở nửa dưới; mọi vùng chạm ≥ 48 × 48 dp. | N3 | P01 | Material 3 accessibility; WCAG 2.5.5 Target size |
| **DP4** | Giá minh bạch | Giá cộng dồn hiển thị ngay khi chọn; tổng tiền thật xuất hiện trước bước thanh toán; lỗi giá/mã có lý do. | N7, N8 | P02 | Nielsen #6 Recognition; #9 Error recovery |
| **DP5** | Không mất công sức khi lỗi | Lỗi không bao giờ xoá giỏ hàng; luôn có ít nhất hai lối thoát (thử lại / cách khác). | N4 | P01 | Nielsen #5 Error prevention; #9; #3 User control |
| **DP6** | Đọc được mọi lúc | Chữ thường ≥ 4,5:1, thành phần điều khiển ≥ 3:1, chữ nội dung ≥ 14 sp; trạng thái có icon + chữ. | N5 | P01 | WCAG 1.4.3, 1.4.11, 1.4.1 |
| **DP7** | Không bắt đăng ký trước | Xem menu và đặt món không cần tạo tài khoản; không thêm bước không phục vụ việc đặt. | N6 | P01 | Nielsen #8 Minimalist design; insight A1, A3 |
| **DP8** | Dễ cho quầy | Thông tin nhận đồ phải đối chiếu được trong vài giây; thao tác của khách không làm hỏng việc của bếp. | N9, N10 | P03 | Supporting persona P03; ràng buộc nghiệp vụ |

Khi hai nguyên tắc xung đột, ưu tiên theo thứ tự persona: **P01 (Primary) → P02 → P03**. Ví dụ: DP7 (không bắt đăng ký) thắng đề xuất tích điểm vì P01 cần tốc độ.

---

## 2. Hệ thống Design Tokens (Token-based Design System)

Toàn bộ các giá trị bên dưới được thiết lập làm **Figma Variables** và là căn cứ để ánh xạ sang Flutter `ThemeData`. Cấm gán cứng giá trị tùy ý trong các component.

### 2.1 Bảng màu quy chuẩn (Color Tokens)

| Token Name | Hex Code | Giá trị RGB | Vai trò & Cách áp dụng |
| :--- | :---: | :---: | :--- |
| `color-primary` | `#F69D39` | `246, 157, 57` | Màu chủ đạo thương hiệu: **nền** nút CTA chính, badge nổi bật, tab đang chọn. Không dùng làm màu chữ trên nền sáng (chỉ 1,98:1 trên `#FFF5E5`). |
| `color-on-primary` | `#622B14` | `98, 43, 20` | Chữ và icon đặt trên nền `color-primary` (5,23:1 — đạt AA cho chữ thường). Thay cho chữ trắng (chỉ 2,14:1). |
| `color-primary-text` | `#B45309` | `180, 83, 9` | Chữ/viền màu cam trên nền sáng: nút Outline, link, giá tiền (4,65:1 trên `#FFF5E5`, 5,02:1 trên trắng). |
| `color-primary-pressed` | `#F8A94F` | `248, 169, 79` | Trạng thái Pressed của nút chính (chữ `#622B14` trên nền này đạt 5,75:1). Thay cho `#E0851F` cũ (chỉ 4,02:1 với chữ nâu). |
| `color-primary-container`| `#FFE8CC` | `255, 232, 204` | Màu nền phụ cho chip danh mục đang chọn, container nổi bật. |
| `color-secondary` | `#E0C375` | `224, 195, 117` | Màu vàng cát ấm: Dùng cho icon ngôi sao đánh giá, tag khuyến mãi. |
| `color-background` | `#FFF5E5` | `255, 245, 229` | Màu nền chung toàn bộ màn hình (Warm Creamy Ivory) giảm chói mắt. |
| `color-surface` | `#FFFFFF` | `255, 255, 255` | Nền các thẻ sản phẩm (Food Cards), Bottom Sheet, Modal Dialog. |
| `color-surface-subtle` | `#FFF9F0` | `255, 249, 240` | Nền ô nhập liệu TextField, nền thẻ tóm tắt thanh toán. |
| `color-text-primary` | `#622B14` | `98, 43, 20` | Màu chữ chính: Nâu đậm espresso, tương phản 10,37:1 trên nền kem, 11,2:1 trên trắng (Đạt WCAG AAA). |
| `color-text-secondary` | `#8A5D48` | `138, 93, 72` | Màu chữ phụ: Mô tả món ăn, giá phụ, nhãn phụ (5,2:1 trên nền kem — đạt AA). Thay cho `#966A55` cũ (chỉ 4,33:1). |
| `color-text-disabled` | `#C8B3A6` | `200, 179, 166` | Chỉ dùng cho chữ của thành phần bị vô hiệu hoá (WCAG 1.4.3 miễn trừ). Placeholder dùng `color-text-secondary`. |
| `color-border` | `#EEDBCA` | `238, 219, 202` | Viền thẻ và đường kẻ phân cách (Divider) — chỉ mang tính trang trí. |
| `color-border-input` | `#8A7A70` | `138, 122, 112` | Viền ô nhập Text field và checkbox chưa chọn (4,12:1 trên trắng, 3,93:1 trên `#FFF9F0` — đạt 3:1 cho thành phần điều khiển, WCAG 1.4.11). |
| `color-success` | `#15803D` | `21, 128, 61` | Trạng thái đơn hoàn tất, áp dụng voucher thành công, thanh toán thành công (5,02:1 trên trắng; `#16A34A` cũ chỉ 3,3:1). |
| `color-error` | `#B91C1C` | `185, 28, 28` | Báo lỗi nhập sai, hết món, cảnh báo lỗi thanh toán (5,99:1 trên nền kem; `#DC2626` cũ chỉ 4,47:1). |
| `color-white` | `#FFFFFF` | `255, 255, 255` | Chữ trên nền `color-error` (nút huỷ/destructive, 6,47:1). Không dùng trên nền cam. |

---

### 2.2 Thang kiểu chữ (Typography Tokens)

* **Font gia đình:** `Nunito` (Google Fonts: tròn trịa, hiện đại, dễ đọc trên màn hình điện thoại).

| Token Name | Cỡ chữ (Size) | Độ đậm (Weight) | Chiều cao dòng (Line-height) | Ứng dụng |
| :--- | :---: | :---: | :---: | :--- |
| `type-display-large` | 24 sp | Bold (700) | 32 dp | Tiêu đề màn hình chính Onboarding, Mã số nhận đơn #A-204 |
| `type-headline` | 20 sp | Bold (700) | 28 dp | Tiêu đề App bar, Tiêu đề mục "Món ngon hôm nay" |
| `type-title-medium` | 16 sp | SemiBold (600) | 24 dp | Tên món ăn trong Card, Tiêu đề Dialog |
| `type-title-small` | 14 sp | SemiBold (600) | 20 dp | Tiêu đề nhóm Topping, Nhãn phương thức thanh toán |
| `type-body-large` | 15 sp | Regular (400) | 22 dp | Mô tả nguyên liệu món ăn, hướng dẫn lấy đồ |
| `type-body-medium` | 14 sp | Regular (400) | 20 dp | Văn bản nội dung cơ bản toàn app (Tối thiểu 14sp theo rubric) |
| `type-label-large` | 14 sp | Bold (700) | 20 dp | Chữ trên nút bấm CTA (Button text) |
| `type-label-small` | 12 sp | Medium (500) | 16 dp | **Chỉ** nhãn tab Bottom Navigation (luôn có icon). Không dùng cho nội dung (D36) |

---

### 2.3 Thang khoảng cách (Spacing & Layout Grid Tokens)

Dựa trên hệ thống lưới cơ sở $4\text{ dp}$ (4-point base grid):

| Token Name | Giá trị (dp) | Ứng dụng |
| :--- | :---: | :--- |
| `spacing-xxs` | 4 dp | Khoảng cách giữa icon và chữ trong badge, khoảng cách nhỏ |
| `spacing-xs` | 8 dp | Khoảng cách giữa các chip danh mục, padding trong input |
| `spacing-sm` | 12 dp | Khoảng cách giữa các dòng thông tin trong Card |
| `spacing-md` | 16 dp | Padding lề chuẩn màn hình mobile (Screen horizontal padding), khoảng cách giữa các Card |
| `spacing-lg` | 24 dp | Khoảng cách giữa các khối nội dung lớn (Sections) |
| `spacing-xl` | 32 dp | Khoảng cách trước nút CTA ghim đáy, margin tiêu đề trang |
| `spacing-xxl` | 48 dp | Vùng chạm tối thiểu (Minimum touch target) cho nút bấm icon và button |

---

### 2.4 Bo góc & Đổ bóng (Border Radius & Elevation Tokens)

* **Corner Radius Tokens:**
  * `radius-sm` (8 dp): Bo góc ô nhập Text field, chip lọc danh mục.
  * `radius-md` (12 dp): Bo góc nút bấm chính (Button), thẻ thông tin nhỏ.
  * `radius-lg` (16 dp): Bo góc thẻ món ăn (Food Item Card), Popup Dialog.
  * `radius-xl` (24 dp): Bo góc Bottom Sheet giỏ hàng, thẻ tóm tắt thanh toán.
  * `radius-full` (999 dp): Nút tròn tăng giảm số lượng (+/-), badge thông báo.
* **Elevation / Shadow Tokens:**
  * `elevation-none`: `0px 0px 0px rgba(0,0,0,0)` (Flat style cho ô nhập liệu).
  * `elevation-1`: `0px 2px 8px rgba(98, 43, 20, 0.08)` (Card món ăn, App bar nổi nhẹ).
  * `elevation-2`: `0px 4px 16px rgba(98, 43, 20, 0.12)` (Nút CTA ghim đáy, Bottom Navigation Bar).
  * `elevation-3`: `0px 8px 24px rgba(98, 43, 20, 0.18)` (Modal Dialog, Thông báo Toast).

### 2.5 Lịch sử thay đổi token màu

Bảng màu ở mục 2.1 là phiên bản đã sửa sau khi đo lại độ tương phản (công thức WCAG 2.x). Bản gửi cho Stitch ở `ai/ai-design-log.md` dùng giá trị cũ; prompt được giữ nguyên văn.

| Token | Giá trị cũ | Giá trị mới | Lý do |
| :--- | :---: | :---: | :--- |
| Chữ trên nút primary | `#FFFFFF` (2,14:1) | `#622B14` (5,23:1) | Chữ 14–15sp đậm không được tính là "chữ lớn" (cần ≥ 14pt ≈ 18,7px đậm) nên phải đạt 4,5:1 |
| `color-primary-pressed` | `#E0851F` | `#F8A94F` | Giữ chữ nâu đạt 4,5:1 khi bấm |
| `color-text-secondary` | `#966A55` (4,33:1) | `#8A5D48` (5,2:1) | Không đạt 4,5:1 |
| `color-success` | `#16A34A` (3,3:1) | `#15803D` (5,02:1) | Dùng cho chữ trạng thái |
| `color-error` | `#DC2626` (4,47:1 trên nền kem) | `#B91C1C` (5,99:1) | Dùng cho chữ lỗi |
| Viền ô nhập | `#EEDBCA` (1,34:1) | `#8A7A70` (4,12:1) | Viền thành phần điều khiển cần ≥ 3:1 |

---

## 3. Quy tắc cấu thành Component (Component Construction Rules)

1. **Quy tắc Auto Layout 100%:** Mọi component và màn hình bắt buộc sử dụng Figma Auto Layout (Direction, Spacing, Padding, Fill container / Hug contents). Nghiêm cấm đặt vị trí tọa độ tuyệt đối tự do.
2. **Quy tắc Vùng chạm cảm ứng (Touch Target Rule):** Mọi nút bấm, icon bấm được đều phải bọc trong khung tối thiểu $48 \times 48\text{ dp}$.
3. **Quy tắc Biến thể trạng thái (Variants & States):** Mỗi component phải có đầy đủ các variant bắt buộc trong Section 7 của đề bài (Default, Pressed, Disabled, Loading, Error...).
4. **Quy tắc Không dựa vào màu sắc đơn thuần (Accessibility Non-color Rule):**
   * Trạng thái thành công/thất bại luôn phải đi kèm biểu tượng (Checkmark hoặc Cảnh báo X) bên cạnh màu xanh/đỏ.
   * Text field báo lỗi luôn có đường viền đỏ kèm dòng chữ mô tả lỗi cụ thể bên dưới.
