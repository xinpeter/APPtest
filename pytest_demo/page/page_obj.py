from pytest_demo.page.networkmode_page import Network_Page
from pytest_demo.page.settings_page import Settings

class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def network_page(self):
        return Network_Page(self.driver)

    def settings(self):
        return Settings(self.driver)