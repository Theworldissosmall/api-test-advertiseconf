"""
==========================================
author:田剑锋
file: run_test.py
time: 2019/09/2019/9/18/21:03
E-mail:tianjianfeng1995@163.com
==========================================
"""
import  unittest
"""
引入单条测试用例类
"""
from testcases.test_insure import InsureDetail

"""
项目启动文件
"""
from pack_lib.HTMLTestRunnerNew import HTMLTestRunner
from common.mylogger import log
from common.constant import CASE_DIR,REPORT_DIR
import os
import time
log.info('---------正在开启测试运行程序----------')
now = time.strftime('%Y-%m-%d_%H_%M_%S')
#创建测试套件
suite = unittest.TestSuite()
#将用例添加到套件中
loader = unittest.TestLoader()
#执行testcases包下所有的用例
suite.addTest(loader.discover(CASE_DIR))
#执行单条测试用例类
# suite.addTest(loader.loadTestsFromTestCase(InsureDetail))

#执行单个方法：
# suite.addTest(loader.loadTestsFromModule(test_insuredetail))

# 拼接报告的路径
report_file_path = os.path.join(REPORT_DIR,'report' + now + '.html')
#执行用例，生成测试报告
with open(report_file_path,'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='接口测试报告',
                            description='商业化接口测试报告',
                            tester='Tian')

    runner.run(suite)
log.info('---------测试运行程序执行完毕----------')
