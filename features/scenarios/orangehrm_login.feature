Feature: OrangeHRM Login

  Scenario: Logo presence on OrangeHRM homepage
    Given launch chrome browser
    When open orange hrm homepage
    And enter username "admin" and password "admin123"
    And click on login button
    Then user must successfully login to the dashboard page