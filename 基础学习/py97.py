#! /usr/bin/env/python
#_*_coding:utf-8_*_

import requests
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.listdir())


try:
    import http.cookiejar as cookielib
except:
    import cookielib

session=requests.session()
session.cookies=cookielib.LWPCookieJar(filename='cookie.txt')

try:
    cookielib.LWPCookieJar.load(ignore_discard=True)##待确定点
except:
    print('cookit未能加载')

agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
headers={
    "HOST":"www.taiqischool.com",
    "Referer":"http://www.taiqischool.com/login",
    "User-Agent":agent

}

def is_login():
    response=session.get('http://www.taiqischool.com/message/',headers=headers,allow_redirects=False)
    if response.status_code!=200:
        print('尚未登录')
    else:
        print('已经登录')

def get_xsrf_path():
    response=session.get('http://www.taiqischool.com/',headers=headers)
    response.raise_for_status()
    html=response.text
    # print(html)
    # text_1='<input type="hidden" name="_target_path" value="http://www.taiqischool.com/classroom/36/courses">'
    # text_2= '<input type="hidden" name="_csrf_token" value="qa1rn5xo51rkJ7AghGtH26h7cA_fMi1LI6BC1NV72Gc">'
    # match_path=re.match(r'.*name="_target_path" value="(.*?)"',html)

    match_xsrf=re.findall(r'.*name="_csrf_token" value="(.*?)"',html)
    # print(match_path.group(1))
    print(match_xsrf[0])
    return match_xsrf


def taiqi_login(account,password):
    post_url='http://www.taiqischool.com/login_check'
    post_data={
        '_username':account,
        '_password':password,
        '_remember_me':'on',
        '_target_path':'http://www.taiqischool.com/classroom/36/courses',
        '_csrf_token':get_xsrf_path(),

    }
    response=session.post(post_url,data=post_data,headers=headers)
    session.cookies.save()
    print(response.status_code)


def index_page():
    response=session.get('http://www.taiqischool.com/login',headers=headers)
    with open('index_page.html','wb') as f:
        f.write(response.text.encode('utf-8'))
    print('页面信息已经写入')


if __name__=='__main__':
    taiqi_login('renchao7060','987321Aa')
    is_login()
    index_page()









# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

# data={
#     '_username':'renchao7060',
#     '_password':'987321Aa',
#     '_remember_me':'on',
#     '_target_path':'http://www.taiqischool.com/classroom/36/courses',
#     '_csrf_token':'xV6KdRmIX12igGXPdzmJ6JJTMTTICWlstwH7POVzCpc'
#     }
#
# url='https://www.taiqischool.com/login'
# response=requests.post(url,data=data,headers=headers)
# response.raise_for_status()
# response.encoding=response.apparent_encoding
# html=response.text()
# print(html)

#selenium自动登录泰其教育
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver=webdriver.Chrome()
# wait=WebDriverWait(driver,10)

# def login_taiqi(user="15634813399",passwd="987321Aa"):
    # driver.get('http://www.taiqischool.com/login')
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="_username"]'))).send_keys(user)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="_password"]'))).send_keys(passwd)
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[class="btn btn-primary btn-lg btn-block"]'))).click()


# if __name__=='__main__':
    # login_taiqi()
    
    
    