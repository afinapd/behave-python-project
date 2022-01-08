from behave import step
from features.pages.login_page import loginPage

@step('user login with username "{user}" and password "{password}"')
def step_impl(self, user, password):
    loginPage.inputUserPassword(user, password)
    loginPage.clickLoginButton()