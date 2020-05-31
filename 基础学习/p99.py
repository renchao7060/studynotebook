from collections import namedtuple
from collections import defaultdict
from collections import deque
name_tuple=['renchao',30,'jinan']
name,age,address=range(3)
print(name_tuple[name])
print(name_tuple[age])
print(name_tuple[address])

User=namedtuple('Test',['name','age','address'])
user=User('zhenzhen',31,'jinan')
print(user.name,user.age,user.address)

class User():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
user2=User('yanning',4,'jinan')
print(user2.name,user2.age,user2.address)


list1=['renchao','zhenzhen','yanning','zhenzhen','yanning']
dict1={}
dict2={}
dict3={}
for user in list1:
    if user not in dict1:
        dict1[user]=1
    else:
        dict1[user]+=1
print(dict1)

for user in list1:
    dict2.setdefault(user,0)
    dict2[user]+=1
print(dict2)

default_dict=defaultdict(int)
for user in list1:
    default_dict[user]+=1

print(default_dict)

