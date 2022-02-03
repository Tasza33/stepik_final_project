from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert "login" in browser.current_url, "login is not a substring of login_url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        user_email.send_keys(email)
        user_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        user_password2.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

