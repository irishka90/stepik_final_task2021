import time

import pytest
from pages.product_page import PageObject
from pages.login_page import LoginPage


@pytest.mark.xfail(reason="won't be fixed")
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    login_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, login_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_add_to_basket()
    page.book_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = PageObject(browser, login_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = PageObject(browser, login_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = PageObject(browser, login_link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, login_link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user()
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = PageObject(browser, login_link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = PageObject(browser, login_link)
        page.open()
        page.add_to_basket()
        page.success_add_to_basket()
        page.book_price()
