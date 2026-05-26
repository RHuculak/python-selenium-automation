Feature: Test cases for Target product search

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown

  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query  |product     |
    |coffee        |coffee      |
    |coffee cup    |coffee cup  |
    |sugar         |sugar       |

  Scenario Outline: User can search for a color
    Given Open shirt page
    Then Give search results for <color>
    Examples:
    |color |
    |black |
    |blue  |
    |white |
    |gray  |
    |pink  |


