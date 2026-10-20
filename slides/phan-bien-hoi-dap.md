# Chuẩn bị phản biện — câu hỏi xoáy và cách trả lời

Thầy hỏi xoáy là để xem **em có hiểu vì sao mình quyết định như vậy không**, không phải để nghe một con số đẹp. Nguyên tắc chung:

1. **Tách rõ "dữ liệu" và "giả định".** Câu "em giả định X, và kiểm chứng bằng Y" mạnh hơn nhiều so với một con số không có nguồn.
2. **Mỗi quyết định có một chuỗi lý do:** quan sát hoặc dữ liệu → nhu cầu của persona → nguyên tắc (heuristic, WCAG, Material) → lựa chọn → cách kiểm tra.
3. **Tự nói ra điểm yếu trước khi bị hỏi.** "Hạn chế của em là…, nếu có thêm thời gian em sẽ…" thường được đánh giá cao hơn chống chế.
4. **Không bịa nghiên cứu.** Chưa phỏng vấn thì nói là chưa. Đề cũng nêu rõ log giả bị xử lý theo quy chế liêm chính học thuật.

---

## A. Lỗ hổng trong repo hiện tại mà thầy có thể bắt

Sửa hoặc chuẩn bị câu trả lời trước khi lên trình bày.

| # | Chỗ yếu | Vì sao bị bắt | Nên làm |
|---|---|---|---|
| 1 | Persona dùng **iPhone 13**, nhưng thiết kế lại theo **Material 3, Android 360 dp** | iPhone 13 rộng 390 pt, chạy iOS. Thiết kế kiểu Android cho người dùng iPhone là mâu thuẫn | Đổi thiết bị của persona sang Android tầm trung (360–412 dp), **hoặc** giải thích: app Flutter đa nền tảng, frame chuẩn của lab là 360 × 800 nên lấy Android làm gốc |
| 2 | "Campus **Hòa Lạc / ĐH Quốc Gia**" | Đó là hai nơi khác nhau, nghe như viết cho có | Chọn đúng một nơi bạn thật sự quan sát được |
| 3 | Thời gian xếp hàng ghi **12–15 phút** (mindmap) và **12–18 phút** (pain point) | Hai con số trong cùng một file lệch nhau, lại không có nguồn | Đo thật (xem mục C) hoặc ghi rõ là ước lượng |
| 4 | Giờ cao điểm **09:15–09:30, 11:30–12:00** | Thầy sẽ hỏi lấy từ đâu | Đối chiếu với lịch slot thật của trường, hoặc tự quan sát 1–2 buổi |
| 5 | Chỉ số thành công **dưới 35 giây** | Vì sao là 35 mà không phải 60? | Lập luận: 15 phút nghỉ, 5–7 phút đi lại, còn lại ~1 phút để đặt món. 35 giây là mục tiêu có dư. Tốt nhất là bấm giờ thử trên prototype |
| 6 | Có màn **Onboarding** (SCR-01) dù persona luôn vội | Onboarding thêm bước, đi ngược mục tiêu "nhanh" | Nói rõ: chỉ hiện ở lần mở đầu tiên, có nút "Bỏ qua" (Stitch có nút này); từ lần sau vào thẳng Home |
| 7 | App **không có giao hàng** | "Sao không giao tận nơi như Grab?" | Persona ở trong trường, không cần giao; shipper không vào được tòa nhà/phòng lab (SIM-A1, A5). Đây là quyết định **thu hẹp phạm vi** có chủ đích (MVP, `ux/p0-problem-framing.md` mục 5) |
| 8 | "Kiosk FtaCode **Tòa Alpha** trong trường" | Thầy có thể hỏi quán có thật không | Nói thẳng: "Em giả định quán mở kiosk trong trường; tên món, giá và topping là dữ liệu mẫu" |
| 9 | Bảng quyết định **chưa có đề xuất nào bị Từ chối** | Hướng dẫn chấm có câu "một đề xuất AI nào bị từ chối, vì sao?" | Nếu thực tế có từ chối thì thêm vào log; nếu không có, nói thật là đã chỉnh sửa thay vì từ chối và giải thích vì sao |

---

## B. Câu hỏi xoáy theo chủ đề

### 1. Persona — "Lấy cơ sở gì để có persona này?"

**Câu trả lời trung thực (khi chưa có nghiên cứu):**
> "Đây là **proto-persona**, tức persona giả định, xây từ quan sát của chính em và bạn cùng lớp: lịch học theo slot, giờ nghỉ ngắn, hàng ở căn tin. Theo Nielsen Norman Group, proto-persona dùng được ở giai đoạn đầu nếu ghi rõ là giả định và kiểm chứng sau. Hạn chế là em chưa phỏng vấn đủ người, nên các con số như thời gian xếp hàng là ước lượng. Bước tiếp theo là phỏng vấn 5 bạn và bấm giờ hàng thật."

**Nếu đã làm mục C:**
> "Em phỏng vấn [N] bạn và bấm giờ hàng [N] lần vào [ngày]. Thời gian chờ trung bình là [X] phút; [N/N] bạn nói từng bỏ bữa vì không kịp. Từ đó em ra hai pain point chính…"

**Hỏi nối tiếp có thể gặp:**
- *"Sao 1 persona mà không phải 2–3?"* → Đề yêu cầu một persona chính. Nhóm phụ (giảng viên, nhân viên quầy) em ghi nhận nhưng chưa thiết kế cho họ, vì phạm vi lab.
- *"Persona khác 'sinh viên chung chung' ở điểm nào?"* → Ràng buộc cụ thể: 15 phút, một tay, mạng chập chờn, ngoài nắng. Mỗi ràng buộc dẫn tới một quyết định thiết kế có thể chỉ ra trên màn hình.
- *"Nếu persona sai thì thiết kế sai ở đâu?"* → Nếu sinh viên thực ra có 30 phút nghỉ, thì tính năng hẹn giờ và tối ưu số chạm bớt quan trọng; ưu tiên sẽ chuyển sang xem món, giá và combo.

### 2. Màu sắc — "Sao chọn màu cam/nâu/kem?"

**Lý do chọn màu:**
1. **Bảng màu thương hiệu, chốt trong DESIGN.md:** cam `#F69D39` làm màu nhấn, nâu đậm `#622B14` cho chữ, nền kem `#FFF5E5`. Tông ấm hợp với quán đồ ăn; một màu nhấn duy nhất giúp nhận ra ngay nút chính. Font Nunito nét tròn, thân thiện, đủ dấu tiếng Việt.
2. **Chức năng trước, cảm xúc sau:** màu ấm hay gắn với đồ ăn, nhưng đó chỉ là lý do phụ. Đừng nói "màu cam kích thích vị giác" như một sự thật khoa học. Nếu thầy hỏi nguồn mà không có thì chỉ nói "thường được dùng trong ngành F&B".
3. **Đo bằng WCAG, không đo bằng mắt:** đây là phần mạnh nhất. Kể lại chuyện sửa sai: chữ trắng trên cam chỉ 2,14:1 → giữ cam cho nền, đổi chữ sang nâu (5,23:1).

**Hỏi nối tiếp:**
- *"Sao không đổi luôn sang cam đậm cho chữ trắng đọc được?"* → Cam đậm `#B45309` thì chữ trắng đạt 5,02:1, nhưng làm mất màu nhận diện của thương hiệu. Chữ nâu trên cam vừa giữ thương hiệu vừa đạt chuẩn. Đây là đánh đổi có chủ đích.
- *"Chữ lớn trong WCAG là bao nhiêu?"* → Từ 18pt (~24px) chữ thường, hoặc 14pt (~18,7px) chữ đậm. Chữ nút 14–15sp đậm chưa tới mức đó nên phải đạt 4,5:1.
- *"Người mù màu thì sao?"* → Trạng thái không chỉ dựa vào màu: luôn có icon và chữ đi kèm (WCAG 1.4.1).
- *"Có dark mode không?"* → Đề chỉ bắt buộc light theme; em ưu tiên làm cho đạt chuẩn tương phản trước.

### 3. Font, kích thước, layout

- *"Sao Nunito?"* → Nét tròn khớp tông thân thiện của quán; hỗ trợ tiếng Việt có dấu đầy đủ. Đừng chỉ nói "vì đẹp".
- *"Sao 48 dp?"* → Material Design khuyến nghị vùng chạm tối thiểu 48 × 48 dp, khoảng 9 mm. Persona vừa đi vừa bấm nên càng cần.
- *"Sao bottom nav mà không phải drawer?"* → Vùng ngón cái khi cầm một tay; drawer giấu điều hướng, vi phạm heuristic #6 (nhận diện thay vì ghi nhớ). Material khuyến nghị bottom nav cho 3–5 đích đến.
- *"Sao 4 tab?"* → Mỗi tab là một việc persona làm thường xuyên: xem nhanh, xem menu, theo dõi đơn, đặt lại. Profile/cài đặt không đủ thường xuyên để chiếm một tab. *(Lưu ý: Figma đang ghi tab 4 là "Cá nhân" — phải sửa cho khớp.)*
- *"360 × 800 lấy từ đâu?"* → Đề bài quy định; đây cũng là kích thước Android phổ biến nhất. Em kiểm tra thêm ở 412 dp.

### 4. User flow và chức năng

- *"Sao cần chọn giờ nhận?"* → Persona biết trước giờ ra chơi; hẹn giờ giúp món vừa xong lúc tới quầy, không phải đứng chờ.
- *"Sao fallback là tiền mặt?"* → Khi cổng thanh toán online lỗi, tiền mặt tại quầy là phương án không phụ thuộc mạng. Mục tiêu là đơn không bị mất (heuristic #9).
- *"Nếu cả tiền mặt cũng không được?"* → Giỏ hàng vẫn được giữ để thử lại sau; nút quay lại giỏ hàng luôn có.
- *"Chỉ huỷ đơn trong 60 giây — dựa vào đâu?"* → Ràng buộc nghiệp vụ: sau khi bếp bắt đầu nấu thì huỷ gây lỗ. 60 giây là giả định; con số thật nên hỏi chủ quán.
- *"Đo 35 giây kiểu gì?"* → Đếm 8 lần chạm trong Flow 1; nhờ 3–5 bạn chạy prototype và bấm giờ. *(Làm thử trước buổi chấm, ghi kết quả vào persona.md.)*

### 5. AI — "Em làm hay AI làm?"

- *"AI viết hết à?"* → Trả lời đúng sự thật. Mô tả rõ phần nào AI sinh, phần nào em quyết. Đề cho phép dùng AI nhưng phải khai báo đầy đủ.
- *"Sao tin AI critique?"* → Không tin hoàn toàn. Ví dụ: AI (và chính em lúc đầu) cho rằng chữ trắng trên `#F69D39` đạt chuẩn, nhưng đo lại thì sai. Từ đó em kiểm tra mọi con số bằng công thức WCAG.
- *"Heuristic #6 / #9 / #3 là gì?"* → Phải thuộc 10 heuristic. Ít nhất là 5 cái em đã dùng:
  - **#1** Hiển thị trạng thái hệ thống (Visibility of system status)
  - **#3** Quyền kiểm soát và tự do của người dùng (User control and freedom)
  - **#5** Phòng ngừa lỗi (Error prevention)
  - **#6** Nhận diện thay vì ghi nhớ (Recognition rather than recall)
  - **#9** Giúp người dùng nhận ra, chẩn đoán và phục hồi lỗi
- *"Vòng lặp nào AI làm sai?"* → Vòng 1: prompt yêu cầu "chữ trắng trên `#F69D39` đạt WCAG AA", nhưng đó là yêu cầu sai ngay từ đầu.

### 6. Design system, handoff

- *"Đổi biến primary thì màn nào đổi?"* → Demo trực tiếp. Nếu có màn không đổi, nghĩa là có màu đang gán cứng; nói thật và sửa.
- *"Variables và Styles khác gì?"* → Variables là giá trị đơn (màu, số), có thể có nhiều mode như light/dark. Styles là tổ hợp thuộc tính như text style hay effect.
- *"Developer biết TextField báo lỗi khi nào?"* → Chỉ vào mục *User interactions* trong handoff: quy tắc validate và nội dung câu báo lỗi.

---

## C. Bộ nghiên cứu nhanh — làm trong 1–2 ngày để có cơ sở thật

Làm thật, ghi đúng kết quả (kể cả khi khác giả định), rồi thêm mục "Cơ sở dữ liệu" vào `ux/persona.md`. Kết quả khác giả định là chuyện bình thường: cứ sửa persona theo dữ liệu và nói ra khi trình bày, đó là điểm cộng.

### C1. Quan sát hàng chờ (30 phút)
Đứng ở căn tin/quầy vào 2 khung giờ nghỉ. Ghi:

| Ngày | Giờ | Người trong hàng | Thời gian từ lúc xếp hàng đến khi nhận món (bấm 5 người) | Ghi chú |
|---|---|---|---|---|

### C2. Phỏng vấn nhanh 5 bạn (mỗi bạn 5 phút)
1. Giữa hai slot bạn có bao nhiêu phút? Bạn thường ăn uống gì trong lúc đó?
2. Lần gần nhất mua đồ ở căn tin, bạn chờ bao lâu? Có lần nào bỏ ăn vì không kịp không?
3. Bạn từng đặt món qua app nào? Điều gì làm bạn khó chịu nhất?
4. Bạn trả tiền bằng gì: tiền mặt, QR ngân hàng hay ví?
5. Bạn dùng điện thoại gì? Hay cầm một tay hay hai tay khi đi bộ?

Ghi lại nguyên câu trả lời (ẩn danh), sau đó gom thành các nhóm ý giống nhau (affinity map).

### C3. Khảo sát online (tuỳ chọn, Google Form 6 câu)
Số phút nghỉ giữa slot · thời gian chờ thường gặp · tần suất bỏ bữa · phương thức trả tiền · hệ điều hành · có muốn đặt trước không (thang 1–5). Ghi rõ số người trả lời và ngày khảo sát.

### C4. Kiểm thử nhanh prototype (15 phút)
Nhờ 3 bạn làm Flow 1 trên Figma Present, bấm giờ và đếm số chạm. Đây là bằng chứng trực tiếp cho chỉ số "dưới 35 giây, 8 chạm" — câu thầy rất hay hỏi.

| Người | Thời gian | Số chạm | Chỗ bị khựng |
|---|---|---|---|

---

## D. Câu "cứu nguy" khi bị hỏi điều chưa làm

> "Phần đó em chưa kiểm chứng. Hiện em dựa trên [giả định], và nếu làm tiếp em sẽ kiểm tra bằng [phương pháp cụ thể]."

Đừng đoán số, đừng nói "theo nghiên cứu" khi không nêu được nghiên cứu nào.

---

## E. Câu hỏi về quy trình nghiên cứu (thầy hỏi nhiều nhất)

Quy trình thầy muốn thấy: **khảo sát thị trường → phỏng vấn (có thể phỏng vấn AI) để ra persona → UX research → file prompt cho Stitch → AI phản biện → sản phẩm cuối.** Mỗi bước phải có đầu ra lưu trong repo.

| Câu hỏi | Ý trả lời (chỉ dùng khi đã làm thật) |
|---|---|
| Em khảo sát người dùng thế nào? | Khảo sát Google Form 22 câu cho RQ1–RQ5, hỏi về lần gần nhất chứ không hỏi ý kiến về app. Mỗi giả định H1–H5 có ngưỡng đặt trước. Form và sheet phân tích đã chạy thử bằng 20 phản hồi mô phỏng (ghi rõ nhãn Assumed); đang thu phản hồi thật. RQ6 hỏi trực tiếp nhân viên quầy |
| Persona này rút ra từ đâu? | "Em phỏng vấn [N] sinh viên giả lập bằng [AI nào] với bộ [N] câu hỏi, cộng [N] bạn thật (nếu có). Các ý lặp lại nhiều nhất là…, nên persona có các pain point…" — chỉ vào file log phỏng vấn |
| Phỏng vấn AI thì tin được không? | Không thay được người thật. AI hay trả lời theo khuôn mẫu, thiên về câu trả lời "hợp lý". Em dùng nó để nghĩ ra giả thuyết nhanh, rồi kiểm lại với [N] bạn thật hoặc bằng quan sát hàng chờ. Chỗ nào AI và người thật khác nhau, em theo người thật |
| Sao không chọn nhóm người dùng khác (giảng viên, nhân viên quầy)? | Sinh viên là nhóm đông nhất và chịu ràng buộc thời gian gắt nhất. Nhân viên quầy là người dùng phụ, nằm ngoài phạm vi lab |
| UX research em làm những gì? | Kể đúng phương pháp đã dùng: khảo sát Google Form, phỏng vấn mô phỏng AI để tạo giả thuyết, affinity map gom ý, journey map hiện tại (xếp hàng) so với tương lai (đặt trước) |
| Từ research ra prompt Stitch thế nào? | Mỗi dòng trong prompt truy được về một phát hiện. Ví dụ: "phải vừa đi vừa bấm" → "touch target 48 dp"; "không biết quầy mở hay đóng" → trạng thái Kiosk trên Home |
| Nếu chỉ mang sản phẩm cuối lên thì sao? | Đây là lý do thầy yêu cầu quy trình: sản phẩm đẹp nhưng không truy được về nhu cầu thật thì không chứng minh được là đúng người dùng cần |
| Sao app chỉ có 8 màn? Tab Cá nhân, lịch sử, thông báo đâu? | Phạm vi MVP chọn từ P0: đặt nhanh, nhận tại quầy, phục hồi lỗi thanh toán. Em đã thiết kế sẵn 17 màn mở rộng (S09–S25: tài khoản, lịch sử, nhận món, quán đóng, đánh giá…) trong Figma nhưng để ở backlog, chưa đưa vào MVP vì chưa có nghiên cứu người dùng thật xác nhận. Xem `design/extended-screens.md` |

**Câu trả lời trung thực nếu phần research chưa làm:**
> "Em đi thẳng từ persona giả định sang thiết kế, chưa có khảo sát thị trường và phỏng vấn. Đây là điểm yếu lớn nhất của bài. Nếu làm lại em sẽ…"
