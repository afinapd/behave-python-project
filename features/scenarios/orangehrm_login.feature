Feature: OrangeHRM Login

  Scenario: User successfully login
    Given launch chrome browser
    When open orange hrm homepage
    And user login with username "admin" and password "admin123"
    Then user must successfully login to the dashboard page
    And close browser