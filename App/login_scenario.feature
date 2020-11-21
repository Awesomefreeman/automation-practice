Feature: Login
  Scenario: Login on site
    Given open authentication page
    When enter credentials and login
    Then verify that "sign out" button exist