from playwright.async_api import async_playwright

class BrowserManager:
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def capture_screenshot(self, url: str, output_path: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            page = await browser.new_page()
            await page.goto(url)
            await page.screenshot(path=output_path, full_page=True)
            await browser.close()