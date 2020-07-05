from hyrobot.common import *
from lib.webapi import apimgr

class Test_001:
    name = '添加客户 - API-0151'

    # 初始化方法
    def setup(self):
        apimgr.mgr_login()
        apimgr.order_del_all()
        apimgr.customer_del_all()
        apimgr.medicine_del_all()

    #清除方法
    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def test_添加客户01(self):

        # STEP(1, '添加一个客户')
        r = apimgr.customer_add('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")

        addRet = r.json()

        self.addedCustomerId = addRet['id']

        CHECK_POINT('返回的ret值=0',
                    addRet['ret'] == 0)


        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "武汉市桥西医院北路",
                    "id": addRet['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                }
            ] ,
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)
