Feature: Test cases for Target

#  Scenario: User can search for a product on Target
#    Given Open Target main page
#    When Search for coffee
#    Then Verify search results for coffee shown

  Scenario: Clicking empty cart sends a message
    Given Open Target main page
    When Cart icon is clicked
    Then Cart empty message is shown

  Scenario: Clicking Sign In opens sign in form
    Given Open Target main page
    When Sign In is clicked
    Then Sign In form opens