# Phỏng vấn sinh viên giả lập bằng AI (Phụ lục B của AI log)

- **Công cụ:** Claude Opus 5.5 (Anthropic), chạy trong Claude Code · **Ngày:** 17/10/2026
- **Cách làm:** theo `ux/ai-interview-kit.md`. AI đóng vai từng nhân vật hư cấu, bị yêu cầu nói tự nhiên, được phép phàn nàn và không được khen để làm vừa lòng.
- **Giới hạn:** đây là **dữ liệu giả lập**, chỉ dùng để tạo giả thuyết; không phải lời của người thật. Người dùng giả lập thường nông và dễ đồng thuận hơn người thật ([tổng hợp NN/g](https://radar.zurb.com/article/nielsen-norman-synthetic-users-were-too-shallow-to-be-useful-against-three-real-studies)).
- Nội dung dưới đây được ghi nguyên văn, không chỉnh sửa sau khi sinh.

---

## B1. Prompt tạo hồ sơ

```text
Tôi đang làm nghiên cứu UX cho một app đặt đồ ăn trước và nhận tại quầy trong khuôn viên trường đại học ở Việt Nam.
Hãy tạo 5 hồ sơ sinh viên GIẢ LẬP khác nhau rõ rệt để tôi phỏng vấn. Đa dạng về năm học, ngành, lịch học, nơi ở,
ngân sách, thiết bị, thói quen thanh toán và mức hài lòng với căn tin. Có ít nhất 1 người KHÔNG thích đặt món qua app
và 1 người ít khi ăn ở trường. Mỗi hồ sơ 5–6 dòng. Không bịa số liệu thống kê; đây là nhân vật hư cấu.
```

**Câu trả lời của AI:**

- **A1 — Quân, 20, năm 2 Kỹ thuật phần mềm.** Ở ký túc xá. 3 slot/ngày, nghỉ giữa slot khoảng 15 phút. Ngân sách ăn ~60.000đ/ngày. Samsung Galaxy A35 (Android). Trả bằng QR ngân hàng. Thấy căn tin "ngon nhưng đông".
- **A2 — Linh, 19, năm 1 Thiết kế đồ hoạ.** Ở trọ cách trường 3 km, đi xe buýt. Lịch học dồn buổi sáng, hay đói lúc 10h. Ngân sách ~40.000đ/ngày, rất để ý giá. iPhone 11 cũ. Hay dùng ví MoMo. Ngại căn tin vì chen lấn.
- **A3 — Tuấn, 22, năm 4 Quản trị kinh doanh.** Đang thực tập, chỉ lên trường 2 buổi/tuần. Ít ăn ở trường. Xiaomi tầm trung. Trả tiền mặt hoặc thẻ. Không thích app đặt món vì "nhiều app quá, cài rồi xoá".
- **A4 — Hà, 21, năm 3 Ngôn ngữ Anh.** Ở nhà cùng gia đình, mang cơm từ nhà 3–4 ngày/tuần. Chỉ mua đồ uống và đồ ăn vặt ở trường. Oppo A-series. Trả tiền mặt là chính.
- **A5 — Khang, 20, năm 2 An toàn thông tin.** Ở ký túc xá, làm trợ giảng lab buổi chiều nên giờ nghỉ thất thường. Hay đặt GrabFood về KTX buổi tối. Pixel cũ. Dùng thẻ và ví điện tử. Hay bị cầm điện thoại một tay vì tay kia cầm laptop.

---

## B2. Phỏng vấn từng nhân vật

Mỗi nhân vật một phiên riêng, cùng prompt nhập vai trong kit và cùng 10 câu hỏi. Ghi nguyên văn.

### A1 — Quân

1. **Một ngày đi học?** — "Sáng mình học slot 1 từ 7 giờ, xong slot 2, nghỉ trưa rồi slot 3. Tối về KTX code bài tập. Bữa sáng thường bỏ, ăn bù lúc giải lao."
2. **Giữa hai ca làm gì, bao lâu?** — "Khoảng 15 phút. Nếu phòng sau ở tòa khác thì mất 5 phút đi bộ, còn lại 10 phút để mua gì đó."
3. **Lần gần nhất mua đồ ở trường?** — "Hôm qua, mua bánh mì với trà ở căn tin. Hàng dài, mình chờ chắc 8–10 phút, vào lớp trễ mấy phút."
4. **Có bỏ ăn hay vào lớp muộn vì mua đồ?** — "Có, tuần nào cũng vài lần. Nhiều khi thấy hàng dài là bỏ luôn, nhịn tới trưa."
5. **Từng đặt app khi ở trường?** — "Có đặt Grab mấy lần, nhưng shipper không vào được tòa nhà, phải chạy ra cổng lấy, mất thời gian hơn."
6. **Trả tiền bằng gì, từng lỗi chưa?** — "QR ngân hàng. Có lần chuyển rồi mà quán chưa thấy, phải đứng chờ họ kiểm tra, rất ngại."
7. **Cầm điện thoại khi đi bộ?** — "Một tay, tay kia cầm balo hoặc ly nước. Mấy nút nhỏ ở góc trên là bấm trật."
8. **Điều gì khiến bạn KHÔNG dùng app đặt trước?** — "Nếu tới quầy mà món chưa xong, hoặc phải đăng ký tài khoản lằng nhằng. Với nếu không biết quán còn mở không."
9. **Muốn biết gì trước khi đặt?** — "Bao lâu thì xong, quán mở hay đóng, còn món không, giá cuối cùng là bao nhiêu."
10. **Điều gì khác quan trọng?** — "Mạng trong tòa nhà hay chập chờn, app mà cứ quay vòng vòng là mình bỏ."

### A2 — Linh

1. "Mình đi xe buýt 6 giờ rưỡi, học liền 2 slot buổi sáng. Chiều thường về nhà trọ làm đồ án."
2. "Nghỉ chừng 15–20 phút tuỳ lịch. Mình hay ra hành lang ngồi, đói thì mới đi mua."
3. "Tuần trước, mua xôi. Chờ không lâu nhưng chen lấn quá, mình không thích."
4. "Bỏ ăn thì có, vì đông quá ngại chen. Vào lớp muộn thì ít."
5. "Ít đặt app vì phí ship với phí dịch vụ cộng vào đắt hơn cả món. Mình sinh viên, mỗi nghìn đều tính."
6. "MoMo là chính. Chưa lỗi bao giờ, nhưng nếu lỗi chắc mình sẽ trả tiền mặt luôn cho nhanh."
7. "Hai tay, vì mình hay đứng yên khi dùng điện thoại. Nhưng chữ nhỏ là mình phải phóng to."
8. "Nếu giá trên app cao hơn mua trực tiếp, hoặc có phí gì đó, mình sẽ không dùng."
9. "Giá, có combo hay giảm giá sinh viên không. Ảnh món phải giống thật."
10. "Mình thích thấy trước tổng tiền, đừng tới bước cuối mới hiện thêm phí."

### A3 — Tuấn

1. "Mình đang thực tập, tuần lên trường 2 buổi. Lên là học dồn 3 slot liên tục."
2. "Nghỉ ngắn thôi, thường mình ở lại lớp nói chuyện hoặc trả lời mail công việc."
3. "Lâu rồi mình không mua ở căn tin. Hay mua cà phê ngoài cổng trước khi vào."
4. "Không, mình ít ăn ở trường nên không gặp chuyện đó."
5. "Có cài vài app nhưng xoá rồi. Nhiều app quá, mỗi app một tài khoản."
6. "Tiền mặt hoặc thẻ. Lỗi thanh toán là mình bỏ đơn luôn, không thử lại."
7. "Hai tay. Mình không hay vừa đi vừa bấm."
8. "Phải tải thêm một app nữa chỉ để mua đồ ở trường thì mình không tải. Nếu có web hoặc quét QR tại bàn thì có thể."
9. "Thật ra mình chỉ cần biết có cà phê không và bao lâu xong."
10. "Đừng bắt đăng nhập trước khi xem menu."

### A4 — Hà

1. "Mình mang cơm từ nhà, chỉ mua trà sữa hoặc bánh ở trường. Lịch học xen kẽ, có hôm trống 2 tiếng."
2. "Có hôm nghỉ 10 phút, có hôm trống cả tiếng. Lúc rảnh mình lên thư viện."
3. "Hôm kia mua trà sữa, chờ khoảng 5 phút. Không sao."
4. "Ít khi. Mình có cơm nhà rồi."
5. "Chưa bao giờ đặt app khi ở trường. Thấy không cần."
6. "Tiền mặt. Mình không thích liên kết ngân hàng vào nhiều app."
7. "Một tay khi đi, nhưng mình không bấm điện thoại khi đang đi bộ."
8. "Nếu bắt trả online mới đặt được. Mình muốn được trả tiền mặt lúc lấy."
9. "Có món mình thích không, có hết không."
10. "Mình nghĩ app này hợp với mấy bạn ở KTX hơn là mình."

### A5 — Khang

1. "Sáng học, chiều làm trợ giảng lab. Có hôm chạy qua lại giữa lab và phòng học liên tục."
2. "Không cố định. Có lúc chỉ 10 phút giữa hai việc."
3. "Hôm qua mua nước ở quầy, chờ tầm 7 phút vì đúng giờ nghỉ của cả khu."
4. "Có, hôm nào lab đông là mình nhịn tới tối."
5. "Đặt Grab về KTX buổi tối thì ổn. Ban ngày ở trường thì không, vì không ai mang vào lab cho mình."
6. "Thẻ và ví. Từng bị lỗi cổng thanh toán, app báo 'thất bại' rồi mất luôn giỏ hàng, mình phải chọn lại từ đầu, bực lắm."
7. "Một tay, tay kia cầm laptop. Nên mình rất ghét nút xác nhận nằm trên cao."
8. "Nếu trạng thái đơn không rõ, mình không biết đã xong chưa để chạy xuống lấy."
9. "Thời gian chờ ước tính và quầy nào, tầng nào để lấy."
10. "Cho mình hẹn giờ lấy, vì mình biết trước lúc nào rảnh."

---

## B3. Tổng hợp bằng AI

**Prompt:** như Bước 3 trong `ux/ai-interview-kit.md`, dán 5 bản ghi ở trên.

**Câu trả lời của AI:**

**1. Ý lặp lại (≥ 2 người)**
- *Thời gian nghỉ ngắn, hàng chờ làm bỏ bữa hoặc trễ lớp* — A1, A5 (A2 bỏ ăn vì chen lấn). "Thấy hàng dài là bỏ luôn, nhịn tới trưa." (A1)
- *Cầm điện thoại một tay, ghét nút ở trên cao* — A1, A5. "Rất ghét nút xác nhận nằm trên cao." (A5)
- *App giao hàng không vào được tòa nhà hoặc lab* — A1, A5.
- *Muốn biết trước thời gian chờ và trạng thái quán, món* — A1, A3, A4, A5.
- *Ngại phí ẩn, muốn thấy tổng tiền sớm* — A2, A1 ("giá cuối cùng").
- *Không muốn đăng ký hay đăng nhập rườm rà* — A1, A3.
- *Lỗi thanh toán: muốn giữ giỏ hàng hoặc trả tiền mặt* — A5, A2, A4.

**2. Ý mâu thuẫn**
- A3 và A4 ít ăn ở trường, không thấy cần app; A1 và A5 thì rất cần.
- A3 không muốn tải thêm app, chỉ chấp nhận web hoặc QR; những người khác không phản đối app.
- A4 muốn trả tiền mặt; A1 và A5 ưu tiên QR, ví.

**3. Persona chính đề xuất:** sinh viên ở ký túc xá, có lịch học dày và giờ nghỉ ngắn hoặc thất thường (A1, A5). Đây là nhóm đau nhất (bỏ bữa, trễ lớp) và có tần suất mua ở trường cao nhất. A2 là nhóm phụ nhạy cảm về giá. A3 và A4 nằm ngoài nhóm mục tiêu.

**4. Giả thuyết cần kiểm chứng với người thật**
1. Đa số sinh viên ở KTX có giờ nghỉ giữa slot ≤ 15 phút. → *"Giữa hai slot gần nhất của bạn có bao nhiêu phút?"*
2. Hàng chờ giờ nghỉ đủ dài để làm sinh viên bỏ mua. → *"Tuần qua bạn bỏ mua ở căn tin mấy lần vì đông?"*
3. Biết trước thời gian chờ và trạng thái quán là yếu tố quyết định có đặt hay không. → *"Bạn cần biết gì trước khi đặt?"*
4. Sinh viên chấp nhận cài app riêng của quán. → *"Bạn có cài app chỉ để mua ở căn tin không? Vì sao?"*
5. Khi thanh toán lỗi, sinh viên muốn chuyển sang tiền mặt hơn là thử lại. → *"Lần thanh toán lỗi gần nhất bạn làm gì?"*

---

## B5. AI phản biện persona

**Prompt:** như Bước 5 trong kit, dán `ux/persona.md` (bản trước khi sửa) và B3.

**Câu trả lời của AI:**
1. **Không có dữ liệu chống lưng:** các con số "xếp hàng 12–18 phút", "giờ cao điểm 09:15–09:30" không có nguồn. Bản ghi giả lập chỉ cho thời gian chờ 5–10 phút, ngắn hơn nhiều.
2. **Mâu thuẫn:** persona dùng iPhone 13, nhưng thiết kế lại theo Android Material 3, khung 360 dp. Các nhân vật đau nhất (A1, A5) dùng Android. Ngoài ra "Hòa Lạc / ĐH Quốc Gia" là hai nơi khác nhau.
3. **Bỏ sót:** chưa nhắc rào cản "không muốn cài thêm app" (A3) và "ngại phí ẩn" (A2).
4. **5 câu giảng viên sẽ hỏi:** (a) con số 12–18 phút lấy ở đâu; (b) vì sao chọn nhóm ở KTX chứ không phải toàn bộ sinh viên; (c) persona dùng iPhone sao lại thiết kế theo Android; (d) nếu sinh viên không muốn cài app thì sản phẩm có còn ý nghĩa không; (e) phỏng vấn AI khác người thật ở đâu.

**Quyết định với phản biện này** (ghi trong `ai/ai-design-log.md` mục 5, dòng 07–09):
- (1) **Chấp nhận:** bỏ con số không có nguồn, ghi thời gian chờ là giả thuyết cần đo.
- (2) **Chấp nhận:** đổi thiết bị của persona sang Android tầm trung; bỏ "Hòa Lạc / ĐH Quốc Gia".
- (3) **Chỉnh sửa:** thêm rào cản "không muốn đăng ký" vào pain point (xem menu không cần đăng nhập). Rào cản "không muốn cài app" ghi là rủi ro sản phẩm; hướng web đặt qua QR là phương án dự phòng.
