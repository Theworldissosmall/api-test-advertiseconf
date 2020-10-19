

import pymysql
from common.conifg import myconf
class ReadSQL(object):
    def __init__(self):

        # 连接到数据库--loan常用库
        # self.conn = pymysql.connect(
        #                             host=myconf.get('mysql','host'),
        #                             user=myconf.get('mysql','user'),
        #                             password=myconf.get('mysql','password'),
        #                             database=myconf.get('mysql','database'),
        #                             charset=myconf.get('mysql','charset')
        #                             )
        # 连接到数据库--common公共库
        self.conn = pymysql.connect(
                                    host=myconf.get('mysql-common', 'host'),
                                    user=myconf.get('mysql-common', 'user'),
                                    password=myconf.get('mysql-common', 'password'),
                                    database=myconf.get('mysql-common', 'database'),
                                    charset=myconf.get('mysql-common', 'charset')
        )

# 创建游标
        self.cur = self.conn.cursor()


    def close(self):
        # 关闭游标
        self.cur.close()
        # 断开连接
        self.coon.close()


    def find_one(self, sql):
        """获取单条数据"""
        # self.coon.commit() #插入、更新、删除需要commit提交事务才会生效
        res =self.cur.execute(sql)
        # res = self.cur.execute('select * from vipship.vip_account_info')
        print(res)
        return self.cur.fetchone()

    def find_all(self, sql):
        """返回sql查询的所有结果"""
        # self.coon.commit() #插入、更新、删除需要commit提交事务才会生效
        self.cur.execute(sql)
        return self.cur.fetchall()


    def find_count(self, sql):
        """查询数据的条数"""
        # self.coon.commit() #插入、更新、删除需要commit提交事务才会生效
        count = self.cur.execute(sql)
        return count


# 执行 增加、删除、修改的sql语句时，执行完了要提交事务才会生效
# 注意：查询操作commit操作会报属性错误；
# conn.commit()


