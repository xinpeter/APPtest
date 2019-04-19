from selenium.webdriver.common.by import By
from pytest_demo.PO.base_page import Base
from appium import webdriver

class Settings(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.search_BTN = (By.ID,"com.android.settings:id/search_action_bar")
        self.search_input = (By.ID,"android:id/search_src_text")
        self.search_back = (By.XPATH,"//android.widget.ImageButton[@content-desc='Navigate up']")

    def open_search_bar(self):
        self.click_element(self.search_BTN)

    def input_search_text(self,text):
        self.input_element(self.search_input,text)
