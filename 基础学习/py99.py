
from PIL import Image
import time
import random
import os
import json
import re
print(os.chdir('d:'))
def get_screen_size():
    #获取屏幕分辨率
    #1920*1080
    size_str=os.popen('adb shell wm size').read()
    return size_str
    # if not size_str:
        # print('请安装adb及驱动并配置环境变量')
        # exit()
    # m=re.search(r'(\d+)x(\d+)',size_str)
    # if m:
        # return '%sx%s'%(m.group(2),m.group(1))

    
def init():
    '''初始化，获取配置，检查环境'''
    #获取分辨率
    screen_size=get_screen_size()
    #获文件路径
    config_file_path='config/%s/config.json'%screen_size
    if os.path.exists(config_file_path):
        with open('config_file_path','r') as f:
            print('Load config file from %s'%config_file_path)
            return json.loads(f.read())
    else:
        with open('config/default.json','r') as f:
            print('Load default config')
            return json.loads(f.read())
    
    return

def get_screenshot():
    '''获取截图,auto.png'''
    pass
    
def find_piece_board():
    ''' 根据图片和配置文件找到棋盘棋子坐标'''
    pass
    
    
    
def run():
    '''主函数'''
    #获取配置，检查环境
    config=init()
    print(config)
    while True:
        #获取截图
        get_screenshot()
        img=Image.open('auto.png')
        #获取棋子棋盘坐标
        piece_x,piece_y,board_x,board_y=find_piece_board(img,config)
        #计算距离
        distance=((piece_x-board_x)**2+(piece_y-board_y)**2)**0.5
        #跳
        jump(distance,config['press_ratio'])
        #随机
        time.sleep(1+random.random()*2)

if __name__=='__main__':
    run()
    
    
    
    
    
    
    