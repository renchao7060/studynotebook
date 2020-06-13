'''

print('方式一:以列为单位，左对齐'.center(70,'-'))
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={:<4}'.format(j,i,j*i), end='')
    print(end='\n')

print('方式二：以列为单位，右对齐'.center(70,'-'))
for i in range(1,10):
    for k in range(1,10-i):
        print(end='        ')
    for j in range(i,0,-1):
        print('{}*{}={:<4}'.format(j,i,j*i), end='')
    print(end='\n')

print('方式三：以行为单位，左对齐'.center(70,'-'))

for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()


print('方式四：以行为单位，右对齐'.center(70,'-'))

for i in range(1,10):
    for k in range(1,i):
        print(end='        ')
    for j in range(i,10):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()

print('方式五:占位符%使用'.center(70,'-'))

for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print('%s*%s=%-4s'%(j,i,j*i),end='')
    print()

'''

class Multiplication():
    def __init__(self):
        pass

    def column_left(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('{}*{}={:<4}'.format(j,i,j*i), end='')
            print(end='\n')
    
    def column_right(self):
        for i in range(1,10):
            for k in range(1,10-i):
                print(end='        ')
            for j in range(i,0,-1):
                print('{}*{}={:<4}'.format(j,i,j*i), end='')
            print(end='\n')

    def row_left(self):
        for i in range(1,10):
            for j in range(i,10):
                print('{}*{}={}'.format(i,j,i*j),end='\t')
            print()
        
    def row_right(self):
        for i in range(1,10):
            for k in range(1,i):
                print(end='        ')
            for j in range(i,10):
                print('{}*{}={}'.format(i,j,i*j),end='\t')
            print()

if __name__=='__main__':
    multable=Multiplication()
    menu='''
        1:方式一:以列为单位，左对齐
        2:方式二：以列为单位，右对齐
        3:方式三：以行为单位，左对齐
        4:方式四：以行为单位，右对齐
        5:退出程序

        '''
    dict1={
        '1':'column_left',
        '2':'column_right',
        '3':'row_left',
        '4':'row_right',
        '5':'quit'

    }
    
    while True:
        print('Menu'.center(70,'-'))
        print(menu)
        try:
            choice=input('请输入你的选择：')
            choice=dict1[choice]
        except:
            print('输入错误，请输入数字1-5：')
            continue
        if choice=='quit':
            break
        else:
            getattr(multable,choice)()

    

    # print('方式一:以列为单位，左对齐'.center(70,'-'))
    # multable.column_left()

    # print('方式二：以列为单位，右对齐'.center(70,'-'))
    # multable.column_right()

    # print('方式三：以行为单位，左对齐'.center(70,'-'))
    # multable.row_right()

    # print('方式四：以行为单位，右对齐'.center(70,'-'))
    # multable.row_left()
