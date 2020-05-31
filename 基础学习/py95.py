# selenium模拟登陆知乎
#开源中国博客模拟鼠标侠岚，selenium调用JS实现

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

def login_zhihu(user="15634813399",passwd="987321"):
    driver.get('https://www.zhihu.com/signin')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='username']"))).send_keys(user)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='password']"))).send_keys(passwd)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    # driver.find_element_by_css_selector("input[name='username']").send_keys('15634813399')
    # driver.find_element_by_css_selector("input[type='password']").send_keys('987321')
    # driver.find_element_by_css_selector('button[type="submit"]').click()

if __name__=='__main__':
    login_zhihu()
    模拟鼠标下拉
    import time
    driver.get('http://www.oschina.net/blog')
    time.sleep(5)
    for i in range(5):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
        time.sleep(2)


# import requests
# import time
# import re
# from bs4 import BeautifullSoup

# def login_zhihu():
    # url=''
    # header=''
    # data={}
    # response=requests.post('',headers=header,data=data)
    # html=response.text
    