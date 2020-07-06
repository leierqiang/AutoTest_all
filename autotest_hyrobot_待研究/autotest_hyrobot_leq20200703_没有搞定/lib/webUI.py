from selenium import webdriver

from hyrobot.common import GSTORE


def open_browser():
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    return wd


def login(wd):
    wd.get('http:127.0.0.1/mgr/sign.html')

    # 根据id找到并输入账号密码
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')


def get_global_webdriver():
    return GSTORE['global_webdriver']
