
import configparser
from common.constant import CONF_DIR
import os
#拼接配置文件路径
# conf_file_path = os.path.join(CONF_DIR,'conf.ini')

os.chdir('/Users/tianjianfeng/PycharmProjects/api-test-tian/conf')
cf = configparser.ConfigParser()
# filename = cf.read('conf.ini')
# print(filename)
#写入
# add section 添加section项
# set(section,option,value) 给section项中写入键值对
cf.add_section("mq")
cf.set("mq", "user", "laozhang")
cf.add_section("kafka")
cf.set("kafka", "user", "xiaozhang")

# write to file
with open("test1.ini","w+") as f:
    cf.write(f)

