
import configparser
from common.constant import CONF_DIR
import os

#拼接配置文件路径
# conf_file_path = os.path.join(CONF_DIR,'conf.ini')

os.chdir('/Users/tianjianfeng/PycharmProjects/api-test-tian/conf')
cf = configparser.ConfigParser()

# read 读取文件内容
filename = cf.read('conf.ini')
print(filename)

# 得到所有的section 以列表格式返回
sec = cf.sections()
print(sec)

# options(section) 得到section下的所有option
opt = cf.options('test')
print(opt)

# items 得到section的所有键值对
value = cf.items("test")
print(value)

# get(section,option) 得到section中的option值，返回string/int类型的结果
mysql_host = cf.get("test","test01")
mysql_password = cf.get("test","test02")
print(mysql_host,mysql_password)







