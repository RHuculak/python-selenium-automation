from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")

@then("Verify search results for {search_query} shown")
def verify_search_results(context, search_query):
    expected_result = search_query
    actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

# @then("Verify search results for coffee shown")
# def verify_search_results(context):
#     expected_result = search_query
#     actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
#     assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'