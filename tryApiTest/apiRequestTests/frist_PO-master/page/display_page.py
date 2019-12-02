from base.base_action import BaseAction
from selenium.webdriver.common.by import By

class DisplayPage(BaseAction):
    # 初始化方法
    # 显示按钮
    see_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 放大镜按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 放大镜旁边的输入文本
    search_edit_text = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"
    #
    # # 定义一个函数，取按钮的元素
    # def act_click(self,loc):
    #     return self.driver.find_element(loc[0],loc[1]).click()
    # # 定义一个函数，取输入框的元素
    # def act_text(self,loc,text):
    #     return self.driver.find_element(loc[0],loc[1]).send_keys(text)

    # def __init__(self, driver):
    #     self.driver = driver


    # 点击显示
    def click_see(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(self.see_button).click()
        self.act_click(self.see_button)

    # 点击放大镜
    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element(self.search_button).click()
        self.act_click(self.search_button)


    # 输入文本
    def input_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.driver.find_element(self.search_edit_text).send_keys(text)
        self.act_text(self.search_edit_text,text)

    # 点击返回
    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element(self.back_button).click()
        self.act_click(self.back_button)

