"""
==========================================
author:田剑锋
file: http_requests.py
time: 2019/09/2019/9/18/21:03
E-mail:tianjianfeng1995@163.com
==========================================
"""
import requests


class HTTPRequest(object):
    """直接发请求不记录cookies信息的 """

    def request(self, method, url,data=None, headers=None):
        """GET   get"""
        # 发送请求的方法
        method = method.lower()
        if method == 'post':
            # 判断是否使用json来传参
            return requests.post(url=url, json=data, headers=headers)

        elif method == 'get':
            return requests.get(url=url, params=data, headers=headers)
        else:
            print('excel表单中方法输入错误，请修改后重新执行')


class HTTPSession(object):
    """使用session对象发送请求，自动记录cookies信息 """

    def __init__(self):
        # 创建一个session对象
        self.session = requests.session()

    def request(self, method, url,data=None, headers=None):
        # 判断请求的方法
        method = method.lower()
        if method == 'post':
            return self.session.post(url=url, data=data, headers=headers)
        elif method == 'get':
            return self.session.get(url=url, params=data, headers=headers)
        else:
            print('excel表单中方法输入错误，请修改后重新执行')

    def close(self):
        self.session.close()
