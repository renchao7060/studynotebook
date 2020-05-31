# 模拟购物车流程
product_list=[
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Coffee',30),
    ('Alex python',120)
]
shopping_list=[]
salary=input("Input your salary：")

if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice=input("请选择商品编号>>:")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]

                if p_item[1]<=salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shopping list"%p_item[0])
                else:
                    print("你的余额只剩%s,无法购买，请充值"%salary)
            else:
                print("producd code %s is not exits"%user_choice)
        elif user_choice=='q':
            print('shooping list'.center(20,'*'))
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("invalid option")

