from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_PURCHASE), \
            "No 'Continue purchase' link. The basket is not empty"
        empty_basket = self.browser.find_element(By.ID, "content_inner").text
        assert empty_basket == "Ваша корзина пуста Продолжить покупки", "No text 'Empty basket'"
