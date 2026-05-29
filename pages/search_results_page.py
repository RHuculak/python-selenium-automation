from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):
    SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    def verify_search_results(self, search_query):
        actual_result = self.find_element(*self.SEARCH_RESULT_COUNT_TEXT).text
        assert search_query in actual_result, \
            f'Expected "{search_query}" not in actual "{actual_result}"'