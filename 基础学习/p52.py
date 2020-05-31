'''利用反射功能进行菜单栏呈现'''

class Sdn(object):
    def get_devices(self):
        print('get_devices')

    def get_all_flows(self):
        print('get_all_flows')
        
    def get_all_ports(self):
        print('get_all_ports')
        
    def add_flow(self):
        print('add_flow')
        
    def remove_flow(self):
        print('remove_flow')

s=Sdn()

dict1={
    '1':'get_devices',
    '2':'get_all_flows',
    '3':'get_all_ports',
    '4':'add_flow',
    '5':'remove_flow',
    '6':'quit'
    }

print('Menu'.center(30,"-"))   
menu='''
    1:get_devices
    2:get_all_flows
    3:get_all_ports
    4:add_flow
    5:remove_flow
    6:quit
    '''
print(menu)
print('End'.center(30,"-")) 


while True:
    try:
        choice=input('Please input your choice:')
        choice=dict1[choice]
    except:
        print('input error!\n')
        print(menu)
        continue
    if choice=='quit':
        break
    while True:
        if hasattr(s,choice):
            func=getattr(s,choice)
            func()
            print(menu)
            break
            
            
            
          
            