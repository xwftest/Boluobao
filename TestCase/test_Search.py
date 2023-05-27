import unittest

from selenium.webdriver.common.by import By
from time import sleep
from Public.base_driver import init_driver
from Page.stack_page import StackPage
from Page.search_page import SearchPage


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = init_driver(isReset=True)
        cls.stack_page = StackPage(driver=cls.driver)
        cls.search_page = SearchPage(driver=cls.driver)

    # 轻小说搜索
    def test_01_novel_search(self):
        # 点击书库首页搜索入口
        sleep(3)
        self.stack_page.click_search_tip()
        sleep(3)
        # 输入作品名关键词搜索
        self.search_page.input_Search('英雄')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            self.assertEqual('英雄再临(英雄？我早就不当了)', self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookTitle').text)
        except NotImplementedError as e:
            return e
        # 输入作者名搜索
        self.search_page.input_Search_clear()
        self.search_page.input_Search('妄动')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            assert'妄动' in self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookAutor').text
        except NotImplementedError as e:
            return e

        # 点击筛选弹窗
        self.search_page.click_tvSortTag()
        sleep(2)
        # 选择标签、作品状态等进行筛选
        self.search_page.novel_screen()
        sleep(5)
        try:
            self.assertEqual('脑洞', self.driver.find_element(By.ID, 'com.sfacg:id/tvKey').text)
        except NotImplementedError as e:
            return e

    def test_02_comic_search(self):
        # 切换到漫画tab
        self.search_page.click_comic_tap()
        # 清楚输入框内容，并输入作品关键词
        self.search_page.input_Search_clear()
        self.search_page.input_Search('英雄')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            self.assertEqual('英雄？我早就不当了',
                             self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookTitle').text)
        except NotImplementedError as e:
            return e
        # 输入作者名搜索
        self.search_page.input_Search_clear()
        self.search_page.input_Search('太枣糕')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            assert'太枣糕' in self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookAutor').text
        except NotImplementedError as e:
            return e

    def test_03_audible_search(self):
        # 切换到有声tab
        self.search_page.click_audible_tap()
        # 清楚输入框内容，并输入作品关键词
        self.search_page.input_Search_clear()
        self.search_page.input_Search('我是高富帅')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            self.assertEqual('我是高富帅',
                             self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookTitle').text)
        except NotImplementedError as e:
            return e
        # 输入作者名搜索
        self.search_page.input_Search_clear()
        self.search_page.input_Search('SF有声制作组')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            element = self.driver.find_elements(By.ID, 'com.sfacg:id/tvbBookTitle')
            self.assertTrue(len(element) > 0)
        except NotImplementedError as e:
            return e

    def test_04_dialogue_search(self):
        # 切换到对话tab
        self.search_page.click_dialogue_tap()
        # 清楚输入框内容，并输入作品关键词
        self.search_page.input_Search_clear()
        self.search_page.input_Search('江湖策')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            self.assertEqual('江湖策',
                             self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookTitle').text)
        except NotImplementedError as e:
            return e
         # 输入作者名搜索
        self.search_page.input_Search_clear()
        self.search_page.input_Search('妄动')
        self.search_page.click_search_btn()
        sleep(3)
        try:
            assert '妄动' in self.driver.find_element(By.ID, 'com.sfacg:id/tvbBookAutor').text
        except NotImplementedError as e:
            return e

        # 点击筛选弹窗
        self.search_page.click_tvSortTag()
        sleep(2)
        # 选择标签、作品状态等进行筛选
        self.search_page.novel_screen()
        sleep(5)
        try:
            self.assertEqual('脑洞', self.driver.find_element(By.ID, 'com.sfacg:id/tvKey').text)
        except NotImplementedError as e:
            return e

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()