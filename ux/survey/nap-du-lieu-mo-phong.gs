/**
 * Nạp 20 phản hồi MÔ PHỎNG (SIM-S01…S20) vào Google Sheet kết quả để thử phân tích.
 * - Không đụng vào sheet câu trả lời thật của form.
 * - Tạo 2 sheet: SIM_MoPhong (dữ liệu thử, cùng thứ tự cột với form) và PhanTich (công thức H1–H5).
 * - Ô B1 của PhanTich chọn nguồn: SIM_MoPhong hoặc sheet câu trả lời thật.
 * Cách dùng: dán file này vào cùng project Apps Script → chọn hàm napDuLieuMoPhong → Run.
 */
var SHEET_ID = '1NbuOGWFWtj7noiPPfZCY8vFDO32ianjRirY26dipCA8';
var SIM = 'SIM_MoPhong';

function napDuLieuMoPhong() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var formSheet = timSheetForm(ss);
  var header = formSheet.getRange(1, 1, 1, formSheet.getLastColumn()).getValues()[0];

  // Dữ liệu: [mã, thời gian, Q0 … Q22]
  var data = [["SIM-S01","20/10/2026 19:00","Tôi đồng ý tham gia","Năm 1","Ký túc xá","2","Android","10–15 phút","2–5 phút","Một tay","Hôm nay","6–10 phút","1","Nhịn tới bữa sau","Giá",5,4,5,4,3,"ShopeeFood","Trong tháng này",4,"Phải đăng ký tài khoản","Chuyển khoản / QR ngân hàng","Có","Trả tiền mặt","",""],["SIM-S02","20/10/2026 19:07","Tôi đồng ý tham gia","Năm 2","Nhà trọ gần trường","3","iPhone","Dưới 10 phút","Trên 5 phút","Một tay","Trong tuần này","Trên 10 phút","2–3","Nhịn tới bữa sau, Mua ở ngoài cổng","Không biết gì cả",4,4,5,4,2,"GrabFood, ShopeeFood","Trong tuần này",5,"Không có lý do","Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Có","Đổi sang cách trả khác","Ra căn tin thì hàng dài, đứng 10 phút chưa tới lượt nên bỏ về lớp, nhịn tới trưa.",""],["SIM-S03","20/10/2026 19:14","Tôi đồng ý tham gia","Năm 2","Ký túc xá","2","Android","10–15 phút","2–5 phút","Hai tay","Trong tuần này","6–10 phút","1","Ăn đồ mang theo","Giá, Món nào còn",5,5,5,3,3,"ShopeeFood","Trong tháng này",4,"Phải đăng ký tài khoản, Tốn bộ nhớ","Tiền mặt, Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S04","20/10/2026 19:21","Tôi đồng ý tham gia","Năm 3","Nhà riêng / người thân","2","Android","16–20 phút","Dưới 2 phút","Một tay","Trong tháng này","3–5 phút","0","Không áp dụng","Quán mở hay đóng, Giá",4,3,4,4,4,"Không dùng","Vài tháng trước",2,"Ít khi mua ở trường","Tiền mặt","Không","","",""],["SIM-S05","20/10/2026 19:28","Tôi đồng ý tham gia","Năm 1","Ký túc xá","3","Android","10–15 phút","2–5 phút","Một tay","Hôm nay","6–10 phút","2–3","Mua ở ngoài cổng","Không biết gì cả",5,4,5,5,3,"ShopeeFood, beFood","Trong tháng này",4,"Phải đăng ký tài khoản","Chuyển khoản / QR ngân hàng","Có","Trả tiền mặt","",""],["SIM-S06","20/10/2026 19:35","Tôi đồng ý tham gia","Năm 2","Nhà trọ gần trường","4 trở lên","iPhone","Dưới 10 phút","Trên 5 phút","Một tay","Trong tuần này","Trên 10 phút","4 lần trở lên","Nhịn tới bữa sau, Đặt app giao hàng","Giá",4,4,4,3,2,"GrabFood","Trong tuần này",3,"Đã có app khác, Phải đăng ký tài khoản","Ví điện tử (MoMo, ZaloPay…), Thẻ","Có","Bỏ đơn","Chuyển khoản xong quầy chưa thấy tiền, phải đứng chờ kiểm tra nên vào lớp trễ.",""],["SIM-S07","20/10/2026 19:42","Tôi đồng ý tham gia","Năm 3","Nhà trọ gần trường","2","Android","10–15 phút","2–5 phút","Hai tay","Trong tuần này","6–10 phút","1","Nhịn tới bữa sau","Không biết gì cả",5,5,5,4,3,"ShopeeFood","Trong tháng này",5,"Không có lý do","Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S08","20/10/2026 19:49","Tôi đồng ý tham gia","Năm 4 trở lên","Ký túc xá","3","iPhone","Trên 20 phút","Dưới 2 phút","Không dùng khi đi bộ","Trong tháng này","Dưới 3 phút","0","Không áp dụng","Quán mở hay đóng, Giá",3,4,4,4,3,"GrabFood, ShopeeFood","Vài tháng trước",3,"Ít khi mua ở trường, Tốn bộ nhớ","Tiền mặt, Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S09","20/10/2026 19:56","Tôi đồng ý tham gia","Năm 2","Nhà riêng / người thân","2","Android","16–20 phút","2–5 phút","Một tay","Lâu hơn","Không nhớ","0","Không áp dụng","Giá",4,3,3,4,4,"Không dùng","Không nhớ",2,"Ít khi mua ở trường","Tiền mặt","Không","","",""],["SIM-S10","20/10/2026 20:03","Tôi đồng ý tham gia","Năm 1","Ký túc xá","2","Android","10–15 phút","2–5 phút","Một tay","Hôm nay","6–10 phút","2–3","Mua ở ngoài cổng","Không biết gì cả",5,5,5,4,3,"ShopeeFood","Trong tuần này",4,"Tốn bộ nhớ","Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Có","Thử lại cách cũ","Không biết quán hết bánh mì, đi xuống rồi mới biết, quay lên không kịp mua chỗ khác.",""],["SIM-S11","20/10/2026 20:10","Tôi đồng ý tham gia","Năm 3","Nhà trọ gần trường","3","Android","Dưới 10 phút","Trên 5 phút","Một tay","Trong tuần này","6–10 phút","2–3","Nhịn tới bữa sau","Giá",4,4,5,3,2,"GrabFood","Vài tháng trước",3,"Phải đăng ký tài khoản, Lo về thanh toán","Tiền mặt, Chuyển khoản / QR ngân hàng","Có","Trả tiền mặt","Giờ nghỉ 10 phút mà phòng ở tầng 5, xuống tới nơi đông quá nên thôi.",""],["SIM-S12","20/10/2026 20:17","Tôi đồng ý tham gia","Năm 2","Ký túc xá","2","iPhone","10–15 phút","2–5 phút","Hai tay","Trong tuần này","3–5 phút","0","Không áp dụng","Quán mở hay đóng",5,4,5,4,3,"ShopeeFood, Xanh SM Ngon","Trong tháng này",5,"Không có lý do","Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S13","20/10/2026 20:24","Tôi đồng ý tham gia","Năm 1","Nhà riêng / người thân","1","Android","Không nhớ","Dưới 2 phút","Một tay","Chưa bao giờ","","","","Không biết gì cả",3,3,3,4,3,"Không dùng","Vài tháng trước",1,"Ít khi mua ở trường, Đã có app khác","Tiền mặt","Không","","",""],["SIM-S14","20/10/2026 20:31","Tôi đồng ý tham gia","Năm 2","Nhà trọ gần trường","3","Android","10–15 phút","2–5 phút","Một tay","Trong tuần này","6–10 phút","1","Ăn đồ mang theo","Giá, Món nào còn",5,5,5,5,4,"ShopeeFood","Trong tháng này",4,"Phải đăng ký tài khoản","Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Có","Đổi sang cách trả khác","",""],["SIM-S15","20/10/2026 20:38","Tôi đồng ý tham gia","Năm 3","Ký túc xá","2","iPhone","16–20 phút","Dưới 2 phút","Hai tay","Trong tháng này","3–5 phút","0","Không áp dụng","Giá",4,4,4,3,2,"GrabFood, ShopeeFood","Vài tháng trước",3,"Tốn bộ nhớ, Đã có app khác","Tiền mặt, Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S16","20/10/2026 20:45","Tôi đồng ý tham gia","Năm 4 trở lên","Nhà trọ gần trường","2","Android","Dưới 10 phút","Trên 5 phút","Một tay","Trong tuần này","Trên 10 phút","2–3","Đặt app giao hàng, Mua ở ngoài cổng","Không biết gì cả",4,4,4,4,3,"ShopeeFood","Trong tuần này",4,"Phải đăng ký tài khoản, Lo về thanh toán","Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Có","Trả tiền mặt","Đặt ShopeeFood nhưng shipper không vào được tòa nhà, phải chạy ra cổng lấy.",""],["SIM-S17","20/10/2026 20:52","Tôi đồng ý tham gia","Năm 2","Ký túc xá","3","iPhone","10–15 phút","2–5 phút","Một tay","Hôm nay","6–10 phút","1","Nhịn tới bữa sau","Giá",5,5,5,4,3,"GrabFood","Trong tháng này",5,"Tốn bộ nhớ","Chuyển khoản / QR ngân hàng","Không","","",""],["SIM-S18","20/10/2026 20:59","Tôi đồng ý tham gia","Năm 1","Nhà riêng / người thân","2","Android","Trên 20 phút","Dưới 2 phút","Không dùng khi đi bộ","Chưa bao giờ","","","","Không biết gì cả",4,4,5,4,3,"Không dùng","Không nhớ",2,"Ít khi mua ở trường, Phải đăng ký tài khoản","Tiền mặt","Không","","",""],["SIM-S19","20/10/2026 21:06","Tôi đồng ý tham gia","Năm 3","Nhà trọ gần trường","3","Android","10–15 phút","2–5 phút","Hai tay","Trong tuần này","3–5 phút","0","Không áp dụng","Quán mở hay đóng, Giá",5,4,5,4,4,"ShopeeFood, beFood","Trong tháng này",4,"Phải đăng ký tài khoản, Tốn bộ nhớ","Tiền mặt, Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Có","Thử lại cách cũ","",""],["SIM-S20","20/10/2026 21:13","Tôi đồng ý tham gia","Năm 2","Ký túc xá","2","iPhone","16–20 phút","2–5 phút","Một tay","Trong tháng này","Dưới 3 phút","0","Không áp dụng","Giá",4,4,4,3,2,"GrabFood","Vài tháng trước",3,"Đã có app khác, Lo về thanh toán","Chuyển khoản / QR ngân hàng, Ví điện tử (MoMo, ZaloPay…)","Không","","",""]];
  if (header.length !== data[0].length - 1) {
    throw new Error('Sheet form có ' + header.length + ' cột, dữ liệu thử có ' + (data[0].length - 1) + ' cột.');
  }
  var values = data.map(function (r) {
    var p = r[1].split(/[\/ :]/); // dd/mm/yyyy hh:mm
    var ts = new Date(+p[2], +p[1] - 1, +p[0], +p[3], +p[4]);
    return [ts].concat(r.slice(2)).concat([r[0]]);
  });

  var sim = taoLaiSheet(ss, SIM);
  sim.getRange(1, 1, 1, header.length + 1).setValues([header.concat(['Mã (mô phỏng)'])])
     .setFontWeight('bold').setBackground('#622B14').setFontColor('#FFFFFF');
  sim.getRange(2, 1, values.length, values[0].length).setValues(values);
  sim.getRange(2, 1, values.length, 1).setNumberFormat('dd/MM/yyyy HH:mm');
  sim.getRange('A1').setNote('DỮ LIỆU MÔ PHỎNG do AI tạo ngày 20/10/2026, theo hướng ủng hộ giả định. Không dùng làm bằng chứng.');
  sim.setTabColor('#B91C1C');
  sim.setFrozenRows(1);

  taoPhanTich(ss, formSheet.getName());
  Logger.log('Đã nạp ' + values.length + ' dòng vào ' + SIM + '. Mở sheet PhanTich để xem kết quả.');
}

function timSheetForm(ss) {
  var sheets = ss.getSheets();
  for (var i = 0; i < sheets.length; i++) {
    if (sheets[i].getFormUrl()) return sheets[i];
  }
  throw new Error('Không tìm thấy sheet câu trả lời của form.');
}

function taoLaiSheet(ss, name) {
  var old = ss.getSheetByName(name);
  if (old) ss.deleteSheet(old);
  return ss.insertSheet(name);
}

function taoPhanTich(ss, formSheetName) {
  var sh = taoLaiSheet(ss, 'PhanTich');
  var R = function (c) { return 'INDIRECT("\'"&$B$1&"\'!' + c + '2:' + c + '")'; };
  var NUM = function (c) { return 'ARRAYFORMULA(VALUE(FILTER(' + R(c) + ',' + R(c) + '<>"")))'; };
  var rows = [
    ['Nguồn dữ liệu', SIM, '', '← chọn ' + SIM + ' (thử) hoặc sheet câu trả lời thật', ''],
    ['Chỉ số', 'Giá trị', 'Ngưỡng', 'Kết luận', 'Câu'],
    ['Số phản hồi', '=COUNTA(' + R('A') + ')', '', '', ''],
    ['H1 · Tỉ lệ nghỉ ≤ 15 phút', '=(COUNTIF(' + R('G') + ',"Dưới 10 phút")+COUNTIF(' + R('G') + ',"10–15 phút"))/B3', 0.5, '=IF(B4>=C4,"Đạt","Không đạt")', 'Q5'],
    ['Số người từng mua ở trường', '=COUNTA(' + R('L') + ')', '', '', 'Q8'],
    ['H2 · Tỉ lệ bỏ mua ≥ 1 lần / 7 ngày', '=(B5-SUMPRODUCT(--(TO_TEXT(' + R('L') + ')="0")))/B5', 0.4, '=IF(B6>=C6,"Đạt","Không đạt")', 'Q10'],
    ['H2 · Tỉ lệ chờ ≥ 6 phút', '=(COUNTIF(' + R('K') + ',"6–10 phút")+COUNTIF(' + R('K') + ',"Trên 10 phút"))/B5', 0.5, '=IF(B7>=C7,"Đạt","Không đạt")', 'Q9'],
    ['H3 · Điểm TB: quán mở/đóng', '=AVERAGE(' + NUM('O') + ')', 4, '=IF(B8>=C8,"Đạt","Không đạt")', 'Q13'],
    ['H3 · Điểm TB: thời gian chờ', '=AVERAGE(' + NUM('Q') + ')', 4, '=IF(B9>=C9,"Đạt","Không đạt")', 'Q13'],
    ['H3 · Tỉ lệ "Không biết gì cả" trước khi mua', '=COUNTIF(' + R('N') + ',"Không biết gì cả")/B3', '', 'Tham khảo', 'Q12'],
    ['H4 · Tỉ lệ chọn 4–5 khả năng cài app', '=SUMPRODUCT(--(' + NUM('V') + '>=4))/B3', 0.5, '=IF(B11>=C11,"Đạt","Không đạt")', 'Q16'],
    ['H4 · Lý do: Phải đăng ký tài khoản', '=COUNTIF(' + R('W') + ',"*đăng ký*")', '', 'Tham khảo', 'Q17'],
    ['H4 · Lý do: Tốn bộ nhớ', '=COUNTIF(' + R('W') + ',"*bộ nhớ*")', '', 'Tham khảo', 'Q17'],
    ['H4 · Lý do: Ít khi mua ở trường', '=COUNTIF(' + R('W') + ',"*Ít khi*")', '', 'Tham khảo', 'Q17'],
    ['Số người từng lỗi thanh toán', '=COUNTIF(' + R('Y') + ',"Có")', '', '', 'Q19'],
    ['H5 · Tỉ lệ xử lý bằng tiền mặt / đổi cách trả', '=(COUNTIF(' + R('Z') + ',"Trả tiền mặt")+COUNTIF(' + R('Z') + ',"Đổi sang cách trả khác"))/B15', 0.5, '=IF(B16>=C16,"Đạt","Không đạt")', 'Q20']
  ];
  sh.getRange(1, 1, rows.length, 5).setValues(rows);
  sh.getRange('B1').setDataValidation(
    SpreadsheetApp.newDataValidation().requireValueInList([SIM, formSheetName], true).build()
  ).setBackground('#FDE68A').setFontWeight('bold');
  sh.getRange('A2:E2').setFontWeight('bold').setBackground('#622B14').setFontColor('#FFFFFF');
  ['B4', 'B6', 'B7', 'B10', 'B11', 'B16', 'C4', 'C6', 'C7', 'C11', 'C16'].forEach(function (a) {
    sh.getRange(a).setNumberFormat('0%');
  });
  sh.getRange('B8:B9').setNumberFormat('0.00');
  sh.getRange('A18').setValue('Khi B1 = ' + SIM + ': dữ liệu MÔ PHỎNG, nhãn Assumed, không dùng làm bằng chứng.')
    .setFontColor('#B91C1C').setFontWeight('bold');
  sh.setColumnWidth(1, 330);
  sh.setColumnWidth(4, 120);
  sh.activate();
}
