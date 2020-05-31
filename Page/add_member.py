from Page.base_page import BasePage


class AddMember(BasePage):
    # 添加成员
    def add_member(self):
        # 定位到用户名
        self.locateElement('id', 'username').sendKeys('孙悟空')
        # 定位要英文名
        self.locateElement('id', 'memberAdd_english_name').sendKeys('wukong')
        # 邮箱
        self.locateElement('id', 'memberAdd_acctid').sendKeys('guozongmei97@163.com')
        # 手机号
        self.locateElement('id', 'memberAdd_phon').sendKeys('17775593096')
        # 保存按钮
        self.locateElement('css','form .ww_operationBar:nth-of-type(3) .js_btn_save').click()
