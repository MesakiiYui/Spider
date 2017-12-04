# -*- coding:utf-8 -*-
from lxml import html
import requests
import json
import re
import scrapy
from bs4 import BeautifulSoup



#通过beautifulsoup解析文档
def bs4analysis(html_doc):
    soup = BeautifulSoup(html_doc,"lxml")
    
    if soup.find_all('a'):
        
        a = soup.a.string
        return a
    elif soup.find_all('span'):
        
        c = 'None'
        
        return c
    else:
        
        return html_doc
        
