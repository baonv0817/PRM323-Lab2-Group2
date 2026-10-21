# Design Decisions & Accessibility Checklist

> **Tài liệu:** `design/design-decisions.md`  
> **Dự án:** BreakBite App — Campus Quick Food Ordering  
> **Môn học:** PRM323 — Lab 2  
> **Figma Design Link:** [BreakBite Figma Project (View Access)](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) *(Bao gồm đầy đủ 6 Trang & 3 Flow Prototype tương tác)*

---

## 1. Top 8 Quyết định thiết kế quan trọng nhất (Design Decisions with Justification)

Toàn bộ các quyết định thiết kế dưới đây đều được xây dựng dựa trên nhu cầu của Persona (sinh viên di chuyển nhanh), 10 nguyên lý Usability Heuristics của Nielsen Norman Group và các ràng buộc công thái học di động:

| # | Quyết định thiết kế (Design Decision) | Lựa chọn áp dụng | Lý do & Căn cứ lập luận (Persona / Heuristic / Ràng buộc) |
| :---: | :--- | :--- | :--- |
| **01** | **Vị trí thanh điều hướng chính** | Sử dụng thanh Bottom Navigation Bar 4 tabs cố định thay vì Navigation Drawer (Menu hamburger góc trên). | **Căn cứ Persona & Fitts's Law:** Sinh viên thường xuyên di chuyển giữa các giảng đường và cầm điện thoại bằng 1 tay (One-handed thumb zone). Đưa điều hướng xuống đáy giúp ngón cái tiếp cận tức thì mà không phải với tay lên góc trên màn hình. |
| **02** | **Cơ chế hiển thị mã nhận đồ tại quầy Kiosk** | Sử dụng kết hợp **Mã số lớn (#A-204)** và **Mã QR Code động** ngay trung tâm màn hình `SCR-07`. | **Căn cứ Heuristic #1 (Visibility of system status) & Persona:** Tiếng ồn và đám đông tại quầy căn tin khiến sinh viên khó nghe tiếng gọi loa. Mã số to và QR code giúp máy quét Kiosk nhận diện trong 1 giây, giảm ùn tắc quầy nhận. |
| **03** | **Cơ chế cập nhật giá khi thêm Topping** | Hiển thị tổng tiền động trực tiếp trên nút CTA ghim đáy ở màn hình `SCR-04` (ví dụ: "Thêm vào giỏ hàng • 45.000đ"). | **Căn cứ Heuristic #6 (Recognition rather than recall):** Người dùng không cần phải tự tính nhẩm giá gốc cộng thêm từng loại topping trong đầu. Mọi thao tác chọn checkbox đều lập tức phản hồi con số tổng lên nút bấm. |
| **04** | **Phục hồi khi thanh toán lỗi (Flow 3 Recovery)** | Giữ nguyên trạng thái giỏ hàng và cung cấp nút chuyển ngay sang "Thanh toán tiền mặt tại quầy" khi cổng thanh toán online bị timeout. | **Căn cứ Heuristic #9 (Help users recognize, diagnose, and recover from errors) & Heuristic #5 (Error prevention):** Tránh việc hủy toàn bộ đơn khiến người dùng phải chọn món lại từ đầu, gây ức chế và làm trễ giờ học. |
| **05** | **Tách Giỏ hàng thành màn hình độc lập (`SCR-05`)** | Dùng màn hình riêng thay vì Drawer trượt nửa màn hình, tức là màn hình chuẩn (Dedicated Screen) cho mobile. | **Căn cứ Ràng buộc Mobile Screen (360×800dp):** Trên màn hình di động nhỏ, không gian cho giỏ hàng cần chứa danh sách món, ô voucher, chọn giờ nhận và bảng tính tiền. Dùng màn hình đầy đủ giúp hiển thị thoáng đãng và đạt chuẩn touch target 48dp. |
| **06** | **Chức năng Đặt lại đơn cũ 1 chạm (Quick Reorder)** | Bổ sung nút "Đặt lại đơn này" ngay trên thẻ lịch sử `SCR-08`. | **Căn cứ Heuristic #7 (Flexibility and efficiency of use):** Sinh viên có thói quen ăn uống lặp lại theo tuần (ví dụ: thứ 3 luôn uống Trà đào). Tính năng này rút ngắn thời gian đặt món xuống chỉ còn 10 giây. |
| **07** | **Không truyền đạt thông tin chỉ bằng màu sắc** | Các trạng thái đơn hàng (Thành công, Đang làm, Báo lỗi) luôn đi kèm cả **Màu sắc + Biểu tượng Icon + Nhãn chữ rõ ràng**. | **Căn cứ WCAG 2.1 Success Criterion 1.4.1 (Use of Color):** Đảm bảo sinh viên bị mù màu (Color blindness) hoặc người dùng sử dụng máy dưới ánh sáng chói của sân trường vẫn nhận biết chính xác trạng thái đơn. |
| **08** | **Độ cao vùng chạm tương tác tối thiểu** | Thiết lập tất cả các Button, Checkbox, Icon tương tác có kích thước tối thiểu $48 \times 48\text{ dp}$. | **Căn cứ Material Design 3 Accessibility & WCAG 2.5.5:** Đảm bảo khi sinh viên vừa đi bộ vừa bấm không bị bấm trượt hoặc bấm nhầm sang phần tử lân cận. |

---

## 2. Kết quả kiểm chứng Accessibility & Responsive Checklist

Dưới đây là kết quả kiểm tra thực tế trên hệ thống Design Tokens và màn hình của BreakBite:

```mermaid
graph LR
    Checklist[Accessibility & Responsive Checklist] --> C1[1. Tỷ lệ tương phản chữ WCAG 2.1]
    Checklist --> C2[2. Vùng chạm cảm ứng Touch Target]
    Checklist --> C3[3. Cỡ chữ nội dung & Không dùng màu đơn độc]
    Checklist --> C4[4. Kiểm thử Auto Layout 360dp vs 412dp]
```

### 2.1 Bảng đo lường tỷ lệ tương phản màu sắc (Color Contrast - WCAG 2.1)

Tiêu chuẩn yêu cầu: Tối thiểu **4.5:1** đối với văn bản thường và **3:1** đối với văn bản lớn / nút điều khiển UI.

| Cặp màu kiểm tra (Text / Background) | Tỷ lệ tương phản (Contrast Ratio) | Đánh giá WCAG 2.1 | Kết quả thực tế |
| :--- | :---: | :---: | :---: |
| `color-text-primary` (`#622B14`) trên `color-background` (`#FFF5E5`) | **10,37 : 1** | AAA (yêu cầu 4,5:1) | ✅ ĐẠT |
| `color-text-primary` (`#622B14`) trên `color-surface` (`#FFFFFF`) | **11,2 : 1** | AAA (yêu cầu 4,5:1) | ✅ ĐẠT |
| `color-text-secondary` (`#8A5D48`) trên `color-background` (`#FFF5E5`) | **5,2 : 1** | AA (yêu cầu 4,5:1) | ✅ ĐẠT — bản cũ `#966A55` chỉ 4,33:1 ❌ |
| Chữ nút `color-on-primary` (`#622B14`) trên `color-primary` (`#F69D39`) | **5,23 : 1** | AA (yêu cầu 4,5:1) | ✅ ĐẠT — bản cũ chữ trắng chỉ 2,14:1 ❌ |
| Chữ nút `#622B14` trên `color-primary-pressed` (`#F8A94F`) | **5,75 : 1** | AA | ✅ ĐẠT |
| `color-primary-text` (`#B45309`) trên `color-background` (`#FFF5E5`) — giá, link, nút Outline | **4,65 : 1** | AA | ✅ ĐẠT — dùng `#F69D39` làm chữ chỉ 1,98:1 ❌ |
| `color-error` (`#B91C1C`) trên `color-background` (`#FFF5E5`) | **5,99 : 1** | AA | ✅ ĐẠT — bản cũ `#DC2626` chỉ 4,47:1 ❌ |
| `color-success` (`#15803D`) trên `color-surface` (`#FFFFFF`) | **5,02 : 1** | AA | ✅ ĐẠT — bản cũ `#16A34A` chỉ 3,3:1 ❌ |
| Viền ô nhập `color-border-input` (`#8A7A70`) trên `#FFF9F0` | **3,93 : 1** | Thành phần điều khiển (yêu cầu 3:1, WCAG 1.4.11) | ✅ ĐẠT — viền cũ `#EEDBCA` chỉ 1,34:1 ❌ |

> **Ghi chú:** Lần đo trước ghi chữ trắng trên `#F69D39` đạt 3,08:1 và coi chữ nút 14sp đậm là "chữ lớn". Cả hai đều sai: tỷ lệ thật là 2,14:1, và WCAG chỉ coi chữ ≥ 14pt (≈ 18,7px) đậm hoặc ≥ 18pt thường là chữ lớn. Các token đã được sửa ở `design/DESIGN.md` mục 2.5. **[TODO: cập nhật các token này trong Figma Variables và chụp lại màn hình làm minh chứng.]**

---

### 2.2 Kiểm tra vùng chạm tối thiểu (Touch Target: $\ge 48 \times 48\text{ dp}$)

* **Nút bấm chính (Buttons):** Chiều cao ghim đáy đạt $52\text{ dp}$ ($> 48\text{ dp}$), chiều rộng full container.
* **Bộ tăng giảm số lượng (+/-):** Nút tròn đường kính $36\text{ dp}$ nhưng được bọc trong vùng cảm ứng chạm (Touch target frame) có padding đạt $48 \times 48\text{ dp}$.
* **Icon buttons trên App bar:** Kích thước hiển thị $24\text{ dp}$, khung padding bao quanh $48 \times 48\text{ dp}$.
* **Checkbox & Radio buttons:** Chiều cao cả dòng chọn đạt $48\text{ dp}$, người dùng có thể chạm vào bất kỳ đâu trên cả dòng để kích hoạt.
* **Kết luận:** ✅ **100% phần tử tương tác đạt chuẩn $\ge 48 \times 48\text{ dp}$.**

---

### 2.3 Cỡ chữ nội dung & Nguyên tắc không dựa vào màu sắc đơn độc

* **Cỡ chữ nội dung (Body text):** Toàn bộ văn bản mô tả, nhãn trường nhập, giá tiền đều sử dụng cỡ chữ từ $14\text{ sp}$ trở lên (`type-body-medium` = 14sp, `type-body-large` = 15sp). Không có chữ nội dung nào nhỏ hơn 14sp.
* **Không dùng màu đơn độc (No color-only meaning):**
  * Trường nhập lỗi có cả viền đỏ + Biểu tượng dấu chấm than `(!)` + Dòng chữ lỗi *"Mã giảm giá không tồn tại hoặc đã hết hạn"*.
  * Trạng thái hoàn thành có cả màu xanh lá + Biểu tượng tích xanh `(✓)` + Nhãn chữ *"Đã chuẩn bị xong"*.
* **Kết luận:** ✅ Đạt sau khi sửa token màu chữ lỗi/thành công (xem bảng 2.1).

---

### 2.4 Kiểm tra kiểm thử bố cục trên màn hình 360 dp và 412 dp (Responsive Layout Check)

Toàn bộ màn hình được thiết kế bằng **Auto Layout với thuộc tính Fill Container (Horizontal)**:

1. **Tại độ rộng 360 dp (Chuẩn thiết kế gốc - ví dụ Samsung Galaxy A series):**
   * Lề hai bên (Horizontal padding): $16\text{ dp}$.
   * Vùng nội dung khả dụng: $360 - (16 \times 2) = 328\text{ dp}$.
   * Thẻ món ăn và nút CTA co dãn hoàn hảo, không bị tràn ngang, các nút không bị đè lên nhau.
2. **Tại độ rộng 412 dp (Màn hình lớn - ví dụ Google Pixel 7, Samsung S23 Ultra):**
   * Lề hai bên tự động giữ $16\text{ dp}$ hoặc mở rộng thành $20\text{ dp}$.
   * Vùng nội dung mở rộng: $412 - 32 = 380\text{ dp}$.
   * Các phần tử nội dung tự động dãn đều (Flex space), khoảng cách giữa ảnh món ăn và thông tin giá giữ tỷ lệ cân đối, tuyệt đối không bị vỡ layout hay xuất hiện thanh cuộn ngang ngoài ý muốn.
* **Kết luận:** ✅ **Bố cục co dãn linh hoạt, đáp ứng mượt mà trên cả 360dp và 412dp.**
