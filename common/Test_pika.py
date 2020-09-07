"""
# ================================================
# @name    : Tian
# @Time    : 2019/12/13 下午6:10
# @Author  : jesse
# @File    : pika.py
# @Email   :tianjianfeng1995@163.com
# ================================================
"""

import pika
import random

credentials = pika.PlainCredentials('admin', 'admin')
# 这里可以连接远程IP，请记得打开远程端口
parameters = pika.ConnectionParameters('rabbitmq01.ali-bj-dev01.shuheo.net', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# channel.queue_declare(queue='hello')
# number = random.randint(1, 1000)
body = 'hello world:田剑锋你个'

channel.basic_publish(exchange='trans.queue.coupon',
                    routing_key="trans.queue.coupon",
                      body=body)
print (" [x] Sent %s" % body)
connection.close()