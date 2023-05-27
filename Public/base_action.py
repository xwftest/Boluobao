from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=1):
        """

        :param location: 元素位置
        :param timeout: 设置多少秒
        :param poll: 每多少秒找一次
        :return:
        """
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(*location))

    def find_elements(self, location, timeout=10, poll=1):
        """

        :param location: 元素位置
        :param timeout: 设置多少秒
        :param poll: 每多少秒找一次
        :return:
        """
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(*location))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, test):
        self.find_element(location).send_keys(test)

    def clear(self, location):
        self.find_element(location).clear()
