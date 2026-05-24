from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
# to do: separate this into different files
@when("Sign In is clicked")
def click_signin(context):
    account_button = context.driver.find_element(By.ID, "account-sign-in")
    account_button.click()
    sleep(4)

    signin_button = context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    signin_button.click()
    sleep(3)

@then("Sign In form opens")
def verify_empty_message(context):
    text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
    signin_button = context.driver.find_element(By.XPATH, "//button[text()='Continue']")
    signin_button = context.driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']")