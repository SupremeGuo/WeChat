import time
from Page.base_page import BasePage
from Page.register import Register
from Page.login import Login

'''
创建进入企业微信的首页page
'''


class Index(BasePage):
    # 企业微信的url
    base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        # 定位到立即注册按钮
        self.locateElement('text', "立即注册").click()
        # 点击注册之后跳转到注册页面
        return Register(self.driver)

    def goto_logo(self):
        # 登录
        return Login(self.driver)

    def quit(self):
        # 关闭浏览器
        self.driver.quit()
