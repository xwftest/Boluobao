from selenium.webdriver.common.by import By
from Public.base_action import BaseAction
from time import sleep


class SearchPage(BaseAction):
    # 搜索输入框
    inputSearch = (By.ID, 'com.sfacg:id/inputSearch')
    # 执行搜索
    searchBtn = (By.ID, 'com.sfacg:id/tv_think_text')
    # 筛选入口
    tvSortTag = (By.ID, 'com.sfacg:id/tvSortTag')
    # 脑洞标签
    zd_label = (By.XPATH, "//android.widget.TextView[@text='脑洞']")
    # 选择连载中
    work_status = (By.ID, 'com.sfacg:id/status_online_btn')
    # 筛选弹窗中，点击确定
    tvOk = (By.ID, 'com.sfacg:id/tvOk')
    # 选择漫画tab
    comic_tap = (By.XPATH, "//android.widget.TextView[@text='漫画']")
    # 选择有声tab
    audible_tap = (By.XPATH, "//android.widget.TextView[@text='有声']")
    # 选择对话tab
    dialogue_tap = (By.XPATH, "//android.widget.TextView[@text='对话']")

    def input_Search(self, test):
        self.input(self.inputSearch, test)

    def input_Search_clear(self):
        self.clear(self.inputSearch)

    def click_search_btn(self):
        self.click(self.searchBtn)

    def click_tvSortTag(self):
        self.click(self.tvSortTag)

    def click_comic_tap(self):
        self.click(self.comic_tap)

    def click_audible_tap(self):
        self.click(self.audible_tap)

    def click_dialogue_tap(self):
        self.click(self.dialogue_tap)

    def novel_screen(self):
        # 选择脑洞标签
        self.click(self.zd_label)
        # 选择连载中
        self.click(self.work_status)
        sleep(1)
        # 点击确定按钮
        self.click(self.tvOk)

