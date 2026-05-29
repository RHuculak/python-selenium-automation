from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

MAIN_PAGE = "main"
CIRCLE_PAGE = "circle"
COLOR_TEST_PAGE = "https://www.target.com/p/men-s-performance-dress-standard-fit-long-sleeve-button-down-shirt-goodfellow-co/-/A-87418571"

@given("Open Target {path} page")
def open_target_page(context, path):
    if path == MAIN_PAGE:
        path = ""
    # context.driver.get(f'https://www.target.com/{path}')
    context.app.page.open_url(path)

@given("Open shirt page")
def open_shirt_page(context):
    context.driver.get(COLOR_TEST_PAGE)