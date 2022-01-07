from behave import step
from features.pages.login_page import loginPage

@step('enter username "{user}" and password "{password}"')
def inputUserPassword(self, user, password):
    loginPage.inputUserPassword(user, password)


@step('click on login button')
def clickButtonLogin(self):
    loginPage.clickButtonLogin()