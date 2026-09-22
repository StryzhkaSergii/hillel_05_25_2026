from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright, expect


def func():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.wait_for_timeout(3000)
        logo_locator = page.locator(".login_logo")
        expect(logo_locator).to_be_visible()
        expect(page).to_have_title("Swag Labs")
        expect(page).to_have_url("https://www.saucedemo.com/")
        browser.close()

if __name__ == "__main__":
    func()