from hyrobot.common import *
from lib.webapi import apimgr

class Test_002:
    name = '添加药品 - API-0251'

    # 初始化方法
    def setup(self):
        apimgr.mgr_login()  # 登录
        apimgr.order_del_all()  # 删除全部订单  数据库中有外键关联，所以要按顺序删
        apimgr.customer_del_all()  # 删除全部客户
        apimgr.medicine_del_all()  # 除全部药品

    # 清除方法
    def teardown(self):
        # apimgr.customer_del(self.addedCustomerId)
        pass

    def test_添加药品01(self):
        pass