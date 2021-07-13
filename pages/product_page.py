import time
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class PageObject(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "No 'Add to basket' button"
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()

    def success_add_to_basket(self):
        book_title = self.browser.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1").text
        success_comment_title = self.browser.find_element(By.CSS_SELECTOR,
                                                          "#messages > div:nth-child(1) > div > strong").text
        assert book_title == success_comment_title, "The title is wrong"
        time.sleep(2)

    def book_price(self):
        book_price = self.browser.find_element(By.XPATH,
                                               "//*[@id='content_inner']/article/div[1]/div[2]/p[1]").text
        basket_price = self.browser.find_element(By.XPATH,
                                                 "//*[@id='messages']/div[3]/div/p[1]/strong").text
        assert book_price == basket_price, "The price is wrong"
        time.sleep(2)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappear"

    def reregister_new_user(self):
        pass
