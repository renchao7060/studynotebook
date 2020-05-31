#! /usr/bin/env/python
#_*_coding:utf-8_*_

# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
# #定位元素
# driver.find_element_by_id('kw').send_keys('python')
# time.sleep(2)
# driver.find_element_by_id('su').click()
# driver.find
# time.sleep(10)
# driver.quit()

#页面等待
#1、time.sleep() 不推荐 其实也不能确定页面加载的时间
#2、显示等待 指满足一个条件后再执行后面的代码，可以设置最长等待时间

######################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #负责循环等待
# from selenium.webdriver.support.ui import WebDriverWait
# #负责条件
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
# driver.get('http://www.xxxxx.com/loading')
# try:
#     element=WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located(By.ID,'mydynmicElement')
#     )
# finally:
#     driver.quit()

#########################################################################

#css定位
#id 属性 class 标签定位 可以组合在一起
# #表示ID属性 .表示class 标签直接使用

# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
# #定位元素
# driver.find_element_by_css_selector('#kw')
# driver.find_element_by_css_selector('.s_ipt')
# driver.find_element_by_css_selector('input')
# driver.find_element_by_css_selector('[name="kw"]')
# driver.find_element_by_css_selector('input[ad="css"]')
# driver.find_element_by_css_selector('input > span >a')

###############################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#负责循环等待
from selenium.webdriver.support import expected_conditions as EC# 负责条件
from selenium.common.exceptions import TimeoutException#超时的异常
from bs4 import BeautifulSoup
import sys

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

def search(shop=None):
    print('开始搜索了')
    driver.get('https://www.taobao.com')
    try:
        input=wait.until(
            EC.presence_of_element_located(
                    (By.CSS_SELECTOR,'#q')
            )
        )
        input.send_keys('{}'.format(shop))
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        submit.click()
        get_response()
    except:
        return search(shop)

def get_response():
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item'))
    )
    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    items=soup.find('div',class_='m-itemlist').find_all('div',class_='item')
    for item in items:
        product={
            'images':item.find('a').find('img')['src'],
            'price':item.find('div',class_='price g_price g_price-highlight').text,
            'num':item.find('div',class_='deal-cnt').text[:-3],
            'title':item.find('div',class_='row row-2 title').text,
            'location':item.find('div',class_='location').text,
        }
        print(product)


def next_page(page,num_retries=2):
    print('当前是第{}页'.format(page))
    try:
        input=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))[0]
        # print(input)
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page)
        submit.click()
        judge=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page)))
        print(judge)
        if judge:
            get_response()
        else:
            sys.exit(0)
    except:
        if num_retries>0:
            return next_page(page,num_retries-1)
        else:
            sys.exit(0)


if __name__=='__main__':
    shop=input('请输入要搜索商品的名字:')
    search(shop)
    for page in range(99,120):
        next_page(page)

