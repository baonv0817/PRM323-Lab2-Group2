# Bố cục từng bảng trong quy trình

Mỗi bảng ghi: **dùng ở bước nào** (theo `02-QUY-TRINH-DE-HIEU.md`), **đặt ở file nào**, **các cột**, và **1 dòng ví dụ** của BreakBite. Copy bảng trống về dùng.

Mã định danh theo chuẩn của môn: **E** bằng chứng · **P** persona · **N** nhu cầu · **F** flow · **S** màn hình · **I** vòng lặp AI · **D** quyết định · **T** test.

| # | Bảng | Bước | File |
|---|---|---|---|
| 1 | Danh sách giả định | 9 | `02-P1-nghien-cuu/02-research.md` |
| 2 | Người liên quan | 10 | `02-P1-nghien-cuu/02-research.md` |
| 3 | Ghi chép phỏng vấn | 14 | `02-P1-nghien-cuu/02-research.md` |
| 4 | Phân tích đối thủ | 16 | `02-P1-nghien-cuu/02-research.md` |
| 5 | Gom ý (affinity) | 17–18 | `02-P1-nghien-cuu/02-research.md` |
| 6 | Persona 12 mục | 21 | `03-P2-ux-design/01-persona.md` |
| 7 | Ai cần gì (coverage) | 23 | `03-P2-ux-design/02-persona-mapping.xlsx` |
| 8 | Bảng truy vết | 23 → 43 | `03-P2-ux-design/02-persona-mapping.xlsx` |
| 9 | User story | 24 | `03-P2-ux-design/04-user-flow.md` |
| 10 | Danh sách màn hình (IA) | 25 | `03-P2-ux-design/04-user-flow.md` |
| 11 | Luồng → màn hình | 27 | `03-P2-ux-design/04-user-flow.md` |
| 12 | Vòng lặp AI | 33–34 | `08-ai-log/01-ai-design-log.md` |
| 13 | Phát hiện của AI | 35 | `08-ai-log/01-ai-design-log.md` |
| 14 | Quyết định | 36 | `08-ai-log/01-ai-design-log.md` |
| 15 | Kiểm accessibility | 42 | `05-P4-ui-design/05-design-decisions.md` |
| 16 | Chấm UI checklist | 42 | `05-P4-ui-design/05-design-decisions.md` |
| 17 | Thử với người dùng | 43 | `02-P1-nghien-cuu/02-research.md` |
| 18 | Danh sách lỗi | 43 | `02-P1-nghien-cuu/02-research.md` |
| 19 | Token → Flutter | 44 | `06-P5-kiem-thu-ban-giao/03-flutter-handoff.md` |
| 20 | Component → Widget | 44 | `06-P5-kiem-thu-ban-giao/03-flutter-handoff.md` |

---

## Chặng 1 — Xác định vấn đề

### 1. Danh sách giả định (bước 9)
| ID | Nội dung | Loại | Nếu sai thì sao | Kiểm bằng cách nào | Ưu tiên |
|---|---|---|---|---|---|
| H1 | Giờ nghỉ giữa slot ≤ 15 phút | Đoán | "Đặt trước" ít giá trị | Khảo sát Google Form (Q5) | Cao |

Cột **Loại**: *Biết chắc* (Fact) · *Đoán* (Hypothesis) · *Chưa biết* (Unknown).

### 2. Người liên quan (bước 10)
| Nhóm | Ai | Liên quan thế nào | Trong phạm vi? |
|---|---|---|---|
| Dùng trực tiếp | SV ở KTX | Đặt món, nhận món | Có |
| Hỗ trợ | Nhân viên quầy | Nhận đơn, trả món | Một phần |
| Ngoài phạm vi | Cổng thanh toán | Xử lý tiền | Không |

---

## Chặng 2 — Hỏi người dùng thật

### 3. Ghi chép phỏng vấn (bước 14)
| Mã | Người (ẩn danh) | Ngày | Câu hỏi | Trả lời (gần nguyên văn) | Nhãn |
|---|---|---|---|---|---|
| E01 | SV năm 2, ở KTX | 18/10 | Lần gần nhất mua ở căn tin chờ bao lâu? | "Khoảng 10 phút, vào lớp trễ" | Reported |

### 4. Phân tích đối thủ (bước 16)
| Tiêu chí | Đối thủ A | Đối thủ B | Cách hiện tại | App của mình |
|---|---|---|---|---|
| Cách nhận món | Giao tận nơi | Giao tận nơi | Xếp hàng | Nhận tại quầy |
| Phí | Phí giao + dịch vụ | … | Không | Không phí giao |
| Điểm yếu với persona | Không vào được tòa nhà | … | Mất thời gian | — |

### 5. Gom ý — affinity (bước 17–18)
| Nhóm ý | Ý cụ thể | Nguồn | Số người nhắc | Nhãn | Kết luận |
|---|---|---|---|---|---|
| Thời gian | Hàng chờ làm bỏ bữa | E01, E03, E05 | 3/6 | Reported | Pain point chính |

---

## Chặng 3 — Persona, luồng, khung xám

### 6. Persona 12 mục (bước 21)
Mỗi persona một bảng:

| # | Mục | Nội dung | Nhãn & nguồn |
|---|---|---|---|
| 1 | Là ai | 20 tuổi, SV năm 2, ở KTX | Reported — E01 |
| 2 | Mức ưu tiên | Primary | Inferred |
| 3 | Dùng app ở đâu, lúc nào | Đi bộ giữa 2 tòa, một tay | Reported — E01, E03 |
| 4 | Mục tiêu | Ăn kịp giờ nghỉ | |
| 5 | Khi…, tôi muốn…, để… | Khi chỉ có 15 phút, tôi muốn đặt trước, để ăn kịp | |
| 6 | Hiện đang làm thế nào | Thấy hàng dài thì bỏ | |
| 7 | Khó chịu ở đâu | Hàng chờ, không biết quán mở hay đóng | |
| 8 | Động lực | Tiết kiệm thời gian | |
| 9 | Bị giới hạn bởi gì | 15 phút, một tay, mạng yếu | |
| 10 | Tình huống cụ thể | Cuối slot đặt combo, hẹn giờ, xuống lấy | |
| 11 | Đo thành công | Đặt xong < 35 giây | |
| 12 | Nguồn & trạng thái | Từ E01–E06; đã kiểm chứng một phần | |

Thêm 4 dòng bắt buộc của Lab 2: **tuổi · vai trò · thiết bị · accessibility**.

### 7. Ai cần gì — coverage matrix (bước 23, làm xong ngay)
| ID | Nhu cầu | P01 Quân | P02 Linh | P03 Cô Hạnh |
|---|---|:---:|:---:|:---:|
| N1 | Đặt nhanh trong giờ nghỉ | ● | ○ | |
| N7 | Biết tổng tiền sớm | ○ | ● | |
| N9 | Mã nhận đồ dễ đối chiếu | ● | | ● |

● cần nhiều · ○ cần ít · trống: không cần.

### 8. Bảng truy vết (bắt đầu bước 23, điền dần tới bước 43)
| Persona | Nhu cầu | Nguyên tắc | Quyết định UI | Màn hình | Kiểm chứng bằng | Kết quả |
|---|---|---|---|---|---|---|
| P01 | N4 Không mất đơn khi mạng yếu | DP5 Không mất công sức khi lỗi | Màn lỗi giữ giỏ, cho trả tiền mặt | S06-ERR | Chạy F3 trên prototype | Đạt |

| Cột | Điền ở bước |
|---|---|
| Persona, Nhu cầu | 23 |
| Màn hình | 27 |
| Nguyên tắc, Quyết định UI | 36 |
| Kiểm chứng bằng, Kết quả | 43 |

### 9. User story (bước 24)
| ID | Là… | Tôi muốn… | Để… | Nhu cầu | Ưu tiên |
|---|---|---|---|---|---|
| US01 | SV có 15 phút nghỉ | hẹn giờ nhận món | lấy ngay khi xuống quầy | N1 | Cao |

### 10. Danh sách màn hình — IA (bước 25)
| ID | Màn hình | Cấp | Để làm gì | Đi tới |
|---|---|---|---|---|
| S02 | Home | Cấp cao (tab 1) | Xem nhanh, trạng thái quán | S03, S04, S05 |
| S04 | Chi tiết món | Màn con | Chọn topping, số lượng | S05 |

Dialog và trạng thái (loading, empty, error) **không** tính là màn riêng.

### 11. Luồng → màn hình (bước 27)
| Flow | Bắt đầu → Kết thúc | Màn hình dùng | Nhánh thay thế / lỗi |
|---|---|---|---|
| F1 Đặt nhanh | S02 → S07 | S02, S04, S05, S06, S07 | Dialog xác nhận → loading → mã nhận đồ |
| F3 Lỗi thanh toán | S06 → S07 | S05, S06, S06-ERR, S07 | Timeout → Thử lại / Tiền mặt |

Kiểm: **mọi màn ở bảng 10 đều phải xuất hiện ở bảng này.**

---

## Chặng 4 — Tạo UI bằng AI và phản biện

### 12. Vòng lặp AI (bước 33–34)
| ID | Vấn đề (có tên) | Màn | Prompt (nguyên văn) | Ảnh trước | Ảnh sau | Tự kiểm lại | Quyết định |
|---|---|---|---|---|---|---|---|
| I01 | Nút chính khó đọc | S04, S05 | "Fix low contrast…" | iteration1_before.png | iteration1_after.png | Đo: 2,14:1 → chưa đạt | D06 |

**Mỗi vòng một vấn đề khác nhau. Hai ảnh trước và sau phải khác nhau.**

### 13. Phát hiện của AI (bước 35, ≥ 5 dòng)
| ID | Màn | Tiêu chí | Mức độ | Vấn đề | AI đề xuất | Quyết định |
|---|---|---|---|---|---|---|
| C10 | S02 | Nielsen #6 | Cao | Ảnh món là ô trống | Dùng ảnh thật | D14 |

Cột **Tiêu chí** ghi heuristic Nielsen, mục WCAG, hoặc điểm nào trong persona.

### 14. Quyết định (bước 36)
| ID | Đề xuất | Màn | Loại | Lý do (persona / heuristic / ràng buộc) | Thay đổi trong Figma |
|---|---|---|---|---|---|
| D12 | Thêm đăng nhập để tích điểm | S02 | **Từ chối** | E01, E03 nói sẽ bỏ app nếu bắt đăng ký; mục tiêu < 35 giây | Không đổi |

Cột **Loại** chỉ có 3 giá trị: **Chấp nhận / Sửa lại / Từ chối**. Lý do "AI bảo vậy" hay "em thích" không được tính.

---

## Chặng 5 — Giao diện cuối

### 15. Kiểm accessibility (bước 42)
| Kiểm gì | Ngưỡng | Đo được | Đạt? | Bằng chứng |
|---|---|---|---|---|
| Chữ thường trên nền | ≥ 4,5:1 | 10,37:1 | ✅ | Ảnh WebAIM |
| Chữ trên nút | ≥ 4,5:1 | 5,23:1 | ✅ | |
| Viền ô nhập | ≥ 3:1 | 3,93:1 | ✅ | |
| Vùng chạm | ≥ 48 × 48 dp | 48 dp | ✅ | Ảnh đo trong Figma |
| Cỡ chữ nội dung | ≥ 14 sp | 14 sp | ✅ | |
| Không chỉ dùng màu | icon + chữ | | | Ảnh đen trắng |
| Màn 360 dp và 412 dp | không vỡ | | | Ảnh 2 độ rộng |

### 16. Chấm UI checklist (bước 42, mỗi màn chính một dòng)
| Màn | A Chữ (/20) | B Màu (/20) | C Mật độ (/20) | D Thứ bậc (/20) | E Nhất quán (/20) | Tổng (/100) | Test 5 giây | Test đen trắng | Ghi chú sửa |
|---|---|---|---|---|---|---|---|---|---|
| S02 Home | 15 | 20 | 15 | 20 | 15 | 85 | Đạt | Đạt | Chữ phụ nhỏ |

Mỗi nhóm có 4 tiêu chí, mỗi tiêu chí 5 điểm. Mục tiêu **≥ 80**.

---

## Chặng 6 — Thử, bàn giao

### 17. Thử với người dùng (bước 43)
| ID | Người | Việc giao | Làm được? | Thời gian | Số chạm | Vướng ở đâu |
|---|---|---|---|---|---|---|
| T01 | U1 (SV năm 2) | Đặt 1 combo, hẹn giờ nhận | Có | 41 giây | 9 | Tìm nút chọn giờ |

So với chỉ số thành công (< 35 giây, ≤ 8 chạm).

### 18. Danh sách lỗi (bước 43)
| ID | Lỗi | Màn | Mức | Từ test | Cách sửa | Đã test lại? |
|---|---|---|---|---|---|---|
| B01 | Ô chọn giờ nằm dưới cùng, khó thấy | S05 | P1 major | T01, T03 | Đưa lên ngay dưới danh sách món | Có, đạt |

Mức: **P0 blocker** (không làm được việc) · **P1 major** (làm được nhưng rất khó) · **P2 minor**.

### 19. Token → Flutter (bước 44)
| Loại | Token | Giá trị | Flutter |
|---|---|---|---|
| Màu | color-primary | #F69D39 | `ColorScheme.primary` |
| Chữ | type-body-medium | 14 sp | `TextTheme.bodyMedium` |
| Khoảng cách | spacing-md | 16 dp | `AppSpacing.md` |

### 20. Component → Widget (bước 44)
| Component | Variant / State | Flutter widget |
|---|---|---|
| Button | Primary · default / pressed / disabled / loading | `FilledButton` |
| Text field | default / focused / error / disabled | `TextFormField` |
| Navigation | Home / Menu / Đơn / Lịch sử | `NavigationBar` |
| Dialog | Xác nhận / Destructive | `AlertDialog` |
