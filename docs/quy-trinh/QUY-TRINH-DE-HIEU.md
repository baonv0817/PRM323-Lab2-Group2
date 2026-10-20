# Quy trình làm Lab 2 — bản dễ hiểu, từng bước

Làm **đúng thứ tự**, mỗi bước xong thì **commit** (thầy xem lịch sử Git và lịch sử phiên bản Figma, nên đừng dồn vào một ngày).
Mỗi lần dùng AI đều ghi vào `ai/ai-design-log.md`: **prompt nguyên văn + câu trả lời nguyên văn + bạn quyết định gì, vì sao**.

Có 6 chặng, tổng cộng 45 bước. Gợi ý: mỗi chặng làm trong một ngày.

---

## Chặng 0 — Chuẩn bị (30 phút)

1. **Chọn đề tài thật cụ thể** và hỏi thầy duyệt.
   - Sai: "app đặt đồ ăn".
   - Đúng: "app đặt món trước cho sinh viên ở KTX chỉ có 15 phút nghỉ giữa hai slot".
2. **Tạo repo GitHub** tên `prm323-lab2-<MSSV>`, gồm các thư mục `ux/`, `design/`, `ai/`, `assets/stitch/`, `assets/figma/`, `handoff/` và file `README.md`.
3. **Tạo file Figma** có đúng 6 page theo thứ tự: `01 User Flow`, `02 Wireframe`, `03 Final UI`, `04 Design System`, `05 Components`, `06 Prototype`. Bật chia sẻ "Anyone with the link can view".
4. **Tạo file `ai/ai-design-log.md`.** Từ giờ mọi lần dùng AI đều ghi vào đây.
5. **Commit lần đầu.**

---

## Chặng 1 — Xác định vấn đề (1–2 giờ, chưa vẽ gì)

6. **Nghĩ 2–3 hướng giải pháp** cho cùng một vấn đề. Ví dụ: app đặt trước tại quầy · màn hình gọi số ở căn tin · đặt qua QR trên bàn.
7. **Chọn 1 hướng**, ghi lý do: hướng nào giúp được nhiều người nhất, và có làm kịp không.
8. **Viết problem statement một câu**, đủ 4 ý: *ai* – *gặp khó gì* – *trong bối cảnh nào* – *hậu quả gì*.
   > "Sinh viên ở KTX có lịch học dày (ai) không mua kịp đồ ăn (khó gì) vì hàng chờ đúng giờ nghỉ chung (bối cảnh), nên bỏ bữa hoặc vào lớp trễ (hậu quả)."
9. **Liệt kê giả định**, chia 3 cột: *Biết chắc* · *Đoán* · *Chưa biết*.
10. **Vẽ sơ đồ người liên quan:** ai dùng trực tiếp, ai hỗ trợ (ví dụ nhân viên quầy), ai liên quan nhưng ngoài phạm vi.
11. **Cho AI phản biện:**
    ```text
    Đóng vai giảng viên UX khó tính. Đây là problem statement và danh sách giả định của tôi: [dán].
    Kiểm tra: (1) đủ ai – vấn đề – bối cảnh – hậu quả chưa; (2) chỗ nào tôi lẫn giả định với sự thật;
    (3) chỗ nào là giải pháp trá hình; (4) 3 câu hỏi tôi cần đi hỏi người dùng thật.
    ```
    Ghi log, sửa theo những ý bạn đồng ý, commit.

---

## Chặng 2 — Hỏi người dùng thật (nửa ngày)

12. **Viết kế hoạch hỏi:** muốn biết điều gì, hỏi ai, mấy người, hỏi trực tiếp hay qua chat.
13. **Soạn 5–8 câu hỏi về việc người ta đã làm**, không hỏi ý kiến.
    - Đúng: "Lần gần nhất bạn mua đồ ở căn tin là khi nào? Bạn chờ bao lâu?"
    - Sai: "Bạn có thích app đặt món không?"
14. **Hỏi 5–6 người thật** thuộc nhóm mục tiêu, mỗi người 5–10 phút. Ghi chép **ẩn danh**, đánh mã **E01, E02…**
15. (Nên làm) **Quan sát tại chỗ:** đứng ở căn tin giờ nghỉ, bấm giờ xem mỗi người chờ bao lâu.
16. **Xem đối thủ:** mở 2–3 app hoặc cách làm đang có (Grab, ShopeeFood, mua trực tiếp). Thử đặt một món, chụp màn hình, ghi điểm mạnh và yếu.
17. **Gom ý (affinity map):** mỗi ý một thẻ, ghi mã nguồn (E03…), rồi gom các thẻ giống nhau thành nhóm như *thời gian*, *thanh toán*, *thao tác*.
18. **Gắn nhãn cho từng ý:**
    - **Observed:** tự thấy.
    - **Reported:** người ta kể lại.
    - **Inferred:** bạn suy ra từ các ý khác.
    - **Assumed:** chưa có bằng chứng.
19. **Cho AI tổng hợp**, chỉ dựa trên ghi chép của bạn, không được bịa thêm:
    ```text
    Chỉ dùng ghi chú tôi đưa, mỗi đoạn có mã E01… Tách hành vi, mục tiêu, nỗi đau, ràng buộc; gom theo hành vi;
    mỗi kết luận ghi mã nguồn; thiếu thì ghi "UNKNOWN". Không bịa câu nói hay số liệu.
    Trả về: bảng bằng chứng → các nhóm người dùng → bản nháp persona → câu hỏi còn mở. [dán ghi chú]
    ```
20. **Cho AI phản biện nghiên cứu:** chỉ ra thiên lệch, ý nào chỉ một người nói mà bạn đang coi là xu hướng, kết luận nào không có nguồn.

> Không kịp hỏi người thật thì có thể **phỏng vấn sinh viên giả lập bằng AI** (`ux/ai-interview-kit.md`). Khi đó phải ghi rõ đây là dữ liệu giả lập, gắn nhãn **Assumed**, và ghi lý do vào phần hạn chế.

---

## Chặng 3 — Persona, luồng và khung xám (1 ngày)

21. **Viết persona** gồm 1 persona chính, nên có thêm 1–2 persona phụ, mỗi người đủ **12 mục**:
    1. Là ai
    2. Mức ưu tiên
    3. Dùng app ở đâu, lúc nào
    4. Mục tiêu
    5. "Khi…, tôi muốn…, để…"
    6. Hiện đang làm thế nào
    7. Khó chịu ở đâu
    8. Động lực
    9. Bị giới hạn bởi gì
    10. Một tình huống dùng app cụ thể
    11. Đo thành công thế nào
    12. Thông tin lấy từ đâu, đã kiểm chứng chưa

    Thêm 4 mục bắt buộc của Lab 2: **tuổi, vai trò, thiết bị, nhu cầu accessibility**. Mỗi mục ghi nhãn kèm mã nguồn, ví dụ "Reported — E03".
22. **Viết chỉ số thành công đo được**, ví dụ: "đặt xong một đơn dưới 35 giây".
23. **Lập 2 bảng ma trận** (`ux/persona-mapping.xlsx`):
    - **Bảng "ai cần gì"** (coverage matrix): hàng là nhu cầu, cột là persona. Làm **xong ngay** ở bước này.
    - **Bảng truy vết** Persona → Nhu cầu → Nguyên tắc → Quyết định UI → Màn hình → Cách kiểm chứng. Bước này mới điền **2 cột đầu** (persona, nhu cầu); các cột sau điền dần ở bước 27, 36 và 43.
24. **Viết user story:** "Là [persona], tôi muốn [việc], để [kết quả]".
25. **Liệt kê ≥ 8 màn hình** và màn nào đi tới màn nào (IA). Dialog và trạng thái lỗi không tính là màn riêng.
26. **Vẽ ≥ 3 luồng (flow)**, mỗi luồng có điểm bắt đầu, mục tiêu, điểm kết thúc, đường đi thuận và ≥ 1 nhánh rẽ. **Ít nhất 1 luồng có lỗi và cách phục hồi**, ví dụ mất mạng khi thanh toán.
27. **Lập bảng luồng → màn hình.** Màn nào không thuộc luồng nào thì bỏ. Điền cột **Màn hình** vào bảng truy vết: mỗi nhu cầu được đáp ứng ở màn nào.
28. **Cho AI phản biện persona và flow:** persona có khác nhau thật không, chỗ nào thiếu bằng chứng, có ngõ cụt không, Back đi về đâu.
29. **Vẽ khung xám (wireframe)** cho mọi màn ở Figma Page 02: chỉ có hộp và chữ, chưa màu.
30. **Tự đi thử từng luồng** trên khung xám, hoặc nhờ một bạn thử. Ghi lại chỗ cần sửa.

---

## Chặng 4 — Tạo UI bằng AI và cho AI phản biện (1–2 ngày, nhiều điểm nhất)

31. **Viết `design/DESIGN.md` trước khi mở Stitch:** tông giọng, màu (mỗi màu dùng làm gì), cỡ chữ, khoảng cách, bo góc, đổ bóng, quy tắc component, và nguyên tắc thiết kế gắn với persona. **Đo tương phản ngay khi chọn màu:** chữ ≥ 4,5:1, nút ≥ 3:1. Commit file này **trước** khi dùng Stitch.
32. **Thử ≥ 2 phong cách** cho cùng một màn chính trên Stitch, ví dụ ấm và nhiều ảnh, hoặc tối giản. Chọn một phong cách và ghi lý do theo persona.
33. **Viết prompt đầu tiên cho Stitch**, đủ 5 phần: *persona* · *các màn cần vẽ* · *nền tảng (Android 360 × 800 dp)* · *ràng buộc (nút 48 dp, chữ 14 sp, một nút chính mỗi màn)* · *phong cách*. Dán prompt nguyên văn vào log, chụp ảnh mọi màn được sinh ra.
34. **Vòng lặp 1, 2, 3, mỗi vòng sửa một vấn đề khác nhau có tên rõ.** Ví dụ: (1) nút chính khó đọc · (2) thiếu màn giỏ hàng trống · (3) lỗi thanh toán là ngõ cụt. Mỗi vòng:
    - chụp **ảnh trước**;
    - viết prompt sửa đúng vấn đề đó;
    - chụp **ảnh sau**; hai ảnh phải khác nhau và đúng màn đang sửa;
    - **tự kiểm lại**, ví dụ đo tương phản, vì AI hay nói đã đạt khi chưa đạt.
35. **Cho một AI khác phản biện toàn bộ UI** (≥ 5 lỗi gắn màn hình cụ thể):
    ```text
    Đóng vai chuyên gia UX khó tính. Đánh giá các màn hình đính kèm theo 10 heuristic của Nielsen,
    WCAG (tương phản 4.5:1 / 3:1, vùng chạm 48 dp, chữ ≥ 14 sp, không chỉ dùng màu) và persona: [tóm tắt].
    Mỗi lỗi ghi: màn hình · tiêu chí · mức độ · vấn đề · đề xuất. Ít nhất 8 lỗi. Nêu cả điểm làm tốt.
    ```
    Dán **toàn bộ** câu trả lời vào log, không chỉ tóm tắt.
36. **Lập bảng quyết định:** mỗi đề xuất quan trọng ghi **Chấp nhận / Sửa lại / Từ chối** kèm lý do (persona, heuristic hoặc ràng buộc). **Nên có ít nhất 1 Từ chối thật**, vì thầy gần như chắc chắn hỏi câu này. Điền cột **Nguyên tắc** và **Quyết định UI** vào bảng truy vết.
37. **Figma Page 04:** tạo token bằng **Variables** gồm màu, chữ, khoảng cách, bo góc, đổ bóng.
38. **Figma Page 05:** dựng **9 component** bằng Auto Layout, đủ trạng thái:
    - Button: thường / nhấn / tắt / đang tải
    - Text field: thường / đang nhập / đã nhập / lỗi / tắt
    - Card: thường / nhấn
    - Thanh điều hướng: mỗi tab ở trạng thái được chọn
    - App bar: thường / có nút
    - Dialog: xác nhận và bản cảnh báo/lỗi
    - Loading
    - Empty
    - Error

    Component phải dùng token, không gán màu cứng.

---

## Chặng 5 — Giao diện cuối và bản bấm thử (1 ngày)

39. **Figma Page 03:** dựng ≥ 8 màn 360 × 800 dp, **chỉ dùng bản sao (instance) của component**. Đặt các trạng thái (đang tải, trống, lỗi) **cạnh** màn gốc.
40. **Kiểm 360 dp và 412 dp:** nhân bản frame, đổi chiều rộng sang 412, xem có bị vỡ không, rồi chụp ảnh lại.
41. **Figma Page 06:** nối 3 luồng bấm được từ đầu tới cuối, mỗi luồng có **điểm bắt đầu**, có **1 dialog nổi lên trên màn**, có **1 màn đang tải chuyển sang kết quả**, Back đúng, không ngõ cụt.
42. **Tự chấm từng màn** theo 20 tiêu chí UI Checklist, mục tiêu ≥ 80 điểm. Làm thêm 3 bài test nhanh:
    - nhìn 5 giây xem có hiểu màn đó để làm gì không;
    - chuyển sang ảnh đen trắng xem có phụ thuộc màu không;
    - thử bỏ bớt thứ trang trí xem có mất thông tin không.

    Viết `design/design-decisions.md` (≤ 10 quyết định + bảng kiểm accessibility có số đo) và `design/screen-spec.md` (từng màn để làm gì, có gì, thuộc luồng nào). Xuất ảnh PNG từ **chính Figma** vào `assets/figma/`.

---

## Chặng 6 — Thử với người dùng, bàn giao, bảo vệ (1 ngày)

43. **Thử với 3–5 người:** giao việc, ví dụ "đặt một combo và chọn giờ nhận", và **không chỉ từng bước**. Ghi lại: làm được không, mất bao lâu, bao nhiêu lần chạm, vướng ở đâu. Sửa lỗi nặng rồi thử lại. So kết quả với chỉ số thành công ở bước 22. Điền cột **Kết quả kiểm chứng** vào bảng truy vết (đạt / không đạt).
44. **Viết `handoff/flutter-handoff.md`:** mỗi màn đủ 6 mục:
    - bố cục từ trên xuống, phần nào cuộn;
    - component dùng ở đâu;
    - các trạng thái;
    - mỗi lần bấm hoặc nhập thì xảy ra gì, kể cả quy tắc kiểm tra dữ liệu;
    - đi tới đâu, Back về đâu;
    - giới hạn: vùng chạm, bàn phím, chữ dài, màn ≥ 600 dp.

    Kèm **2 bảng**: token → Flutter, và component → widget. Nhờ một bạn dựng thử một màn chỉ dựa vào handoff; câu nào bạn ấy phải hỏi lại là chỗ còn thiếu.
45. **Hoàn thiện và chuẩn bị bảo vệ:**
    - Viết `README.md`: đề tài, persona một dòng, link Figma, AI đã dùng, file nào ở đâu.
    - Mở link Figma và GitHub bằng **cửa sổ ẩn danh** để chắc người khác xem được.
    - Làm 12 slide và tập demo theo kịch bản trong `slides/`.

---

## Nhớ 4 điều

1. **AI tạo ra, bạn quyết định.** Mỗi đề xuất của AI phải có Chấp nhận / Sửa lại / Từ chối kèm lý do.
2. **Ghi nguyên văn** mọi prompt và câu trả lời, lưu ảnh trước và sau.
3. **Tự kiểm lại** những gì AI nói: đo tương phản, đo kích thước, tự bấm chạy luồng.
4. **Chưa có bằng chứng thì ghi "Assumed"**, không bịa số liệu.

Chi tiết từng chặng (checklist qua gate, prompt đầy đủ, mẫu log) nằm trong `HUONG-DAN-LAM-TU-DAU.md`.
