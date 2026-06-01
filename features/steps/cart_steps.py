from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MESSAGE = (By.XPATH, "//*[text()='Your cart is empty']")
CART_ITEM = (By.CSS_SELECTOR, "div[aria-label*='cart item']")

@then("Cart empty message is shown")
def verify_empty_message(context):
    # context.driver.find_element(*CART_EMPTY_MESSAGE)
    # call app. function
    context.app.cart.verify_empty_cart()

@then("Cart is filled")
def verify_cart_is_filled(context):
    context.app.cart.verify_cart_is_filled()
    # cart_items = context.driver.find_elements(*CART_ITEM)
    # assert len(cart_items) > 0

