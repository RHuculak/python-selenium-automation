from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='/cart']")
    ACCOUNT_SIGN_IN_BUTTON = (By.ID, "account-sign-in")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='close']")
    SHIPPING_BUTTON = (By.CSS_SELECTOR, "[data-test*='fulfillment-cell-shipping']")
    ADD_TO_CART_SHIPPING_BUTTON = (By.CSS_SELECTOR, "[data-test*='shippingButton']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id*='addToCartButton']")

    def search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart_icon(self):
        # context.driver.wait.until(
        #     EC.element_to_be_clickable(CART_ICON), message='not clickable'
        # ).click()
        self.click(*self.CART_ICON)
        sleep(3)
        # context.driver.find_element(*CART_ICON).click()

    def click_signin(self):
        self.click(*self.ACCOUNT_SIGN_IN_BUTTON)
        self.click(*self.SIGN_IN_BUTTON)

        # context.driver.wait.until(
        #     EC.element_to_be_clickable(ACCOUNT_SIGN_IN_BUTTON)
        # ).click()

        # account_button = context.driver.find_element(By.ID, "account-sign-in")
        # account_button.click()

        # context.driver.wait.until(
        #     EC.element_to_be_clickable(SIGN_IN_BUTTON)
        # ).click()

        # signin_button = context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
        # signin_button.click()

    def add_to_cart(self):
        # context.driver.wait = WebDriverWait(context.driver, 10)
        # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON), message='not clickable').click()
        self.click(*self.ADD_TO_CART_BUTTON)
        sleep(1)
        self.click(*self.SHIPPING_BUTTON)
        sleep(1)
        self.click(*self.ADD_TO_CART_SHIPPING_BUTTON)
        sleep(1)
        close_buttons = self.find_elements(*self.CLOSE_BUTTON)
        close_buttons[1].click()
        # self.click(*self.CLOSE_BUTTON)