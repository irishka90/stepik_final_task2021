from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    INSPECT_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")


class BasketPageLocators():
    CONTINUE_PURCHASE = (By.XPATH, "//*[@id='content_inner']/p/a")