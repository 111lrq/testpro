from appium import webdriver
from app.appium_xueqiuframework.page.base_page import BasePage
from app.appium_xueqiuframework.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps['noReset'] = 'true'  # 记住关闭首次启动弹窗状态，再次启动不会打开弹窗
            caps['unicodeKeyBoard'] = True  # 支持中文键盘输入
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            caps['skipLogcatCapture'] = True
            caps['resetKeyBoard'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def end(self):
        print('teardown_class')
        self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)
