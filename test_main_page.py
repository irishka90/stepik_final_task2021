
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import PageObject

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_login(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.go_to_login_and_register_form()
    page.should_be_login_form()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    new_link = browser.current_url
    new_page = BasketPage(browser, new_link)
    new_page.open()
    new_page.empty_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = PageObject(browser, login_link)
    page.open()
    page.go_to_basket()
    new_link = browser.current_url
    new_page = BasketPage(browser, new_link)
    new_page.open()
    new_page.empty_basket()

























