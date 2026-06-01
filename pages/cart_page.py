from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Cart(Page):
    CART_EMPTY_MESSAGE = (By.XPATH, "//*[text()='Your cart is empty']")
    CART_ITEM = (By.CSS_SELECTOR, "div[aria-label*='cart item']")
    def verify_empty_cart(self):
        self.find_element(*self.CART_EMPTY_MESSAGE)

    def verify_cart_is_filled(self):
        self.find_element(*self.CART_ITEM)
        # cart_items = context.driver.find_elements(*CART_ITEM)
        # assert len(cart_items) > 0