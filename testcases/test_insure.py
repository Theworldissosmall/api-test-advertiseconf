"""
# ================================================
# @name    : Tian
# @Time    : 2019/12/4 下午4:16
# @File    : test_insure.py
# @Email   :tianjianfeng1995@163.com
# ================================================
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

"""
测试用例保险查询模块
/insure/product/{productId}/detail
/orderInsure
/insuredOrderInfo/{uid}
/insuredInfo
/insureChannels
"""

# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")


"""获取保险入口"""
@ddt
class InsureDetail(unittest.TestCase):
    """获取保险入口"""
    excel = ReadExcel(data_file_path, 'detail')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_insuredetail(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data) #get方法，故不需要传值data；
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers = eval(case.headers)


        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容
        res = response.json()
        ress = res['remark']
        # print(ress)
        # 比对预期结果和实际结果，断言用例是否通过
        try:

            self.assertEqual(excepted, res)

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



    def tes(self):
        insure = InsureDetail.test_insuredetail()
        insuss = getattr(insure,'res')
        print(insuss)

#===========================================================================================#
"""摩卡订单查询"""


@ddt
class IusureOrderInsure(unittest.TestCase):
    """摩卡订单查询"""
    excel = ReadExcel(data_file_path, 'orderinsure')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_case_pointpark(self, case):
        # 准备测试用例数据
        url = case.url
        # data = eval(case.data) get方法，故不需要传值data；
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))


        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容
        res = response.json()

        # 将接口请求返回随机生成的token，替换掉用例里的*token*
        ress = res['orderStatus']
        if '*orderStatus*' in case.excepted:
            case.excepted = case.excepted.replace('*orderStatus*', ress)
            # return case.excepted
        excepted = eval(case.excepted)


        # 比对预期结果和实际结果，断言用例是否通过
        try:

            self.assertEqual(excepted, res)

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

# #===========================================================================================#
# """摩卡订单查询"""
# @ddt
# class InsuredOrderInfo(unittest.TestCase):
#     """摩卡订单查询"""
#     excel = ReadExcel(data_file_path, 'insuredOrderInfo')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         # data = eval(case.data) get方法，故不需要传值data；
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers)
#         # 获取返回的内容
#         res = response.json()
#
#
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             self.assertEqual(excepted, res)
#
#             print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format(excepted))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """借款相关投保信息"""
# @ddt
# class InsureInfo(unittest.TestCase):
#     """借款相关投保信息"""
#     excel = ReadExcel(data_file_path, 'insuredInfo')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         # data = eval(case.data) get方法，故不需要传值data；
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers)
#         # 获取返回的内容
#         res = response.json()
#
#
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             self.assertEqual(excepted, res)
#
#             print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format(excepted))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """查询保险渠道列表"""
# @ddt
# class InsureInfo(unittest.TestCase):
#     """查询保险渠道列表"""
#     excel = ReadExcel(data_file_path, 'insureChannels')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         # data = eval(case.data) get方法，故不需要传值data；
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers)
#         # 获取返回的内容
#         res = response.json()
#         # 将接口请求返回随机生成的token，替换掉用例里的*token*
#         ress = res['insureToken']
#         if '*insureToken*' in case.excepted:
#             case.excepted = case.excepted.replace('*insureToken*', ress)
#             # return case.excepted
#         excepted = eval(case.excepted)
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             self.assertEqual(excepted, res)
#
#             print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format(excepted))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """
# 摩卡客服操作接口-测试用例扣款取消模块
# insureRefund/checkRefundInfo/{insureNum}
# insureRefund/applyInsureRefund
# /insure/pay
# /insure/cancel
# """
# """核对退款人信息"""
# @ddt
# class CheckRefundInfo(unittest.TestCase):
#     """核对退款人信息"""
#     excel = ReadExcel(data_file_path, 'checkRefundInfo')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         # data = eval(case.data) get方法，故不需要传值data；
#         method = case.method
#
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers)
#         # 获取返回的内容
#         res = response.json()
#         #将接口请求返回随机生成的token，替换掉用例里的*token*
#         ress = res['token']
#         if '*token*' in case.excepted:
#             case.excepted = case.excepted.replace('*token*',ress)
#             # return case.excepted
#         excepted = eval(case.excepted)
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             self.assertEqual(excepted, res)
#             print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format(excepted))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
#
# #===========================================================================================#
#
# """退款操作申请"""
# @ddt
# class ApplyInsureRefund(unittest.TestCase):
#     """退款操作申请"""
#     excel = ReadExcel(data_file_path, 'applyInsureRefund')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     # data = excel.read_data_obj()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         data = eval(case.data)
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers,data=data)
#         # 获取返回的内容
#         res = response.json()
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             self.assertEqual(excepted, res)
#
#             print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format(excepted))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """支付保险--人工扣款"""
# @ddt
# class InsurePay(unittest.TestCase):
#     """支付保险--人工扣款"""
#     excel = ReadExcel(data_file_path, 'pay')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     # data = excel.read_data_obj()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         data = eval(case.data)
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers,data=data)
#         # 获取返回的内容
#         # res = response.json()
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#
#             # self.assertEqual(excepted, res)
#             if case.check_sql:
#                 db_res = self.db.find_count(case.check_sql)
#                 self.assertEqual(1,db_res)
#             # print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format('sql校验正确'))
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """撤销选中的保险"""
# @ddt
# class InsureCancel(unittest.TestCase):
#     """撤销选中的保险"""
#     excel = ReadExcel(data_file_path, 'cancel')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#     # data = excel.read_data_obj()
#     @data(*cases)
#     def test_case_pointpark(self, case):
#         # 准备测试用例数据
#         url = case.url
#         data = eval(case.data)
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         headers = eval(case.headers)
#
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers,data=data)
#         # 获取返回的内容
#         # res = response.json()
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#             if case.check_sql:
#                 db_res = self.db.find_count(case.check_sql)
#                 self.assertEqual(1,db_res)
#             # print('实际接口请求结果为:{}'.format(res))
#             print('预期接口请求结果为:{}'.format('sql校验正确'))
#
#         except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#             self.excel.write_data(row=row, column=9, value='未通过')
#             log.debug('{}，该条用例执行未通过'.format(case.title))
#             raise e
#
#         else:
#             # 测试用例执行通过
#             self.excel.write_data(row=row, column=9, value='通过')
#             log.debug('{}，该条用例执行通过'.format(case.title))
#
# #===========================================================================================#
# """
# 测试用例还款搭售模块
# /repay/products--获取搭售产品
# /repay/product/{code}--获取产品详情
# /repay/init--还款init
# /repay/confirm--还款确认
# /repay/cancel--还款确认取消
# """
#
#
#
#
#
#
#
# #===========================================================================================#
#
#
# """
# 测试用例搭售配置模块
# /tyingConfigs--搭售配置-查询列表
# /tyingConfigs--搭售配置-新增or修改
# /tyingConfigs/{id}--根据id查询搭售配置信息
# /tyingConfigs/{id}/{status}--更新搭售配置状态
# /tyingChannels--查询搭售渠道配置
# /tyingConfigs/sort--优先级调整
# /qualifications--查询资格
# /tying/filter/config--搭售过滤配置
# """






















