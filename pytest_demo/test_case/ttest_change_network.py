import yaml
import sys,os
import pytest
sys.path.append(os.getcwd())
print(sys.path)
from pytest_demo.page.page_obj import Page_Obj
from pytest_demo.PO.Init_driver import init_driver

class Test_change_network:
    def setup_class(self):
        self.driver = init_driver()
        self.test = Page_Obj(self.driver).network_page()

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(scope='class',autouse=True)
    def open_mn(self):
        self.test.open_mobile_network()
        with open('data.yml','r') as f:
            self.mode_data = yaml.load(f)

    @pytest.mark.parametrize()
    def test_netwok_type(self,mode):
        # self.driver.launch_app()
        self.test.change_neworkmode(mode)
        assert "%s" %mode in self.driver.page_source

    @pytest.mark.skipif(2>1,reason='haha')
    def test_4G(self):
        self.driver.launch_app()
        self.test.change_neworkmode_to_4G()
        assert "4G" in self.driver.page_source

if __name__ == "__main__":
    pytest.main()