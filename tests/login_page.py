import pytest
from pages.home_page import HomePage
from utils import BrowserManager

@pytest.fixture(scope="function")
def setup():
    manager = BrowserManager(headless=False)
    browser = manager.start_browser()
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.navigate()
    yield home_page
    page.close()
    manager.stop_browser()

def test_successful_login(setup):
    home_page = setup
    home_page.login('standard_user', 'secret_sauce')

    # Assert that the login was successful by checking the URL
    home_page.page.wait_for_url('https://www.saucedemo.com/v1/inventory.html')
    assert home_page.page.url == 'https://www.saucedemo.com/v1/inventory.html'

def test_unsuccessful_login(setup):
    home_page = setup
    home_page.login('invalid_user', 'invalid_password')

    # Assert that an error message is displayed
    assert home_page.is_error_message_visible()
    assert "Epic sadface: Username and password do not match any user in this service" in home_page.get_error_message()

def test_login_with_empty_fields(setup):
    home_page = setup
    home_page.login('', '')

    # Assert that an error message is displayed
    assert home_page.is_error_message_visible()
    assert "Epic sadface: Username is required" in home_page.get_error_message()
