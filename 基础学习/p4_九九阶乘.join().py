for i in range(1, 10):
    for j in range(1, i + 1):
        # print(str(j)+'*'+str(i)+'='+str(j*i)+' ',end='')#end=''表示输出不换行'''
        print('%s*%s=%s\t' % (j, i, i * j), end='')
    print('\n', end='')

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,j*i),end='')
    print('\n',end='')

# ['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]
# [['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)] for i in range(1,10)]
# [' '.join(['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]
# '\n'.join([' '.join(['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)])
print('\n'.join([' '.join(['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))




    # print('\n'.join([' '.join(['%s*%s=%s'%(x,y,x*y) for x in range(1,y+1)]) for y in range(1,10)]))
    # print('\n'.join([' '.join(['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))
    # print('\n'.join([' '.join(['%s*%s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))

    # 1*1=1
    # 1*2=2 2*2=4
    # 1*3=3 2*3=6 3*3=9
    # 1*4=4 2*4=8 3*4=12 4*4=16
    # 1*5=5 2*5=10 3*5=15 4*5=20 5*5=25
    # 1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
    # 1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
    # 1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
    # 1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81

# 1*1=1
# 1*2=2	2*2=4
# 1*3=3	2*3=6	3*3=9
# 1*4=4	2*4=8	3*4=12	4*4=16	
# 1*5=5	2*5=10	3*5=15	4*5=20	5*5=25
# 1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36
# 1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49
# 1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64
# 1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81



