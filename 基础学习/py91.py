#! /usr/bin/env/python
#_*_coding:utf-8_*_

import requests
import re
import json
import os
from itertools import count
import time

os.chdir('D:\KuGou\spider')
# http://music.baidu.com/search?key=刘德华
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
def get_song(sid):
    api = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17202741599001012014_1513517333931&songid=%s&_=1513517334915' % sid
    response = requests.get(api,headers=headers)
    data = response.text
    data = re.findall(r'\((.*)\)', data)[0]
    data = json.loads(data)
    mp3_name = data['songinfo']['title']
    mp3_name=re.sub(r'"|/|\\|:|\*|\?','',mp3_name)
    mp3_url = data['bitrate']['file_link']
    print(mp3_name)
    print(mp3_url)

    # # 发送http 请求
    response = requests.get(mp3_url,headers=headers)
    # print(response.content) # 是二进制 的数据
    # 持久化 写文件
    filename = '%s.mp3' % mp3_name
    with open(filename, 'wb') as f: # write bytes 写二进制
        f.write(response.content)

# http://music.baidu.com/search/song?s=1&key=%E5%88%98%E5%BE%B7%E5%8D%8E&jump=0&start=20&size=20&third_type=0

def get_url_list(quary):
    for d in count(0,20):
        url='http://music.baidu.com/search/song?s=1&key=%s&jump=0&start=%d&size=20&third_type=0'%(quary,d)
        # data={'key':quary}
        print(url)
        response=requests.get(url,headers=headers)
        response.encoding='utf-8'
        data=response.text
        reg=r'sid&quot;:(\d+)'
        IDList=re.findall(reg,data)
        # print(IDList)
        if IDList:
            for sid in IDList:
                get_song(sid)
                time.sleep(0.5)
        else:
            print('数据爬取结束')
            break


if __name__=='__main__':
    get_url_list('刘德华')



# def get_songid(quary,url):
#     data={'key':quary}
#     response=requests.get('http://music.baidu.com/search',params=data)
#     response.encoding='utf-8'
#     data=response.text
#     reg=r'sid&quot;:(\d+)'
#     IDList=re.findall(reg,data)
#     return IDList