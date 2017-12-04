# -*- coding:utf-8 -*-
from lxml import html
import requests
import json

import scrapy


def getComments(id, page):  # id（字符串类型）：某条微博的id，page（整型）：评论翻页参数

    url = 'https://m.weibo.cn/api/comments/show?id=' + id + '&page=' + str(page)
    response = requests.get(url)
    ob_json = json.loads(response.text)
    # print ob_json

    if "total_number" in ob_json:

        total_comment = ob_json['total_number']  # 每一个微博评论总数为total_number
        list_comments = ob_json['data']
    else:
        total_comment = 0
        list_comments = 0

    return total_comment, list_comments