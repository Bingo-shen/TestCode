from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):

# 抽离元素
    # 更多按钮
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 网络移动按钮
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    #首选网络类型按钮
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2G选择按钮
    button_2g = By.XPATH, "//*[contains(@text,'2G')]"
    # 3G选择按钮
    button_3g = By.XPATH, "//*[contains(@text,'3G')]"

# 代码精简方式，提取公共元素
    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'更多')]").click()
        self.act_click(self.more_button)


    def click_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'移动网络')]").click()
        self.act_click(self.network_button)


    def click_first_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'首选网络类型')]").click()
        self.act_click(self.first_network_button)

    def mobile_network_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'2G')]").click()
        self.act_click(self.button_2g)


    def mobile_network_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'2G')]").click()
        self.act_click(self.button_3g)