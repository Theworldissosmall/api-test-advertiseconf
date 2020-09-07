"""
==========================================
author:田剑锋
file: test_pointpark.py
time: 2019/09/2019/9/18/21:03
E-mail:tianjianfeng1995@163.com
==========================================
"""

"""
测试用例模块

"""
import os
import unittest
from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest
from common.mylogger import log
from common.constant import DATA_DIR
from common.my_mysql import ReadSQL
from common.text_replace import ConText,data_replace
import random

# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")


"""消耗积分"""
@ddt
class ConsumePointTestCase(unittest.TestCase):
    """try积分接口"""
    excel = ReadExcel(data_file_path, 'consumePoint')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_case_pointpark(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)

        # 处理case用例里需要替换的uid参数
        # if '#uid#' in case.data:
        #     case.data = data_replace(case.data)


        # 处理case用例里需要替换的serialNo参数
        serialNo = self.random_serialNo()

        if '*serialNo*' in case.data:
            case.data = case.data.replace('*serialNo*',serialNo)

            return case.data

        # if 'point' in case.data:
        #     sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)[8]
        #     if self.find_count(sql):
        #         excepted = case.data.replace('*point*',sql)
        #         return excepted




        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        # 获取返回的内容
        res = response.json()



        # 比对预期结果和实际结果，断言用例是否通过
        try:

            self.assertEqual(excepted, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual('1',db_res)
            print('实际接口请求结果为:{}'.format(res))
            print('预期接口请求结果为:{}'.format(excepted))
        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=9, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e

        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=9, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))
    def random_serialNo(self):
        '''随机生成serialNo'''
        while True:
            serialNo = "13"
            for i in range(9):
                num = random.randint(1,9)
                serialNo += str(num)

            # 数据库查询serialNo是否存在
            sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)
            if not self.db.find_count(sql):
                return serialNo


#===========================================================================================#


"""发放积分"""
@ddt
class SendPrizeTestCase(unittest.TestCase):
    """try积分接口"""
    excel = ReadExcel(data_file_path, 'sendPrize')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_case_pointpark(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)
        # 处理case用例里需要替换的uid参数
        if "#uid#" in case.data:
            case.data = data_replace(case.data)

        # 处理case用例里需要替换的serialNo参数
        serialNo = self.random_serialNo()
        if "*serialNo*" in case.data:
            case.data = case.data.replace("*serialNo*", serialNo)


        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        # 获取返回的内容
        res = response.json()
        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(excepted, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual(1, db_res)
            # print('实际接口请求结果为:{}'.format(res))
            # print('预期接口请求结果为:{}'.format(excepted))
            self.assertEqual(excepted, res)
            # if case.check_sql:
            #     db_res = self.db.find_count(case.check_sql)
            #     self.assertEqual('1',db_res)
            print('实际接口请求结果为:{}'.format(res))
            print('预期接口请求结果为:{}'.format(excepted))
        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=9, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=9, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))

    def random_serialNo(self):
        '''随机生成serialNo'''
        while True:
            serialNo = "13"
            for i in range(9):
                num = random.randint(1, 9)
                serialNo += str(num)

            # 数据库查询serialNo是否存在
            sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)
            if not self.db.find_count(sql):
                return serialNo


#===========================================================================================#

"""查询积分发放结果"""
@ddt
class QueryPointResultTestCase(unittest.TestCase):
    """try积分接口"""
    excel = ReadExcel(data_file_path, 'queryPointResult')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_case_pointpark(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)

        # 处理case用例里需要替换的uid参数
        if "#uid#" in case.data:
            case.data = data_replace(case.data)

        # 处理case用例里需要替换的serialNo参数
        serialNo = self.random_serialNo()
        if "*serialNo*" in case.data:
            case.data = case.data.replace("*serialNo*", serialNo)

        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        # 获取返回的内容
        res = response.json()
        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(excepted, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual(1, db_res)
            print('实际接口请求结果为:{}'.format(res))
            print('预期接口请求结果为:{}'.format(excepted))

        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=9, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=9, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))

    def random_serialNo(self):
        '''随机生成serialNo'''
        while True:
            serialNo = "13"
            for i in range(9):
                num = random.randint(1, 9)
                serialNo += str(num)

            # 数据库查询serialNo是否存在
            sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)
            if not self.db.find_count(sql):
                return serialNo

#===========================================================================================#


"""商品直充"""
@ddt
class StraightSendPrizeTestCase(unittest.TestCase):
    """try积分接口"""
    excel = ReadExcel(data_file_path, 'straightSendPrize')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    def random_serialNo(self):
        '''随机生成serialNo'''
        while True:
            serialNo = "13"
            for i in range(9):
                num = random.randint(1, 9)
                serialNo += str(num)

            # 数据库查询serialNo是否存在
            sql = "SELECT * FROM pointpark.point_activity_info where serialNo='{}'".format(serialNo)
            if not self.db.find_count(sql):
                return serialNo


    @data(*cases)
    def test_case_pointpark(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)
        # 处理case用例里需要替换的uid参数
        if "#uid#" in case.data:
            case.data = data_replace(case.data)

        # 处理case用例里需要替换的serialNo参数
        serialNo = self.random_serialNo()
        if "*serialNo*" in case.data:
            case.data = case.data.replace("*serialNo*", serialNo)


        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        # 获取返回的内容
        res = response.json()
        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(excepted, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual(1, db_res)
            print('实际接口请求结果为:{}'.format(res))
            print('预期接口请求结果为:{}'.format(excepted))
        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=9, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=9, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))
    db = ReadSQL()