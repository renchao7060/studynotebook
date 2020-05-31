
from collections import Iterable,Iterator
import requests
import sys

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getweather(self,city):
        r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)
        # print(r.json())
        data=r.json()['data']['forecast'][1]
        return '%s:%s,%s,%s,%s'%(city,data['date'],data['type'],data['low'],data['high'])
    def __next__(self):
        if self.index==len(self.cities):
            raise StopIteration
            # print('StopIteration')
            # sys.exit()
        city=self.cities[self.index]
        self.index+=1
        return self.getweather(city)
        
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    
    def __iter__(self):
        return WeatherIterator(self.cities)
        
for i in WeatherIterable(['济南','枣庄','东营']):
    print(i)
        
        
        