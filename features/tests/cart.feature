# Created by Ryan at 5/20/2026
Feature: Cart test cases
  # Enter feature description here

  Scenario: Clicking empty cart sends a message
    Given Open Target main page
    When Cart icon is clicked
    Then Cart empty message is shown

  Scenario: Adding product to cart fills the cart
    Given Open Target main page
    When Product is added to cart
    When Cart icon is clicked
    Then Cart is filled
