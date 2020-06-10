import os
from excel_magic.dataset import open_file
# print(os.curdir())
now=os.curdir
print(now)

file_name = '招福银行客户信息总表.xlsx'
excel_file=open_file(file_name)


for f in os.listdir():
    if '支行' in f:
        excel_file.merge_file(f)
excel_file.save()



