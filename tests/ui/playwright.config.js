const { defineConfig } = require("@playwright/test");

const PORT = 5177;

module.exports = defineConfig({
  testDir: ".",
  timeout: 30000,
  use: { headless: true, baseURL: `http://127.0.0.1:${PORT}` },
  reporter: [["list"]],
  webServer: {
    command: `npx http-server ../../frontend -p ${PORT} -c-1 -s`,
    port: PORT,
    reuseExistingServer: !process.env.CI,
    timeout: 30000,
  },
});
