from appium import webdriver

from app.appium_wework.page.Main import Main
from app.appium_wework.page.basepage import BasePage


class App(BasePage):
    def start(self):
        if self._driver == "none":
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps['noReset'] = 'true'
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def end(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
