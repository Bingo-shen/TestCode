
import os, sys
sys.path.append(os.getcwd())
from page.network_page import NetworkPage
from base.base_driver import Testbase

class TestNetwork:
    def setup(self):
        self.driver = Testbase()
        self.network_page = NetworkPage(self.driver)
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()

    def test_mobile_network_2g(self):

        self.network_page.mobile_network_2g()

    def test_mobile_network_3g(self):
        # self.network_page.click_more()
        # self.network_page.click_network()
        # self.network_page.click_first_network()
        self.network_page.mobile_network_3g()

    def teardown(self):
        self.driver.quit()
