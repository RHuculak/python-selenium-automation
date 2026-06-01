from pages.base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):

    SIGNIN_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")
    SIGNIN_BUTTON = (By.XPATH, "//button[text()='Continue']")
    PASSKEY_BUTTON = (By.XPATH, "//button[text()='Sign in with passkey']")

    def verify_empty_message(self):
        self.find_element(*self.SIGNIN_TEXT)
        self.find_element(*self.SIGNIN_BUTTON)
        self.find_element(*self.PASSKEY_BUTTON)
        # text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
        # signin_button = context.driver.find_element(By.XPATH, "//button[text()='Continue']")
        # signin_button = context.driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']")