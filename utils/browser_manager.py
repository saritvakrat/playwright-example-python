from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, headless=True):
        self.playwright = None
        self.browser = None
        self.headless = headless

    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        return self.browser

    def stop_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
