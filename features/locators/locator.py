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