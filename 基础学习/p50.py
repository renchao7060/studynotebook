
# 遍历目录文件夹下的所有文件，并进行文件统计
import os
count=0
def print_directory_contents(sPath):
    global count
    for sChild in os.listdir(sPath):
        sChildPath=os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            count+=1

            
print_directory_contents(os.getcwd())
# print_directory_contents(os.chdir('e:'))
print(count)
        