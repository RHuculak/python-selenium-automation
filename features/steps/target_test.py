from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page")
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

# @when("Search for coffee")
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('coffee')
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
#     sleep(6)

# @then("Verify search results for coffee shown")
# def verify_search_results(context):
#     expected_result = 'coffee'
#     actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
#     assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

@when("Cart icon is clicked")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/cart']").click()
    sleep(3)

@then("Cart empty message is shown")
def verify_empty_message(context):
    context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']")

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