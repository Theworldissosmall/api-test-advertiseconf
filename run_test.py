
"""
项目启动文件
"""
import  unittest
from testcases import test_acquirecampaign
from pack_lib.HTMLTestRunnerNew import HTMLTestRunner
from common.mylogger import log
from common.constant import CASE_DIR,REPORT_DIR
import os
import time

from testcases.test_acquirecampaign import AdvertisesPageId, GetAdvertiseByCode, GetAdvertisesListByCodes, \
    GetMaterialByCode, AdvertiseConfigs, GetAdvertiseConfigDetails, SUBT

log.info('---------正在开启测试运行程序----------')
now = time.strftime('%Y-%m-%d_%H_%M_%S')
#创建测试套件
suite = unittest.TestSuite()
#将用例添加到套件中
loader = unittest.TestLoader()

#执行testcases包下所有的用例
# suite.addTest(loader.discover(CASE_DIR))

#执行单条测试用例类
# suite.addTest(loader.loadTestsFromTestCase(AcquireCampaign))
# suite.addTest(loader.loadTestsFromTestCase(SendMsg))
# suite.addTest(loader.loadTestsFromTestCase(Registered_Log))
# suite.addTest(loader.loadTestsFromTestCase(GetByMobileAndAppName))
# suite.addTest(loader.loadTestsFromTestCase(GetByJxUidAndAppName))
suite.addTest(loader.loadTestsFromTestCase(SUBT))

#执行单个方法：
# suite.addTest(loader.loadTestsFromModule(test_acquirecampaign))
# suite.addTest(loader.loadTestsFromModule(test_sendMsg))
# suite.addTest(loader.loadTestsFromModule(GetAdvertiseConfigDetails.test_getAdvertiseConfigDetails))


# 拼接报告的路径
report_file_path = os.path.join(REPORT_DIR,'report' + now + '.html')
#执行用例，生成测试报告
with open(report_file_path,'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='CMS接口测试报告',
                            description='CMS接口自动化测试报告',
                            tester='Tian')

    runner.run(suite)
log.info('---------测试运行程序执行完毕----------')
