from Page.add_member import AddMember
from Page.base_page import BasePage


class Home(BasePage):
    '''
    成功登录之后，有很多常用功能，比如添加成员，导入通讯录，成员加入，消息群发，客户联系，打卡
    '''
    def add_member(self):
        self.locateElement('text', '添加成员').click()
        # 点击后又要跳到新的页面去了->通讯录页面
        return AddMember(self.driver)