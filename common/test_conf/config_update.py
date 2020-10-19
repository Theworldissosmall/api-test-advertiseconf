# coding=utf-8
import configparser
import os

os.chdir('/Users/tianjianfeng/PycharmProjects/api-test-tian/conf')
cf = configparser.ConfigParser()

# 修改配置文件的内容

# remove_section(section)  删除某个section的数值
# remove_option(section,option) 删除某个section下的option的数值
# cf.read("test1.ini")
# cf.remove_option("kafka","user")
# cf.remove_section("mq")

#打开目标配置文件
cf.read("conf.ini")
#添加节
# cf.add_section("conf")
#为添加的节设置键和值
cf["res"]["userType"]="group01"
#把修改写入配置文件
cf.write(open("conf.ini","w"))



# write to file
# with open("test1.ini","w+") as f:
#     cf.write(f)