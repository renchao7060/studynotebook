#健康食谱输出 列出5种不同的食材，请输出他们可能组成的所有菜式名称

diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
count=0
for x in range(0,5):
    for y in range(0,5):
        if not (x==y):
            print('{}{}'.format(diet[x],diet[y]))
            count+=1


print('共组合食谱数量为{}'.format(count))