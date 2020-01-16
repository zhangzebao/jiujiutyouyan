from appium import webdriver


class GetDriver:
    driver = None

    # 获取driver对象
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            caps = dict()
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '5.1'
            caps['deviceName'] = '192.168.56.101:5555'
            caps['automationName'] = 'Uiautomator2'
            caps['appPackage'] = 'com.xraybot.jiujiutouyan'
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            caps['noReset'] = True
            caps['appActivity'] = 'com.xraybot.touyan.home.ui.activity.HomeActivity'
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        return cls.driver

    # 关闭driver对象
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    print("第一次获取driver对象：", GetDriver.get_driver())
    GetDriver.quit_driver()
    print("第二次获取driver对象：", GetDriver.get_driver())
