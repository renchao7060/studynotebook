# Python join()逗号分割练习题要求，按逗号分隔列表。

list1=[1,2,3,4,5,6]
#print(type(list1))
str1=','.join(str(n) for n in list1)#list1中的每一个元素若为str类型，可直接调用列表list1
#print(type(str1))
print(list1,type(list1))
print(str1,type(str1))


# [1, 2, 3, 4, 5, 6] <class 'list'>
# 1,2,3,4,5,6 <class 'str'>

var_list = ['tom', 'david', 'john']
a = '###'
print(a.join(var_list))
# tom###david###john
