# Flutter Handoff Specification

> **Tài liệu:** `06-P5-kiem-thu-ban-giao/03-flutter-handoff.md`  
> **Dự án:** BreakBite App — Campus Quick Food Ordering  
> **Môn học:** PRM323 — Lab 2  
> **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) *(Bao gồm đầy đủ 6 Trang & 3 Flow Prototype tương tác)*  
> **Mục tiêu:** Cung cấp đặc tả kỹ thuật chi tiết để lập trình viên Flutter có thể lập trình hoàn chỉnh toàn bộ giao diện và các trạng thái mà không cần phải hỏi lại Designer bất kỳ câu hỏi nào.

---

## 1. Hai bảng ánh xạ chung (Global Mapping Tables)

### 1.1 Bảng 1: Ánh xạ Design Tokens sang Flutter ThemeData / Constants

| Loại Token | Tên Token trong Figma | Giá trị thiết kế | Thuộc tính tương ứng trong Flutter (`ThemeData`) |
| :--- | :--- | :---: | :--- |
| **Color** | `color-primary` | `#F69D39` | `Theme.of(context).colorScheme.primary` |
| **Color** | `color-on-primary` | `#622B14` | `Theme.of(context).colorScheme.onPrimary` (chữ/icon trên nút primary) |
| **Color** | `color-primary-text` | `#B45309` | `AppColors.primaryText` (`ThemeExtension`) — giá tiền, link, nút Outline |
| **Color** | `color-primary-pressed` | `#F8A94F` | `WidgetStateProperty` cho `backgroundColor` khi `WidgetState.pressed` |
| **Color** | `color-primary-container` | `#FFE8CC` | `Theme.of(context).colorScheme.primaryContainer` |
| **Color** | `color-secondary` | `#E0C375` | `Theme.of(context).colorScheme.secondary` |
| **Color** | `color-background` | `#FFF5E5` | `Theme.of(context).colorScheme.background` (`scaffoldBackgroundColor`) |
| **Color** | `color-surface` | `#FFFFFF` | `Theme.of(context).colorScheme.surface` (Card & Dialog color) |
| **Color** | `color-surface-subtle` | `#FFF9F0` | `Theme.of(context).colorScheme.surfaceVariant` |
| **Color** | `color-text-primary` | `#622B14` | `Theme.of(context).colorScheme.onBackground` / `onSurface` |
| **Color** | `color-text-secondary` | `#8A5D48` | `Theme.of(context).textTheme.bodyMedium?.color` |
| **Color** | `color-border` | `#EEDBCA` | `Theme.of(context).colorScheme.outlineVariant` (divider, viền thẻ) |
| **Color** | `color-border-input` | `#8A7A70` | `Theme.of(context).colorScheme.outline` (viền TextField, checkbox) |
| **Color** | `color-success` | `#15803D` | `const Color(0xFF15803D)` (`AppColors.success`) |
| **Color** | `color-error` | `#B91C1C` | `Theme.of(context).colorScheme.error` |
| **Typography** | `type-display-large` | 24sp, Bold 700 | `Theme.of(context).textTheme.headlineMedium?.copyWith(fontFamily: 'Nunito', fontWeight: FontWeight.w700, fontSize: 24)` |
| **Typography** | `type-headline` | 20sp, Bold 700 | `Theme.of(context).textTheme.titleLarge?.copyWith(fontFamily: 'Nunito', fontWeight: FontWeight.w700, fontSize: 20)` |
| **Typography** | `type-title-medium` | 16sp, SemiBold 600| `Theme.of(context).textTheme.titleMedium?.copyWith(fontFamily: 'Nunito', fontWeight: FontWeight.w600, fontSize: 16)` |
| **Typography** | `type-title-small` | 14sp, SemiBold 600| `Theme.of(context).textTheme.titleSmall?.copyWith(fontFamily: 'Nunito', fontWeight: FontWeight.w600, fontSize: 14)` |
| **Typography** | `type-body-large` | 15sp, Regular 400 | `Theme.of(context).textTheme.bodyLarge?.copyWith(fontFamily: 'Nunito', fontSize: 15)` |
| **Typography** | `type-body-medium` | 14sp, Regular 400 | `Theme.of(context).textTheme.bodyMedium?.copyWith(fontFamily: 'Nunito', fontSize: 14)` |
| **Typography** | `type-label-large` | 14sp, Bold 700 | `Theme.of(context).textTheme.labelLarge?.copyWith(fontFamily: 'Nunito', fontWeight: FontWeight.w700, fontSize: 14)` |
| **Spacing** | `spacing-xxs` | 4 dp | `const EdgeInsets.all(4.0)` / `const SizedBox(width: 4, height: 4)` |
| **Spacing** | `spacing-xs` | 8 dp | `const EdgeInsets.all(8.0)` / `const SizedBox(width: 8, height: 8)` |
| **Spacing** | `spacing-sm` | 12 dp | `const EdgeInsets.all(12.0)` / `const SizedBox(width: 12, height: 12)` |
| **Spacing** | `spacing-md` | 16 dp | `const EdgeInsets.all(16.0)` (Standard Screen Margin) |
| **Spacing** | `spacing-lg` | 24 dp | `const EdgeInsets.all(24.0)` / `const SizedBox(height: 24)` |
| **Spacing** | `spacing-xl` | 32 dp | `const EdgeInsets.all(32.0)` / `const SizedBox(height: 32)` |
| **Radius** | `radius-sm` | 8 dp | `BorderRadius.circular(8.0)` |
| **Radius** | `radius-md` | 12 dp | `BorderRadius.circular(12.0)` |
| **Radius** | `radius-lg` | 16 dp | `BorderRadius.circular(16.0)` |
| **Radius** | `radius-xl` | 24 dp | `BorderRadius.circular(24.0)` |

---

### 1.2 Bảng 2: Ánh xạ Component thư viện sang Flutter Material 3 Widgets

| Nhóm Component Figma | Variant trong Figma | Flutter Widget tương ứng & Cấu hình |
| :--- | :--- | :--- |
| **1. Button** | `Variant=Primary`, `State=Default/Pressed/Disabled/Loading` | `FilledButton` / `ElevatedButton` với `ButtonStyle` (BackgroundColor: `#F69D39`, ForegroundColor: `#622B14`, Pressed: `#F8A94F`, Shape: `RoundedRectangleBorder(borderRadius: BorderRadius.circular(12))`). Khi `Loading` hiển thị `SizedBox(width: 20, height: 20, child: CircularProgressIndicator(color: Color(0xFF622B14), strokeWidth: 2))`. |
| **1. Button** | `Variant=Secondary / Outline` | `OutlinedButton` (BorderSide: `#B45309`, ForegroundColor: `#B45309`). |
| **2. Text Field** | `State=Default/Focused/Filled/Error/Disabled` | `TextFormField` với `InputDecoration` (`filled: true`, `fillColor: Color(0xFFFFF9F0)`, `border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: BorderSide(color: Color(0xFF8A7A70)))`, `errorBorder: OutlineInputBorder(borderSide: BorderSide(color: Color(0xFFB91C1C), width: 2))`). |
| **3. Card** | `Variant=FoodItemCard`, `State=Default/Pressed` | `Card` hoặc `InkWell` bọc trong `Container` (`color: Colors.white`, `elevation: 1`, `borderRadius: BorderRadius.circular(16)`). |
| **4. Navigation** | `Type=BottomNavigationBar`, `Tab=Home/Menu/Orders/Profile` | `NavigationBar` (Material 3) với 4 `NavigationDestination`, `indicatorColor: Color(0xFFFFE8CC)`. |
| **5. App Bar** | `Type=DefaultAppBar`, `HasBack=true/false` | `AppBar` (`backgroundColor: Color(0xFFFFF5E5)`, `elevation: 0`, `leading: BackButton(color: Color(0xFF622B14))`, `actions: [IconButton(icon: Badge(...))]`). |
| **6. Dialog** | `Type=ConfirmationDialog / DestructiveDialog` | `AlertDialog` (`shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16))`, `actions: [TextButton(Cancel), FilledButton(Confirm)]`). |
| **7. Loading State** | `Type=ScreenSkeleton / InlineSpinner` | Thư viện `shimmer` package (`Shimmer.fromColors(baseColor: Color(0xFFEEDBCA), highlightColor: Color(0xFFFFF9F0))`) hoặc `CircularProgressIndicator(color: Color(0xFFF69D39))`. |
| **8. Empty State** | `Type=EmptyCart / EmptyOrders` | `Column` (`mainAxisAlignment: MainAxisAlignment.center`, `children: [SvgPicture.asset(...), Text(...), FilledButton(...)]`). |
| **9. Error State** | `Type=ErrorBanner / ErrorScreen` | `Container` hoặc `Scaffold` hiển thị icon cảnh báo `Icon(Icons.error_outline, color: Color(0xFFB91C1C), size: 48)`, nhãn giải thích và nút thử lại `OutlinedButton`. |

---

## 2. Đặc tả chi tiết S01–S08 (Per-Screen Specification - Đủ 6 mục bắt buộc)

> Bản cũ của S01–S08. Giao diện hiện hành xem mục 5.

---

### Màn hình 1: SCR-01 — Splash & Onboarding
1. **Layout Hierarchy:**
   * `Scaffold` (Background: `#FFF5E5`) $\to$ `SafeArea` $\to$ `Padding(spacing-md)` $\to$ `Column`:
     * Phần trên (Flex 6): Hình minh họa món ăn Kiosk BreakBite (`Image.asset` hoặc SVG).
     * Phần giữa (Flex 3): Tiêu đề `type-display-large` ("BreakBite - Ăn nhanh giải lao"), nội dung mô tả `type-body-large`.
     * Phần dưới (Ghim đáy): Nút Button Primary `Bắt đầu ngay` và dòng liên kết Đăng nhập email sinh viên.
   * *Phần cuộn:* Không cuộn (Màn hình cố định 800dp).
2. **Components & Variants:**
   * `Button` (`Variant=Primary`, `State=Default`, `Width=double.infinity`, `Height=52`).
3. **States:** Default.
4. **User Interactions:**
   * Bấm nút "Bắt đầu ngay" $\to$ Lưu `hasSeenOnboarding = true` vào SharedPreferences $\to$ Chuyển sang `SCR-02`.
   * Bấm "Đăng nhập email trường" $\to$ Mở màn hình/web SSO FPT University.
5. **Navigation:**
   * Người dùng đến từ: Khởi chạy app lần đầu.
   * Hành động dẫn tới: `SCR-02` (Home Screen).
   * Nút Back: Thoát app (`SystemNavigator.pop()`).
6. **Important UI Constraints:**
   * Nút bấm cao 52dp (vượt chuẩn 48dp). Chữ tiêu đề tối đa 2 dòng, tự động co dãn chữ nếu màn hình hẹp.

---

### Màn hình 2: SCR-02 — Home & Quick Discovery
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Tùy biến với location dropdown và Cart Badge) $\to$ `SingleChildScrollView` $\to$ `Column`:
     * Section 1: Banner sự kiện (`SizedBox(height: 140)` với `PageView` auto-scroll).
     * Section 2: Ô tìm kiếm (`TextFormField` dạng search bar readonly, bấm vào mở search).
     * Section 3: Thanh chip danh mục cuộn ngang (`SingleChildScrollView(scrollDirection: Axis.horizontal)`).
     * Section 4: Tiêu đề danh mục "Món lấy nhanh dưới 5p" (`type-headline`).
     * Section 5: Danh sách sản phẩm 2 cột (`GridView.builder(physics: NeverScrollableScrollPhysics(), shrinkWrap: true)`).
   * `bottomNavigationBar`: `NavigationBar` 4 destinations cố định.
   * *Phần cuộn:* Toàn bộ `Column` bên trong cuộn dọc, App bar và Bottom bar cố định.
2. **Components & Variants:**
   * `App bar` (`Type=HomeAppBar`, có icon giỏ hàng kèm badge số lượng).
   * `Card` (`Variant=FoodItemCard`, hiển thị ảnh, tên, badge "⚡ 3-5m", giá tiền, nút tròn "+" thêm nhanh).
   * `Navigation` (`Type=BottomNavigationBar`, selected index = 0).
3. **States:**
   * `Default`: Hiển thị danh sách món.
   * `Loading`: Hiển thị Skeleton Shimmer cho các Card món ăn.
   * `Error`: Banner hiển thị "Không thể cập nhật thực đơn lúc này" kèm nút Refresh.
4. **User Interactions:**
   * Chạm vào Food Card $\to$ Mở `SCR-04` (Chi tiết món).
   * Chạm vào nút "+" trên card $\to$ Thêm 1 sản phẩm vào giỏ, icon giỏ hàng trên App bar rung nhẹ (Haptic feedback) và tăng badge counter.
   * Chạm vào icon Giỏ hàng $\to$ Mở `SCR-05`.
   * Chạm vào các tab Bottom bar $\to$ Chuyển đổi tab tương ứng (`SCR-03`, `SCR-07`, `SCR-08`).
5. **Navigation:**
   * Đến từ: `SCR-01` hoặc chọn Tab 1 từ bất kỳ đâu.
   * Nút Back: Bấm 2 lần trong 2 giây để thoát app (Double tap to exit).
6. **Important UI Constraints:**
   * Touch target nút "+" tối thiểu $48 \times 48\text{ dp}$. Tên món giới hạn tối đa 2 dòng (TextOverflow.ellipsis).

---

### Màn hình 3: SCR-03 — Menu & Category Search
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Search TextField tích hợp + Nút Filter) $\to$ `Column`:
     * Thanh Tab lọc danh mục cố định (`TabBar`: Tất cả / Tacos / Mì trộn / Nước).
     * `Expanded` $\to$ `ListView.builder` cuộn dọc chứa các thẻ món ăn dạng nằm ngang (Horizontal food card).
   * `bottomNavigationBar`: `NavigationBar` (selected index = 1).
   * *Phần cuộn:* Danh sách món ăn cuộn dọc độc lập bên dưới TabBar.
2. **Components & Variants:**
   * `Text field` (`Type=SearchField`, có nút clear "x").
   * `Card` (`Variant=HorizontalFoodCard`, ảnh bên trái, thông tin bên phải).
   * `Navigation` (`Type=BottomNavigationBar`, selected index = 1).
3. **States:**
   * `Populated`: Danh sách kết quả tìm kiếm.
   * `Empty`: Khi tìm từ khóa không có món $\to$ Hiển thị `Empty state` ("Không tìm thấy món ăn phù hợp, hãy thử tìm Tacos hoặc Mì trộn").
4. **User Interactions:**
   * Gõ từ khóa $\to$ Debounce 300ms tự động lọc danh sách món.
   * Chạm vào thẻ món $\to$ Mở `SCR-04`.
5. **Navigation:**
   * Đến từ: Bottom Nav Tab 2. Nút Back trên thiết bị chuyển về Tab Trang chủ (`SCR-02`).
6. **Important UI Constraints:**
   * Bàn phím ảo mở lên không được gây overflow màn hình (`resizeToAvoidBottomInset: true`).

---

### Màn hình 4: SCR-04 — Product Detail & Topping Customization
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `CustomScrollView` (SliverAppBar có ảnh món co dãn) $\to$ `SliverList`:
     * Khối 1: Tên món, đánh giá sao, nhãn thời gian làm ("~4 phút").
     * Khối 2: Mô tả nguyên liệu (`type-body-large`).
     * Khối 3: Cụm chọn cấp độ cay (RadioListTile 3 mức).
     * Khối 4: Cụm chọn Topping thêm (`CheckboxListTile` danh sách 4 loại topping kèm đơn giá).
     * Khối 5: Ô ghi chú đầu bếp (`TextFormField(maxLines: 2)`).
     * Khoảng trống đệm đáy: `SizedBox(height: 80)` để không bị thanh CTA che khuất.
   * `bottomSheet` / Sticky Bottom Bar:
     * `Container(color: Colors.white, padding: spacing-md)` $\to$ `Row`: Cụm nút bấm (+/-) số lượng + `FilledButton` ("Thêm vào giỏ • [Giá]").
   * *Phần cuộn:* Toàn bộ nội dung bên trên cuộn mượt mà dưới thanh AppBar dạng Sliver.
2. **Components & Variants:**
   * `Button` (`Variant=Primary`, `State=Default`, chữ in đậm kèm giá động).
   * `Text field` (`Variant=Default`, ghi chú đầu bếp).
3. **States:**
   * `Default`: Hiển thị món và topping mặc định.
   * `Loading`: Hiển thị Shimmer khi đang tải dữ liệu món từ API.
4. **User Interactions:**
   * Tick/Untick checkbox Topping $\to$ Giá tiền hiển thị trên nút CTA ghim đáy lập tức tăng/giảm theo thời gian thực (Real-time recalculation).
   * Bấm nút "+/-" $\to$ Tăng/giảm số lượng (tối thiểu 1, tối đa 20).
   * Bấm nút "Thêm vào giỏ" $\to$ Hiển thị SnackBar "Đã thêm món vào giỏ hàng thành công!" $\to$ Chuyển thẳng tới `SCR-05` (Giỏ hàng). SnackBar có action "Thêm món khác" để quay lại `SCR-03` (chốt theo quyết định D29).
5. **Navigation:**
   * Đến từ: Bấm vào thẻ món ở `SCR-02` hoặc `SCR-03`.
   * Nút Back: Quay lại màn hình danh sách trước đó mà không lưu thay đổi.
6. **Important UI Constraints:**
   * Chiều cao mỗi dòng Checkbox Topping đạt chuẩn $48\text{ dp}$ để dễ chọn.

---

### Màn hình 5: SCR-05 — Cart & Order Summary
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Tiêu đề "Giỏ hàng" + Icon thùng rác xóa tất cả) $\to$ `Column`:
     * Phần trên (`Expanded` $\to$ `ListView` cuộn dọc):
       * Danh sách các món trong giỏ (`CartItemTile` gồm ảnh, tên, danh sách topping phụ, đơn giá, bộ tăng giảm số lượng).
       * Card chọn khung giờ nhận món tại Kiosk (Dropdown hoặc Radio: "Lấy ngay" hoặc "Hẹn giờ 09:20").
       * Khối nhập mã giảm giá (`Row`: `TextFormField` + `OutlinedButton` "Áp dụng").
       * Bảng hóa đơn tóm tắt (Tạm tính, Khuyến mãi, Tổng thanh toán).
     * Phần dưới (Ghim đáy):
       * `Container(color: Colors.white)` $\to$ `FilledButton` ("Tiến hành thanh toán • 45.000đ").
   * *Phần cuộn:* Danh sách món và tóm tắt cuộn dọc; nút thanh toán cố định ở đáy.
2. **Components & Variants:**
   * `Button` (`Variant=Primary`, chiều cao 52dp).
   * `Text field` (`Variant=Default / Error` khi mã voucher sai).
   * `Dialog` (`ConfirmationDialog` khi giảm số lượng về 0 hoặc xóa giỏ).
   * `Empty state` (`Variant=EmptyCart` hiển thị khi giỏ có 0 món).
3. **States:**
   * `Populated`: Giỏ hàng có sản phẩm.
   * `Empty`: Giỏ trống $\to$ Hiển thị hình vẽ đĩa ăn rỗng, dòng chữ "Giỏ hàng đang đói" và nút "Khám phá món ngay" dẫn về `SCR-02`.
   * `Error`: Ô voucher hiển thị viền đỏ và text lỗi khi nhập sai mã.
4. **User Interactions:**
   * Bấm dấu "-" khi số lượng = 1 $\to$ Bật popup Dialog xác nhận "Xóa món này khỏi giỏ hàng?".
   * Nhập mã `BB20` và bấm "Áp dụng" $\to$ Giảm giá 20% vào dòng Tổng tiền, hiện tick xanh.
   * Bấm "Tiến hành thanh toán" $\to$ Chuyển sang `SCR-06`.
5. **Navigation:**
   * Đến từ: Icon giỏ hàng trên App bar hoặc sau khi bấm thêm món ở `SCR-04`.
   * Nút Back: Quay lại màn hình trước.
6. **Important UI Constraints:**
   * Nút thanh toán luôn hiển thị trên bàn phím khi người dùng focus vào ô nhập mã giảm giá.

---

### Màn hình 6: SCR-06 — Checkout & Payment Method
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Tiêu đề "Xác nhận & Thanh toán") $\to$ `SingleChildScrollView` $\to$ `Column`:
     * Section 1: Thẻ thông tin địa điểm nhận ("Kiosk Q9 · Tầng 2 - Giờ giải lao ca 1").
     * Section 2: Tiêu đề "Phương thức thanh toán".
     * Section 3: Cụm lựa chọn hình thức (`RadioListTile` 3 phương thức: Ví MoMo, Chuyển khoản VietQR, Tiền mặt tại quầy Kiosk).
     * Section 4: Card tóm tắt hóa đơn cuối cùng (Tổng tiền in đậm 20sp).
     * Section 5: Ghi chú cam kết an toàn & bảo lưu giỏ hàng nếu lỗi mạng.
     * Section 6: Nút bấm xác nhận thanh toán ghim đáy.
   * *Phần cuộn:* Toàn bộ nội dung cuộn dọc.
2. **Components & Variants:**
   * `Button` (`Variant=Primary`, `State=Default / Loading`).
   * `Dialog` (`ConfirmationDialog` xác nhận thanh toán).
3. **States:**
   * `Default`: Cho phép chọn phương thức.
   * `Loading`: Khi đang gửi lệnh thanh toán sang cổng MoMo/Ngân hàng $\to$ Hiển thị Modal Progress Indicator toàn màn hình.
   * `Error (SCR-06-ERR)`: Khi kết nối bị timeout hoặc người dùng hủy giao dịch ví $\to$ Chuyển sang màn hình Phục hồi lỗi `SCR-06-ERR`.
4. **User Interactions:**
   * Chọn phương thức thanh toán $\to$ Highlight viền cam xung quanh phương thức đó.
   * Bấm "Xác nhận thanh toán":
     * Nếu chọn "Tiền mặt tại quầy" $\to$ Tạo đơn ngay $\to$ Chuyển sang `SCR-07`.
     * Nếu chọn "Ví MoMo / QR" $\to$ Kích hoạt Deep Link mở app MoMo. Nếu thành công $\to$ Sang `SCR-07`; Nếu lỗi $\to$ Sang `SCR-06-ERR`.
5. **Navigation:**
   * Đến từ: `SCR-05`.
   * Nút Back: Quay lại Giỏ hàng để điều chỉnh món.
6. **Important UI Constraints:**
   * Nút thanh toán phải vô hiệu hóa (disabled) khi đang trong trạng thái processing để tránh double-charge.

---

### Màn hình 7: SCR-07 — Order Tracking & Pickup Status
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Tiêu đề "Trạng thái đơn hàng", không có nút Back để tránh người dùng tưởng đơn bị hủy) $\to$ `SingleChildScrollView` $\to$ `Column`:
     * Section 1: Thẻ mã nhận đồ nổi bật (`Container(color: Colors.white, borderRadius: 24, padding: 24)`):
       * Nhãn "Mã số nhận món tại Kiosk": Text lớn **#A-204** (`type-display-large`, cỡ chữ 32sp).
       * Mã QR Code (`QrImageView(data: 'ORDER-A28')`).
       * Thời gian hẹn: "Dự kiến: 09:22 (Còn 4 phút)".
     * Section 2: Thanh tiến trình 4 giai đoạn (`Stepper` hoặc custom widget 4 bước nằm ngang).
     * Section 3: Chi tiết các món đang nấu rút gọn.
     * Section 4: Nút Hỗ trợ & Nút Hủy đơn (OutlinedButton màu đỏ nhạt).
   * `bottomNavigationBar`: `NavigationBar` (selected index = 2).
   * *Phần cuộn:* Cuộn dọc nội dung.
2. **Components & Variants:**
   * `Dialog` (`DestructiveDialog` cảnh báo khi bấm nút Hủy đơn: "Bạn có chắc chắn muốn hủy đơn hàng này không?").
   * `Button` (`Variant=Outline`, hotline hỗ trợ).
3. **States:**
   * `Step 1 (Đã nhận)`: Icon checkmark xanh.
   * `Step 2 (Đang làm)`: Icon đầu bếp hoạt họa nhấp nháy.
   * `Step 3 (Sẵn sàng tại quầy)`: Phát âm thanh chuông báo và rung điện thoại khi chuyển sang bước này.
   * `Step 4 (Hoàn tất)`: Đóng đơn và hiển thị nút Đánh giá 5 sao.
4. **User Interactions:**
   * Bấm vào mã QR $\to$ Phóng to QR toàn màn hình để dễ quét qua lớp kính Kiosk.
   * Bấm nút "Hủy đơn" (trong 60 giây đầu) $\to$ Mở Dialog xác nhận hủy $\to$ Đơn hủy và hoàn tiền.
   * Bấm Tab Trang chủ trên Bottom Nav $\to$ Quay về Home, đơn hàng vẫn chạy ngầm trên thanh Notification.
5. **Navigation:**
   * Đến từ: Sau khi thanh toán thành công ở `SCR-06` hoặc từ Tab Đơn hàng (`Tab 3`).
   * Nút Back: Chuyển về Trang chủ `SCR-02` (không thể back lại màn hình thanh toán đã hoàn thành).
6. **Important UI Constraints:**
   * Độ sáng màn hình tự động đẩy lên mức tối đa khi hiển thị mã QR để đầu đọc Kiosk dễ quét.

---

### Màn hình 8: SCR-08 — Order History & Quick Reorder
1. **Layout Hierarchy:**
   * `Scaffold` $\to$ `AppBar` (Tiêu đề "Lịch sử đặt món") $\to$ `Column`:
     * Thanh chip bộ lọc thời gian: "Tất cả", "Tháng này", "Đã hủy".
     * `Expanded` $\to$ `ListView.builder` cuộn dọc các thẻ đơn hàng cũ (`HistoryOrderCard`).
   * `bottomNavigationBar`: `NavigationBar` (selected index = 3).
   * *Phần cuộn:* Danh sách thẻ đơn hàng cũ cuộn dọc.
2. **Components & Variants:**
   * `Card` (`Variant=HistoryCard`, hiển thị mã đơn, ngày giờ, ảnh đại diện món, số tiền đã trả, trạng thái Hoàn tất / Đã hủy).
   * `Button` (`Variant=Primary / Small`, nút "Đặt lại đơn này").
   * `Navigation` (`Type=BottomNavigationBar`, selected index = 3).
3. **States:**
   * `Populated`: Danh sách các đơn cũ.
   * `Empty`: Chưa có đơn hàng nào $\to$ Hiển thị hình ảnh minh họa + nút "Bắt đầu đặt đơn đầu tiên".
4. **User Interactions:**
   * Chạm vào thẻ đơn cũ $\to$ Mở chi tiết hóa đơn cũ.
   * Chạm vào nút **"Đặt lại đơn này"** $\to$ Hệ thống tự động thêm lại toàn bộ các món và topping của đơn đó vào Giỏ hàng $\to$ Mở ngay `SCR-05` (Chỉ mất 1 chạm để ăn lại món quen).
5. **Navigation:**
   * Đến từ: Bottom Nav Tab 4. Nút Back trên thiết bị chuyển về Tab 1 (`SCR-02`).
6. **Important UI Constraints:**
   * Nếu có món cũ hiện tại đang tạm hết hàng, khi bấm "Đặt lại" hệ thống sẽ hiển thị Dialog thông báo rõ món nào hết và chỉ nạp các món còn lại vào giỏ.

---

## 3. Đặc tả hành vi thích ứng trên màn hình rộng (Wider Screen Behavior: $\ge 600\text{ dp}$)

Theo yêu cầu mục 6 và mục 8 của đề bài, dưới đây là đặc tả bố cục khi ứng dụng chạy trên máy tính bảng (Tablet), màn hình gập (Foldable) hoặc giao diện ngang ($\ge 600\text{ dp}$):

1. **Giới hạn độ rộng tối đa nội dung (Max Content Width Constraint):**
   * Trên màn hình $\ge 600\text{ dp}$, toàn bộ vùng nội dung được bao bọc trong một container căn giữa với độ rộng tối đa $540\text{ dp}$ (`Center(child: ConstrainedBox(constraints: BoxConstraints(maxWidth: 540)))`), hai bên hiển thị nền phụ màu kem nhạt `#FFF5E5`. Cách tiếp cận này giúp giữ nguyên tỷ lệ công thái học hoàn hảo của giao diện di động mà không làm biến dạng các nút bấm hay kéo dãn ảnh món ăn quá mức.
2. **Chuyển đổi bố cục 2 cột (Adaptive Split View):**
   * Tại màn hình Giỏ hàng (`SCR-05`) và Thanh toán (`SCR-06`), bố cục tự động chuyển từ 1 cột dọc sang **2 cột song song**:
     * Cột bên trái (60%): Danh sách món ăn và tùy chọn topping.
     * Cột bên phải (40%): Cụm tóm tắt thanh toán, ô nhập mã giảm giá và nút bấm CTA thanh toán.
3. **Chuyển đổi thanh điều hướng:**
   * Thanh Bottom Navigation Bar dưới đáy tự động chuyển thành **Navigation Rail** dạng cột đứng ghim ở cạnh trái màn hình, tối ưu hóa không gian hiển thị theo chiều dọc.

---

## 4. Quy tắc ảnh món (áp dụng S02, S03, S04 — quyết định D37)

* Tỉ lệ ảnh 1:1 trên thẻ, 16:9 ở S04; `BoxFit.cover`; nền `#FFF5E5`.
* Đang tải: khối skeleton cùng kích thước.
* Tải lỗi: khối màu `#FFE8CC` hiện tên món (`type-title-medium`, tối đa 2 dòng, ellipsis); không để ô trống.
* Món **Tạm hết** (D30): ảnh mờ 40%, nhãn "Tạm hết" có icon, nút + bị tắt.

---

## 5. Cập nhật Final UI v2 (S01–S25)

Final UI v2 thay các màn cũ ở mục 2. Mã màn dùng `S01…S25`; bảng dưới ánh xạ từ mã `SCR-xx` cũ. Vị trí khung: Figma Page 03, khung có hậu tố " v2"; số đo và quyết định: [`05-P4-ui-design/06-phan-bien-giao-dien/03-bao-cao-tong-hop.md`](../05-P4-ui-design/06-phan-bien-giao-dien/03-bao-cao-tong-hop.md).

| SCR cũ | Màn v2 | Thay đổi so với mục 2 |
|---|---|---|
| SCR-01 | S01 Onboarding | Hero là ô icon 120 dp thay emoji; ba lợi ích dùng icon vector; một nút chính "Bắt đầu đặt món" |
| SCR-02 | S02 Trang chủ | Thanh trên có địa điểm, trạng thái quán, chuông thông báo, giỏ; chip một kiểu; thẻ món dùng `Card/Food` v2 |
| SCR-03 | S03 Thực đơn | Chip lọc chữ thuần; thẻ món có icon theo loại; món hết dùng badge "Tạm hết" |
| SCR-04 | S04 Chi tiết món | Thanh dưới cố định: bước số lượng 48 dp và nút "Thêm vào giỏ · giá" |
| SCR-05 | S05 Giỏ hàng | Chỉ còn giỏ hàng, giờ nhận, mã giảm giá, tổng tiền; nút "Tiếp tục thanh toán" |
| SCR-06 | S06 Thanh toán | Chọn phương thức tại đây (MoMo mặc định) và nút "Xác nhận đặt đơn · giá" |
| SCR-07 | S07 Theo dõi đơn | Nút chính "Chỉ đường tới Kiosk"; "Về trang chủ" là nút chữ; bước trạng thái dùng nhãn 14 sp |
| SCR-08 | S08 Đơn hàng | Hai tab (Đang xử lý, Lịch sử); thẻ đơn đang làm có nút phụ "Xem mã QR nhận món" |

### 5.1 Token bổ sung

| Token Figma | Hex | Flutter | Dùng cho |
|---|---|---|---|
| `color/v2-background` | `#FAF8F5` | `ColorScheme.surface` (nền màn) | Nền mọi màn |
| `color/v2-surface-variant` | `#F3F0EA` | `surfaceContainerHighest` | Ô ảnh món, ô illustration |
| `color/v2-border` | `#E4DFD8` | `outlineVariant` | Viền thẻ, đường chia |
| `color/v2-selected` | `#FFF1DE` | `secondaryContainer` | Chip và hàng đang chọn |
| `color/v2-muted` | `#6B5F55` | `onSurfaceVariant` | Chữ phụ, icon |

Quy tắc màu: cam `#F69D39` chỉ cho một `FilledButton` chính mỗi màn và trạng thái đang chọn; chữ cam dùng `#B45309`; viền ô nhập `#8A7A70`.

### 5.2 Component bổ sung

| Component Figma | Flutter | Ghi chú |
|---|---|---|
| `v2/Chip` (Default, Selected) | `ChoiceChip`, cao 48 dp | Chọn: nền `#FFF1DE`, viền cam |
| `v2/NavBar` (4 tab) | `NavigationBar`, cao 64 dp | Nhãn 12 sp; tab chọn có pill `#FFF1DE` |
| `v2/Card/Food` (Food/Drink × Default/OutOfStock) | `Card` + `ListTile` tuỳ biến, 328 × 96 | Nút + 48 dp; hết hàng hiện badge, không có nút + |
| `v2/IconButton` | `IconButton`, `minimumSize: Size(48, 48)` | Thuộc tính Icon đổi icon |
| `v2/Button/Secondary` | `OutlinedButton`, cao 48 dp | Viền `#8A7A70` |
| `v2/Button/Text` | `TextButton`, cao 48 dp | Chữ `#B45309` |
| `Icon/*` (27 icon) | `Icon(Icons.*_rounded)` hoặc `flutter_svg` | Một nét, 24 dp, màu `onSurfaceVariant` |

Danh sách icon: home, restaurant, receipt, person, search, cart, back, close, add, remove, check, chevron, location, schedule, delete, bell, replay, error, offer, card, cash, wallet, qr, cafe, navigate, heart, checkCircle.

### 5.3 Đặc tả S09–S25 (6 mục)

Khung 360 × 800 dp, lề 16 dp, thanh trên cao 56 dp, nút chính cao 56 dp ở dưới cùng.

| Màn | Layout | Component | State | Tương tác | Điều hướng | Ràng buộc |
|---|---|---|---|---|---|---|
| S09 Sửa đơn | Banner hạn sửa, chip giờ nhận, hai dòng số lượng, ô ghi chú, nút lưu | `v2/Chip`, `v2/IconButton`, TextField | Chỉ sửa được khi bếp chưa làm (hạn 10:12) | Đổi giờ, số lượng, ghi chú; Lưu | Lưu → S07; Giữ nguyên → S07 | Không đổi món (D04) |
| S10 Đơn đã huỷ | Illustration thành công, tóm tắt hoàn tiền | Button | Thành công | Về trang chủ; Đặt lại đơn này | → S02; → S05 | Hoàn 54.000đ về ví gốc trong khoảng 30 giây |
| S11 Lịch sử | Hai tab Tuần/Tháng, thẻ chi tiêu với biểu đồ 7 cột, danh sách đơn | NavBar | Tuần, Tháng | Đổi tab; chạm đơn | Đơn → S12 | Cột cao nhất tô cam; trục có nhãn chữ |
| S12 Chi tiết đơn | Hoá đơn, tổng tiền, trạng thái, phương thức thanh toán | Button | Đã nhận | Đặt lại đơn này; Báo sự cố | → S05; → S24 | Tiền dạng `54.000đ` |
| S13 Món yêu thích | Chip lọc, danh sách thẻ món kèm số lần đã đặt | `v2/Card/Food`, `v2/Chip` | Mặc định | Chạm + thêm vào giỏ | + → S05 | Tab Cá nhân đang chọn |
| S14 Đặt lại nhanh | Bottom sheet 540 dp trên lớp phủ 45% | Button, radio | Chọn đơn | Chọn đơn; Thêm vào giỏ | → S05; Chọn từ thực đơn → S03 | Lớp phủ chặn thao tác phía sau |
| S15 Cá nhân | Thẻ hồ sơ, danh sách 5 mục, link xoá dữ liệu | NavBar | Mặc định | Chạm từng mục | → S16, S17, S18, S13, S11 | Xoá dữ liệu cần xác nhận |
| S16 Hồ sơ | Ghi chú không bắt buộc, 4 ô nhập, nút lưu | TextField, Button | Trống, đã điền | Nhập; Lưu | Back → S15 | Không bắt buộc đăng nhập (D12) |
| S17 Thanh toán | Bốn phương thức dạng radio | Button | Một mục được chọn | Chọn mặc định; Lưu | Back → S15 | Mặc định MoMo |
| S18 Cài đặt thông báo | Bốn công tắc kèm mô tả | Switch tuỳ biến 52 × 32 | Bật (có dấu tích), tắt | Bật/tắt | Back → S15 | Trạng thái bật có icon, không chỉ màu |
| S19 Thông báo | Nhóm Hôm nay, Trước đó; thẻ chưa đọc có chấm và nút | Button/Secondary | Chưa đọc, đã đọc | Xem mã nhận món | → S20 | Nút ≥ 48 dp |
| S20 Nhận món | Thẻ QR lớn 189 dp, mã đơn, giờ giữ món | Button | Sẵn sàng | Tôi đã nhận món | → S23 | QR cần độ sáng tối đa |
| S21 Quán đóng | Thanh trạng thái màu lỗi kèm icon, thẻ hẹn nhận, xem trước thực đơn | `v2/Card/Food` (hết), Button | Đóng cửa | Hẹn nhận; Nhắc tôi | → S25 | Thẻ món không có nút + |
| S22 Món hết | Thẻ món hết, ghi chú giờ có lại, hai món thay thế | `v2/Card/Food` | Hết hàng | Thêm món thay thế; Báo khi có lại | + → S05 | Gợi ý chỉ món còn hàng |
| S23 Đánh giá | Thang 1–5, chip lý do, ghi chú | Chip, TextField, Button | Đã chọn điểm | Chọn điểm, chip; Gửi; Bỏ qua | → S02 | Mỗi điểm có nhãn chữ |
| S24 Báo sự cố | Chip lý do, ô mô tả, thêm ảnh, ghi chú hoàn tiền | Chip, TextField, Button | Mặc định | Chọn lý do; Gửi báo cáo | → S12 | Ảnh tuỳ chọn |
| S25 Hẹn giờ | Thẻ lịch học nhập tay, chip gợi ý giờ nhận | Chip, Button | Mặc định | Chọn giờ; Tiếp tục | → S05 | Lịch học do người dùng nhập |

### 5.4 Màn bổ sung S26–S30

| Màn | Layout | Component | State | Tương tác | Điều hướng | Ràng buộc |
|---|---|---|---|---|---|---|
| S26 Đăng nhập | Illustration, tiêu đề, ô email, nút gửi mã | TextField, Button | Trống | Nhập email; Gửi mã; Tiếp tục không cần tài khoản | → S26-OTP; → S02 | Không bắt buộc (D12) |
| S26-OTP | 6 ô số, đếm ngược gửi lại | TextField ×6, Button | Đang nhập | Nhập số; Xác nhận | → S02 | Mã hiệu lực 5 phút |
| S27 Chọn Kiosk | Ô tìm, danh sách thẻ kiosk kèm radio | Card, radio, Button | Chọn một | Chọn kiosk | → S02 | Kiosk đóng hiện chữ và icon, không chỉ màu |
| S28 Kết quả tìm kiếm | Thanh tìm trong app bar, chip lọc, thẻ món | `v2/Card/Food`, `v2/Chip` | Có kết quả | Chạm món; + | → S04; → S05 | Số kết quả hiện bằng chữ |
| S28-EMPTY | Illustration, gợi ý từ khoá | `v2/Chip` | Không có kết quả | Chạm gợi ý | → S28 | |
| S29 Mã giảm giá | Ô nhập mã, danh sách thẻ mã | TextField, Button/Secondary, radio | Chọn, hết hạn | Áp dụng; Dùng mã | → S05 | Mã hết hạn có icon lỗi và chữ |
| S30 Mất kết nối | Illustration, thông báo, hai nút | Button, Button/Text | Lỗi mạng | Thử lại; Xem giỏ hàng | → S02; → S05 | Giỏ hàng lưu cục bộ (DP5) |
| S02-LOADING | Khối xám thay cho nội dung | Skeleton | Đang tải | — | Tự chuyển sau 1,2 giây → S02 | Cùng kích thước nội dung thật |

## 6. App người bán (K01–K15)

Ứng dụng riêng cho nhân viên quầy, dùng cùng token và component ở mục 5. Đặc tả chi tiết và flow: [`05-P4-ui-design/03-kitchen-app.md`](../05-P4-ui-design/03-kitchen-app.md). Thanh dưới 4 tab (Đơn, Quét mã, Món, Quán) dùng `NavigationBar` như `v2/NavBar`.

| Màn | Layout | Component | State | Tương tác | Điều hướng | Ràng buộc |
|---|---|---|---|---|---|---|
| K01 Đăng nhập | Logo, ô mã quầy, ô PIN, nút đăng nhập | TextField, Button | Mặc định | Nhập mã quầy và PIN | → K02-EMPTY | PIN ẩn ký tự |
| K02 Danh sách đơn | Trạng thái quầy, chip 4 trạng thái, thẻ đơn 156 dp | `v2/Chip`, Card, Button/Secondary | Có đơn | Chạm thẻ; Nhận đơn; chuông | → K03; → K13 | Thanh toán hiện trên thẻ |
| K02-EMPTY | Illustration, chú thích | — | Trống | Chờ đơn mới | Tự chuyển → K02 | |
| K03 Chi tiết đơn | Thẻ giờ nhận, thẻ món, thanh toán | Card, Button, Button/Text | Mới | Nhận đơn; Từ chối | → K04; → K12 | Từ chối cần lý do |
| K04 Đang chuẩn bị | Đếm ngược, thanh tiến độ, checklist | Checkbox, Button | Đang làm | Tick từng món; Xong; Báo thiếu | → K02; → K08 | Cả dòng là vùng bấm |
| K05 Quét mã | Khung ngắm 280 dp, nhập tay | Camera, TextField, Button/Secondary | Chờ quét | Quét; Tìm đơn | → K06; → K05-ERR | Cần quyền camera |
| K05-ERR | Khung ngắm viền lỗi, thông báo | — | Lỗi | Nhập tay | → K06-CASH | Lỗi có icon và chữ |
| K06 Xác nhận giao | Mã hợp lệ, món, thanh toán | Card, Button | Đã thanh toán | Xác nhận đã giao | → K02 | Đổi trạng thái đơn thành Hoàn tất |
| K06-CASH | Như K06, thẻ thu tiền nổi bật | Card, Button | Trả tại quầy | Đã thu tiền và giao | → K02 | Phải xác nhận đã thu tiền |
| K08 Quản lý món | Chip lọc, hàng món kèm công tắc | `v2/Chip`, Switch | Còn, hết | Bật/tắt | → K09 | Công tắc bật có dấu tích |
| K09 Hết món | Bottom sheet: lý do, giờ có lại | `v2/Chip`, Button | Overlay | Chọn; Xác nhận | → K08 | Khách thấy "Tạm hết" kèm giờ có lại |
| K14 Thêm món mới | Ảnh, tên, giá, danh mục, thời gian chuẩn bị, còn hàng | TextField, `v2/Chip`, Switch, Button | Trống | Nhập; Lưu món | → K14-ERR (thiếu thông tin) hoặc K08 | Tên và giá bắt buộc, giá > 0 |
| K14-ERR | Như K14, viền và chữ lỗi | TextField, Button | Lỗi | Sửa; Lưu món | → K08 | Lỗi có icon và chữ |
| K15 Sửa món | Như K14, điền sẵn | TextField, `v2/Chip`, Switch, Button, Button/Text | Đã điền | Lưu thay đổi; Xoá món | → K08 | Xoá cần xác nhận |
| K10 Quán | Thẻ trạng thái, cài đặt, liên kết | Switch, `v2/IconButton`, Button/Secondary | Đang nhận đơn | Bật/tắt; đổi số đơn tối đa | → K11; → K01 | Tắt nhận đơn: khách thấy S21 |
| K11 Thống kê ca | Bốn thẻ số, biểu đồ cột | Card | Mặc định | — | Back → K10 | Cột cao nhất tô cam |
| K12 Từ chối đơn | Dialog 320 dp: lý do, hai nút | radio, Button | Overlay | Chọn lý do; Từ chối | → K02 | Hoàn tiền tự động |
| K13 Sự cố | Lý do, mô tả, ảnh khách, đơn liên quan | Card, Button | Mới | Hoàn tiền; Từ chối và giải thích | → K02 | Hoàn tiền cần xác nhận |
