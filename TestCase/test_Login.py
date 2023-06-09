import unittest

from selenium.webdriver.common.by import By
from Page.my_page import MyPage
from Page.protocol_popup_page import ProtocolPopupPage
from Page.sign_up_page import SignUpPage
from Public.base_driver import init_driver
from time import sleep
from Public.get_data import getData


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = init_driver(isReset=False)
        self.protocol_popup_page = ProtocolPopupPage(driver=self.driver)
        self.my_page = MyPage(driver=self.driver)
        self.sign_up_page = SignUpPage(driver=self.driver)

    def test_login(self):
        self.protocol_popup_page.agree_click()
        sleep(3)
        # 跳转我的页面
        self.driver.find_element(By.ID, 'com.sfacg:id/main_tab_container5').click()
        sleep(2)
        self.my_page.click_signin()
        # 获取登录账号和密码
        name = getData(1, 2)
        pwd = getData(1, 3)
        sleep(3)
        self.sign_up_page.account_input(number=name)
        self.sign_up_page.password_input(password=pwd)
        self.sign_up_page.login_click()
        sleep(1)
        self.sign_up_page.agreement()
        sleep(5)
        try:
            self.assertEqual('妄动',self.driver.find_element(By.ID, 'com.sfacg:id/nickname').text)
        except NotImplementedError as e:
            return e

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()