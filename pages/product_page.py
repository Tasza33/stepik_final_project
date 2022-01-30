from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def name_for_product_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        add_message_name = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE_NAME).text
        assert book_name == add_message_name, 'book name in basket is not correct'

    def price_for_product_in_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        add_message_price = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE_PRICE).text
        assert book_price in add_message_price, 'book price in basket is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappear, but should be"