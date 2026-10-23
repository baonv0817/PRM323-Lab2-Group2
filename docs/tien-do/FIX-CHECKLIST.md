# Checklist sửa trước khi nộp

Các file tài liệu trong repo đã được sửa. Những việc dưới đây phải tự làm vì cần tài khoản Figma, Stitch và GitHub. Làm xong mục nào thì đánh dấu và commit.

## 1. GitHub
- [x] Tên repo: `PRM323-Lab2-Group2` (nhóm đặt; đề gốc gợi ý `prm323-lab2-<MSSV>`, hỏi lại giảng viên nếu cần).
- [x] Điền họ tên, MSSV các thành viên và mã lớp vào README.
- [ ] Repo này tạo lại với **một commit khởi tạo**; lịch sử commit cũ nằm ở repo `prm393-lab2` ngoài. Từ nay commit đều theo từng phase để có lịch sử làm việc.

## 2. Figma — đổi token màu (Page 04 Variables, Page 05 Components)
Giá trị mới lấy từ `design/DESIGN.md` mục 2.5.

| Biến | Đổi thành | Dùng ở |
|---|---|---|
| Chữ trên nút primary | `#622B14` (trước là trắng) | Button primary: mọi state; label và icon loading |
| `color-primary-pressed` | `#F8A94F` (trước là `#E0851F`) | Button/pressed |
| `color-primary-text` (mới) | `#B45309` | Nút Outline, giá tiền, link "Xem tất cả" |
| `color-text-secondary` | `#8A5D48` | Mô tả món, nhãn phụ |
| `color-border-input` (mới) | `#8A7A70` | Viền Text field, checkbox chưa chọn |
| `color-success` | `#15803D` | Badge/chữ thành công |
| `color-error` | `#B91C1C` | Viền và chữ lỗi, nút Huỷ |

- [ ] Sau khi đổi, kiểm tra Page 03 xem các màn hình có tự đổi màu theo không. Nếu không đổi thì component đang gán màu cứng, cần gán lại vào biến.

## 3. Figma — cho khớp với repo
- [ ] Thêm biến thể **Loading** (skeleton) cho S02, S03, S07; badge **quán đóng** ở S02; **lỗi mã giảm giá** ở S05 — D40 (Critical G4).
- [ ] Thẻ món: bỏ sao đánh giá; giá gạch chỉ khi khuyến mãi — D38.
- [ ] S06-ERR: lời giải thích 2 dòng, "Giỏ hàng của bạn vẫn được giữ" — D39.
- [ ] Prototype: màn loading không có hotspot; Back của S07 về S02 — D41.
- [ ] Sau khi sửa: chấm lại UI Checklist cho S02, S04, S05, S06 (mục tiêu ≥ 80) — D42.
- [ ] S02: dựng lại theo concept đã chọn (D33) — khối trạng thái quán ở đầu, banner nhỏ, thấy ≥ 3 món không cần cuộn.
- [ ] Ảnh món thật, tỉ lệ 1:1, fallback tên món khi lỗi (D14, D37).
- [x] Kiểm S02 ở 412 dp: `assets/figma/final-ui-v2/412/S02.png`.
- [ ] Thêm biến thể Card **"Tạm hết"** (thẻ mờ, nhãn, không bấm được) — D30.
- [ ] S07: thêm badge **"Đã thanh toán" / "Trả tại quầy"** cạnh mã nhận đồ — D31.
- [ ] S05: giờ nhận mặc định **"Lấy ngay"** — D28.
- [ ] S04 → "Thêm vào giỏ" nối thẳng tới S05 trong prototype — D29.
- [ ] **Page 01:** mã màn hình trong sơ đồ đang khác repo. Sửa lại: SCR-03 = Menu, SCR-04 = Chi tiết món, SCR-05 = Giỏ hàng, SCR-06 = Checkout, SCR-06-ERR = Lỗi thanh toán, SCR-07 = Theo dõi đơn, SCR-08 = Lịch sử.
- [ ] **Page 01:** đổi tên 3 flow theo `ux/user-flow.md`: F1 Đặt nhanh nhận tại quầy · F2 Tuỳ chỉnh món & voucher · F3 Lỗi thanh toán & phục hồi.
- [ ] **Page 01:** nối mỗi bước trong sơ đồ tới frame màn hình tương ứng.
- [ ] **Bottom nav:** tab thứ 4 trong Figma là "Cá nhân", nhưng repo coi tab 4 là SCR-08 Lịch sử. Đổi nhãn tab thành "Lịch sử".
- [ ] Đổi tên file "Untitled" thành `PRM323 Lab2 – BreakBite – <MSSV>`.
- [ ] Đặt 3 flow starting point ở Page 06 trùng tên F1/F2/F3, rồi bấm Present chạy thử từng flow.

## 4. Minh chứng phải chụp lại (không được dựng lại bằng tay)
- [ ] `assets/stitch/iteration{1,2,3}_{before,after}_*.png`: hiện đang trùng file với ảnh Stitch ban đầu. Mở lịch sử phiên bản trong Stitch và chụp đúng màn trước và sau mỗi prompt tinh chỉnh.
- [ ] `assets/figma/final-ui/*.png`: xuất lại từ Figma Page 03 (chọn frame → Export PNG 2x). Hiện S03, S04, S05-EMPTY, S06-ERR chỉ là ảnh chụp độ phân giải thấp (≈ 180 × 400).
- [x] Ảnh bố cục 412 dp: `assets/figma/final-ui-v2/412/` (chưa chèn vào slide 32).
- [ ] Dán nguyên văn câu trả lời AI critique vào `ai/ai-design-log.md` Phụ lục A.

## 5. Slide (`slides/BreakBite_Lab2_Presentation.pptx`, 42 trang)
Bộ slide hiện hành đã dựng theo bài mẫu và dùng ảnh Figma thật. Bản 12 trang và 37 trang cũ nằm ở `archive/slides-cu/`.
- [x] Họ tên, MSSV (slide 1); phần "Tồn tại" cập nhật ở slide 39.
- [ ] Slide 18–20: chụp lại ảnh Stitch trước/sau từ lịch sử phiên bản Stitch (đang là khung trống).
- [x] Slide 35: ảnh 412 dp đã chèn.
- [ ] Slide 8: thay biểu đồ khảo sát mô phỏng bằng số liệu thật khi có phản hồi thật (đang ghi rõ là dữ liệu mô phỏng).
