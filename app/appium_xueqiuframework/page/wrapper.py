from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        from app.appium_xueqiuframework.page.base_page import BasePage
        _black_list = [
            # 伪造弹窗，将中间一步操作作为黑名单进行
            # self.find(By.XPATH, '//*[contains(@resource-id,"action_search"]')
            # (By.XPATH, '//*[contains(@resource-id,"action_search"]'),
            (By.ID, 'com.xueqiu.android:id/action_search'),
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_errnum = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            # 隐式等待时间恢复
            instance._driver.implicitly_wait(10)
            # 找到之后 _error_num 归0
            _error_num = 0
            return element
        # 处理黑名单中的弹窗
        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹
            instance._driver.implicitly_wait(2)
            # 判断异常处理次数
            if _error_num > _max_errnum:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return wrapper(*args, **kwargs)
                raise e
    return wrapper
