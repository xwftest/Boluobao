from selenium.webdriver.common.by import By
from Public.base_action import BaseAction


class StackPage(BaseAction):
    # 点击搜索输入框
    tv_search_tip = (By.ID, 'com.sfacg:id/search_img')

    def click_search_tip(self):
        self.click(self.tv_search_tip)
