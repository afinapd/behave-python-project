from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorDashboardPage

class DashboardPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = DashboardPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def verifyDashboard(self):
        super().element_exists(LocatorDashboardPage.DashboardMenu)

    def clickAssignLeaveMenu(self):
        super().perform_action_on_element(LocatorDashboardPage.AssignLeaveMenu, "click")

dashboardPage = DashboardPage.get_instance()
