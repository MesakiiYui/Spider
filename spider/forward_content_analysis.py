# -*- coding:utf-8 -*-
from lxml import html
import requests
import json
import re
import scrapy
from bs4 import BeautifulSoup



#通过beautifulsoup解析转发的内容信息，返回一则信息
def bs4_forward_analysis(html_doc):
    soup = BeautifulSoup(html_doc,"lxml")
    if soup.find_all('a'):
        return soup.a.string
    elif soup.find_all('span'):
        return soup.span.previousSibling
    else:
        return html_doc
        
'''   
if __name__ == '__main__':
    f = open('shuweibo.txt', 'r')
    fh = open('analysis.txt', 'a')
    while True:
        line = f.readline()
        if line == '':
            break
        print '*******************'
        bs4analysis(line)
        print '*******************'
        


    f.close()
    fh.close()
'''
