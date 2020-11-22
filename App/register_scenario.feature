Feature: Register
  Scenario: Register on site
    Given open authentication page
    When create new account
    And enter personal information
    And enter address
    Then register successful