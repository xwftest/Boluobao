from selenium.webdriver.common.by import By
from Public.base_action import BaseAction


class SignUpPage(BaseAction):
    # 输入账号
    etAccount = (By.ID, 'com.sfacg:id/etAccount')
    # 输入密码
    etPassword = (By.ID, 'com.sfacg:id/etPassword')
    # 登录按钮
    btn_login = (By.ID, 'com.sfacg:id/btn_login')
    # 同意协议按钮
    tvConfirm = (By.ID, 'com.sfacg:id/tvConfirm')

    def account_input(self, number):
        self.input(self.etAccount, number)

    def password_input(self, password):
        self.input(self.etPassword, password)

    def login_click(self):
        self.click(self.btn_login)

    def agreement(self):
        self.click(self.tvConfirm)