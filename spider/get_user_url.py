# -*- coding:utf-8 -*-
import MySQLdb

'''
主要的功能：
查询数据表
返回需要爬取的用户的id和用户名
'''
def spider_start():
    # 连接数据库
    conn_check = MySQLdb.connect(host='202.121.197.87', user='root', passwd='!@QWaszx',
                           port=3306, db='weibo', charset='utf8', use_unicode=True)
    cur = conn_check.cursor()
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    # 执行查询语句
    sql="SELECT user_id,user_name FROM source_user WHERE crawl_status = '%s'" %("0")
    cur.execute(sql)
    result = cur.fetchall()
    print result[0][0]
    print result[0][1]

    cur.close()
    conn_check.commit()
    conn_check.close()
    return result[0][0], result[0][1]
# spider_start()

