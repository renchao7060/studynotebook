#coding=utf-8

import re
import requests
import os
import time
import sys
from bs4 import BeautifulSoup
os.chdir(r'E:\Progect\practice\tmp')



def home_urls():
    urls_home=['http://yeyemo.net/a/list_33_{}.html'.format(n) for n in range(1,8)]
    # print(urls_home)
    for url_home in urls_home:
        # print(url_home)
        geturllist(url_home)

def geturllist(url):
    base_url='http://yeyemo.net'
    req=requests.get(url)
    # print(req.encoding)#ISO-8859-1
    req.encoding='utf-8'
    html_code=req.text
    soup=BeautifulSoup(html_code,'lxml')
    urllists=soup.select('body > div.home > div.listz > div.listw > ul > li > a')
    # print(len(urllists))
    for urllist in urllists:
        link=urllist.get('href')
        full_url = base_url+link
        name=urllist.get('title')
        # print(full_url,name)
        getcontent(full_url, name)
    # print(html_code)
    # reg=re.compile(r'<li><span>.+</span><a href="(.*?)" title=.*>(.*?)</a></li>')
    # reg = re.compile(r'<a href="(.*?)" title=.*>(.*?)</a>')
    # urllists=re.findall(reg,html_code)
    # print(len(urllists))
    # print(len(set(urllists)))
    # for urllist in urllists:
    #     # print(urllist[0],urllist[1])
    #     full_url=base_url+urllist[0]
    #     title=urllist[1]
    #     print(full_url,title)
    #     # getcontent(full_url,title)

# url="http://yeyemo.net/a/wife/201507/53861.html"
def getcontent(url,filename):
    try:
        req=requests.get(url)
        req.encoding='utf-8'
        html_code=req.text
    except:
        print('未获取网页源码')
    # print(html_code)
    reg=re.compile(r"<div>\s*(.*?)</div>\s*<div>\s*&nbsp;</div>")
    contents=re.findall(reg,html_code)
    # print(contents)
    if contents:
        filename='{}.txt'.format(filename)
        for content in contents:
            with open(filename,'a') as f:
                f.write('    '+content+'\n')


# getcontent(url,'bb')
if __name__=='__main__':
    home_urls()