"""0、1、1、2、3、5、8、13、21、34"""
def fab(num):
    if num <= 0:
        return "传递的参数必须是大于0的正整数！"

    elif num == 1:
        return 0
    else:
        # 给前两个数赋值为0，1
        a,b = 0,1
        # 初始化列表变量，列表的前两个值分别为0，1
        fab_lst = [0,1]
        # 由于fab_lst已经有了两个数值，所以n个数只需要循环n-2次
        for i in range(num-2):
            # 后一个数等于前两个数的和
            a,b = b, a+b
            # 把前两个数的和加到列表中
            fab_lst.append(b)
        # 返回列表
        return fab_lst


print(fab(7))
