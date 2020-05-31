
#遍历嵌套列表（递归）
# def traverse_list(args):
    # for i in args:
        # if not isinstance(i,list):
            # print(i)
        # else:
            # traverse_list(i)
# if __name__=='__main__':
    # list1=[1,2,3,[4,5,6],7,8,[9,10,11]]
    # traverse_list(list1)
    
def traverse_list(args):
    for i in args:
        if isinstance(i,list):
            traverse_list(i)
        else:
            print(i)
            
if __name__=='__main__':
    list1=[1,2,3,[4,5,6],7,8,[9,10,11]]
    traverse_list(list1)