/**
 * Tạo Google Form khảo sát cho P1 · UX Research (BreakBite).
 * Cách dùng: dán vào https://script.google.com → Run → cho phép quyền → xem Execution log.
 * Câu hỏi và cách đọc kết quả: 02-P1-nghien-cuu/khao-sat/khao-sat-cau-hoi.md
 */
function taoFormKhaoSat() {
  var form = FormApp.create('Khảo sát: Ăn uống trong giờ nghỉ giữa các slot');
  form.setDescription(
    'Khảo sát ẩn danh khoảng 3 phút cho bài học môn PRM323. ' +
    'Câu hỏi về những lần bạn mua đồ ăn/uống ở trường gần đây. Không có câu trả lời đúng hay sai.'
  );
  form.setProgressBar(true);
  form.setCollectEmail(false);
  form.setConfirmationMessage('Cảm ơn bạn đã tham gia!');

  // Phần 0 · Đồng ý
  form.addCheckboxItem()
    .setTitle('Khảo sát ẩn danh, chỉ dùng cho bài học môn PRM323. Bạn có thể dừng bất cứ lúc nào.')
    .setChoiceValues(['Tôi đồng ý tham gia'])
    .setRequired(true);

  // Phần 1 · Về bạn
  form.addPageBreakItem().setTitle('Phần 1 · Về bạn');
  mc(form, 'Bạn là sinh viên năm mấy?', ['Năm 1', 'Năm 2', 'Năm 3', 'Năm 4 trở lên']);
  mc(form, 'Bạn đang ở đâu?', ['Ký túc xá', 'Nhà trọ gần trường', 'Nhà riêng / người thân'], true);
  mc(form, 'Một ngày học bình thường bạn có mấy slot trên trường?', ['1', '2', '3', '4 trở lên']);
  mc(form, 'Bạn dùng điện thoại gì?', ['Android', 'iPhone'], true);

  // Phần 2 · Giờ nghỉ
  form.addPageBreakItem().setTitle('Phần 2 · Giờ nghỉ giữa hai slot');
  mc(form, 'Giữa hai slot gần nhất của bạn có bao nhiêu phút nghỉ?',
     ['Dưới 10 phút', '10–15 phút', '16–20 phút', 'Trên 20 phút', 'Không nhớ']);
  mc(form, 'Đi từ phòng này sang phòng học tiếp theo thường mất bao lâu?',
     ['Dưới 2 phút', '2–5 phút', 'Trên 5 phút']);
  mc(form, 'Khi vừa đi vừa dùng điện thoại giữa các khu trong campus, bạn thường cầm máy thế nào?',
     ['Một tay', 'Hai tay', 'Không dùng khi đi bộ']);
  var q8 = form.addMultipleChoiceItem()
    .setTitle('Lần gần nhất bạn mua đồ ăn/uống ở trường (căn tin, quầy, kiosk) là khi nào?')
    .setRequired(true);

  // Phần 3 · Lần mua gần nhất
  var p3 = form.addPageBreakItem().setTitle('Phần 3 · Lần mua gần nhất ở trường');
  mc(form, 'Lần đó, từ lúc bắt đầu xếp hàng tới lúc cầm được món mất bao lâu?',
     ['Dưới 3 phút', '3–5 phút', '6–10 phút', 'Trên 10 phút', 'Không nhớ']);
  mc(form, 'Trong 7 ngày qua, bạn đã bao nhiêu lần định mua ở trường nhưng bỏ vì đông hoặc không kịp?',
     ['0', '1', '2–3', '4 lần trở lên']);
  cb(form, 'Những lần bỏ mua đó, bạn đã làm gì?',
     ['Nhịn tới bữa sau', 'Mua ở ngoài cổng', 'Đặt app giao hàng', 'Ăn đồ mang theo', 'Không áp dụng'], true);

  // Phần 4 · Trước khi mua
  var p4 = form.addPageBreakItem().setTitle('Phần 4 · Trước khi quyết định mua');
  cb(form, 'Lần gần nhất, trước khi đi mua, bạn đã biết những gì?',
     ['Quán mở hay đóng', 'Món nào còn', 'Giá', 'Phải chờ bao lâu', 'Không biết gì cả']);
  form.addGridItem()
    .setTitle('Mỗi thông tin dưới đây quan trọng thế nào khi bạn quyết định có đi mua hay không? (1 = không quan trọng, 5 = rất quan trọng)')
    .setRows(['Quán đang mở hay đóng', 'Món còn hay hết', 'Thời gian chờ', 'Tổng tiền phải trả', 'Khuyến mãi'])
    .setColumns(['1', '2', '3', '4', '5'])
    .setRequired(true);

  // Phần 5 · App và thanh toán
  form.addPageBreakItem().setTitle('Phần 5 · App và thanh toán');
  cb(form, 'Trong tháng qua bạn đã dùng app đặt đồ ăn nào?',
     ['GrabFood', 'ShopeeFood', 'beFood', 'Xanh SM Ngon', 'Không dùng'], true);
  mc(form, 'Lần gần nhất bạn cài một app mới là khi nào?',
     ['Trong tuần này', 'Trong tháng này', 'Vài tháng trước', 'Không nhớ']);
  form.addScaleItem()
    .setTitle('Nếu quán ăn trong trường có app riêng để đặt trước, khả năng bạn cài là bao nhiêu?')
    .setBounds(1, 5)
    .setLabels('Chắc chắn không', 'Chắc chắn có')
    .setRequired(true);
  cb(form, 'Điều gì có thể khiến bạn KHÔNG cài một app như vậy?',
     ['Phải đăng ký tài khoản', 'Tốn bộ nhớ', 'Ít khi mua ở trường', 'Đã có app khác',
      'Lo về thanh toán', 'Không có lý do'], true);
  cb(form, 'Khi mua đồ ăn ở trường, bạn thường trả bằng gì?',
     ['Tiền mặt', 'Chuyển khoản / QR ngân hàng', 'Ví điện tử (MoMo, ZaloPay…)', 'Thẻ']);
  var q19 = form.addMultipleChoiceItem()
    .setTitle('Bạn đã từng bị lỗi khi thanh toán online lúc mua đồ ăn chưa?')
    .setRequired(true);

  // Phần 6 · Thanh toán lỗi
  var p6 = form.addPageBreakItem().setTitle('Phần 6 · Lần thanh toán lỗi gần nhất');
  mc(form, 'Lần gần nhất bị lỗi, bạn đã làm gì?',
     ['Thử lại cách cũ', 'Đổi sang cách trả khác', 'Trả tiền mặt', 'Bỏ đơn'], true);

  // Phần 7 · Kết thúc
  var p7 = form.addPageBreakItem().setTitle('Phần 7 · Kết thúc');
  form.addParagraphTextItem()
    .setTitle('Kể ngắn lần gần nhất bạn không kịp ăn hoặc uống trong giờ nghỉ: chuyện gì xảy ra? (không bắt buộc)');
  form.addTextItem()
    .setTitle('Bạn có muốn nói chuyện thêm 5 phút không? Nếu có, để lại Zalo hoặc email (không bắt buộc). Thông tin chỉ dùng để liên hệ và sẽ xoá sau khi xong bài.');

  // Rẽ nhánh
  q8.setChoices([
    q8.createChoice('Hôm nay', p3),
    q8.createChoice('Trong tuần này', p3),
    q8.createChoice('Trong tháng này', p3),
    q8.createChoice('Lâu hơn', p3),
    q8.createChoice('Chưa bao giờ', p4)
  ]);
  q19.setChoices([
    q19.createChoice('Có', p6),
    q19.createChoice('Không', p7)
  ]);

  // Sheet nhận câu trả lời
  var ss = SpreadsheetApp.create('Kết quả - Khảo sát giờ nghỉ (PRM323)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Link gửi khảo sát: ' + form.getPublishedUrl());
  Logger.log('Link sửa form:     ' + form.getEditUrl());
  Logger.log('Google Sheet:      ' + ss.getUrl());
}

/** Câu hỏi 1 lựa chọn, bắt buộc. */
function mc(form, title, choices, hasOther) {
  var item = form.addMultipleChoiceItem().setTitle(title).setChoiceValues(choices).setRequired(true);
  if (hasOther) item.showOtherOption(true);
  return item;
}

/** Câu hỏi nhiều lựa chọn, bắt buộc. */
function cb(form, title, choices, hasOther) {
  var item = form.addCheckboxItem().setTitle(title).setChoiceValues(choices).setRequired(true);
  if (hasOther) item.showOtherOption(true);
  return item;
}
