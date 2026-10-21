# Màn hình S09–S25

> FtaCode Mobile · Figma [PRM323](https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260), Page 03 (khung có hậu tố " v2" là bản Final UI)
> Ảnh bản cũ: `assets/figma/ext/` · Tổng quan: `assets/figma/final-ui-s09-s25/contact-sheet.png`

![S09–S25](../assets/figma/final-ui-s09-s25/contact-sheet.png)

Cùng S01–S08 ([`screen-spec.md`](screen-spec.md)), S09–S25 tạo thành bộ 25 màn của app, đủ vòng đời một đơn hàng. Wireframe nằm ở Page 02 (`ux/wireframe/`), user flow F4–F11 ở Page 01 (`ux/userflow/`).

## 1. Vì sao có các màn này

| Lỗ hổng | Màn | Căn cứ |
|---|---|---|
| Tab **Cá nhân** ở thanh dưới không dẫn tới màn nào | S15–S18 | Thanh điều hướng có 4 tab |
| Chỉ thấy đơn gần nhất; không xem lại theo tuần/tháng | S11, S12 | P02 nhạy cảm về chi tiêu (INS-04) |
| Huỷ đơn có dialog (D04) nhưng không có màn kết quả, không sửa được đơn | S09, S10 | D04: huỷ trong 60 giây |
| Lúc món xong, nhân viên quầy cần một màn nhận món rõ ràng | S19, S20 | Persona P03 cần trả món khoảng 30 giây |
| Quán đóng, món hết mới có badge (D30) | S21, S22 | INS-02: muốn biết trước trạng thái quán |
| Không có phản hồi sau khi nhận món, không có chỗ báo sự cố | S23, S24 | Flow 3 chỉ xử lý lỗi trước khi tạo đơn |
| Đặt hàng chưa gắn với giờ nghỉ 15 phút | S25 | HMW ở P0 |
| Đặt lại món hay mua phải đi qua thực đơn | S13, S14 | Giảm số chạm cho Flow 1 |

## 2. Sơ đồ điều hướng

Ảnh: `ux/userflow/IA-mo-rong.png`.

| Tab | Màn |
|---|---|
| **S02 Trang chủ** | S04 Chi tiết món, S05 Giỏ hàng, S06 Thanh toán (+ LOADING, ERR), S07 Theo dõi đơn, S14 Đặt lại nhanh, S19 Thông báo, S21 Quán đóng, S25 Hẹn giờ theo slot |
| **S03 Thực đơn** | S04 Chi tiết món, S22 Món hết |
| **S08 Đơn hàng** | S07 Theo dõi đơn, S11 Lịch sử, S12 Chi tiết đơn, S09 Sửa đơn, S10 Đơn đã huỷ, S20 Nhận món, S23 Đánh giá, S24 Báo sự cố |
| **S15 Cá nhân** | S16 Hồ sơ, S17 Thanh toán, S18 Cài đặt thông báo, S13 Món yêu thích |

## 3. Flow F4–F11

Mỗi flow trong Figma có dải **INPUT → OUTPUT** ở đầu.

| Flow | Input | Output | Đường đi |
|---|---|---|---|
| **F4 Sửa và huỷ đơn** | Muốn đổi giờ nhận, số lượng, ghi chú, hoặc huỷ khi bếp chưa làm (60 giây) | Đơn cập nhật, hoặc hoàn 54.000đ trong 30 giây | S07 → S09 → lưu → S07; S07 → dialog huỷ → S10 |
| **F5 Lịch sử và chi tiêu** | Muốn xem lại đã mua gì, tiêu bao nhiêu | Lịch sử theo tuần/tháng kèm tổng chi; đặt lại đơn cũ bằng một chạm | S08 → S11 → S12 → Đặt lại → S05 |
| **F6 Yêu thích và đặt lại** | Muốn đặt lại món hay mua | Món vào giỏ trong tối đa 3 chạm | S15 → S13 → + → S05; S02 → S14 → Thêm vào giỏ → S05 |
| **F7 Tài khoản** | Muốn chỉnh hồ sơ, cách trả tiền, thông báo mà không bị ép đăng nhập | Thiết lập được lưu; vẫn đặt món được khi không có tài khoản | S15 → S16 / S17 / S18 |
| **F8 Thông báo và nhận món** | Cần biết khi món xong và nhận món nhanh | Mã QR mở từ thông báo; nhận món tối đa 30 giây | S02 chuông → S19 → Xem mã → S20 → Tôi đã nhận món |
| **F9 Quán đóng và món hết** | Quán đóng hoặc món hết nhưng vẫn muốn có đồ ăn trong giờ nghỉ | Biết giờ mở, hẹn nhận hoặc chọn món thay thế | S02 (đóng) → S21; S03 → món hết → S22 |
| **F10 Sau khi nhận món** | Vừa nhận món, muốn đánh giá hoặc báo sự cố | Đánh giá một chạm; báo sự cố có mã tiếp nhận | S19 / S08 → S23; S12 → S24 |
| **F11 Đặt theo lịch học** | Giờ nghỉ chỉ 15 phút, cần món sẵn sàng đúng lúc | Giờ nhận gợi ý theo lịch học; đơn đi tiếp sang giỏ | S02 → S25 → chọn giờ → S05 |

## 4. Danh sách màn

| Mã | Màn | Nội dung chính | Trạng thái | Component |
|---|---|---|---|---|
| S09 | Sửa đơn | Đổi giờ nhận, số lượng, ghi chú; hạn sửa 10:12 | Có điều kiện (bếp chưa làm) | Button, TextField, Chip |
| S10 | Đơn đã huỷ | Hoàn 54.000đ về MoMo trong 30 giây | Thành công | Button |
| S11 | Lịch sử tuần/tháng | Tab lọc, tổng chi tháng, biểu đồ 7 cột, danh sách đơn | Mặc định | NavBar |
| S12 | Chi tiết đơn | Hoá đơn, ưu đãi, thanh toán; Đặt lại, Báo sự cố | Mặc định | Button |
| S13 | Món yêu thích | Lọc, số lần đã đặt, thêm vào giỏ một chạm | Mặc định | Card/Food, Chip, NavBar |
| S14 | Đặt lại nhanh | Bottom sheet chọn đơn gần đây | Overlay | Button |
| S15 | Cá nhân | Hồ sơ, số đơn, 5 mục cài đặt, xoá dữ liệu | Mặc định | NavBar |
| S16 | Hồ sơ sinh viên | Họ tên, MSSV, SĐT, nơi nhận mặc định; không bắt buộc | Trống / đã điền | TextField, Button |
| S17 | Phương thức thanh toán | 4 cách trả, chọn mặc định | Đã chọn | Button |
| S18 | Cài đặt thông báo | 4 công tắc, nhắc trước giờ nghỉ | Bật / tắt | — |
| S19 | Thông báo | Hôm nay / trước đó, chấm chưa đọc, nút Xem mã | Chưa đọc / đã đọc | Button/Secondary |
| S20 | Nhận món (QR) | Mã #A-204, QR lớn, giữ món đến 10:30 | Sẵn sàng | Button |
| S21 | Quán đóng | Trạng thái đóng cửa, hẹn nhận khi mở lại, nhắc, xem trước thực đơn | Đóng | Card/Food, Button, NavBar |
| S22 | Món hết | Tạm hết kèm giờ có lại; hai món thay thế còn hàng | Hết hàng | Card/Food |
| S23 | Đánh giá | Thang 1–5, thẻ lý do, ghi chú | Đã chọn | Chip, TextField, Button |
| S24 | Báo sự cố | Lý do, mô tả, ảnh tuỳ chọn, hoàn tiền trong 24 giờ | Mặc định | Chip, TextField, Button |
| S25 | Hẹn giờ theo slot | Lịch học, giờ nghỉ 15 phút, gợi ý giờ nhận | Mặc định | Chip, Button |

## 5. Quyết định thiết kế

- **S16 không bắt buộc đăng nhập** (D12): xem menu và đặt món không cần tài khoản.
- **Không có điểm tích luỹ hay thẻ thành viên** (D12, Reject).
- **S09 chỉ cho sửa giờ, số lượng, ghi chú**, không đổi món, vì bếp bắt đầu làm là phải cố định (D04).
- **S25 cần người dùng tự nhập lịch học**, vì app không có dữ liệu thời khoá biểu của trường.
- **S02 và S21 có chuông thông báo** dẫn tới S19.
