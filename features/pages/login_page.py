from features.pages.reusable_page import ReusablePage
from features.locators.locator import LocatorLoginPage

class LoginPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def inputUserPassword(self, username, password):
        super().perform_action_on_element(LocatorLoginPage.UserName, "Type", username)
        super().perform_action_on_element(LocatorLoginPage.Password, "Type", password)

    def clickButtonLogin(self):
        super().perform_action_on_element(LocatorLoginPage.LoginButton, "Click")

loginPage = LoginPage.get_instance()
