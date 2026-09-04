from playwright.sync_api import Page, expect

from core.pages.base_page import BasePage
from core.pages.inventory_page import InventoryPage
from settings import settings

class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.__username = page.get_by_role("textbox", name="Username")
        self.__password = page.get_by_placeholder("Password")
        # self.password = page.get_by_test_id("password") // має бути data-testid, а в нас data-test
        self.__login_button = page.get_by_role("button", name="Login")
        self.__login_credentials = page.locator(".login_credentials_wrap-inner")
        self.__error_message = page.locator("//div[contains(@class, 'error')]")

    def is_displayed(self):
        expect(self.__login_credentials).to_be_visible()

    def open(self):
        self.page.goto(f"{settings.SAUCE_DEMO_BASE_URL}")

    def login_valid_user(self, username, password):
        self.__username.fill(username)
        self.__password.fill(password)
        self.__login_button.click()
        return InventoryPage(self.page)

    def login_via_enter(self, username, password):
        self.__username.fill(username)
        self.__password.fill(password)
        self.__password.press("Enter")
        self.__login_button.focus()
        return InventoryPage(self.page)

    def do_invalid_login(self, username, password):
        self.__username.fill(username)
        self.__password.fill(password)
        self.__login_button.click()

    def get_error_message(self):
        return self.__error_message.text_content()

    def get_error_element(self):
        return self.__error_message