# -*- coding:utf-8 -*-
import time
import txt_title_analysis
import forward_content_analysis
import get_Comments
import get_Forwards
import get_weibo_total_number
import get_Weibo
import get_user_url
import weibo_into_mysql
import change_crawl_status
#需要实现的功能：抓取userhomepage的微博信息

'''
彻底改写这段代码，把txt的操作全部删除
'''


def printAllTopic(source_user_id,page,user_name):
    global commentpage
    global forwardpage
    global forwardpage
    global primarykey
    user_id = str(source_user_id)
    # 调用geiweibo函数，发送的ID是博主的ID
    # 需要寻找每条微博的ID
    list_cards = get_Weibo.getWeibo(user_id, page)
    # print list_cards
    # 建立主键primarykey
    # 遍历当页所有微博，输出内容，并根据id查
    # 第一个for 循环，用于抓取该页的所有微博标题
    # print 'printAllTopic'
    for card in list_cards:
        if card['card_type'] == 9:
            weibo_list = []
            comment_list = []
            forward_list = []
            time.sleep(3)
            # 过滤出微博，card_type=9的是微博card
            # 说明抓取到了一条微博
            primarykey = primarykey+1
            # m_id是指具体微博的ID，不是user_id
            m_id = card['mblog']['id']
            # 微博的编写时间
            edit_time = card['mblog']['created_at']
            # 微博的手机版网址
            weibo_url = 'https://m.weibo.cn/status/'+m_id
            # print weibo_url
            # 微博内容，待解析
            text = card['mblog']['text']
            # 获取微博的主题，内容
            s_primarykey = str(primarykey)
            print 'primarykey='+s_primarykey
            content = txt_title_analysis.bs4analysis(text)
            if content == None:
                content = "转发微博"
            print content
            # 写入顺序 前微博用户ID-微博序号-编辑时间-内容-微博地址
            # 把之前写入txt文本的数据现在全部写入weibo_list
            str_primarykey = str(primarykey)
            weibo_list=[user_id,user_name,primarykey,edit_time,content,weibo_url]
            #weibo_into_mysql.insert_to_mysql(str(user_id),str(primarykey),str(user_name),edit_time,content,weibo_url)

            # 用户评论
            # 抓取评论人的用户信息，需要抓取所有人
            # 这个while需要抓取每一条微博的评论信息
            c_i = 1
            total_comment = 1
            commentpage=1
            # 抓取评论用户信息【comment_username】【comment_time】【comment_content】【comment_user_homepage】
            #print '抓取评论开始'
            while True:
                time.sleep(2)
                total_comment, list_comments = get_Comments.getComments(m_id,commentpage)
                print 'total_comment='+str(total_comment)
                # print 'commentpage=' + str(commentpage)
                if total_comment == 0:
                        break
                # print total_comment #成功获取一条微博的总评论数
                # print '**************************'+str(commentpage)
                for comment in list_comments:
                    print 'for comment in list_comments'
                    comment_username = comment['user']['screen_name']
                    comment_user_id = comment['user']['id']
                    comment_time = comment['created_at']
                    comment_content = comment['text']
                    comment_user_homepage = 'http://weibo.com/u/'+str(comment_user_id)
                    print comment_username
                    # 用户评论解析
                        
                    comment_analysis = forward_content_analysis.bs4_forward_analysis(comment_content)
                    # print comment_analysis
                    if comment_analysis == '':
                        comment_analysis = 'no content'
                    # 现在开始写入评论用户的信息【primarykey】【comment_username】【comment_time】【comment_content】【comment_user_homepage】
                    # 现在全部写入mysql中
                    # comment_into_mysql.insert_to_mysql(user_id, user_name, primarykey, comment_username,
                    #                                   comment_user_id, comment_time, comment_analysis,
                    #                                    comment_user_homepage)
                    c_list_second = str(c_i)
                    c_list_second = [user_id, user_name, str_primarykey, comment_username, comment_user_id, comment_time, comment_analysis, comment_user_homepage]

                    comment_list.append(c_list_second)
                    c_i = c_i+1
                    time.sleep(1)
                        
                time.sleep(1)
                commentpage = commentpage+1
                if c_i > total_comment-1:
                    break

                print str(c_i) + 'of'+str(total_comment)
            # 用户评论******************************************************************
            # 用户转发******************************************************************

            forwardpage = 1
            f_i = 1
            forward_total_number = 1
            # 出现了一个问题，如何判断转发抓取的停止
            # 重新定义一个新的变量，应用于for循环中，循环一次+1，用来记录当前页面下的评论总数
            # 然后再加到f_i上
            while True:
                time.sleep(4)
                forward_total_number, list_forward = get_Forwards.getForwards(m_id, forwardpage)
                # 开始循环抓取转发信息
                print '转发总量'+str(forward_total_number)

                if forward_total_number == 0:
                    break
                # f_ic 用来记录一个循环内的记录的总数（一页转发内的总转发数）
                f_ic = 1
                for forward in list_forward:
                    # 【primarykey】【forward_username】【forward_time】【forward_comment】【forward_user_homepage】
                    forward_user_id = forward['user']['id']
                    forward_username=forward['user']['screen_name']
                    forward_time=forward['created_at']
                    forward_comment = forward['raw_text']
                    forward_user_homepage = 'http://weibo.com/u/'+str(forward_user_id)
                    print forward_username
                    f_ic = f_ic + 1
                    if forward_username == '':
                        print '没有转发用户了'
                        break
                    # 进行转发文本解析
                    forward_comment_analysis=forward_content_analysis.bs4_forward_analysis(forward_comment)
                    # print forward_comment_analysis
                    if forward_comment_analysis == None:
                        forward_comment_analysis='emoji'

                    # 现在开始写入文件
                    # 全部写入mysql

                    #forward_into_mysql.insert_to_mysql(user_id, user_name, primarykey, forward_username,
                    #                                   forward_user_id, forward_time, forward_comment,
                    #                                   forward_user_homepage)
                    f_list_second = str(f_i)
                    f_list_second = [user_id,user_name,str_primarykey,forward_username,forward_user_id,forward_time,forward_comment_analysis,forward_user_homepage]
                    forward_list.append(f_list_second)
                    time.sleep(1)
                # 一页抓取完毕，需要添加到f_i上
                print '该页有'+str(f_ic) + '个转发用户'
                f_i = f_i + f_ic
                if f_ic == 0:
                    print '该页没有转发用户了'
                    break
                print '当前有'+str(f_i) + '个转发用户'
                time.sleep(1)
                forwardpage = forwardpage+1
                if f_i > forward_total_number-1:
                    break
                print str(f_i) + 'of' + str(forward_total_number)
                # 接下来开始处理数据库的操作
            print weibo_list
            weibo_into_mysql.insert_to_mysql(weibo_list,comment_list,forward_list)
            print "insert success"
            weibo_list = None
            comment_list = None
            forward_list = None


# 实例化爬虫类并调用成员方法进行输出
# 中断的话怎么处理：获取当前的source_user_num,source_user_id
# 修改current_user_num = ？的值，获取当前主用户信息，
# 需要获取微博的总条数
# 当前为comment_user_total中的第几个主用户

def open_text():
    # 调用一次该函数，则爬取一个用户的所有微博

    global commentpage
    global forwardpage
    global forwardpage
    global primarykey

    primarykey = 0
    commentpage = 1
    forwardpage = 1
    # 调用get_user_url.spider_start，获取用户的id
    # 第一次访问数据库
    user_id, user_name = get_user_url.spider_start()
    print 'current_user_num is' + str(user_id)
    # 获取了一个等待爬取的用户id，将它标记为2，并且写入ip地址
    # 第二次访问数据库，并进行数据更改
    change_crawl_status.just_crawling(user_id)
    # 删除get_user_info.py文件，所有的数据都到数据库中去查询

    # 将字符串格式的user_id转化为int型
    source_user_id = int(user_id)

    # 获取主用户拥有的微博总数
    weibo_total_num = get_weibo_total_number.get_weibo_total_num(source_user_id)
    print 'weibo_total_num' + str(weibo_total_num)
    print 'source_user_id' + str(source_user_id)
    # 如果发生中断，可以修改当前微博的页码
    #  page_i用来表示当前主用户的第？页微博
    page_i = 1

    # 当前访问主用户的微博id<主用户的微博总数，则反复执行
    # 下面的这个try块不再进行continue操作，遇到error，直接结束当前用户的爬取
    try:
        while primarykey < weibo_total_num - 1:
            # 每一趟循环都会抓取当前用户的一页内容下的所有微博
            print 'the current page is' + str(page_i)
            printAllTopic(source_user_id, page_i,user_name)

            page_i = page_i+1
            print 'if break see the page='+str(page_i)
            change_crawl_status.finish_crawl(user_id)
            time.sleep(4)
        # 该循环跳出，说明爬取结束，需要改变状态为1
    except Exception as e:
        print e

    finally:

        print 'finally finish'





