from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_PRICE = (By.CSS_SELECTOR, '.price_color')
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    ADD_MESSAGE_NAME = (By.CSS_SELECTOR, '.alert:nth-child(1)')
    ADD_MESSAGE_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
