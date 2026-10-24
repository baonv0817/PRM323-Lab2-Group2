# Kịch bản thuyết trình BreakBite (33 slide)

Kịch bản viết để **nói thành lời**, không đọc nguyên văn. Đọc trước vài lần, rồi nói lại bằng giọng của mình; chỗ nào quen miệng hơn thì đổi.

- **Bản đầy đủ:** khoảng 20 phút, chưa tính demo. Demo Figma thêm 4 đến 5 phút (slide 28).
- **Bản 10 phút:** chỉ nói các slide có ★, các slide còn lại lướt qua trong một câu hoặc bỏ qua.
- **Xưng hô:** "nhóm em" khi nói về cả nhóm, "em" khi nói về phần mình, gọi "thầy" và "các bạn".
- **Quy tắc nói thật:** dữ liệu phỏng vấn và khảo sát hiện có là do AI mô phỏng; nói ngay từ slide 7 để thầy không phải hỏi.

## Chia người nói (gợi ý, đổi theo nhóm)

| Phần | Slide | Người nói |
|---|---|---|
| Mở đầu, P0, P1 | 1 đến 8 | Người 1 |
| P2 UX | 9 đến 13 | Người 2 |
| P3 UI Concept | 14 đến 18 | Người 3 |
| P4 UI Design | 19 đến 28 | Người 4, demo do Người 5 |
| P5 và tổng kết | 29 đến 33 | Người 5 |

## Bảng thời gian

| # | Slide | Phút | ★ |
|---|---|---|---|
| 1 | Bìa | 0,5 | ★ |
| 2 | Quy trình P0 → P5 | 1,0 | ★ |
| 3 | Vấn đề cần giải quyết | 1,0 | ★ |
| 4 | Các hướng đã cân nhắc | 0,7 | |
| 5 | Giả định, rủi ro, phạm vi | 0,7 | |
| 6 | Kế hoạch nghiên cứu | 0,6 | |
| 7 | Kết quả nghiên cứu hiện có | 0,8 | ★ |
| 8 | Insight → quyết định | 0,7 | |
| 9 | Persona | 0,8 | ★ |
| 10 | User story | 0,5 | |
| 11 | Kiến trúc thông tin | 0,6 | |
| 12 | Ba flow chính | 1,0 | ★ |
| 13 | Wireframe và flow mở rộng | 0,5 | |
| 14 | Tạo giao diện với Stitch | 0,6 | |
| 15 | Ba hướng visual | 0,8 | ★ |
| 16 | AI phản biện và ba vòng chỉnh | 0,8 | |
| 17 | Accept, Modify, Reject | 0,7 | ★ |
| 18 | App Style Guide | 0,6 | |
| 19 | Phản biện giao diện và bản v2 | 1,0 | ★ |
| 20 | Final UI: luồng đặt món | 0,7 | ★ |
| 21 | Trạng thái hệ thống | 0,6 | ★ |
| 22 | Final UI: vòng đời đơn | 0,5 | |
| 23 | App người bán | 0,7 | |
| 24 | Ánh xạ pain point (1/2) | 0,8 | ★ |
| 25 | Ánh xạ pain point (2/2) | 0,6 | ★ |
| 26 | Bản vẽ trong Figma | 0,4 | |
| 27 | Component và responsive | 0,5 | |
| 28 | Prototype và demo | 0,5 + demo | ★ |
| 29 | Accessibility | 0,7 | ★ |
| 30 | Kiểm thử | 0,7 | |
| 31 | Bàn giao Flutter | 0,5 | |
| 32 | Tự chấm Quality Gates | 0,8 | ★ |
| 33 | Tổng kết | 0,7 | ★ |

---

## Mở đầu

**Slide 1 · Bìa**

"Dạ em chào thầy và các bạn. Nhóm em là nhóm 2, lớp SE1919, và hôm nay tụi em xin trình bày Lab 2 với đề tài BreakBite, một app đặt món trước, nhận tại quầy ngay trong campus.
Ý tưởng gói gọn trong một câu: giữa hai slot chỉ có 15 phút nghỉ, tụi em muốn sinh viên ăn kịp mà không phải đứng xếp hàng. Sản phẩm gồm app cho khách 30 màn và app cho người bán 15 màn. Em xin giới thiệu các thành viên: bạn Bảo, bạn Gia Bảo, bạn Pháp, bạn An và bạn Danh."

**Slide 2 · Quy trình P0 đến P5**

"Trước khi vào nội dung, em nói nhanh cách tụi em làm. Tụi em đi đúng sáu phase của môn, từ P0 là xác định vấn đề cho tới P5 là kiểm thử và bàn giao. Mỗi phase có một cổng chấm, từ G0 đến G5, và buổi hôm nay tụi em cũng trình bày theo đúng thứ tự này.
Về công cụ, tụi em dùng Google Stitch để tạo giao diện nháp, Gemini và Claude để phản biện, Figma để dựng và Playwright để kiểm tra prototype. Quy tắc tụi em tự đặt ra là AI không thay phỏng vấn, không thay usability test và không thay quyết định. Chỗ nào chưa có bằng chứng thật thì tụi em ghi rõ là giả định. Em nói luôn: ở góc dưới bên phải, G5 đang là 'chưa test với người', và tụi em sẽ nói rõ lý do ở cuối bài."

## P0 · Xác định vấn đề

**Slide 3 · Vấn đề cần giải quyết**

"Vấn đề tụi em chọn là thế này. Sinh viên học trên campus có lịch học dày, nghỉ giữa hai slot chỉ 15 phút. Căn tin thì đông đúng vào giờ nghỉ chung, xếp hàng một lúc là gần hết giờ, nên nhiều bạn bỏ bữa hoặc vào lớp trễ.
Từ đó tụi em chia thành bốn nỗi đau. Một là hàng chờ đúng giờ nghỉ. Hai là không biết trước quán còn mở không, còn món không, bao lâu xong. Ba là phí hiện ra ở bước cuối nên bị bất ngờ. Bốn là thanh toán lỗi thì mất giỏ hàng.
Chỉ số thành công tụi em đặt là đặt xong một đơn dưới 35 giây và tối đa 8 chạm. Và một điều tụi em rút ra từ AI phản biện: câu problem statement đầu tiên của tụi em có chứa luôn giải pháp, nên tụi em sửa lại chỉ còn mô tả vấn đề, rồi thêm câu hỏi 'làm sao để sinh viên có đồ ăn mà không phải xếp hàng'."

**Slide 4 · Các hướng đã cân nhắc**

"Tụi em cân nhắc bốn hướng và chấm theo tác động nhân với khả năng làm được. App đặt trước nhận tại quầy được 20 điểm, cao nhất, vì nó gỡ được cả thời gian lẫn thông tin. Web đặt qua QR được 12 điểm, hàng chờ ảo được 9, chatbot Zalo được 4.
Ở đây có một chi tiết đáng nói. AI đề xuất tụi em chuyển sang web QR cho nhẹ, nhưng tụi em từ chối, vì đề bài bắt buộc là app mobile và phải bàn giao cho Flutter. Tuy vậy tụi em vẫn giữ web QR làm phương án dự phòng, phòng khi sinh viên ngại cài thêm app."

**Slide 5 · Giả định, rủi ro, phạm vi**

"Slide này là chỗ tụi em tách rõ cái đã biết với cái chưa biết. Bảng bên trái là bảy giả định tụi em cần kiểm chứng, ví dụ giờ nghỉ có thật sự dưới 15 phút không, hay sinh viên có chịu cài app riêng của quán không. Mỗi giả định ghi rõ sẽ kiểm bằng khảo sát, phỏng vấn hay hỏi quầy.
Bên phải là phạm vi. Trong phạm vi là app khách, app người bán, nhận tại quầy và thanh toán bằng QR, ví hoặc tiền mặt. Ngoài phạm vi là giao hàng tận nơi, tích điểm, dark mode và code Flutter. Tụi em cố tình giữ phạm vi hẹp để làm cho chắc."

## P1 · Nghiên cứu

**Slide 6 · Kế hoạch nghiên cứu**

"Về nghiên cứu, tụi em đặt sáu câu hỏi, từ giữa hai slot có thật sự bao nhiêu phút, tới quầy có làm kịp đơn dồn giờ nghỉ không. Có ba hoạt động. Khảo sát Google Form 22 câu, mục tiêu từ 30 sinh viên, hiện đang thu phản hồi. Phỏng vấn mô phỏng bằng AI với năm hồ sơ sinh viên, cái này đã làm. Và hỏi nhân viên quầy, chủ quán, cái này mới ở mức kế hoạch."

**Slide 7 · Kết quả nghiên cứu hiện có** ★

"Em xin nói thẳng chỗ này để thầy khỏi phải hỏi. Toàn bộ số liệu trên slide là dữ liệu AI mô phỏng, không phải lời của sinh viên thật. Tụi em dùng nó để thử bộ câu hỏi và để tạo giả thuyết.
Ví dụ, trong năm hồ sơ mô phỏng thì bốn người muốn biết trước trạng thái quán, ba người từng bỏ mua vì hàng chờ. Hai mươi phản hồi khảo sát thử cũng vậy, chỉ để chạy thử bảng phân tích. Nên tụi em không dùng các con số này làm bằng chứng và không khẳng định tỉ lệ nào. Khi khảo sát thật có kết quả thì tụi em sẽ thay phần này."

**Slide 8 · Insight → quyết định thiết kế**

"Dù dữ liệu còn mô phỏng, tụi em vẫn buộc mỗi insight phải nối tới một quyết định thiết kế để có thể truy vết. Ví dụ hàng chờ giờ nghỉ dẫn tới việc đặt trước và hẹn giờ nhận. Ngại phí ẩn dẫn tới giá cộng dồn ngay trên nút. Không muốn đăng ký thì cho xem menu mà không cần tài khoản. Insight về lỗi thanh toán chỉ có một nguồn nên tụi em ghi độ tin cậy thấp, nhưng vẫn làm màn phục hồi vì rủi ro mất giỏ hàng khá nặng."

## P2 · Thiết kế trải nghiệm

**Slide 9 · Persona** ★

"Từ đó tụi em dựng persona. Persona chính là Nguyễn Minh Quân, sinh viên năm hai, học nhiều slot liền, nghỉ 15 phút, hay cầm điện thoại một tay khi đi bộ và mạng thì chập chờn. Mục tiêu của bạn ấy là đặt xong dưới 35 giây.
Persona phụ là Mỹ Linh, tính từng nghìn, cần thấy tổng tiền thật trước khi trả. Cô Hạnh là nhân viên quầy, vừa nấu vừa trả món, nên tụi em có hẳn app người bán cho cô. Và nhóm cuối là Tuấn và Hà, ít lên trường, không phải đối tượng nhắm tới, nhưng tụi em ghi thành rủi ro. Tụi em cũng gắn nhãn cho từng trường là có bằng chứng hay chỉ là giả định."

**Slide 10 · User story**

"Từ persona tụi em viết mười hai user story, mỗi story có tiêu chí chấp nhận đo được. Ví dụ story đầu: 'đặt và trả tiền trước khi xuống quầy', tiêu chí là từ trang chủ tới mã nhận đồ trong tối đa tám chạm. Hay story về thao tác một tay: nút chính nằm nửa dưới màn hình và vùng chạm từ 48 dp. Chuỗi truy vết từ insight tới test nằm trong file persona mapping."

**Slide 11 · Kiến trúc thông tin**

"Về kiến trúc thông tin, app khách có bốn tab ở thanh dưới: Trang chủ, Thực đơn, Đơn hàng, Cá nhân. Các màn con xếp theo tab như trên slide. App người bán cũng bốn tab: Đơn, Quét mã, Món, Quán. Tụi em giữ số tab ít để một tay bấm tới được."

**Slide 12 · Ba flow chính** ★

"Đây là ba flow bắt buộc, và ảnh trên slide là màn Figma thật. Flow một là đặt nhanh: chạm dấu cộng để thêm món, xem giỏ, tiếp tục thanh toán, xác nhận đặt đơn, rồi xác nhận ở cổng thanh toán và nhận mã. Flow hai là tuỳ chỉnh món và nhập mã giảm giá, trong đó mã hết hạn sẽ báo lỗi ngay tại ô nhập. Flow ba là lỗi thanh toán: giỏ hàng vẫn được giữ, khách chọn trả tiền mặt tại kiosk, và nếu đổi ý thì huỷ đơn có hộp thoại xác nhận.
Cả ba flow đều có nhánh lỗi, và ngoài ba flow này, tụi em còn vẽ thêm từ F4 tới F13 và ba flow cho người bán."

**Slide 13 · Wireframe và flow mở rộng**

"Trước khi chọn màu, tụi em chốt bố cục bằng wireframe xám. Hình trên slide là tám màn chính ở dạng xám, không màu, chỉ còn thứ bậc khối và một nút chính. Page 02 trong Figma có wireframe cho cả 30 màn khách và app người bán. Em nói thêm là phần đi thử luồng trên wireframe hiện do AI làm, nhóm chưa đi thử với người thật."

## P3 · Ý tưởng giao diện

**Slide 14 · Tạo giao diện với Google Stitch**

"Sang giao diện, tụi em không gõ prompt tự do. Việc đầu tiên là viết file DESIGN.md, trong đó có persona, màu, chữ và tám nguyên tắc thiết kế, viết trước khi mở Stitch. Sau đó tụi em gửi Stitch một prompt có cấu trúc: vai trò nhà thiết kế, mô tả app, light theme, rồi bốn màn đầu tiên là trang chủ, chi tiết món, giỏ hàng và theo dõi đơn. Prompt nguyên văn và ảnh đều lưu trong nhật ký AI. Tụi em coi kết quả của AI là bản nháp để phản biện, không phải thiết kế cuối."

**Slide 15 · Ba hướng visual** ★

"Tụi em so sánh ba hướng cho màn trang chủ, cùng nội dung, cùng khung 360 nhân 800. Hướng A là ấm, thẻ có ảnh, từ Stitch. Hướng B tối giản dạng danh sách. Hướng C nền tối với banner lớn. Em lưu ý trung thực: A là ảnh Stitch thật còn B và C do AI dựng bằng HTML, nên so sánh không hoàn toàn ngang bằng và tụi em có ghi rõ trong tài liệu.
Kết quả chấm: A được 25, B 23, C 15. Quyết định là chọn A, nhưng mượn khối trạng thái quán và banner nhỏ của B. Hướng C bị loại vì nền tối khó đọc ngoài nắng, banner che mất món và đề bài bắt buộc light theme."

**Slide 16 · AI phản biện và ba vòng chỉnh**

"Sau đó tụi em để AI phản biện theo mười heuristic của Nielsen, WCAG và persona, rồi chỉnh ba vòng. Vòng một: chữ trắng trên nút cam khó đọc, nên đổi chữ nút sang màu nâu. Vòng hai: thiếu giỏ hàng trống và dễ xoá nhầm, nên thêm màn giỏ trống và bước xác nhận. Vòng ba: lỗi thanh toán là ngõ cụt, nên thêm màn phục hồi.
Có một chuyện tụi em muốn kể. AI nêu một con số tương phản không đúng, nên tụi em tự đo lại: chữ trắng trên cam thật ra chỉ 2,14 trên 1, còn chữ nâu trên cam là 5,23 trên 1. Vì vậy tụi em không tin con số của AI mà luôn đo lại."

**Slide 17 · Accept, Modify, Reject** ★

"Với mọi đề xuất của AI, tụi em ghi một trong ba quyết định kèm lý do. Accept ví dụ giá cộng dồn trên nút Thêm vào giỏ. Modify ví dụ đổi chữ nút sang nâu. Reject có ba trường hợp: không chuyển sang web QR vì đề bắt buộc app mobile, không dùng concept C nền tối, và không bắt buộc đăng nhập để tích điểm. Tổng cộng hơn bốn mươi quyết định, mỗi quyết định có căn cứ là persona, heuristic hoặc ràng buộc của đề. Đây là phần tụi em muốn nhấn mạnh: AI đề xuất, nhóm là người quyết định."

**Slide 18 · App Style Guide**

"Kết quả của P3 là bộ style guide dùng chung cho hai app. Màu chủ đạo là cam, nhưng cam chỉ dành cho một nút chính mỗi màn và trạng thái đang chọn; nền và thẻ là tông kem trung tính. Chữ dùng Nunito, lưới 4 dp, lề 16, bo góc 8, 12, 16, 24. Có 27 icon vector một nét và bộ component như Chip, NavBar, Card, Button, Dialog, mỗi cái có variant theo trạng thái."

## P4 · Thiết kế giao diện chi tiết

**Slide 19 · Phản biện giao diện và bản v2** ★

"Đến P4, tụi em quay lại đo chính bản của mình trước khi làm tiếp. Dùng Playwright và Figma Plugin API, tụi em phát hiện lỗi lớn nhất không phải nút cam quá to, mà là cả màn dùng chung một họ màu cam be cho mọi vai trò: nó chiếm tới 55% điểm ảnh. Bản v2 giảm xuống còn 4,4%.
Các số khác: emoji trong chữ từ 98 về 0, chữ thiếu tương phản từ 8 chỗ về 0, vùng bấm dưới 48 dp từ 20 trên 39 về 0 trên 217. Em nói rõ một điều: báo cáo đo này do công cụ AI viết nên chưa độc lập; việc nhờ một AI khác phản biện thêm tụi em chưa chạy, và đây là việc còn lại."

**Slide 20 · Final UI: luồng đặt món** ★

"Đây là tám màn của luồng đặt món ở bản v2, từ onboarding, trang chủ, thực đơn, chi tiết món, giỏ hàng, thanh toán, theo dõi đơn tới lịch sử. Mỗi màn chỉ có một nút cam, nền kem, thẻ trắng, một bộ icon, vùng bấm từ 48 dp và chữ từ 14 sp. Địa điểm nhận trong app là Kiosk Campus Quận 9, tầng 2 và tầng 4."

**Slide 21 · Trạng thái hệ thống** ★

"Một giao diện tốt không chỉ có màn đẹp mà còn phải xử lý lúc mọi thứ không suôn sẻ. Tụi em thiết kế đủ bốn loại trạng thái. Rỗng: giỏ hàng trống thì gợi ý món. Đang tải: đang kết nối cổng thanh toán. Lỗi: thanh toán thất bại nhưng giỏ hàng vẫn được giữ và có lối đi tiếp. Thành công: đã nhận đơn, hiện mã QR và bốn bước của đơn."

**Slide 22 · Final UI: vòng đời đơn và tài khoản**

"Từ S09 tới S30 là phần còn lại của app khách: sửa và huỷ đơn, lịch sử, yêu thích, đặt lại, tài khoản, thông báo, nhận món bằng QR, quán đóng, món hết, đánh giá, báo sự cố, hẹn giờ, đăng nhập, chọn kiosk, tìm kiếm, mã giảm giá và mất mạng. Mỗi tình huống kể cả tìm kiếm không ra kết quả hay mất kết nối đều có màn riêng. Đăng nhập là không bắt buộc."

**Slide 23 · App người bán**

"Màn của khách hứa nhiều việc mà quầy phải làm được: nhận đơn, báo sẵn sàng, quét mã QR để giao món, thu tiền mặt, báo hết món, bật tắt nhận đơn, từ chối đơn, hoàn tiền. Vì vậy tụi em làm luôn app người bán 15 màn, dùng chung hệ thiết kế, bốn tab Đơn, Quét mã, Món, Quán. Tụi em cũng chú ý để thanh toán luôn hiện trên thẻ đơn, nhân viên nhìn là biết đơn nào đã trả, đơn nào cần thu tiền mặt."

**Slide 24 · Ánh xạ pain point (1/2)** ★

"Slide này trả lời câu hỏi 'màn nào giải nỗi đau nào'. Bên trái là pain point, ở giữa là cách tụi em giải, bên phải là các màn cụ thể.
Hàng chờ đúng giờ nghỉ thì giải bằng đặt từ lớp, hẹn giờ nhận và nhận bằng mã QR, tương ứng các màn trang chủ, hẹn giờ, theo dõi đơn và nhận món. Không biết quán còn mở hay còn món thì có màn quán đóng, món hết có gợi ý thay thế, giờ dự kiến sẵn sàng ở giỏ hàng và thông báo. Ngại phí ẩn thì giá cộng dồn ngay trên nút ở chi tiết món, tổng chi tiết ở giỏ hàng và màn chọn mã giảm giá."

**Slide 25 · Ánh xạ pain point (2/2)** ★

"Tiếp theo. Lỗi thanh toán làm mất giỏ hàng thì có màn lỗi thanh toán giữ giỏ, trả tiền mặt tại kiosk và màn mất kết nối. Nút nhỏ khó bấm một tay thì mọi màn dùng vùng bấm từ 48 dp, nút chính ở đáy màn. Và phía người bán: khách đứng chờ kiểm tra chuyển khoản, hay huỷ khi món đã nấu, thì đơn đã thanh toán hiện sẵn, có quét QR giao món và hộp thoại từ chối đơn. Nguồn pain point là persona và nghiên cứu, mà như em đã nói, dữ liệu này còn là giả định chờ khảo sát thật."

**Slide 26 · Bản vẽ trong Figma**

"Toàn bộ thiết kế nằm trong một file Figma sáu page. Page 1 là user flow dạng storyboard. Page 2 là wireframe xám. Page 3 là Final UI, 58 màn ở hai kích thước 360 và 412. Page 4 là design system. Page 5 là thư viện component. Page 6 là prototype chạy được, lát nữa tụi em sẽ demo."

**Slide 27 · Component và responsive**

"Tụi em dựng một thư viện component duy nhất và mọi màn dùng instance cùng token, không tô màu trực tiếp. Mỗi component có variant theo trạng thái, ví dụ nút có mặc định, nhấn, vô hiệu, đang tải. Mỗi màn có bản 360 dp và bản 412 dp, dựng bằng constraints nên nội dung co giãn, không phải cuộn ngang. Hai ảnh bên phải là màn giỏ hàng ở hai kích thước."

**Slide 28 · Prototype Figma và demo** ★

"Prototype nối cả hai app, hiện có hơn 260 vùng bấm trên 64 khung và 19 điểm bắt đầu. Thêm món hiện thông báo và nút Xem giỏ, chọn được bốn phương thức thanh toán, cổng thanh toán có thể chấp nhận hoặc từ chối, hộp thoại huỷ đơn dạng overlay, nút Back quay đúng màn trước đó. Giờ tụi em xin chạy thử."

> **Demo (4 đến 5 phút), mở Figma Page 06, bấm Present rồi đổi flow trong menu:**
>
> 1. **F1, bắt đầu ở Trang chủ.** "Em là Quân, đang ở lớp, còn 15 phút. Em chạm dấu cộng ở combo Tacos, bấm Xem giỏ, thấy tổng tiền ngay. Tiếp tục thanh toán, chọn ví MoMo, xác nhận đặt đơn. Màn đang kết nối cổng, rồi tới cổng thanh toán, em xác nhận, ra mã nhận #A-204." Đếm to số chạm: "năm chạm, chưa tới tám". Nếu muốn cho thầy thấy cách chọn khác: ở màn Thanh toán chạm VNPAY-QR hoặc Tiền mặt tại Kiosk để đổi phương thức.
> 2. **F2, bắt đầu ở Thực đơn.** Chọn món, vào giỏ, chạm ô mã giảm giá, chọn mã đã hết hạn. "Mã sai thì báo ngay tại ô nhập, không bị đẩy ra chỗ khác."
> 3. **F3, bắt đầu ở màn lỗi thanh toán.** "Thanh toán MoMo lỗi nhưng giỏ hàng vẫn còn." Bấm Tiền mặt tại Kiosk, rồi thử huỷ đơn để cho thấy hộp thoại xác nhận.
> 4. **Người bán, bắt đầu ở K01.** Đăng nhập, mở đơn, nhận đơn, qua màn đang chuẩn bị. Nếu còn thời gian, mở flow K2: mã QR không đọc được thì thu tiền mặt.
>
> Nếu Figma lỗi hoặc chậm: quay lại slide 20 và 21, nói tiếp bằng ảnh tĩnh. Trước buổi thuyết trình nhớ thử link bằng cửa sổ ẩn danh.

## P5 · Kiểm thử và bàn giao

**Slide 29 · Accessibility** ★

"Về khả năng tiếp cận, tụi em đo bằng công cụ chứ không nhìn bằng mắt. Chữ nút nâu trên nền cam đạt 5,23 trên 1, vượt ngưỡng 4,5 của WCAG. Vùng bấm nhỏ nhất là 48 dp, không có vùng nào dưới 48 trong 217 vùng. Chữ nội dung từ 14 sp, chỉ nhãn thanh dưới là 12. Không dùng emoji, trạng thái luôn có chữ hoặc icon đi kèm màu.
Phần tụi em chưa kiểm: trình đọc màn hình, cỡ chữ hệ thống lớn và người dùng thật bị khiếm thị. Em nói trước để thầy biết giới hạn."

**Slide 30 · Kiểm thử**

"Về kiểm thử, tụi em dùng Playwright mở prototype và bấm theo từng flow. Bản cũ chạy 13 trên 13 test đạt, còn đồ thị flow bản v2 là 10 trên 10. Một kết quả hữu ích: đặt đơn từ Trang chủ tới Theo dõi đơn, đi qua thêm món, giỏ hàng, chọn thanh toán và cổng thanh toán, tối thiểu 5 chạm.
Nhưng em muốn nói rõ, kiểm thử tự động chỉ chứng minh prototype đi đúng đường tụi em đã vẽ, không biết người dùng có hiểu hay có vướng không. Vì vậy tụi em đã soạn sẵn kế hoạch usability test với năm nhiệm vụ cho ba đến năm sinh viên, nhưng chưa chạy, nên chưa dám nói app dễ dùng."

**Slide 31 · Bàn giao cho Flutter**

"Để lập trình viên dựng được, tụi em có tài liệu bàn giao. Gồm bảng chuyển token và component trong Figma sang Flutter, ví dụ màu primary thành ColorScheme.primary, Chip thành ChoiceChip, NavBar thành NavigationBar. Mỗi màn có sáu mục: layout, component, trạng thái, tương tác, điều hướng và ràng buộc. Tụi em cũng ghi hành vi khi màn rộng, từ 600 dp trở lên dùng NavigationRail. Đề không yêu cầu viết code nên tụi em dừng ở đặc tả."

**Slide 32 · Tự chấm Quality Gates** ★

"Cuối cùng là phần tụi em tự chấm theo sáu gate của môn. G0 đạt 6 trên 6. G1 có điều kiện vì chưa có phản hồi khảo sát thật. G2 được 5 trên 6 vì chưa đi thử với người thật. G3 đạt. G4 có điều kiện vì chưa chạy Present hết trên prototype v2. Và G5 chưa qua, vì chưa có usability test.
Em cũng xin nói thêm là thang điểm 80% này là rubric nội bộ của môn, không phải một chuẩn quốc tế; riêng phần tương phản dựa trên WCAG 2.2. Tụi em còn viết một bộ mười ba skill để chấm từng gate cho hệ thống của mình. Kết quả là tự chấm, và tụi em chờ thầy xem xét."

**Slide 33 · Tổng kết** ★ (file pptx hiện tại có 32 slide, thiếu slide này; nếu không thêm lại thì nói đoạn dưới ngay sau slide 32 và đóng bài)

"Để tổng kết. AI giúp tụi em rất nhanh ở phần sinh giao diện nháp, mô phỏng phỏng vấn, phản biện theo Nielsen và WCAG, và ghi chép tài liệu. Còn những việc tụi em phải tự làm: xác định vấn đề, chọn persona, tự đo lại con số AI đưa ra, và quyết định Accept, Modify hay Reject.
Việc còn lại tụi em nói thẳng: nhờ một AI khác phản biện độc lập, thu khảo sát thật từ ba mươi sinh viên, chạy usability test với ba đến năm người và chạy Present trọn vẹn trên prototype. Em xin cảm ơn thầy và các bạn đã lắng nghe. Nhóm em sẵn sàng nhận câu hỏi và có thể demo thêm trên Figma."

---

## Câu hỏi thầy có thể hỏi

Xem [`02-phan-bien-hoi-dap.md`](02-phan-bien-hoi-dap.md). Ba câu hay gặp nhất, trả lời ngắn:

- **"Dữ liệu người dùng đâu ra?"** Phỏng vấn và khảo sát hiện có là AI mô phỏng để thử bộ câu hỏi; khảo sát thật đang thu; tụi em không dùng số mô phỏng làm bằng chứng.
- **"Vì sao không làm web?"** Đề bắt buộc app mobile và bàn giao Flutter; web QR giữ làm phương án dự phòng.
- **"AI làm gì, nhóm làm gì?"** AI sinh bản nháp và phản biện; nhóm xác định vấn đề, đo lại số liệu và quyết định từng đề xuất.

## Việc nhớ làm trước giờ trình bày

1. Mở link Figma bằng cửa sổ ẩn danh, thử Present một lượt.
2. Mở sẵn file slide và Figma ở hai cửa sổ; tắt thông báo.
3. Cả nhóm thống nhất người nói theo bảng chia phần và tập một lượt có bấm giờ.
