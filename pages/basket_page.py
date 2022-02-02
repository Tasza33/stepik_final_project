from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOKS_IN_BASKET), \
        "Books in basket are presented, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "No message about empty basket"
