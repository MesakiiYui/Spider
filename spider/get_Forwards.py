# -*- coding:utf-8 -*-
from lxml import html
import requests
import json

import scrapy


def getForwards(id, page):
    urlf = 'https://m.weibo.cn/api/statuses/repostTimeline?id=' + id + '&page=' + str(page)
    response = requests.get(urlf)
    ob_jsonf = json.loads(response.text)
    if "total_number" in ob_jsonf:
        forward_total_number = ob_jsonf['total_number']
        list_forward = ob_jsonf['data']
    else:
        forward_total_number = 0
        list_forward = 0

    return forward_total_number, list_forward