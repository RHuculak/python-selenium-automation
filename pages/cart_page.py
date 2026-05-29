from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Cart(Page):
    CART_EMPTY_MESSAGE = (By.XPATH, "//*[text()='Your cart is empty']")
    def verify_empty_cart(self):
        self.find_element(*self.CART_EMPTY_MESSAGE)