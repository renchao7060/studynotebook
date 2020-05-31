import os

changefloder=os.chdir('D:\Personal\研宁')
# changefloder=input('请输入文件夹名称')
i=1
for file in os.listdir(changefloder):
	os.rename(file,'[生活]-[研宁]-%s.jpg'%i)
	i+=1