from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
# to do: separate this into different files
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_SIGN_IN_BUTTON = (By.ID, "account-sign-in")
SIGN_IN_BUTTON = (By.XPATH, "//button[@data-test='accountNav-signIn']")

@when("Sign In is clicked")
def click_signin(context):
    context.app.header.click_signin()
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(ACCOUNT_SIGN_IN_BUTTON)
    # ).click()
    #
    # # account_button = context.driver.find_element(By.ID, "account-sign-in")
    # # account_button.click()
    #
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGN_IN_BUTTON)
    # ).click()
    #
    # # signin_button = context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    # # signin_button.click()

@then("Sign In form opens")
def verify_empty_message(context):
    context.app.signin.verify_empty_message()
    # text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
    # signin_button = context.driver.find_element(By.XPATH, "//button[text()='Continue']")
    # signin_button = context.driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']")