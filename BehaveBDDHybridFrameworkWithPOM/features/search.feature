Feature: Search Functionality

  @test1
  Scenario Outline: Search with valid Products
    Given User is able to navigate to Home Page
    When User enters a valid Product say <PRODUCT>
    And User clicks on Search button
    Then Valid products should get displayed in Search Page say <PRODUCT>
    Examples:
    |PRODUCT|
    |Iphone |
    |HP     |

  @test2
  Scenario Outline: Search with Invalid Products
    Given User is able to navigate to Home Page
    When User enters a Invalid Product say <PRODUCT>
    And User clicks on Search button
    Then InValid products message get displayed in Search Page
    Examples:
      | PRODUCT |
      | Honda   |

  @test3
  Scenario Outline: Search with no Products
    Given User is able to navigate to Home Page
    When User enters no Product say <PRODUCT>
    And User clicks on Search button
    Then No products should get displayed in Search Page
    Examples:
      | PRODUCT |
      | <empty> |
