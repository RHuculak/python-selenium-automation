from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='/cart']")

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