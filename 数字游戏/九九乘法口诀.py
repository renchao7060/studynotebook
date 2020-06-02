
print('方式一'.center(50,'-'))
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,j*i),end='\t')
    print(end='\n')

print('方式二'.center(50,'-'))
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={:<2}'.format(j,i,j*i), end='\t')
    print(end='\n')

print('方式三'.center(50,'-'))

for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()

print('方式四'.center(50,'-'))

for i in range(1,10):
    s=''
    for j in range(i,10):
        s+='{}*{}={}'.format(i,j,i*j)
        # print(type(s))
    print(s)
        # print('{}*{}={}'.format(i,j,i*j),end='\t')
    # print()