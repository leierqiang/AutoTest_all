# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

请求相关
'''

import json
import requests
from bs4 import BeautifulSoup
from lib.LoggerHandler import logger


class RequestHandler(object):

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response = self.send_request()

        return response

    def send_request(self):
        """ 发请求 """
        try:
            response = requests.request(
                method=self.case['case_method'],
                url=self.case['case_url'],
                params=self._check_params()
            )

            content_type = response.headers['Content-Type']

            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
                content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                response = getattr(self, '_check_{}_response'.format(content_type))(response)
                # print("\r\n" + "-" * 30 + "\r\n")
                # print(response)
                # print("\r\n" + "-" * 30 + "\r\n")
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']

        return response

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        print(response)
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                # # if self.case_expect[key] == response[key]:  # 用例执行失败的
                #     print("\r\n" + "-" * 30 + "\r\n")
                #     print(self.case_expect)
                #     print(self.case_expect[key])
                #     print(response[key])
                #     print("\r\n" + "-" * 30 + "\r\n")
                return {key: self.case_expect[key]}, {key: response[key]}
            else:  # 执行成功,注：只比较了第一组，只要第一个于预期相符就认为是对的，例如”{'success': True, 'data': [{'id': '5efdafbc13f8b244e57ccb6f', 'author_id': '4...“ 与”{'success': True}“一致
                logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
                return {key: self.case_expect[key]}, {key: response[key]}

    def _check_html_response(self, response):
        """ 校验html类型的数据"""
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        title = soup_obj.find('title').text
        return title, self.case_expect  # 返回title和预期值 两个  准备比对

    def _check_params(self):
        """ 整理参数 """
        if self.case['case_params']:
            """
            做扩展
            """
            pass
        else:
            return {}
