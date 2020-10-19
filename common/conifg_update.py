
from configparser import ConfigParser
from common.constant import CONF_DIR
import os
from testcases.test_acquirecampaign import AcquireCampaign
#拼接配置文件路径


# conf_file_path = os.path.join(CONF_DIR,'conf.ini')

class MyConfigUpdate(ConfigParser):
    """读取配置文件的类"""
    def userType(self):
        # 把返回的动态参数写到conf.ini字段保存，以便下个接口依赖调用
        # 打开目标配置文件
        self.read("conf.ini")
        # 为添加的节设置键和值
        # userType = AcquireCampaign.test1_iacquirecampaign.userType()
        self["res"]["userType"] = userType
        # 把修改写入配置文件
        self.write(open("conf.ini", "w"))

myconf1 = MyConfigUpdate()



