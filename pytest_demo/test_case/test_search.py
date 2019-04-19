import sys,os
import pytest,allure
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)
from pytest_demo.page.page_obj import Page_Obj
from pytest_demo.PO.Init_driver import init_driver
import time
from pytest_demo.PO.load_data import load_data

def search_data():
    data = load_data('search_data').get('data')
    data_list = []
    for i in data.keys():
        data_list.append((i,data.get(i).get('test')))
    return data_list

class Test_search:
    def setup_class(self):
        self.driver = init_driver()
        self.search_obj = Page_Obj(self.driver).settings()
        self.search_obj.open_search_bar()

    def teardown_class(self):
        self.driver.quit()

    # def open_search_init(self):
    #     self.search_obj.open_search_bar()
    @allure.step(title="测试1号") #报告中添加step
    @allure.severity(allure.severity_level.CRITICAL)#报告中添加严重级别
    @pytest.mark.parametrize(('test','text'),search_data())
    def test_01(self,test,text):
        #报告中添加描述
        allure.attach('描述','开始搜索')
        self.search_obj.input_search_text(text)
        time.sleep(2)
        if text == 'call':
            assert False

        self.driver.get_screenshot_as_file("%s_%s.png" %(text,test))

# if __name__ == "__main__":
#     pytest.main()


