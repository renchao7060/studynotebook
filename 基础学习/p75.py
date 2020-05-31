
import random,string,os


os.chdir('d:/project')
str1=string.ascii_uppercase
f=open('info.txt','w+')

for i in range(1,41):
	User=''.join(random.sample(str1,5))
	Pass=''.join(random.sample(str1,5))
	Wpa2=''.join(random.sample(str1,8))
	f.write('%s\t'%User)
	f.write('%s\t'%Pass)
	f.write('%s\n'%Wpa2)
f.close()
f=open('info.txt','r')
info=f.read()
print(info)



