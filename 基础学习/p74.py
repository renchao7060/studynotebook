import random
import time
from collections import OrderedDict

d=OrderedDict()

players=list('ABCDEFGH')
print(players)

for i in range(8):
    start=time.time()
    input('Please answer the question')
    n=players.pop(random.randint(0,7-i))
    end=time.time()
    use_time=end-start
    print(i+1,n,use_time)
    d[n]=(i+1,use_time)

for i in d:
    print(i,d[i])
	

