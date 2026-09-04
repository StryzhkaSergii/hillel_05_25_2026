from playwright.sync_api import Page, expect

from core.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.__app_logo = page.locator("text=Swag Labs")
        self.__backpack_image = page.get_by_alt_text("Sauce Labs Backpack")
        self.__burger_button = page.locator("//div[@class='bm-burger-button']/button")
        self.__inventory_item = page.locator(".inventory_item")
        self.__sorting_select = page.locator(".product_sort_container")

    def is_displayed(self):
        expect(self.__app_logo).to_be_visible()

    def img_loaded(self):
        expect(self.__backpack_image).to_be_visible()

    def __select_item(self, item_name):
        return self.__inventory_item.filter(has_text=item_name)

    def click_one_item(self):
        add_button = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.__inventory_item.filter(has=add_button).get_by_role("button", name="Add to cart").click()

    def get_item_price(self, item_name):
        return  self.__select_item(item_name).locator(".inventory_item_price").text_content()

    def sort_by(self, sorting):
        self.__sorting_select.select_option(sorting)

    def get_price(self):
        self.__inventory_item.locator(".inventory_item_price").text_content()

    # def collect_price(self):
    #     result = []
    #     for item in self.__inventory_item.: