
import random,string,os
import xlwt



os.chdir('/home/renchao/practce')
str1=string.ascii_uppercase
book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('info',cell_overwrite_ok=True)
# sheet.write(0,0,'hello')
# sheet.write(1,0,'你好')
# book.save('d:\project\info.xls')


for i in range(0,10,2):
	User=''.join(random.sample(str1,5))
	Pass=''.join(random.sample(str1,8))
	Wpa2=''.join(random.sample(str1,8))
	sheet.write(i,0,'用户名')#第i行，第0列
	sheet.write(i,1,'密码')
	sheet.write(i,2,'无线密码')
	sheet.write(i+1,0,User)
	sheet.write(i+1,1,Pass)
	sheet.write(i+1,2,Wpa2)
book.save('/home/renchao/practce/newinfo.xls')