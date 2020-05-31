from selenium import webdriver
from selenium.webdriver.common.by import By

'''
    这个类里面封装的是公共方法
'''


class BasePage:
    base_url = ''

    def __init__(self, driver: webdriver = None):
        # 声明一个driver变量，用于初始化webdriver
        driver = ''
        # 第一次打开浏览器的时候，driver是None，执行下边代码初始化一个driver
        if driver is None:
            # 配置Chrome选项
            option = webdriver.ChromeOptions()
            # chrome浏览器不出现‘Chrome正在受到自动软件的控制’的提示语
            option.add_argument('disable-infobars')
            # 打开一个浏览器
            self.driver = webdriver.ChromeOptions(option=option)
            # 浏览器窗口最大化
            self.driver.maxmize_window()
            # 隐式等待 防止出现定位元素的时候页面还未加载出来报错
            self.driver.implicitly_wait(3)

        # 用之前传过来的打开浏览器
        else:
            self.driver = driver
            if self.base_url != '':
                self.driver.get(self.base_url)

    # 封装元素定位
    def locateElement(self, locateType, value):
        el = None
        if locateType == 'id':
            el = self.driver.find_element_by_id(value)
        elif locateType == 'name':
            el = self.driver.find_element_by_name(value)
        elif locateType == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locateType == 'tag':
            el = self.driver.find_element_by_tag_name(value)
        elif locateType == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locateType == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locateType == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locateType == 'css':
            el = self.driver.find_element_by_css_selector(value)
        # 返回到定位元素
        return el
