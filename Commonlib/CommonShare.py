from selenium import webdriver


# 封装开启关闭浏览器
class Common(object):
    # 初始化
    def __init__(self):
        # 创建浏览器
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(3)
        # 最大化浏览器
        self.driver.maximize_window()

    # 访问指定URL
    def openUrl(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # 封装定位
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

    # 封装对元素的基本操作
    def click(self, locateType, value):
        # 调用locateElement
        el = self.locateElement(locateType,value)
        # 执行点击操作
        el.click()

    # 直接对定位到的文本元素进行文本输入
    def input_data(self,locateType,value,data):
        # 调用locateElement
        el = self.locateElement(locateType,value)
        # 执行点击操作
        el.send_keys(data)

    # 获取定位到元素的文本内容<a>xxx</a>
    def getText(self,locateType,value):
        # 调用locateElement
        el = self.locateElement(locateType,value)
        return el.text

    # 获取定位元素的标签属性
    def getAttribute(self,locateType,value,data):
        # 调用locateElement
        el = self.locateElement(locateType,value)
        return el.get_attribute(data)

    def close_driver(self):
        self.driver.quit()

    # 结束的时候销毁
    def __del__(self):
        self.driver.quit()


# 判断文件是否自身执行，如果是，则是执行之后的语句
if __name__ == '__main__':
    com = Common()
    com.openUrl('http://www.baidu.com')
