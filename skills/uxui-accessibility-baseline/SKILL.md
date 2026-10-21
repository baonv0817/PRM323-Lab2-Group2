---
name: uxui-accessibility-baseline
description: Kiểm accessibility nền của UI theo chuẩn của môn và WCAG 2.2 - tương phản chữ 4.5:1, chữ lớn và UI indicator 3:1, vùng chạm 48 dp, chữ nội dung 14 sp, trạng thái không chỉ dựa vào màu. Có script tính tỉ lệ tương phản. Dùng khi chấm G3/G4 hoặc khi người dùng hỏi UI có đạt contrast, cỡ chữ, vùng chạm không.
---

# Accessibility baseline

## Ngưỡng
| Hạng mục | Ngưỡng | Nguồn |
|---|---|---|
| Chữ thường | ≥ 4.5:1 | WCAG 2.2 SC 1.4.3 |
| Chữ lớn (≥ 24 px, hoặc ≥ 18.66 px và đậm) | ≥ 3:1 | WCAG 2.2 SC 1.4.3 |
| Thành phần UI và chỉ báo trạng thái thiết yếu (viền ô nhập, checkbox, icon chức năng) | ≥ 3:1 | WCAG 2.2 SC 1.4.11 |
| Vùng chạm | ≥ 48 × 48 dp | Chuẩn của môn (Material) |
| Chữ nội dung | ≥ 14 sp | Chuẩn của môn |
| Nhãn thanh điều hướng dưới | cho phép 12 sp nếu có ghi ngoại lệ | Quyết định thiết kế của dự án |
| Trạng thái | Không chỉ dựa vào màu: kèm chữ hoặc icon | WCAG 1.4.1 |

## Quy trình
1. **Thu thập cặp màu:** với mỗi vai trò (chữ chính, chữ phụ, chữ trên nút, chữ cam trên nền, viền input, icon) lấy màu chữ và màu nền **thực sự nằm ngay sau chữ** (lớp tô trên cùng, không phải nền trang). Dùng token/variable nếu có.
2. **Tính tỉ lệ** bằng `scripts/contrast.py`:
   ```bash
   python scripts/contrast.py "#622B14" "#F69D39"          # chữ thường
   python scripts/contrast.py "#B45309" "#FFF5E5" --large  # chữ lớn
   python scripts/contrast.py --pairs pairs.csv             # nhiều cặp: fg,bg,nhãn,large(0/1)
   ```
3. **Kiểm cỡ chữ:** liệt kê chữ < 14 sp; chỉ chấp nhận ngoại lệ đã ghi (nhãn nav 12 sp). Chữ trong ảnh/emoji không tính nhưng emoji không được là cách duy nhất truyền nghĩa.
4. **Kiểm vùng chạm:** liệt kê điều khiển có kích thước < 48 dp (icon button, checkbox, chip, switch, link chữ); vùng bấm của prototype có thể lớn hơn hình nhìn thấy, ghi rõ nguồn số đo.
5. **Kiểm trạng thái chỉ bằng màu:** lỗi, thành công, đang chọn, hết hàng đều phải có chữ hoặc icon đi kèm. Thử xem ảnh ở thang xám.
6. **Ghi kết quả** thành bảng: cặp / tỉ lệ / ngưỡng / đạt? / vị trí.

## Cách báo cáo
- Nêu **số đo** và **nơi dùng**, không viết "tương phản kém" chung chung.
- Một cặp trượt ở nhiều chỗ chỉ cần nêu một lần kèm số lần xuất hiện.
- Số do AI ước lượng từ ảnh thường sai; ưu tiên số tính từ giá trị màu thật.

## Lỗi hay gặp
- Chữ trắng trên cam sáng (thường ~2:1).
- Chữ cam trên nền be/đào (đặc biệt dưới 4.5:1 khi chữ nhỏ).
- Viền ô nhập quá nhạt (< 3:1).
- Nhãn nav 10 sp; mô tả phụ 11–13 sp.
