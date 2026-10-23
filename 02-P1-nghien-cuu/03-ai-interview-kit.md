# Bộ prompt phỏng vấn AI để xây persona

**Mục đích:** dùng AI đóng vai nhiều sinh viên khác nhau để nhanh chóng có giả thuyết, sau đó **kiểm chứng với 3 người thật**. Đề yêu cầu ghi lại mọi lần dùng AI, nên mỗi prompt và **toàn bộ câu trả lời** phải được dán nguyên văn vào `08-ai-log/01-ai-design-log.md` Phụ lục B.

**Công cụ:** ChatGPT, Gemini hoặc Claude, tuỳ bạn; ghi rõ tên và ngày dùng. Mỗi người được phỏng vấn mở **một cuộc chat mới**, để AI không nhớ câu trả lời của người trước.

---

## Bước 1 — Tạo 5 hồ sơ khác nhau (1 prompt)

```text
Tôi đang làm nghiên cứu UX cho một app đặt đồ ăn trước và nhận tại quầy trong khuôn viên trường đại học ở Việt Nam.
Hãy tạo 5 hồ sơ sinh viên GIẢ LẬP khác nhau rõ rệt, để tôi phỏng vấn từng người. Cần đa dạng về:
năm học, ngành, lịch học (số slot/ngày, thời gian nghỉ giữa slot), số ngày học trên campus mỗi tuần,
ngân sách ăn uống mỗi ngày, thiết bị (Android/iOS, tầm giá), thói quen thanh toán, và mức độ hài lòng với căn tin.
Có ít nhất 1 người KHÔNG thích đặt món qua app và 1 người ít khi ăn ở trường.
Mỗi hồ sơ chỉ 5–6 dòng. Không bịa số liệu thống kê; đây là nhân vật hư cấu.
```

## Bước 2 — Phỏng vấn từng hồ sơ (mỗi hồ sơ một chat mới)

```text
Bạn hãy nhập vai nhân vật dưới đây và trả lời phỏng vấn như một người thật: nói tự nhiên, có lúc do dự,
được phép phàn nàn, phản đối hoặc nói "không biết". KHÔNG được khen sản phẩm chỉ để làm vừa lòng tôi.
Nếu một câu hỏi không hợp với lối sống của nhân vật thì nói thẳng.

[DÁN HỒ SƠ Ở BƯỚC 1]

Tôi sẽ hỏi lần lượt từng câu. Hãy trả lời từng câu một, mỗi câu 3–6 câu văn.
```

Rồi hỏi **từng câu một** (đừng dán cả danh sách cùng lúc):

1. Kể cho mình nghe một ngày đi học bình thường của bạn, từ sáng tới chiều.
2. Giữa hai ca, bạn thường làm gì? Có bao nhiêu phút?
3. Lần gần nhất bạn mua đồ ăn hoặc uống ở trường là khi nào? Kể lại chuyện đó. Bạn chờ bao lâu?
4. Có lần nào bạn bỏ ăn hoặc vào lớp muộn vì mua đồ không? Chuyện xảy ra thế nào?
5. Bạn từng đặt đồ qua app (Grab, ShopeeFood…) khi đang ở trường chưa? Điều gì làm bạn khó chịu nhất?
6. Bạn thường trả tiền bằng gì? Đã bao giờ thanh toán lỗi chưa, lúc đó bạn làm gì?
7. Khi đang đi bộ giữa các tòa, bạn cầm điện thoại thế nào? Có hay bấm nhầm không?
8. Nếu có app cho đặt trước rồi ghé quầy lấy, điều gì sẽ khiến bạn **không** dùng nó?
9. Bạn muốn biết thông tin gì trước khi quyết định đặt? (giá, thời gian, quán mở hay đóng, còn món không…)
10. Còn điều gì về chuyện ăn uống ở trường mà mình chưa hỏi nhưng bạn thấy quan trọng?

> **Lưu ý (D27, 19/10/2026):** câu 8 giả định sẵn giải pháp ("nếu có app cho đặt trước…"), nên là câu dẫn dắt. Khi hỏi người thật, dùng kịch bản ở `02-P1-nghien-cuu/01-p1-research.md` mục 1.2 (chỉ hỏi việc đã xảy ra).
>
> Câu 8 là câu quan trọng nhất: nó buộc AI nói ra điểm yếu, tránh việc chỉ toàn khen.

## Bước 3 — Tổng hợp (một chat mới, dán toàn bộ 5 bản ghi)

```text
Dưới đây là 5 bản ghi phỏng vấn (nhân vật giả lập). Hãy:
1. Liệt kê các ý xuất hiện ở từ 2 người trở lên, ghi rõ người nào nói (A1–A5) và trích nguyên văn một câu làm minh chứng.
2. Liệt kê các ý MÂU THUẪN nhau giữa các người.
3. Đề xuất 1 persona chính và giải thích vì sao chọn nhóm đó, dựa trên số người nhắc tới và mức độ đau.
4. Liệt kê 5 giả thuyết cần kiểm chứng với người thật, mỗi giả thuyết kèm một câu hỏi để hỏi người thật.
Không thêm số liệu thống kê không có trong bản ghi.

[DÁN 5 BẢN GHI]
```

## Bước 4 — Kiểm chứng với 3 người thật (bắt buộc nên làm)

- Hỏi 3 bạn cùng lớp hoặc cùng trường bằng **5 câu giả thuyết** ở Bước 3, cộng câu 2, 3 và 8 ở Bước 2. Mỗi bạn khoảng 5 phút, qua chat cũng được.
- Ghi vào `02-P1-nghien-cuu/02-research.md` mục 2.2. Điền bảng affinity mục 3, **tách cột AI và người thật**.
- Chỗ nào người thật nói khác AI, sửa persona theo người thật và ghi lại sự khác biệt đó. Đây chính là phần "phản biện AI" thầy muốn thấy.

## Bước 5 — Phản biện chính persona bằng AI

```text
Đây là persona và dữ liệu nghiên cứu của tôi. Hãy đóng vai giảng viên UX khó tính và chỉ ra:
(1) chỗ nào trong persona không có dữ liệu chống lưng,
(2) chỗ nào mâu thuẫn (ví dụ thiết bị, thời gian),
(3) 5 câu hỏi khó nhất bạn sẽ hỏi sinh viên về persona này.

[DÁN 03-P2-ux-design/01-persona.md và 02-P1-nghien-cuu/02-research.md]
```

Sửa những chỗ AI chỉ ra (nếu hợp lý), và ghi quyết định chấp nhận / sửa / từ chối vào log như các vòng khác.

---

## Ghi vào AI log (dán vào `08-ai-log/01-ai-design-log.md`)

```markdown
## Phụ lục B: Phỏng vấn AI để xây persona
- Công cụ: [tên] · Ngày: [..]
- B1 Prompt tạo hồ sơ: (nguyên văn) · Câu trả lời: (nguyên văn)
- B2 Phỏng vấn A1…A5: (nguyên văn từng chat)
- B3 Tổng hợp: prompt + câu trả lời nguyên văn
- B4 Kiểm chứng người thật: tóm tắt + khác biệt so với AI
- B5 Phản biện persona: prompt + câu trả lời + quyết định
```

Nhớ bổ sung "phỏng vấn giả lập để xây persona" vào bảng khai báo công cụ AI ở README.
