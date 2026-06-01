from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.header import Header

CART_ICON = (By.CSS_SELECTOR, "a[href*='/cart']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id*='addToCartButton']")
ADD_TO_CART_OPTION_SELECTED_BUTTON = (By.CSS_SELECTOR, "button[data-test*='shippingButton'],[data-test*='orderPickupButton'],[data-test*='scheduleDeliveryButton']")
AVAILABLE_PRODUCT_OPTION = (By.CSS_SELECTOR, "button[aria-label*='color' i][aria-label*='size' i]:not([aria-label*='Out of Stock' i]):not([id*='addToCartButton'])")
# PRODUCT_COLOR_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='color' i]")
CLOSE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='close']")
SHIPPING_BUTTON = (By.CSS_SELECTOR, "[data-test*='fulfillment-cell-shipping']")
ADD_TO_CART_SHIPPING_BUTTON = (By.CSS_SELECTOR, "[data-test*='shippingButton']")

@when("Cart icon is clicked")
def click_cart_icon(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(CART_ICON), message='not clickable'
    # ).click()
    context.app.header.click_cart_icon()
    sleep(3)
    # context.driver.find_element(*CART_ICON).click()

@when("Search for {search_query}")
def search_product(context, search_query):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    # # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SEARCH_BUTTON), message='not clickable'
    # ).click()
    # # context.driver.find_element(*SEARCH_BUTTON).click()
    context.app.header.search(search_query) #add search_query functionality in header.py

@when("Product is added to cart")
def add_to_cart(context):
    context.app.header.add_to_cart()

    ###
    # context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SHIPPING_BUTTON), message='not clickable').click()
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SHIPPING_BUTTON), message='not clickable').click()
    # context.driver.find_elements(*CLOSE_BUTTON)[0].click()
    ###

    # cart_buttons = context.driver.find_elements(*ADD_TO_CART_BUTTON)
    # add logic to continue on if available product colors aren't there

    # for cart_button in cart_buttons:
    #     cart_button.click()
    #     try:
    #
    #     except TimeoutException:
    #         pass
    #     try:
    #         # if the default product color or size isn't available this will select an available one
    #         context.driver.wait.until(EC.element_to_be_clickable(AVAILABLE_PRODUCT_OPTION), message='not clickable').click()
    #     except TimeoutException:
    #         # if some product option like size or color isn't there because there's only one size, it's okay
    #         pass
    #     try:
    #         # if the product is availiable in the area and not completely out of stock, we can click add to cart
    #         context.driver.wait.until(
    #             EC.element_to_be_clickable(ADD_TO_CART_OPTION_SELECTED_BUTTON), message='not clickable'
    #         ).click()
    #     except TimeoutException:
    #         # close and try another add to cart button for another product on the front page
    #         sleep(1)
    #         # index 0 because it's the first layer of the navbar
    #         context.driver.find_elements(*CLOSE_BUTTON)[0].click()
    #         continue
    #     break
    #     # still close so we can click the cart button on the main page in the next step
    #     # after adding to cart, another sidebar layer appears, covering the first close button
    # context.driver.find_elements(*CLOSE_BUTTON)[1].click()
    #     # EC.element_to_be_clickable()
    #     # context.driver.find_elements(*CLOSE_BUTTON)[1].click()
    #     # sleep(1)
    #     # try:
    #     #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='ReactModal__Overlay--after-open'")).click()
    #     # except TimeoutException:
    #     #     pass
    #     # sleep(1)
    #     # try:
    #     #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='ReactModal__Overlay--after-open'")).click()
    #     # except TimeoutException:
    #     #     pass
    #     # sleep(1)
    # # context.driver.find_element(*AVAILABLE_PRODUCT_COLOR).click()
    # # context.driver.find_element(*ADD_TO_CART_SHIPPING_BUTTON).click()

# @when("Search for coffee")
# def search_product(context):
#     context.driver.find_element(*SEARCH_FIELD).send_keys('coffee')
#     context.driver.find_element(*SEARCH_BUTTON).click()
#     sleep(7)

