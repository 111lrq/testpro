import os
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
action=ActionChains(driver)
handles=driver.window_handles
cur_handles=driver.current_window_handle
#待实践补充的点
#窗口设置大小
# web控件的交互进阶：
#     ActionChains（PC）：点击，按键，移动，其他；TouchActions（PC&）
#     action.click()
# 网页frame与多窗口切换
#     driver.switch_to.frame() #id,index(0),name,webelement传入的对象
#     driver.switch_to.default_content()
#     driver.switch_to.parent_frame()
#     driver.switch_to.handles[-1]
# 多浏览器处理
# def test_browser():
#     browser=os.getenv("browser").lower()
#     if browser=='headless':
#         driver=webdriver.PhantomJS()
#     elif browser=='firefox':
#         driver=webdriver.Firefox()
#     else:
#         driver=webdriver.Chrome()
#     driver.get('')
# 执行JS脚本
#     driver.execute_script()
#     js="return JSON.stringify(performance.timing);"
#     driver.execute_script(js)
#     传参
#         element=driver.find_element(by,locator)
#         driver.execute_script("arguments[0].click();",element)
#     文件上传:定位按钮，send_keys(路径)
#         driver.find_element(By.CSS_SELECTOR,"#js_upload_input").send_keys("./123.png")
#     弹窗处理:(alert,confirm,prompt)
#         WebDriverWait(driver,5).until(EC.alert_is_present())
#         alert=driver.switch_to.alert
#         print(alert.text)
#         alert.send_keys()
#         alert.accept()
#         alert.dimiss()
#     其他JS脚本:
#         除掉元素只读属性
#         driver.execute_script("arguments[0].removeAttribute('readonly')",element)
#         元素滚动至指定位置
#         driver.execute_script(("arguments[0].scrollIntoView(true);",element))
#         元素属性由"none"改为"block"
#         driver.execute_script(('document.querySelector("#js_upload_input")','.style.display="block";'))
#     多个JS脚本执行：
#         js1="return document.getElementById('su')"
#         js2="return document.documentElement.scrollTop=1000"
#         js3="return document.title"
#         js4="return JSON.stringify(performance.timing)"
#         for code in ['js1','js2','js3','js4']: #or['js1;js2;js3;js4']
#             print(driver.execute_script(code)) #return的话，s1之后就不再print
#     JS处理时间控件:
#         大部分时间控件都得readonly属性，需要手动选择对应时间，自动化中JS实现
#         思路：1.取消readonly属性（JS）
#              2.给value赋值（JS）
#              3.JS实现1.2，使用webdriver执行





