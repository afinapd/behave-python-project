from behave import step
from features.pages.dashboard_page import dashboardPage

@step('user must successfully login to the dashboard page')
def step_impl(self):
    dashboardPage.verifyDashboard()

@step('user click Assign Leave menu')
def step_impl(self):
    dashboardPage.clickAssignLeaveMenu()