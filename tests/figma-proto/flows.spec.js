// Bấm thật trên prototype Figma (Page 06) và so từng bước với ảnh chuẩn trong __screenshots__/.
// Lần đầu (hoặc khi chủ động sửa Figma): `npm run update`, rồi XEM LẠI ảnh trước khi commit.
const { test } = require('@playwright/test');
const { openAt, tap, shot } = require('./helpers');

test.describe('F1 · Đặt nhanh, nhận tại quầy', () => {
  test('đường nhanh: S01 → S02 → S05 → S06 → S07', async ({ page }) => {
    const c = await openAt(page, 'S01');
    await shot(c, 'F1a-01-S01');
    await tap(c, 'S01', 'CTA_Bắt_Đầu');            await shot(c, 'F1a-02-S02');
    await tap(c, 'S02', 'Quick_Add_Tacos');        await shot(c, 'F1a-03-S05');
    await tap(c, 'S05', 'Cart_Confirm_Checkout');  await shot(c, 'F1a-04-S06');
    await tap(c, 'S06', 'Pay_MoMo_Success');       // S06-LOADING, tự chuyển sau 1,2 giây
    await page.waitForTimeout(2200);               await shot(c, 'F1a-05-S07');
  });

  test('đường có chọn topping: S02 → S04 → S05', async ({ page }) => {
    const c = await openAt(page, 'S01');
    await tap(c, 'S01', 'CTA_Bắt_Đầu');
    await tap(c, 'S02', 'Card_Tacos_Bo');          await shot(c, 'F1b-01-S04');
    await tap(c, 'S04', 'Add_To_Cart_CTA');        await shot(c, 'F1b-02-S05');
  });
});

test.describe('F2 · Tuỳ chỉnh món và mã giảm giá', () => {
  test('S03 → S04 → S05 → mã sai → nhập lại → S06', async ({ page }) => {
    const c = await openAt(page, 'S03');
    await shot(c, 'F2-01-S03');
    await tap(c, 'S03', 'Menu_Item_Detail');       await shot(c, 'F2-02-S04');
    await tap(c, 'S04', 'Add_To_Cart_CTA');        await shot(c, 'F2-03-S05');
    await tap(c, 'S05', 'Voucher');                await shot(c, 'F2-04-S05-VOUCHER-ERR');
    await tap(c, 'S05-VOUCHER-ERR', 'Voucher');    await shot(c, 'F2-05-S05-nhap-lai');
    await tap(c, 'S05', 'Cart_Confirm_Checkout');  await shot(c, 'F2-06-S06');
  });
});

test.describe('F3 · Lỗi thanh toán và phục hồi', () => {
  test('S06 → S06-ERR → trả tiền mặt → S07-CASH', async ({ page }) => {
    const c = await openAt(page, 'S06');
    await shot(c, 'F3a-01-S06');
    await tap(c, 'S06', 'MoMo_Error_Trigger');     await shot(c, 'F3a-02-S06-ERR');
    await tap(c, 'S06-ERR', 'Retry_VNPAY_Cash');   await shot(c, 'F3a-03-S07-CASH');
  });

  test('S06-ERR → quay lại giỏ hàng (giỏ vẫn giữ)', async ({ page }) => {
    const c = await openAt(page, 'S06');
    await tap(c, 'S06', 'MoMo_Error_Trigger');
    await tap(c, 'S06-ERR', 'Back_To_Cart');       await shot(c, 'F3b-01-S05');
  });
});

test.describe('Huỷ đơn (dialog overlay)', () => {
  test('S07-CASH → mở dialog → Giữ đơn → đóng', async ({ page }) => {
    const c = await openAt(page, 'S07-CASH');
    await shot(c, 'D-01-S07-CASH');
    await tap(c, 'S07-CASH', 'Cancel_Dialog_Trigger'); await shot(c, 'D-02-dialog-mo');
    // Dialog nằm giữa khung: vùng bấm tính theo khung 320 × 180 đặt giữa màn hình 360 × 800.
    const hs = require('./hotspots.json').frames['S07-DIALOG'].hotspots.find((h) => h.name === 'Dialog_Keep_Order');
    const ox = (360 - 320) / 2, oy = (800 - 180) / 2;
    await page.mouse.click(c.rect.x + (ox + hs.x + hs.w / 2) * c.k, c.rect.y + (oy + hs.y + hs.h / 2) * c.k);
    await page.waitForTimeout(900);                    await shot(c, 'D-03-dialog-dong');
  });
});
