from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "a[href*='/cart']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id*='addToCartButton']")
ADD_TO_CART_SHIPPING_BUTTON = (By.CSS_SELECTOR, "button[id*='addToCartButton'][data-test*='shippingButton']")
AVAILABLE_PRODUCT_COLOR = (By.CSS_SELECTOR, "button[aria-label*='color' i]:not([aria-label*='Out of Stock' i]):not([id*='addToCartButton'])")
# PRODUCT_COLOR_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='color' i]")
CLOSE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='close']")

@when("Cart icon is clicked")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)

@when("Search for {search_query}")
def search_product(context, search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)

@when("Product is added to cart")
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(3)
    context.driver.find_element(*AVAILABLE_PRODUCT_COLOR).click()
    sleep(3)
    context.driver.find_element(*ADD_TO_CART_SHIPPING_BUTTON).click()
    sleep(3)
    # after adding to cart, another sidebar layer appears, covering the first close button
    context.driver.find_elements(*CLOSE_BUTTON)[1].click()

# @when("Search for coffee")
# def search_product(context):
#     context.driver.find_element(*SEARCH_FIELD).send_keys('coffee')
#     context.driver.find_element(*SEARCH_BUTTON).click()
#     sleep(7)

