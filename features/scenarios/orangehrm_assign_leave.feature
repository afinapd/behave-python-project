Feature: OrangeHRM Login

  Scenario: User successfully assign leave
    Given launch chrome browser
    When open orange hrm homepage
    And user login with username "admin" and password "admin123"
    And user click Assign Leave menu
    And user type employee name "Joe Root"
    And user select leave type "CAN - Matternity"
    And user type leave balance from date "2022-01-10" to "2022-01-12"
    And user select partial days "All Days"
    And user type comment "sick leave"
    And user click assign leave
    Then user get message "Successfully Assigned"
    And close browser