import pytest
from lib.webUI import *

from lib.webUI import loginAndCheck


class Test_某个使用全局变量driver的用例(object):
    # 初始化方法
    def setup(self):
        print("\r\n------------------初始化方法------------------\r\n")

    # 清除方法
    def teardown(self):
        print("\r\n------------------清除方法------------------\r\n")

        # apimgr.customer_del(self.addedCustomerId)

    # 用例参数化
    @pytest.mark.parametrize('username,password, expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('buhy', None, '请输入密码'),
        ('buhy', 888888889, '登录失败 : 用户名或者密码错误'),
    ])
    # 用例
    def test_UI_00_all(self, username, password, expectedalert):
        alertText = loginAndCheck(username, password)

        driver = Common().driver
        print("执行操作")
        Common.set_driver(driver)  # 浏览器不用频繁开关，操作连贯时间短
        assert alertText == expectedalert
