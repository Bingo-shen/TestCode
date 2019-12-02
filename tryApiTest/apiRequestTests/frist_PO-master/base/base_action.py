from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver
    # 显示等待
    def find_elements(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    # 定义一个函数，取按钮的元素
    def act_click(self,loc):
        return self.act_title(loc).click()
    # 定义一个函数，取输入框的元素
    def act_text(self,loc,text):
        return self.act_title(loc).send_keys(text)
    def act_title(self, loc):
        by = loc[0]
        value = loc[1]
        return self.driver.find_element(by, value)

