import time

from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorAssignLeavePage

class AssignLeavePage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = AssignLeavePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def inputEmployeeName(self, name):
        super().perform_action_on_element(LocatorAssignLeavePage.EmployeeNameTextfield, "type", name)

    def selectLeaveType(self, leaveType):
        super().perform_action_on_element(LocatorAssignLeavePage.LeaveTypeDropdown, "select", leaveType)

    def inputLeaveBalanceFromDate(self, fromDate):
        super().perform_action_on_element(LocatorAssignLeavePage.FromDateTextfield, "clear")
        super().perform_action_on_element(LocatorAssignLeavePage.FromDateTextfield, "type", fromDate)
        super().perform_action_on_element(LocatorAssignLeavePage.FromDateTextfield, "enter")

    def inputLeaveBalanceToDate(self, toDate):
        super().perform_action_on_element(LocatorAssignLeavePage.ToDateTextfield, "clear")
        super().perform_action_on_element(LocatorAssignLeavePage.ToDateTextfield, "type", toDate)
        super().perform_action_on_element(LocatorAssignLeavePage.ToDateTextfield, "enter")

    def selectPartialDays(self, partialDays):
        super().perform_action_on_element(LocatorAssignLeavePage.PartialDaysDropdown, "select", partialDays)

    def inputComment(self, comment):
        super().perform_action_on_element(LocatorAssignLeavePage.CommentTextfield, "type", comment)

    def clickAssignButton(self):
        super().perform_action_on_element(LocatorAssignLeavePage.AssignButton, "click")
        super().perform_action_on_element(LocatorAssignLeavePage.ConfirmOkButton, "click")

    def verifyMessage(self, message):
        super().assert_element_text(LocatorAssignLeavePage.MessageText, message)

assignLeavePage = AssignLeavePage.get_instance()
