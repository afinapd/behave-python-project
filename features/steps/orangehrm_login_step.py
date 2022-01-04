from behave import *

@when('enter username "{user}" and password "{password}"')
def inputUserPassword(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('click on login button')
def clickButtonLogin(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('user must successfully login to the dashboard page')
def verifyDashboard(context):
    status = context.driver.find_element_by_id("menu_dashboard_index").is_displayed()
    assert status is True