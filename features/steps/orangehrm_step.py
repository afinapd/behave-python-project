from behave import step
from selenium import webdriver

@step('launch chrome browser')
def lauchBrowser(context):
    context.driver = webdriver.Chrome(executable_path= "C:\\Users\\user\Downloads\chromedriver.exe")
    # context.driver = webdriver.Chrome()

@step('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@step('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_id("divLogo").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
