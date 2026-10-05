// Rendered-UI + accessibility tests for the Daily Stock Advisor dashboard.
// Backend-independent: /api/recommend is intercepted, so these tests verify the
// real shipped markup/JS (states, cards, confidence, keyboard, disclaimer) and
// run axe-core against BOTH the light and the dark theme (spec §13.3/§13.4, AC-11).

const { test, expect } = require("@playwright/test");
const AxeBuilder = require("@axe-core/playwright").default;

const PAGE_URL = "/index.html";

const WATCHLIST = {
  watchlist: [
    { ticker: "NVDA", rationale: "Largest technology gainer today; broad advance.", confidence: 0.9 },
    { ticker: "ORCL", rationale: "Steady technology gainer aligned to the profile.", confidence: 0.8 },
    { ticker: "XOM", rationale: "Energy exposure per the selected sectors.", confidence: 0.6 },
  ],
  disclaimer: "This is not financial advice.",
};

async function mockRecommend(page, status = 200) {
  await page.route("**/api/recommend", async (route) => {
    if (status !== 200) {
      await route.fulfill({ status, contentType: "application/json", body: JSON.stringify({ detail: "model_unavailable" }) });
      return;
    }
    await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify(WATCHLIST) });
  });
}

async function axeClean(page) {
  const results = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"]).analyze();
  const serious = results.violations.filter((v) => v.impact === "critical" || v.impact === "serious");
  expect(serious, JSON.stringify(serious.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length })), null, 2)).toEqual([]);
}

test("empty state renders on load", async ({ page }) => {
  await page.goto(PAGE_URL);
  await expect(page.locator("#results")).toContainText("Set a profile");
  await expect(page.getByRole("note")).toContainText("Not financial advice");
});

test("submitting a profile renders a grounded watchlist with confidence", async ({ page }) => {
  await mockRecommend(page);
  await page.goto(PAGE_URL);
  await page.getByRole("button", { name: "Get recommendations" }).click();
  await expect(page.locator(".entry")).toHaveCount(3);
  await expect(page.locator(".entry").first()).toContainText("NVDA");
  await expect(page.locator(".entry").first().locator(".cal .val")).toHaveText("0.90");
  await expect(page.getByRole("img", { name: /Confidence 0.90 of 1/ })).toBeVisible();
});

test("reasoning expands and collapses (Escape closes)", async ({ page }) => {
  await mockRecommend(page);
  await page.goto(PAGE_URL);
  await page.getByRole("button", { name: "Get recommendations" }).click();
  const expand = page.locator(".entry").first().getByRole("button", { name: "Show reasoning" });
  await expand.click();
  await expect(page.locator("#note-0")).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(page.locator("#note-0")).toBeHidden();
});

test("error state renders when the API fails", async ({ page }) => {
  await mockRecommend(page, 503);
  await page.goto(PAGE_URL);
  await page.getByRole("button", { name: "Get recommendations" }).click();
  await expect(page.locator("#results")).toContainText("Could not produce a grounded watchlist");
});

test("accessibility: light theme has no critical/serious axe violations", async ({ page }) => {
  await mockRecommend(page);
  await page.goto(PAGE_URL);
  await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
  await page.getByRole("button", { name: "Get recommendations" }).click();
  await expect(page.locator(".entry")).toHaveCount(3);
  await axeClean(page);
});

test("accessibility: dark theme has no critical/serious axe violations", async ({ page }) => {
  await mockRecommend(page);
  await page.goto(PAGE_URL);
  await page.getByRole("button", { name: /mode$/ }).click();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await page.getByRole("button", { name: "Get recommendations" }).click();
  await expect(page.locator(".entry")).toHaveCount(3);
  await axeClean(page);
});
