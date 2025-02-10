"""
课后作业
编写一个函数，使用冒泡排序算法对一个整数列表进行排序。

支持从小到大
或从大到小排序。
打印出排序过程中每一轮比较后的列表状态，以便理解冒泡排序的过程。

统计排序过程中总的交换次数并打印。

在主程序中，接收用户输入的多个整数，并调用排序函数进行排序。 最后打印排序后的结果。
"""
def lst_sort():
    swap_count = 0
    lst =[]
    for s in strs.split(","):
        # print(f'\n\n-------------当前输入的数--{str}')
        lst.append(int(s))

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            print(f'\n\n-------------第{i}轮--当前比较的数--{lst[j]}---当前列表{lst}')
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # print(f'\n\n-------------第{i}轮--当前比较的数--{lst[j]}---当前列表{lst}')
                swap_count += 1
    print(f'共进行了{swap_count}次交换')
    return lst

if __name__ == '__main__':
    # lst = [3, 2, 8, 7, 1]
    strs = input('以,分隔请输入一个整数列表：')
    print(lst_sort())



