"""
==========================================
author:田剑锋
file: config.py
time: 2019/09/2019/9/21/11:20
E-mail:tianjianfeng1995@163.com
==========================================
"""

from configparser import ConfigParser
from common.constant import CONF_DIR
import os

#拼接配置文件路径
conf_file_path = os.path.join(CONF_DIR,'conf.ini')

class MyConfig(ConfigParser):
    """读取配置文件的类"""
    def __init__(self):
        super().__init__()

        # 初始化的时候，打开配置文件
        self.read(conf_file_path)

myconf = MyConfig()


