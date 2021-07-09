from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.ID,"login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    ADD_TO_BASKET = (By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    INSPECT_BASKET = (By.LINK_TEXT,"http://selenium1py.pythonanywhere.com/ru/basket/")
    SUCCESS_MESSAGE =(By.XPATH, "//*[@id='messages']/div[1]/div")

