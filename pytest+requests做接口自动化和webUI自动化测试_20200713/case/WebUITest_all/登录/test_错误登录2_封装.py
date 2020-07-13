# 重要： 执行命令前面加 python -m，否则找不到模块
# python -m pytest case


from selenium import webdriver
from lib import webUI


class Test_登录功能(object):
    # http://127.0.0.1/mgr/sign.html   buhy/88888888
    def test_UI_001(self):
        print('\n 用例 UI_001')

        alertText = webUI.loginAndCheck(None, 88888888)
        assert alertText == '请输入用户名'

    def test_UI_002(self):
        print('\n 用例 test_UI_002')

        alertText = webUI.loginAndCheck('buhy', None)
        assert alertText == '请输入密码'

    def test_UI_003(self):
        print('\n 用例 UI_001')

        alertText = webUI.loginAndCheck('buhy', 888888889)
        assert alertText == '登录失败 : 用户名或者密码错误'
