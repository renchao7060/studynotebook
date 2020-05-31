# 使用生成器函数实现可迭代对象

class PrimeNumber(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
        
    def prime(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        return True
        
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.prime(k):
                yield k
            
p=PrimeNumber(7,9)
for i in p:
    print('%s'%i,end=',')