from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def is_displayed(self):
        pass