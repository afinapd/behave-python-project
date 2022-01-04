Feature: OrangeHRM Logo

  Scenario: Login to orangeHRM with validation
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser