import requests
from bs4 import BeautifulSoup
import traceback
import os
import hashlib
import time
def list_page():
    headers1 = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}  # 伪装的请求头
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}  # 伪装的请求头
    url = 'https://www.gamersky.com/ent/wp/'
    res = requests.get(url)#发送请求
    res.encoding='utf-8'#修改编码
    print(res.text)
    # soup = BeautifulSoup(res.text,'lxml')
    # for i in soup.find('ul',class_='pictxt contentpaging').find_all('li'):
        # try:
            # if not 'https' in i.find('div',class_='tit').find('a').get('href'):
               # list_url= 'https://www.gamersky.com'+i.find('div',class_='tit').find('a').get('href')
               # picture_page(list_url)#爬取图册
            # else:
                # list_url = i.find('div',class_='tit').find('a').get('href')
                # picture_page(list_url)#爬取图册
        # except Exception:#增加异常处理
            # traceback.print_exc()

def picture_page(url):
    pass

    
if __name__ == '__main__':
   list_page()