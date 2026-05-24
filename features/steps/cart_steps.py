from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
# import './header_steps.py'

CART_EMPTY_MESSAGE = (By.XPATH, "//*[text()='Your cart is empty']")
CART_ITEM = (By.CSS_SELECTOR, "div[aria-label*='cart item']")

@then("Cart empty message is shown")
def verify_empty_message(context):
    context.driver.find_element(*CART_EMPTY_MESSAGE)

@then("Cart is filled")
def verify_cart_is_filled(context):
    cart_items = context.driver.find_elements(*CART_ITEM)
    assert len(cart_items) > 0

