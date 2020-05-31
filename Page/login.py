import time

from Page.base_page import BasePage
from Page.home import Home


class Login(BasePage):
    # 定义登录方法
    def login(self):
        # 定位企业登录按钮
        self.locateElement('css','.index_top_operation_loginBtn').click()
        time.sleep(5)
        return Home(self.driver)