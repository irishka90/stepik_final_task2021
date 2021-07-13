from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_2 = (By.NAME, "registration-password2")
    REGISTRATION_BTN = (By.NAME, "registration_submit")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner.wicon")


class ProductPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    INSPECT_BASKET = (
    By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.ID, "content_inner")
