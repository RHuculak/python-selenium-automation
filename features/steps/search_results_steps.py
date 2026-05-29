from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")

@then("Verify search results for {search_query} shown")
def verify_search_results(context, search_query):
    # actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
    # assert search_query in actual_result, \
    #     f'Expected "{search_query}" not in actual "{actual_result}"'
    context.app.search_results.verify_search_results(search_query) # add search_query functionality

@then("Give search results for {color}")
def verify_color_search_results(context, color):
    print(f'searching for {color}')
    colors_found = context.driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='color' i]:not([aria-label*='view full screen'])")
    print(colors_found)
    found = False
    for color_elem in colors_found:
        if color.casefold() in color_elem.get_attribute('aria-label').casefold():
            color_elem.click()
            if 'selected' in color_elem.get_attribute('aria-label').casefold():
                print(f'Found color {color}, verified color selected.')
                found = True
                break
    if not found:
        print(f"No color found for {color}")
