from Page.base_page import BasePage


# 这是注册页面
class Register(BasePage):
    # 方法注册
    def register(self):
        # 定位企业名称 并且输入数据
        self.locateElement('id', 'corp_name').send_keys('mango')
        # 定位行业类型并点击
        self.locateElement('text', "选择行业类型").click()
        # 二级菜单
        self.locateElement('text',
                           "#corp_industry > div > table > tbody > tr > td.register_industry_wrap.register_industry_maintype_wrap > div:nth-child(1) > a").click()
        self.locateElement('text', '选择人员规模')
