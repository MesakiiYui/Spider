# -*- coding:utf-8 -*-
import MySQLdb
import socket
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def finish_crawl(user_id):


    # 当完成一个用户的信息爬取后调用该函数，将爬取状态改为1
    # 每一次循环都要访问source_weibo数据表中的user_id，
    conn_check = MySQLdb.connect(host='202.121.197.87', user='root', passwd='!@QWaszx',
                           port=3306, db='weibo', charset='utf8', use_unicode=True)
    cur = conn_check.cursor()
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    sql = "UPDATE source_user SET crawl_status = '%s' WHERE user_id = '%s'" % ('1', user_id)
    cur.execute(sql)

    cur.close()
    conn_check.commit()
    conn_check.close()
    print "change success,finish"


def just_crawling(user_id):
    localip = socket.gethostbyname(socket.gethostname())#得到本地ip
    # 当完成一个用户的信息爬取后调用该函数，将爬取状态改为1
    # 每一次循环都要访问source_weibo数据表中的user_id，
    conn_check = MySQLdb.connect(host='202.121.197.87', user='root', passwd='!@QWaszx',
                           port=3306, db='weibo', charset='utf8', use_unicode=True)
    cur = conn_check.cursor()
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    sql = "UPDATE source_user SET crawl_status = '%s' WHERE user_id = '%s'" % ('2', user_id)
    cur.execute(sql)
    sql_2 = "UPDATE source_user SET slaver_ip = '%s' WHERE user_id = '%s'" % (str(localip), user_id)
    cur.execute(sql_2)
    cur.close()
    conn_check.commit()
    conn_check.close()
    print "change success，crawling"
