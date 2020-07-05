# 有用例后根据用例梳理自动化脚本
# 用例与自动化的case名称关联，最好一致
import time

from selenium import webdriver
from lib import webUI


class Test_登录功能(object):
    # http://127.0.0.1/mgr/sign.html   buhy/88888888
    def test_UI_001(self):
        # """
        # 用例测试点：不输入账号直接输入密码，测试页面有浏览器的原生提示'请输入用户名'
        # :return:
        # """
        print('\n 用例 UI_001')
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://127.0.0.1/mgr/sign.html')
        # driver.find_element_by_id('username').send_keys('buhy')
        driver.find_element_by_id('password').send_keys('88888888')
        driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(2)

        alertText = driver.switch_to.alert.text
        print(alertText)
        assert alertText == '请输入用户名'

    def test_UI_002(self):
        """
        用例测试点：不输入密码，测试页面有浏览器的原生提示'请输入密码'
        :return:
        """
        print('\n 用例 UI_001')
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://127.0.0.1/mgr/sign.html')
        driver.find_element_by_id('username').send_keys('buhy')
        # driver.find_element_by_id('password').send_keys('88888888')
        driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(2)

        alertText = driver.switch_to.alert.text
        print(alertText)
        assert alertText == '请输入密码'

    def test_UI_003(self):
        """
        用例测试点：用户名或密码错误，测试页面有浏览器的原生提示'用户名或密码错误'
        :return:
        """
        print('\n 用例 UI_001')
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://127.0.0.1/mgr/sign.html')
        driver.find_element_by_id('username').send_keys('buhy')
        driver.find_element_by_id('password').send_keys('888888889')
        driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(2)

        alertText = driver.switch_to.alert.text
        print(alertText)
        assert alertText == '用户名或者密码错误'
