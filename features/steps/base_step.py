import os

from behave import *

from features.pages.base_page import basePage
from helper.config import config


@given('launch chrome browser')
def lauchBrowser(self):
    basePage.get_driver()

@step('open orange hrm homepage')
def openHomePage(self):
    basePage.navigate("https://opensource-demo.orangehrmlive.com/")


@step('verify that the logo present on page')
def verifyLogo(self):
    status = self.driver.find_element_by_id("divLogo").is_displayed()
    assert status is True


@step('close browser')
def closeBrowser(self):
    basePage.close_browser()
