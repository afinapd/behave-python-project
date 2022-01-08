from selenium.webdriver.common.by import By

class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class LocatorLoginPage:
    UserName = Locator(By.ID, "txtUsername")
    Password = Locator(By.ID, "txtPassword")
    LoginButton = Locator(By.ID, "btnLogin")

class LocatorDashboardPage:
    DashboardMenu = Locator(By.ID, "menu_dashboard_index")
    AssignLeaveMenu = Locator(By.XPATH, "//span[contains(.,'Assign Leave')]")

class LocatorAssignLeavePage:
    EmployeeNameTextfield = Locator(By.ID, "assignleave_txtEmployee_empName")
    LeaveTypeDropdown = Locator(By.ID, "assignleave_txtLeaveType")
    FromDateTextfield = Locator(By.ID, "assignleave_txtFromDate")
    ToDateTextfield = Locator(By.ID, "assignleave_txtToDate")
    PartialDaysDropdown = Locator(By.ID, "assignleave_partialDays")
    CommentTextfield = Locator(By.ID, "assignleave_txtComment")
    AssignButton = Locator(By.ID, "assignBtn")
    ConfirmOkButton = Locator(By.ID, "confirmOkButton")
    MessageText = Locator(By.CSS_SELECTOR, ".message")