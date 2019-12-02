# 获取本地地址
import sys, os
sys.path.append(os.getcwd())

from base.base_driver import Testbase
from page.display_page import DisplayPage

class TestDisplay:
    def setup(self):
        self.driver = Testbase()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        # 点击显示
        self.display_page.click_see()
        # 点击放大镜
        self.display_page.click_search()
        # 文本输入
        self.display_page.input_text("hello")
        # 点击返回
        self.display_page.click_back()

    def teardown(self):
        self.driver.quit()


