from selenium.webdriver.common.by import By
from Public.base_action import BaseAction

from Public.base_driver import init_driver
from time import sleep


class NovelSearchPage(BaseAction):
    # 书库搜索入口
    search_layout = (By.ID, 'com.sfacg:id/search_layout')
    # 搜索输入框
    inputSearch = (By.ID, 'com.sfacg:id/inputSearch')
    # 搜索按钮
    search_icon_btn = (By.ID, 'com.sfacg:id/iv_think_icon')

    def search_layout_click(self):
        self.click(self.search_layout)

    def inputSearch_input(self, test):
        self.input(self.inputSearch, test)

    def search_btn(self):
        self.click(self.search_icon_btn)


if __name__ == '__main__':
    Mydriver = init_driver()
    searchpage = NovelSearchPage(Mydriver)
    sleep(2)
    Mydriver.find_element(By.ID, 'com.sfacg:id/tvAgree').click()
    searchpage.search_layout_click()
    sleep(3)
    searchpage.inputSearch_input('英雄')
    sleep(3)
    searchpage.search_btn()
    sleep(6)
    print('调试完成')