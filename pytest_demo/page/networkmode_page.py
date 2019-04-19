from selenium.webdriver.common.by import By
from pytest_demo.PO.base_page import Base
from appium import webdriver
import selenium


class Network_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.network_BTN = (By.XPATH, "//*[contains(@text,'Network')]")
        self.mobilenetwork_BTN = (By.XPATH, "//*[contains(@text,'Mobile network')]")
        self.Advance_BTN = (By.XPATH, "//*[contains(@text,'Advanced')]")
        self.networktype_BTN = (By.XPATH, "//*[contains(@text,'Preferred network type')]")
        self.type_3G_only = (By.XPATH, "//*[contains(@text,'3G only')]")
        self.type_4G_only = (By.XPATH, "//*[contains(@text,'4G only')]")

    def open_mobile_network(self):
        self.click_element(self.network_BTN)
        self.click_element(self.mobilenetwork_BTN)
        self.click_element(self.Advance_BTN)

    def change_neworkmode(self,mode):
        # self.open_mobile_network()
        self.click_element(self.networktype_BTN)
        self.click_element((By.XPATH, "//*[contains(@text,'%s')]" %mode))

    def change_neworkmode_to_4G(self):
        self.open_mobile_network()
        self.click_element(self.type_4G_only)