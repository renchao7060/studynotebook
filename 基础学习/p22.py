#coding:utf-8

import shutil
import os
import sys
import time


os.chdir(r'e:\progect\practice')

try:
	os.makedirs(r'.\a\b\c\d')
except FileExistsError as value:
	print(value)
	

with open(r'.\a\1.txt','w') as f:
	f.write('hello world')

	
shutil.copyfile(r'.\a\1.txt',r'.\a\2.txt')#文件复制
shutil.copytree(r'a',r'aa')#复制目录
time.sleep(5)
shutil.rmtree(r'aa')#删除目录
# shutil.rmtree(r'a')#删除目录

shutil.make_archive('ab','zip',r'.\a')#文件压缩
