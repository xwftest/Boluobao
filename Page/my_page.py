from selenium.webdriver.common.by import By
from Public.base_action import BaseAction


class MyPage(BaseAction):
    # 立即登录按钮
    loginBtn = (By.ID, 'com.sfacg:id/toLoginBtn')

    def click_signin(self):
        self.click(self.loginBtn)
