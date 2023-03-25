from selenium.webdriver.common.by import By
from Public.base_action import BaseAction


class ProtocolPopupPage(BaseAction):
    # 同意协议按钮
    tvAgree = (By.ID, "com.sfacg:id/tvAgree")
    # 不同意协议按钮
    tvDisagree = (By.ID, "com.sfacg:id/tvDisagree")

    def agree_click(self):
        self.click(self.tvAgree)

    def disagree_click(self):
        self.click(self.tvDisagree)