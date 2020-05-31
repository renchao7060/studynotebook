#_*_coding:UTF-8_*_

from collections import Iterable
from collections import Iterator

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance('',Iterable))
#以上均返回Ture,说明列表，字典，元组，集合，字符均是可迭代对象

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance('',Iterator))
#以上均返回False,说明列表，字典，元组，集合，字符不是迭代器（迭代器可以被next()函数调用不断返回下一个值）

print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter(''),Iterator))
#以上均返回True,说明列表，字典，元组，集合，字符通过调用iter()函数后可转化为迭代器

print(isinstance((x for x in range(10) ),Iterable))
print(isinstance((x for x in range(10) ),Iterator))
#以上返回均为True,说明生成器是可迭代对象，另外生成器可调用next()方法，所以生成器也是迭代器

print('*'*60)

for i in [1,2,3,4]:
  pass
  
Iter=iter([1,2,3,4])

while True:
  try:
    print(next(Iter))
  except StopIteration as e:
    print(e.value)
    break
