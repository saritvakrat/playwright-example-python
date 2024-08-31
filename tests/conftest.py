import pytest
from utils.browser_manager import BrowserManager
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def browser():
    # Set headless=False to run with the browser visible
    browser_manager = BrowserManager(headless=False)
    browser = browser_manager.start_browser()
    yield browser
    browser_manager.stop_browser()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)
