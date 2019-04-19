from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    #初始化driver
    def __init__(self,driver):
        self.driver = driver

    #封装查找元素（By.id,"id"）
    def find_element_i(self,loc):
        return WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*loc))
    # def find_element_i(self, loc, timeout=10, poll=0.5):
    #     """
    #     :param loc: 元祖 例如：(By.ID, ID属性值)。。。
    #     :param timeout:
    #     :param poll:
    #     :return: 返回定位对象
    #     """
    #     return WebDriverWait(self.driver, timeout, poll)\
    #         .until(lambda x:x.find_element(*loc))

    #封装点击
    def click_element(self,loc):
        self.find_element_i(loc).click()

    #封装输入key
    def input_element(self,loc,text):
        ob = self.find_element_i(loc)
        ob.clear()
        ob.send_keys(text)
