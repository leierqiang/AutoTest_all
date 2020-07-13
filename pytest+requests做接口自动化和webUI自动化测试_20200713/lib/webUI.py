import time

from selenium import webdriver


def loginAndCheck(username, password):
    """
    登录并检查   # http://127.0.0.1/mgr/sign.html   buhy/88888888
    :param username:
    :param password:
    :return:
    """

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://127.0.0.1/mgr/sign.html')
    if username is not None:
        driver.find_element_by_id('username').send_keys(username)
    if password is not None:
        driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(2)
    alertText = driver.switch_to.alert.text
    print(alertText)
    driver.quit()
    return alertText


# 全局变量
class Common:
    """
    全局driver
    """
    driver = None  # 全局变量

    def staring(self):
        driver = webdriver.Chrome()
        return driver

    def set_driver(self, dr):
        Common.driver = dr
        return Common.driver
