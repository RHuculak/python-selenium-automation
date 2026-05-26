from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

MAIN_PAGE = "main"
CIRCLE_PAGE = "circle"

@given("Open Target {path} page")
def open_target_page(context, path):
    if path == MAIN_PAGE:
        path = ""
    context.driver.get(f'https://www.target.com/{path}')
