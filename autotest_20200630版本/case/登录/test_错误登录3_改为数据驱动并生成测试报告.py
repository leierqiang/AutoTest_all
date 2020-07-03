# 重要： 执行命令前面加 python -m，否则找不到模块
# python -m pytest case
# 数据驱动即把测试数据放在一个列表中统一执行减少代码量，具体实现方式是parametrize装饰器
# 生成测试报告
# python -m pytest -vs case\登录\test_错误登录3_数据驱动parametrize.py --html=./report/report.html --self-contained-html


import pytest
from lib.webUI import *


class Test_登录功能(object):
    # http://127.0.0.1/mgr/sign.html   buhy/88888888
    @pytest.mark.parametrize('username,password, expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('buhy', None, '请输入密码'),
        ('buhy', 888888889, '登录失败 : 用户名或者密码错误'),
    ])
    def test_UI_00_all(self, username, password, expectedalert):
        alertText = loginAndCheck(username, password)
        assert alertText == expectedalert
