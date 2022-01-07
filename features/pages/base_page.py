import os
import shutil
from helper.config import config
# from allure_commons._allure import attach
# from allure_commons.types import AttachmentType
import datetime
from selenium import webdriver

class BasePage(object):
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BasePage()
        return cls.instance

    def __init__(self):
        if config.browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(executable_path=os.getcwd() + r'\library\chromedriver.exe', chrome_options=chrome_options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(config.driver_timeout)
        else:
            raise BasePage.SeleniumDriverNotFound(
                {config.browser} +" is not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()

    def close_browser(self):
        self.driver.close()

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)

    # def capture_screenshot(self):
    #     attach(self.driver.get_screenshot_as_png(), name=datetime.datetime.now().timestamp(), attachment_type =AttachmentType.PNG)

    def capture_screenshots_for_jira(self):
        path= os.getcwd()+"/temp"
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)
        path_to_capture_screenshot=path+"/"+str(datetime.datetime.now().timestamp())+".png"
        self.driver.get_screenshot_as_file(path_to_capture_screenshot)
        return path_to_capture_screenshot


basePage = BasePage.get_instance()