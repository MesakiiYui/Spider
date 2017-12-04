# -*- coding:utf-8 -*-
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def insert_to_mysql(weibo_list,comment_list,forward_list):
    print 'start insert'
    # user_id,primarykey,edit_time,content,weibo_url
    conn = MySQLdb.connect(host='202.121.197.87', user='root', passwd='!@QWaszx',
                           port=3306, db='weibo', charset='utf8', use_unicode=True)
    cur = conn.cursor()
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")

    # weibo_list=[user_id,str_primarykey,user_name,edit_time,content,weibo_url]
    # second_weibo的数据导入

    cur.execute("insert into second_weibo(second_user_id, second_user_name,"
                "weibo_order, edit_time, weibo_content, weibo_webpage) values(%s,%s,%s,%s,%s,%s)",
                [weibo_list[0],weibo_list[1],weibo_list[2],weibo_list[3],weibo_list[4],weibo_list[5]])
    for m in comment_list:

        cur.execute("insert into second_comment(second_user_id, second_user_name,"
                    "weibo_order, third_user_name, third_user_id, edit_time, comment_content, third_user_homepage) "
                    "values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    [ m[0], m[1],m[2],m[3],m[4],m[5],m[6],m[7]])
    for n in forward_list:

        cur.execute("insert into second_forward(second_user_id, second_user_name,"
                    "weibo_order, third_user_name, third_user_id, edit_time, forward_content, third_user_homepage) "
                    "values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    [n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7]])

    cur.close()
    conn.commit()
    conn.close()
