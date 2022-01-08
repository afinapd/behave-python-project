from behave import step

from features.pages.assign_leave_page import assignLeavePage


@step('user type employee name "{name}"')
def step_impl(self, name):
    assignLeavePage.inputEmployeeName(name)


@step('user select leave type "{leaveType}"')
def step_impl(self, leaveType):
    assignLeavePage.selectLeaveType(leaveType)


@step('user type leave balance from date "{fromDate}" to "{toDate}"')
def step_impl(self, fromDate, toDate):
    assignLeavePage.inputLeaveBalanceFromDate(fromDate)
    assignLeavePage.inputLeaveBalanceToDate(toDate)


@step('user select partial days "{partialDays}"')
def step_impl(self, partialDays):
    assignLeavePage.selectPartialDays(partialDays)


@step('user type comment "{comment}"')
def step_impl(self, comment):
    assignLeavePage.inputComment(comment)

@step('user click assign leave')
def step_impl(self):
    assignLeavePage.clickAssignButton()

@step('user get message "{message}"')
def step_impl(self, message):
    assignLeavePage.verifyMessage(message)
