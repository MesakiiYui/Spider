# -*- coding:utf-8 -*-
from lxml import html
import requests
import json
import re
import scrapy

def get_weibo_total_num(id):
    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+str(id)+'&containerid=100505'+str(id)
    response = requests.get(url)
    ob_json = json.loads(response.text)
    weibo_total_num=ob_json['userInfo']['statuses_count']
    return weibo_total_num

