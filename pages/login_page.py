import time
import random
import string
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "No login URL"
        assert True

    def go_to_login_and_register_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No register-login form"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FORM), "No field to input email"
        email = str(time.time()) + "@fakemail.org"
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        input_email.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "No field to input password"
        letters = string.ascii_letters
        password = ''.join(random.choice(letters) for i in range(9))
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        input_password.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "No field to confirm password"
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        confirm_password.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BTN), "No button 'REGISTRATE'"
        registrate_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        registrate_btn.click()
        self.browser.implicitly_wait(3)
        assert self.is_element_present(
            *LoginPageLocators.SUCCESS_MESSAGE), "Success message is not presented,but should be"
