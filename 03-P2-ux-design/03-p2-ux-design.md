# P2 · UX Design & Interaction Architecture

> BreakBite · PRM323 Lab 2 · Gate G2 · Ngày lập: 20/10/2026
> Persona chi tiết: `03-P2-ux-design/01-persona.md` · IA và flow: `03-P2-ux-design/04-user-flow.md` · Ma trận: `03-P2-ux-design/02-persona-mapping.xlsx`

## 1. Persona và mức ưu tiên

| | P01 Quân | P02 Linh | P03 Cô Hạnh |
|---|---|---|---|
| Ưu tiên | **Primary** | Secondary | Supporting |
| Khác biệt hành vi | Bỏ mua khi thấy hàng dài; cầm máy một tay | Bỏ app nếu có phí ẩn | Gọi số, kiểm chuyển khoản bằng tay |
| Ràng buộc | 15 phút nghỉ | ~40.000đ/ngày | Đông khách, tay bận |
| JTBD | Khi chỉ có 15 phút giữa hai slot, tôi muốn đặt trước và ghé quầy lấy ngay, để ăn kịp mà không xếp hàng | Khi đói giữa buổi sáng, tôi muốn biết món nào vừa túi tiền, để không bất ngờ khi trả | Khi nhiều sinh viên tới cùng lúc, tôi muốn biết đơn nào đã trả và tới giờ lấy, để trả nhanh không nhầm |
| Nguồn | SIM-A1, A5 | SIM-A2 | Assumed |
| Nhãn | Assumed | Assumed | Assumed |

## 2. Problem-to-Requirement Matrix

| Insight | Need | Yêu cầu chức năng | Story | Flow | Màn |
|---|---|---|---|---|---|
| INS-01 Hàng chờ giờ nghỉ | N1 Có đồ ăn mà không xếp hàng | Đặt và trả tiền trước; chọn giờ nhận | US01, US02 | F1 | S04–S06 |
| INS-02 Cần biết trước | N2 Biết quán mở/đóng, thời gian chờ | Badge trạng thái quán + thời gian ước tính; trạng thái "Tạm hết" | US03, US04 | F1, F2 | S02, S03 |
| Thao tác một tay | N3 Dùng được khi đi bộ | CTA nửa dưới, vùng chạm ≥ 48 dp | US05 | Tất cả | Tất cả |
| INS-06 Lỗi thanh toán | N4 Không mất đơn khi mạng yếu | Giữ giỏ; Thử lại / Trả tiền mặt | US06 | F3 | S06-ERR |
| INS-05 Không muốn đăng ký | N6 Bắt đầu không cần tài khoản | Xem menu, đặt món không đăng nhập | US07 | F1 | S01, S02 |
| INS-04 Ngại phí ẩn | N7 Biết tổng tiền trước khi trả | Giá topping cộng dồn; tổng ở giỏ; không phí giao | US08 | F1, F2 | S04, S05 |
| INS-04 | N8 Hiểu vì sao mã giảm giá lỗi | Báo lỗi có icon + lý do | US09 | F2 | S05 |
| P03 | N9 Đối chiếu đơn vài giây | Mã nhận đồ lớn + QR + badge thanh toán | US10 | F1 | S07 |
| P03 · H7 | N10 Không bị huỷ khi món đã nấu | Chỉ huỷ trong 60 giây | US11 | — | S07 |
| P01 | N1 | Đặt lại đơn cũ 1 chạm | US12 | F1 | S08 |

## 3. User Stories

**M** Must · **S** Should · **C** Could

| ID | Là… | Tôi muốn… | Để… | Ưu tiên | Tiêu chí chấp nhận |
|---|---|---|---|---|---|
| US01 | P01 | đặt và trả tiền trước khi xuống quầy | không phải xếp hàng | M | Từ S02 tới mã nhận đồ ở S07 trong ≤ 8 chạm |
| US02 | P01 | chọn "Lấy ngay" hoặc hẹn giờ nhận | món xong đúng lúc tôi tới | M | Mặc định "Lấy ngay (~7 phút)"; đổi giờ ≤ 2 chạm |
| US03 | P01 | thấy quán mở hay tạm dừng nhận đơn | không chọn món rồi mới biết không đặt được | M | Badge icon + chữ ở S02; quán đóng thì tắt nút đặt, có lý do |
| US04 | P01 | thấy món nào "Tạm hết" | không chọn món không có | S | Thẻ mờ, nhãn "Tạm hết", không bấm thêm được |
| US05 | P01 | bấm mọi nút chính bằng ngón cái | thao tác khi đi bộ | M | CTA ở nửa dưới; vùng chạm ≥ 48 × 48 dp |
| US06 | P01 | giữ giỏ hàng khi thanh toán lỗi | không phải chọn lại | M | S06-ERR giữ giỏ; có "Thử lại thanh toán" và "Trả tiền mặt tại quầy" |
| US07 | P01 | xem menu không cần tài khoản | bắt đầu nhanh | M | Không có màn đăng nhập trước S02 |
| US08 | P02 | thấy giá cộng dồn và tổng tiền ở giỏ | biết chính xác số tiền | M | Giá trên CTA ở S04 cập nhật ngay; S05 hiện tổng trước bước chọn phương thức |
| US09 | P02 | biết vì sao mã giảm giá không dùng được | sửa hoặc bỏ mã | S | Lỗi có icon + câu lý do cụ thể |
| US10 | P03 | đọc nhanh mã nhận đồ và trạng thái trả tiền | trả đúng món | S | S07 có mã lớn + QR + badge "Đã thanh toán / Trả tại quầy" |
| US11 | P03 | khách chỉ huỷ được trong 60 giây đầu | không lỗ món đã nấu | S | Sau 60 giây ẩn nút Huỷ; trước đó có dialog xác nhận |
| US12 | P01 | đặt lại đơn cũ từ lịch sử | đặt món quen nhanh | C | S08 → "Đặt lại" đưa đủ món vào S05; món đã hết được bỏ qua kèm thông báo |

## 4. Hành trình tương lai — P01 với BreakBite

| Giai đoạn | Cuối slot | Mở app | Chọn món | Thanh toán | Chờ món | Lấy món |
|---|---|---|---|---|---|---|
| Hành động | Mở app | Xem badge quán, thời gian (S02) | Combo + topping, giá tự cộng (S04) | Giỏ → Lấy ngay → Tiền mặt / QR → Xác nhận (S05, S06) | Theo dõi tiến trình (S07) | Đưa mã #A-204 |
| Nỗi đau đã gỡ | Không biết trước | Đi rồi mới biết đóng | Phí bất ngờ | Chờ kiểm chuyển khoản | Không biết bao lâu | Xếp hàng |
| Rủi ro còn lại | — | Mạng yếu | Món hết (US04) | Cổng lỗi (F3) | Bếp quá tải (H7) | Khách không tới lấy (H8) |

## 5. Độ phủ màn hình

| Màn | F1 | F2 | F3 |
|---|:---:|:---:|:---:|
| S01 Onboarding | ● (lần đầu) | | |
| S02 Trang chủ | ● | | |
| S03 Thực đơn | | ● | |
| S04 Chi tiết món | ● | ● | |
| S05 Giỏ hàng | ● | ● | ● |
| S06 Thanh toán (+ S06-ERR) | ● | ● | ● |
| S07 Theo dõi đơn | ● | ● | ● |
| S08 Lịch sử | ● (đặt lại) | | |

Mọi màn thuộc ít nhất một flow.

## 6. Trạng thái biên

| Màn | Empty | Loading | Error | Điều kiện |
|---|---|---|---|---|
| S02 | Chưa có gợi ý → hiện danh mục | Skeleton | Mất mạng → Thử lại | Quán đóng → badge, tắt nút đặt |
| S03 | Không tìm thấy → gợi ý xoá lọc | Skeleton | Mất mạng → Thử lại | Món "Tạm hết" |
| S04 | — | Skeleton ảnh | Ảnh lỗi → hiện tên món | Món vừa hết → tắt nút thêm |
| S05 | Giỏ trống → "Xem thực đơn" | Đang áp mã | Mã sai → icon + lý do | Món trong giỏ hết → đánh dấu, cho xoá |
| S06 | — | Đang kết nối cổng | Timeout → S06-ERR | QR hết hạn → tạo mã mới |
| S07 | — | Đang gửi đơn | Mất kết nối → giữ trạng thái cuối, Thử lại | Quá 60 giây → ẩn Huỷ |
| S08 | Chưa có đơn → "Đặt món đầu tiên" | Skeleton | Mất mạng → Thử lại | Đặt lại có món hết → bỏ qua, thông báo |

## 7. Walkthrough

Cognitive walkthrough do AI (Claude Opus 5.5) thực hiện trên tài liệu flow, chưa phải người dùng thử.

| Flow | Bước | Vấn đề | Mức |
|---|---|---|---|
| F1 | S06 → "Xác nhận" → dialog "Đồng ý" | Xác nhận hai lần | Vừa |
| F1 | S04 → "Thêm vào giỏ" | Hành vi chưa chốt (tới S05 hay về menu) | Vừa |
| F1 | S01 lần đầu | Chỉ số "≤ 8 chạm" chưa nói rõ đối tượng | Thấp |
| F1 (S08) | "Đặt lại" khi món đã hết | Chưa có trạng thái | Cao |
| F3 | Chọn trả tiền mặt | Đơn chưa trả mà bếp vẫn nấu | Vừa |
| F1 | S07 → Back | Về S02, không quay lại S06 | Đạt |
| F2 | Mã sai → nhập lại | Có icon + lý do, giữ giỏ | Đạt |

**Đi thử trên Figma Page 02:**

| Flow | Người thử | Hoàn thành | Số chạm | Vướng ở đâu |
|---|---|---|---|---|
| F1 | | | | |
| F2 | | | | |
| F3 | | | | |

## 8. AI phản biện và quyết định

Claude Opus 5.5, 20/10/2026. Nguyên văn: `08-ai-log/01-ai-design-log.md` Phụ lục E.

| Phát hiện | Quyết định |
|---|---|
| Xác nhận hai lần ở bước thanh toán | **D28 Modify:** giữ dialog (đơn chỉ huỷ được trong 60 giây); giờ nhận mặc định "Lấy ngay" → F1 tối thiểu 7 chạm |
| Hành vi sau "Thêm vào giỏ" chưa chốt | **D29 Accept:** chuyển thẳng tới S05 + snackbar "Thêm món khác" |
| Thiếu trạng thái món hết hàng | **D30 Accept:** thêm US04, Card "Tạm hết" |
| Đơn tiền mặt có thể bị bỏ | **D31 Modify:** giữ tiền mặt; badge "Trả tại quầy" ở S07; thêm giả định H8 |
| Chỉ số thành công chưa rõ đối tượng | **D32 Accept:** áp dụng cho người đã dùng app; S01 có Bỏ qua |

## 9. Gate G2

| Điều kiện | Kết quả |
|---|:---:|
| **[C]** Persona/JTBD khác nhau về hành vi và truy về bằng chứng | ✅ (nguồn mô phỏng, nhãn Assumed) |
| **[C]** Flow ưu tiên rõ bắt đầu, kết thúc, trường hợp lỗi | ✅ |
| **[C]** Có IA và wireframe low-fi cho flow MVP | ✅ (Figma Page 02) |
| Quyết định chức năng nối Insight → Need → User Story | ✅ |
| Có walkthrough và danh sách điểm cần sửa | ⚠️ Walkthrough do AI; chưa đi thử trên Figma |
| Đã xét empty / loading / error / điều kiện | ✅ |

**5/6, đủ Critical.**
