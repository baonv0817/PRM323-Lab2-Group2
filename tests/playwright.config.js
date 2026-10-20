const { defineConfig } = require('@playwright/test');

// Dùng Edge cài sẵn trên máy (channel: 'msedge') nên không phải tải trình duyệt riêng.
// Đổi sang 'chrome' hoặc bỏ dòng channel nếu đã chạy `npx playwright install chromium`.
module.exports = defineConfig({
  testDir: './figma-proto',
  timeout: 120000,
  retries: 1,
  workers: 1, // chạy tuần tự để không dồn tải lên Figma
  reporter: [['list'], ['html', { outputFolder: 'playwright-report', open: 'never' }]],
  snapshotPathTemplate: '{testDir}/__screenshots__/{arg}{ext}',
  use: {
    channel: 'msedge',
    headless: true,
    viewport: { width: 420, height: 880 },
    deviceScaleFactor: 2,
    locale: 'vi-VN',
  },
});
