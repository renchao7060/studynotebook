#!/usr/lib/env/python
#_*_coding:utf-8_*_

import urllib2
import ssl
from json import loads

ssl._create_default_https_context=ssl._create_unverified_context
def gettraininfo():
    '''分析12306返回内容'''
    response=urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-22&leftTicketDTO.from_station=JNK&leftTicketDTO.to_station=FZS&purpose_codes=ADULT').read()
    tmp=loads(response)['data']['result']
    for i in tmp:
        for h,j in enumerate(i.split('|')):
            print('[%s]:%s'%(h,j))
			
gettraininfo()
print(gettraininfo.__doc__)


