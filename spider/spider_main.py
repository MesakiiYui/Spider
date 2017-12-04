# -*- coding:utf-8 -*-
import time
import comment_user_home
import requests
'''
主函数需要实现的功能：
启动comment_user_home
'''

if __name__ == "__main__":
    # 每一趟循环都会抓取一个二级用户的所有数据
    while True:
        try:
            comment_user_home.open_text()
            continue
        except Exception as e:
            print "an error happend"
            print e
            continue




'''
    except requests.exceptions.SSLError as e:
        print ('requests.exceptions.SSLError', e)
        print 'i am break'
        time.sleep(2000)
        print 'start again'
        comment_user_home.open_text()
        
    except:
        print 'i am break'
        time.sleep(2000)
        print 'start again'
        comment_user_home.open_text()

    except ConnectionError as e:
        print ('ConnectionError:',e)
        print 'i am break'
        time.sleep(2000)
        get_user_url.spider_start()'''
