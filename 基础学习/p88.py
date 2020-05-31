'''
12306余票查询
'''

import requests

station_dict={}
def getStation():
    response=requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9035',verify=False)
    for i in response.text.split('@')[1::]:
        tmp=i.split('|')
        station_dict[tmp[1]]=tmp[2]
    return station_dict

def getTrainInfo():
    '''
    3：车次 4：始发站:5：终点站:6：出发站:7：到达站
	8：开车时间 9：到达时间 10：历时 13：查询时间
    23：软卧 26：无座 28：硬卧 29：硬座
    30：二层座 31：一等座 32：商务座特等座
    '''
    response=requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(train_date,from_station,to_station),verify=False)
    infos=response.json()['data']['result']
    for i in infos:
        tmp_list=i.split('|')
        if tmp_list[30]!='无' and tmp_list[30]!='':
            print('出发站：%s\t到达站：%s\t车次：%s\t出发时间：%s\t到达时间：%s'%(reverse_station_dict[tmp_list[6]],reverse_station_dict[tmp_list[7]],tmp_list[3],tmp_list[8],tmp_list[9]))

if __name__=='__main__':
    getStation()
    # print(station_dict)
    train_date=input('请输入乘车日期(如:2017-12-19)：')
    from_station=station_dict[input('请输入出发地(如:济南)')]
    to_station=station_dict[input('请输入目的地(如:福州)：')]
    reverse_station_dict={k:v for v,k in station_dict.items()}
    getTrainInfo()

		








