# Created by 48731 at 17.08.2023
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added


   @library
    Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then status code of response should be 200
      Examples:
        |isbn  |  aisle |
        | fdfee| 8948   |
        | powr | 76333  |