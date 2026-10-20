# Checklist sửa Figma — theo từng page và frame

> File: [FtaCode Figma — PRM323](https://www.figma.com/design/VnryhnE4z3159vHoKvx6jL/PRM323?node-id=1-6) (bản clone, có quyền sửa).
> Rà lần đầu 20/10/2026 ở chế độ xem; **sửa qua Figma MCP cùng ngày**. ☑ = đã sửa trong Figma, ☐ = còn phải làm tay.
> Mã quyết định (Dxx) tra ở `ai/ai-design-log.md`.

## 0. Hiện trạng sau khi sửa

| Page | Trạng thái |
|---|---|
| 01 User Flow | Mã màn S01–S08; voucher chuyển sang Flow 2; bỏ mã lỗi kỹ thuật |
| 02 Wireframe | Đổi tên theo mã S; vẫn 4/8 màn |
| 03 Final UI | 8 màn + 7 biến thể; chữ nút nâu; màu gắn Variables |
| 04 Design System | Màu đúng style guide; hết bị cắt nội dung |
| 05 Components | Thêm 5 Component Set có Variant (bảng cũ giữ làm tham khảo) |
| 06 Prototype | 40 liên kết, 3 điểm bắt đầu flow, loading tự chuyển, dialog dạng overlay |

Thứ tự page đã sắp lại: 01 → 02 → 03 → 04 → 05 → 06.

**Lưu ý:** các màn ở Page 03/06 là **vector và group phẳng** (import từ HTML), không phải auto-layout. Vì vậy những việc cần kéo lại bố cục (cỡ chữ, nút −/+, màn 412 dp, thay bằng instance) phải làm tay.

## 1. Việc trên toàn file

- [x] **Chữ trên nút cam → `#622B14`** (D06). 23 chỗ ở Page 03, 23 ở Page 06, 7 ở Page 05, 4 ở Page 04.
- [x] **Chữ cam trên nền kem → `#B45309`** (primary-text, 4,65:1). Áp cho giá, "Dự kiến sẵn sàng", "Chỉ đường"… (30 chỗ Page 03, 31 chỗ Page 06).
- [x] **Gắn màu vào Variables** thay vì mã hex: khoảng 430 paint ở Page 03, tương tự ở Page 06 và 05.
- [x] **Mã màn thống nhất** S01–S08 trên Page 01, 02, 03, 06.
- [x] **Bỏ sao đánh giá** trên thẻ món S03 (D38).
- [ ] **Chữ nội dung ≥ 14 sp** (D15). Hiện còn khoảng 150 text cỡ 9–13 sp. Tăng cỡ sẽ đè bố cục vì màn là vector phẳng → làm tay, ưu tiên mô tả món và dòng phụ ở S02–S05.
- [ ] **Ảnh món 1:1** (D14, D37): vẫn là emoji.

## 2. Page 01 · User Flow

- [x] Đổi toàn bộ "SCR-xx" sang S01–S08 (13 nhãn).
- [x] Flow 1 bỏ bước voucher, thay bằng "Giờ nhận: Lấy ngay" (D28).
- [x] Flow 2 đổi tên "Customization & Voucher"; node cuối là "Nhập mã giảm giá · S05 · Mã sai → báo lỗi, nhập lại".
- [x] Flow 3 bỏ "Mã lỗi: #PAY_402", thay bằng "Mạng yếu / hết thời gian".
- [x] **Mọi flow (3 flow lõi + F4–F11) có dải INPUT → OUTPUT**: Input là người dùng cần gì, Output là nhận được gì. Ảnh flow lõi: `ux/userflow/flows-core-io.png`.
- [x] Thêm sơ đồ Flow 4–F11 (Phase 2) dưới 3 flow bắt buộc, cùng kiểu nút/mũi tên; có nhánh lỗi. Ảnh: `ux/userflow/flows-F4-F7.png`, `flows-F8-F11.png`.

## 3. Page 02 · Wireframe

- [x] Đổi tên 4 khung: S01, S02, S04, S06-ERR.
- [x] Đã thêm wireframe xám cho S03, S05, S06, S07, S08, các biến thể (S05-EMPTY, S05-VOUCHER-ERR, S06-LOADING, S07-DIALOG, S07-CASH, S08-EMPTY) và 17 màn Phase 2 (S09–S25). Nằm dưới khung wireframe cũ trên Page 02; mỗi khung có chú thích "CTA chính". Ảnh tổng quan: `ux/wireframe/wireframes-1.png`, `wireframes-2.png`.
- [ ] S02 wireframe: thêm khối trạng thái quán (D33).

## 4. Page 03 · Final UI — từng frame

| Frame | Đã sửa | Còn làm tay |
|---|---|---|
| S01 Onboarding | Chữ nút nâu | — |
| S02 Trang chủ | Chữ nút, giá → `#B45309`, nút "+" chữ nâu | Thu nhỏ banner để thấy ≥ 3 món (D33) — header đã có "Sẵn sàng (5–7 phút)" |
| S03 Thực đơn | Bỏ sao; thẻ Trà Đào thành **Tạm hết** (mờ, nhãn đỏ, ẩn nút +) | — |
| S04 Chi tiết món | Chữ CTA nâu | Nút −/+ lên 48 dp (D13) |
| S05 Giỏ hàng | Chữ CTA nâu | Nút −/+ 48 dp; mặc định "Lấy ngay" (D28) |
| S06 Thanh toán | Chữ CTA nâu | — |
| S07 Theo dõi đơn | Chữ, giá đổi màu | Ẩn nút Huỷ sau 60 giây — cần thêm 1 biến thể (D04) |
| S08 Lịch sử | — | — |
| S06-ERR | Màu đúng token | Rút lời giải thích còn 2 dòng (D39) |

**Biến thể mới (hàng cuối Page 03 và 06):**
- [x] `S05-VOUCHER-ERR` — mã FTASV20 hết hạn, viền và chữ đỏ, tổng tiền không giảm.
- [x] `S06-LOADING` — lớp phủ mờ + spinner "Đang kết nối cổng MoMo…", "Giỏ hàng của bạn vẫn được giữ".
- [x] `S07-CASH` — badge "Trả tại quầy", dòng "💵 Trả tại quầy khi nhận: 54.000đ" (D31).
- [x] `S08-EMPTY` — "Chưa có đơn nào" + nút "Xem thực đơn".
- [x] Đổi tên `Dialog` → `S07-DIALOG · Xác nhận huỷ đơn`.

**Responsive:**
- [ ] Dựng S02, S04, S05 ở 412 × 915. Cần dựng lại bằng auto-layout (màn hiện tại không co giãn).
- [ ] Thử tên món 2 dòng, giá 6 chữ số.

## 5. Page 04 · Design System

| Token | Trước | Sau |
|---|---|---|
| text-secondary | `#966A55` | ☑ `#8A5D48` |
| success | `#16A34A` | ☑ `#15803D` |
| error | `#DC2626` | ☑ `#B91C1C` |
| primary-dark | `#E0851F` | ☑ đổi tên `primary-pressed` = `#F8A94F` |
| on-primary · primary-text · border-input | thiếu | ☑ `#622B14` · `#B45309` · `#8A7A70` |
| spacing/xs…2xl, radius/sm…xl | thiếu | ☑ 10 biến số |

- [x] Scope của biến: màu chữ chỉ hiện ở Text fill, viền ở Stroke, spacing ở Gap, radius ở Corner radius.
- [x] Nhãn hex trên bảng màu đã sửa; "Nunito/Inter" → "Nunito".
- [x] Khung "Spacing & Typography Specs" hết bị cắt.
- [ ] File có 2 bộ biến trùng nhau: `FtaCode Tokens` (cũ) và `FtaCode Design Tokens` (đang dùng). Xoá bộ cũ trong Local variables.

## 6. Page 05 · Components

Thêm khung **"Components · Variants"** ngay dưới bảng cũ. Mọi màu, padding, radius đều gắn Variables.

| Component Set | Variant | Thuộc tính |
|---|---|---|
| `Button/Primary` | State = Default · Pressed · Disabled · Loading | Label (text) |
| `TextField` | State = Default · Focused · Filled · Error · Disabled | Value (text) |
| `Card/Food` | State = Default · OutOfStock | Name, Price (text); nút + 48 dp |
| `NavBar` | Selected = Home · Menu · Orders · Profile | — |
| `Dialog` | Type = Confirm · Destructive | Title, Body (text) |

- [ ] Thay nút, thẻ món, nav bar trên Page 03 bằng **instance** của các component này. Làm dần từng màn: xoá group cũ → kéo instance từ Assets → đặt lại vị trí.

## 7. Page 06 · Prototype

- [x] 3 điểm bắt đầu: **Flow 1** S01, **Flow 2** S03, **Flow 3** S06.
- [x] Bỏ liên kết "bấm đâu cũng chuyển" trên 12 frame (dễ bấm nhầm khi demo).
- [x] S06 "Thanh toán MoMo" → **S06-LOADING** → tự chuyển S07 sau 1,2 giây.
- [x] S06-ERR "Thử lại / Tiền mặt" → **S07-CASH**.
- [x] S07 và S07-CASH: nút Huỷ mở **S07-DIALOG dạng overlay**; "Giữ đơn" → đóng overlay.
- [x] S05: bấm ô mã giảm giá → S05-VOUCHER-ERR; bấm lại → S05 (mã đúng).
- [x] S08-EMPTY: "Xem thực đơn" → S03.
- [ ] Trong panel Prototype của S07-DIALOG, chọn **Overlay → Center, Close when clicking outside** (plugin không đặt được thuộc tính này).
- [ ] Chạy **Present** cả 3 flow, quay màn hình làm minh chứng.
- [ ] Share → **Anyone with the link can view**.

## 7b. Màn mở rộng Phase 2

- 17 màn S09–S25 và sơ đồ IA mở rộng nằm ở **cuối Page 03** (gói Figma Starter chỉ cho 3 page nên không tạo được page 07). Chi tiết: `design/extended-screens.md`.
- [ ] Nối prototype cho S09–S25; thêm chuông thông báo vào app bar S02.

## 8. Sau khi làm xong phần còn lại

- [ ] Export PNG các màn (2×) vào `assets/figma/final-ui/` (ghi đè ảnh 1× hiện có).
- [ ] Chấm lại UI Simplicity Checklist trên Figma (mục tiêu màn chính ≥ 80, D42).
