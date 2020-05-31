
#如何进行反向迭代以及如何实现反向迭代

class FloatRange(object):
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        t=self.start
        while t<=self.end:
            yield t
            t+=self.step
    def __reversed__(self):
        t=self.end
        while t>=self.start:
            yield t
            t-=self.step
        
for i in FloatRange(1.0,4.0,0.5):
    print(i)
for i in reversed(FloatRange(1.0,4.0,0.5)):
    print(i)

