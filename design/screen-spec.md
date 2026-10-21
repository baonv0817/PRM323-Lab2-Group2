# Design Specification: Screen Inventory & Intent

> **Tài liệu:** `design/screen-spec.md`  
> **Dự án:** BreakBite App — Campus Quick Food Ordering  
> **Môn học:** PRM323 — Lab 2  
> **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) *(Bao gồm đầy đủ 6 Trang & 3 Flow Prototype tương tác)*  
> **Khung kích thước chuẩn di động:** $360 \times 800\text{ dp}$ (Tỷ lệ khung 9:20 phổ biến trên Android & iOS)

---

## 1. Danh sách chi tiết 8 Màn hình chính (Screen Specifications)

---

### Màn hình 1: SCR-01 — Splash & Onboarding (Chào mừng & Định danh khuôn viên)
* **Mục đích thiết kế (Design Intent):** Tạo ấn tượng thị giác đầu tiên chuyên nghiệp, ấm cúng; truyền tải tức thì 3 lợi ích cốt lõi cho sinh viên ("Đặt món trước - Không chờ đợi - Lấy đồ tại Kiosk trong 30 giây").
* **Thuộc luồng (Flow Association):** Điểm khởi đầu của ứng dụng khi người dùng lần đầu cài đặt.
* **Nội dung hiển thị (Content Structure):**
  * **Header/Logo:** Logo BreakBite với biểu tượng bánh Tacos cách điệu và chiếc thìa/dĩa năng động.
  * **Hero Image:** Hình ảnh minh họa sinh viên nhận món ăn tại quầy Kiosk hiện đại.
  * **Tiêu đề & Khẩu hiệu:** Tiêu đề lớn `type-display-large`: "Ăn ngon - Học tốt - Không chờ đợi". Mô tả ngắn về việc tiết kiệm 15 phút giải lao.
  * **Hành động chính (Primary CTA):** Nút Button lớn `variant=Primary`: "Bắt đầu đặt món ngay" (chiều cao 52dp, ghim đáy).
  * **Hành động phụ (Secondary CTA):** Dòng liên kết "Đăng nhập với email trường (@fpt.edu.vn) để tích điểm sinh viên".

---

### Màn hình 2: SCR-02 — Home & Quick Discovery (Trang chủ & Gợi ý nhanh)
* **Mục đích thiết kế (Design Intent):** Tối ưu hóa tốc độ chọn món cho sinh viên đang vội bằng cách đưa các combo bữa phụ bán chạy nhất và thanh tìm kiếm lên vị trí nổi bật nhất.
* **Thuộc luồng (Flow Association):** Điểm bắt đầu (Start) của **Flow 1 (Quick Campus Pickup)**.
* **Nội dung hiển thị (Content Structure):**
  * **Top App Bar:** Lời chào cá nhân hóa "Chào Quân 👋", ô chọn địa điểm nhận ("Kiosk Tòa Alpha"), biểu tượng Giỏ hàng có huy hiệu (Cart badge counter).
  * **Banner khẩn cấp / Ưu đãi:** Card trượt ngang hiển thị chương trình "Combo Giờ Vàng giải lao 09h - Giảm 15%".
  * **Thanh tìm kiếm nhanh (Search Field):** Ô tìm kiếm có icon kính lúp, placeholder "Tìm Tacos, Mì trộn, Trà sữa...".
  * **Danh mục cuộn ngang (Category Chips):** Chip "Tất cả", "⭐ Nổi bật", "Tacos giòn", "Mì trộn cay", "Trà & Đồ uống".
  * **Khu vực "Gợi ý lấy nhanh dưới 5 phút" (Vertical List/Grid):** Các Food Cards hiển thị ảnh món, tên, thời gian chế biến ước tính ("⚡ 3-5 phút"), giá tiền và nút "+" thêm nhanh.
  * **Bottom Navigation Bar:** Ghim đáy với 4 tab (Trang chủ [Active], Thực đơn, Đơn hàng, Cá nhân).

---

### Màn hình 3: SCR-03 — Menu & Filter Search (Thực đơn & Tìm kiếm phân loại)
* **Mục đích thiết kế (Design Intent):** Giúp sinh viên duyệt toàn bộ thực đơn phong phú của căn tin, lọc món theo ngân sách sinh viên và nhóm sở thích ăn uống.
* **Thuộc luồng (Flow Association):** Điểm bắt đầu (Start) của **Flow 2 (Customize & Voucher)**.
* **Nội dung hiển thị (Content Structure):**
  * **App Bar:** Tiêu đề "Thực đơn BreakBite" + Nút mở bộ lọc (Filter icon).
  * **Bộ lọc phân loại (Filter Section):** Tab điều hướng phân loại món (Tacos / Mì Trộn / Đồ Uống) và chip lọc giá ("< 30k", "30k - 50k", "Ăn kèm").
  * **Danh sách món ăn:** Danh sách 2 cột (Staggered Grid) hiển thị ảnh sắc nét, tag "Best Seller", tên món, nguyên liệu tóm tắt và giá bán.
  * **Floating Cart Button:** Nút nổi ở góc dưới hiển thị tổng số món trong giỏ và tổng tiền tạm tính, bấm vào chuyển ngay tới giỏ hàng.

---

### Màn hình 4: SCR-04 — Product Detail & Topping Customization (Chi tiết món ăn & Topping)
* **Mục đích thiết kế (Design Intent):** Cho phép sinh viên cá nhân hóa bữa ăn theo khẩu vị riêng (chọn độ cay, thêm topping) và quan sát giá tiền cập nhật theo thời gian thực (Real-time price feedback).
* **Thuộc luồng (Flow Association):** Xuất hiện trong cả **Flow 1** và **Flow 2**.
* **Nội dung hiển thị (Content Structure):**
  * **Hero Product Banner:** Ảnh chụp cận cảnh món ăn chất lượng cao, nút Back và nút Yêu thích dạng hình tròn nổi trên ảnh.
  * **Thông tin món:** Tên món cỡ lớn, giá gốc, nhãn thời gian làm ("~4 phút chuẩn bị"), mô tả thành phần nguyên liệu.
  * **Khu vực tùy chỉnh cấp độ cay:** Radio button chọn 3 mức: "Không cay", "Cay vừa", "Siêu cay cấp 2".
  * **Khu vực chọn Topping (Checkbox List):** Danh sách topping kèm giá cộng thêm (Trứng ốp la +5k, Phô mai sợi +8k, Xúc xích nướng +10k, Trân châu đen +5k).
  * **Ô ghi chú đầu bếp:** TextField nhập yêu cầu đặc biệt ("Không cho hành lá", "Ít ngọt").
  * **Bottom Sticky Bar:** Bộ đếm số lượng (+/-) và nút CTA lớn: "Thêm vào giỏ hàng • [Tổng tiền động]" (Cao 52dp, ghim đáy).

---

### Màn hình 5: SCR-05 — Cart & Order Summary (Giỏ hàng & Hẹn giờ nhận món)
* **Mục đích thiết kế (Design Intent):** Minh bạch toàn bộ danh sách món đã chọn, tính toán chính xác số tiền, cho phép nhập mã ưu đãi và chọn khung giờ nhận đồ để tránh chờ đợi.
* **Thuộc luồng (Flow Association):** Xuất hiện trong cả 3 Flows.
* **Nội dung hiển thị (Content Structure):**
  * **App Bar:** Nút Back + Tiêu đề "Giỏ hàng của bạn" + Nút "Xóa tất cả".
  * **Danh sách món đã đặt:** Card từng món gồm ảnh thu nhỏ, tên món kèm ghi chú topping đã chọn, đơn giá và cụm nút (+/-) điều chỉnh số lượng.
  * **Khung hẹn giờ nhận món (Campus Pickup Slot):** Tùy chọn: "Lấy ngay khi xong (~7 phút)" (**mặc định**, quyết định D28) hoặc "Hẹn giờ: 09:20 (Giờ giải lao ca 1)".
  * **Ô nhập mã giảm giá (`CouponInput`):** TextField nhập code kèm nút "Áp dụng", hiển thị badge xanh lá khi mã `BB20` được duyệt.
  * **Bảng chi tiết thanh toán:** Tạm tính, Giảm giá sinh viên, Phí đóng gói mang đi (0đ), Tổng thanh toán cuối cùng.
  * **Nút CTA ghim đáy:** "Tiến hành thanh toán • 45.000đ".
  * **Trạng thái rỗng (Empty State Variant):** Nếu giỏ hàng trống, hiển thị hình vẽ đĩa ăn rỗng, dòng chữ "Giỏ hàng đang trống" và nút "Khám phá món ngay".

---

### Màn hình 6: SCR-06 — Checkout & Payment Method (Xác nhận đơn & Thanh toán)
* **Mục đích thiết kế (Design Intent):** Cung cấp các phương thức thanh toán quen thuộc nhất với sinh viên, hiển thị rõ ràng chính sách hoàn tiền/giữ đơn nếu giao dịch gặp sự cố.
* **Thuộc luồng (Flow Association):** Màn hình then chốt trong **Flow 1, Flow 2** và là nơi phát sinh **Flow 3 (Error & Recovery)**.
* **Nội dung hiển thị (Content Structure):**
  * **Thông tin nhận đồ:** Tên người nhận (Quân - 0987xxx), Điểm nhận (Kiosk BreakBite - Tòa Alpha).
  * **Danh sách phương thức thanh toán (Radio Selection Cards):**
    1. Ví MoMo (Biểu tượng logo ví điện tử).
    2. Chuyển khoản VietQR sinh viên (Tự động mở app ngân hàng).
    3. Trả tiền mặt tại quầy khi nhận món (Cash on Pickup).
  * **Tóm tắt đơn hàng rút gọn:** Số lượng món, tổng tiền thanh toán in đậm cỡ lớn.
  * **Cam kết an toàn:** Icon khiên bảo mật + Dòng ghi chú "Bảo lưu giỏ hàng 15 phút nếu thanh toán gặp lỗi mạng".
  * **Nút CTA chính:** "Xác nhận & Thanh toán".

---

### Màn hình 7: SCR-07 — Order Tracking & Pickup Status (Theo dõi trạng thái & Mã nhận Kiosk)
* **Mục đích thiết kế (Design Intent):** Giải tỏa hoàn toàn cảm giác sốt ruột của sinh viên bằng mã số nhận đồ cỡ lớn và thanh tiến trình 4 giai đoạn rõ ràng.
* **Thuộc luồng (Flow Association):** Điểm kết thúc (End) của cả 3 User Flows.
* **Nội dung hiển thị (Content Structure):**
  * **Thẻ mã nhận đồ nổi bật (Pickup Pass Card):**
    * Mã số đơn hàng in cực lớn: **#A-204** (Cỡ chữ 32sp, màu `#622B14`).
    * Mã QR Code động hiển thị ngay giữa màn hình để máy quét tại Kiosk nhận diện trong 1 giây.
    * Thời gian sẵn sàng ước tính: "Dự kiến: 09:22 (Còn 4 phút)".
  * **Thanh tiến trình đơn hàng (Step Progress Tracker):**
    * Bước 1: Đã nhận đơn (Checkmark xanh)
    * Bước 2: Bếp đang chuẩn bị (Icon đầu bếp đang nhấp nháy hoạt họa)
    * Bước 3: Sẵn sàng tại quầy (Sáng đèn khi xong)
    * Bước 4: Đã nhận đồ hoàn tất
  * **Chi tiết đơn hàng rút gọn:** 1x Tacos phô mai, 1x Trà đào chanh sả.
  * **Khu vực hỗ trợ:** Nút "Gọi nhân viên quầy Kiosk" và Nút "Hủy đơn hàng" (chỉ khả dụng trong 60 giây đầu khi bếp chưa làm).

---

### Màn hình 8: SCR-08 — Order History & Quick Reorder (Lịch sử đơn hàng & Đặt lại đơn cũ)
* **Mục đích thiết kế (Design Intent):** Giúp sinh viên quen khẩu vị có thể đặt lại bữa sáng/bữa trưa quen thuộc chỉ bằng đúng 1 chạm mà không cần tìm kiếm lại từ đầu.
* **Thuộc luồng (Flow Association):** Top-level Tab 4 trên thanh điều hướng Bottom Navigation.
* **Nội dung hiển thị (Content Structure):**
  * **App Bar:** Tiêu đề "Lịch sử đơn hàng" + Bộ lọc "Tất cả / Đã hoàn thành / Đã hủy".
  * **Danh sách thẻ đơn hàng cũ:**
    * Thẻ đơn ngày hôm qua: Ngày giờ đặt, Mã số đơn #A-14, Danh sách món tóm tắt, Tổng tiền đã trả.
    * Trạng thái đơn: Tag "Hoàn thành" màu xanh lá.
    * Nút hành động nổi bật: **"Đặt lại đơn này"** (Reorder button) $\rightarrow$ Tự động nạp lại toàn bộ món và topping cũ vào Giỏ hàng `SCR-05`.
  * **Thẻ đơn bị hủy:** Hiển thị lý do hủy (Khách hủy / Hết nguyên liệu) và trạng thái "Đã hoàn tiền vào ví".
