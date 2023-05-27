from appium import webdriver


def init_driver(isReset):
    # 配置信息，字典类型，直接复用上面的 Appium json就可以
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "e7044d18",
        # "app": "C:\\Users\\xxxx\\Downloads\\com.ddnapalon.calculator.gp_3.1.33_999349.apk",
        "appPackage": "com.sfacg",
        "appActivity": "com.sf.ui.launcher.LauncherActivity",
        "noReset": isReset,  # 不重置session信息
    }

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == "__main__":
    driver = init_driver()
