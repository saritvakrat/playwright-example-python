class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/v1/"
        self.login_btn_selector = "#login-button"
        self.username_selector = "#user-name"
        self.password_selector = "#password"
        self.error_message_selector = 'h3[data-test="error"]'

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username_selector, username)
        self.page.fill(self.password_selector, password)
        self.page.click(self.login_btn_selector)

    def is_loaded(self):
        return self.page.is_visible(self.login_btn_selector)

    def get_error_message(self):
        return self.page.locator(self.error_message_selector).text_content()

    def is_error_message_visible(self):
        return self.page.locator(self.error_message_selector).is_visible()
