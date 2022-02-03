from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_PRICE = (By.CSS_SELECTOR, '.price_color')
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    ADD_MESSAGE_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    ADD_MESSAGE_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasketPageLocators:
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a')
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'empty')]")
    BOOKS_IN_BASKET = (By.CSS_SELECTOR, '.thumbnail')
