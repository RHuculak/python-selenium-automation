from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

STORYCARD = (By.CSS_SELECTOR, "div[class*='StoryblockImageContainer']")

@then("{expected_count} storycards are visible")
def verify_two_storycards(context, expected_count):
    storycards = context.driver.find_elements(*STORYCARD)
    assert len(storycards) == int(expected_count)