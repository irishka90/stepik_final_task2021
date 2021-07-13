from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "'Empty basket' is not presented"
