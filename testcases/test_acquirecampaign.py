import unittest
from common.random_phone import generate_random_str, create_phone
from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest
from common.mylogger import log
from common.constant import DATA_DIR
from common.my_mysql import ReadSQL
# import common.my_mysql
import configparser
import os

os.chdir('/Users/tianjianfeng/PycharmProjects/api-test-tian/conf')
cf = configparser.ConfigParser()

"""
#SafetyAdvertiseController#
/advertises/{pageId}---通过pageId获取保底广告
/getAdvertises/{pageId}---通过pageId获取保底广告

#GetAdvertiseController#
/getAdvertiseByCode?adConfigcode ----根据广告配置code获取广告配置
/getAdvertisesListByCodes----根据广告配置codes获取广告配置
/getMaterialByCode---根据素材code获取广告素材
/advertiseConfigs/{tagCode}---根据广告配置code获取广告配置
/getAdvertiseConfigDetails---根据广告配置code获取广告配置

#CmsConfigController#
/config/batch/save---批量保存cms配置内容----body问题待确认
/config/save----批量保存cms配置内容---body问题待确认
/config/online---组件配置信息上线
/config/offline---组件配置信息下线
/config/query/{code}/{version}/{minVersion}---根据code获取cms配置
/component/config/preview---h5组件预览接口
/config/list---获取cms配置列表
/component/online_config/all---获取所有线上配置列表
/config/delete/{code}/{version}/{minVersion}---根据code删除cms配置
/finance/product/businesstype/list---金融产品业务类型
/config/operate_log/list---获取操作日志
/config/compare/list---获取组件比较结果，仅比较出组件和素材及角标级别
/config/cache---配置缓存



"""
# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "advertiseconf.xlsx")

"""通过pageId获取保底广告"""
@ddt
class AdvertisesPageId(unittest.TestCase):
    """通过pageId获取保底广告"""
    excel = ReadExcel(data_file_path, 'advertises-pageId')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_advertisespageId(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # sql = case.check_sql
         # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code
        # 获取返回的内容
        response= response.json()


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            # self.assertEqual(excepted,response)

            print('实际该接口请求实际返回的状态码为:{}'.format(res))
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

###################################################################

"""通过pageId获取保底广告"""
@ddt
class GetAdvertisesPageId(unittest.TestCase):
    """通过pageId获取保底广告"""
    excel = ReadExcel(data_file_path, 'getAdvertises-pageId')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_getAdvertisespageId(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # sql = case.check_sql
         # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code
        # 获取返回的内容
        response= response.json()


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            # self.assertEqual(excepted,response)

            print('实际该接口请求实际返回的状态码为:{}'.format(res))
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

###################################################################


"""根据广告配置code获取广告配置"""
@ddt
class GetAdvertiseByCode(unittest.TestCase):
    """根据广告配置code获取广告配置"""
    excel = ReadExcel(data_file_path, 'getAdvertiseByCode')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_getAdvertiseByCode(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                #如果数据库检索出条数，就与1比对
                if db_res == 1:
                    self.assertEqual(1, db_res)
                # 如果数据库检索不出条数，就与0比对
                else:
                    self.assertEqual(0, db_res)
                print('实际该接口查询的sql为:{}'.format(case.check_sql))
                print('实际该接口执行sql查询出的数据条数为:{}'.format(db_res))
            print('实际该接口请求实际返回的状态码为:{}'.format(res))


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

###################################################################

"""根据广告配置codes获取广告配置"""
@ddt
class GetAdvertisesListByCodes(unittest.TestCase):
    """根据广告配置code获取广告配置"""
    excel = ReadExcel(data_file_path, 'getAdvertisesListByCodes')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_getAdvertisesListByCodes(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                #如果数据库检索出条数，就与1比对
                if db_res == 1:
                    self.assertEqual(1, db_res)
                # 如果数据库检索不出条数，就与0比对
                else:
                    self.assertEqual(0, db_res)
                print('实际该接口查询的sql为:{}'.format(case.check_sql))
                print('实际该接口执行sql查询出的数据条数为:{}'.format(db_res))
            print('实际该接口请求实际返回的状态码为:{}'.format(res))


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

###################################################################

"""根据素材code获取广告素材"""
@ddt
class GetMaterialByCode(unittest.TestCase):
    """根据素材code获取广告素材"""
    excel = ReadExcel(data_file_path, 'getMaterialByCode')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_getMaterialByCode(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                #如果数据库检索出条数，就与1比对
                if db_res == 1:
                    self.assertEqual(1, db_res)
                # 如果数据库检索不出条数，就与0比对
                else:
                    self.assertEqual(0, db_res)
                print('实际该接口查询的sql为:{}'.format(case.check_sql))
                print('实际该接口执行sql查询出的数据条数为:{}'.format(db_res))
            print('实际该接口请求实际返回的状态码为:{}'.format(res))


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

###################################################################

"""根据广告配置code获取广告配置"""
@ddt
class AdvertiseConfigs(unittest.TestCase):
    """根据广告配置code获取广告配置"""
    excel = ReadExcel(data_file_path, 'advertiseConfigs')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_advertiseConfigs(self, case):
        # 准备测试用例数据
        url = case.url
        # excepted = case.excepted
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(200, res)
            if case.check_sql:
                db_res = self.db.find_count(case.check_sql)
                #如果数据库检索出条数，就与1比对
                if db_res == 1:
                    self.assertEqual(1, db_res)
                # 如果数据库检索不出条数，就与0比对
                else:
                    self.assertEqual(0, db_res)
                print('实际该接口查询的sql为:{}'.format(case.check_sql))
                print('实际该接口执行sql查询出的数据条数为:{}'.format(db_res))
            print('实际该接口请求实际返回的状态码为:{}'.format(res))


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

###################################################################

"""根据广告配置code获取广告配置"""
@ddt
class GetAdvertiseConfigDetails(unittest.TestCase):
    """根据广告配置code获取广告配置"""
    excel = ReadExcel(data_file_path, 'getAdvertiseConfigDetails')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_getAdvertiseConfigDetails(self, case):
        # 准备测试用例数据
        url = case.url
        method = case.method
        row = case.case_id + 1
        headers = eval(case.headers)
        # 发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url,headers=headers)
        # 获取返回的内容,该接口无返回参数，只需获取状态码即可
        res = response.status_code


        # 比对预期结果和实际结果，断言用例是否通过
        try:
            if res==200:
                self.assertEqual(200, res)
            else:
                self.assertEqual(500, res)
            if case.check_sql:
                db_res =self.db.find_count(case.check_sql)
                if db_res == 1:
                    self.assertEqual(1,db_res)
                else:
                    self.assertEqual(0,db_res)
            print('实际该接口请求实际返回的状态码为:{}'.format(res))


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

###################################################################
#
# """批量保存cms配置内容"""
# @ddt
# class BatchSave(unittest.TestCase):
#     """批量保存cms配置内容"""
#     excel = ReadExcel(data_file_path, 'batchsave')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#     db = ReadSQL()
#
#     @data(*cases)
#     def test_batchsave(self, case):
#         # 准备测试用例数据
#         url = case.url
#         method = case.method
#         row = case.case_id + 1
#         headers = eval(case.headers)
#         # 发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url,headers=headers)
#         # 获取返回的内容,该接口无返回参数，只需获取状态码即可
#         res = response.status_code
#
#
#         # 比对预期结果和实际结果，断言用例是否通过
#         try:
#             if res==200:
#                 self.assertEqual(200, res)
#             else:
#                 self.assertEqual(500, res)
#             if case.check_sql:
#                 db_res =self.db.find_count(case.check_sql)
#                 if db_res == 1:
#                     self.assertEqual(1,db_res)
#                 else:
#                     self.assertEqual(0,db_res)
#             print('实际该接口请求实际返回的状态码为:{}'.format(res))
#
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
# ###################################################################
#
# #
"""继承类测试"""
class SUBT(GetAdvertiseConfigDetails):
    excel = ReadExcel(data_file_path, 'AdvertiseConfigs')
    print(excel)

#
# ###################################################################