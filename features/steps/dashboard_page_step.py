from behave import step
from features.pages.dashboard_page import dashboardPage

@step('user must successfully login to the dashboard page')
def verifyDashboard(self):
    dashboardPage.verifyDashboard()