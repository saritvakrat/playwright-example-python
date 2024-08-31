import pytest
from playwright.async_api import async_playwright
from pages.home_page import HomePage


@pytest.fixture(scope="function")
async def setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        home_page = HomePage(page)
        home_page.navigate()
        yield home_page
        await browser.close()


@pytest.fixture(scope="function", autouse=True)
async def teardown(setup):
    page = setup.page
    await page.close()


@pytest.mark.asyncio
async def test_successful_login(setup):
    home_page = setup
    home_page.login('standard_user', 'secret_sauce')

    # Assert that the login was successful by checking the URL
    await home_page.page.wait_for_url('https://www.saucedemo.com/v1/inventory.html')
    assert home_page.page.url == 'https://www.saucedemo.com/v1/inventory.html'


@pytest.mark.asyncio
async def test_unsuccessful_login(setup):
    home_page = setup
    home_page.login('invalid_user', 'invalid_password')

    # Assert that an error message is displayed
    assert await home_page.is_error_message_visible()
    assert "Epic sadface: Username and password do not match any user in this service" in await home_page.get_error_message()


@pytest.mark.asyncio
async def test_login_with_empty_fields(setup):
    home_page = setup
    home_page.login('', '')

    # Assert that an error message is displayed
    assert await home_page.is_error_message_visible()
    assert "Epic sadface: Username is required" in await home_page.get_error_message()
