"""
实战：冒泡排序
编写一个 Python 程序，实现冒泡排序。
对于要排序的数组，从第一位开始从前往后比较相邻两个数字，若前者大，则交换两数字位置，然后比较位向右移动一位
"""
def bubble_sort(arr):
    # 循环次数
    for i in range(len(arr) - 1): # i = 0, range()

        # 数字之间比较大小
        # 取出数组中第一个最大的数字
        for j in range(len(arr)-1):
            # 第一个数字和第二个数字比较大小
            # 第一个数字大于第二个数字，则交换位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
# 优化第一版后
def bubble_sort2(arr):
    # 控制循环次数
    for i in range(len(arr) - 1): # i 从0开始
        swap = False # 初始化swap= False

        # 数字之间比较大小
        # 取出数组中第一个最大的数字
        for j in range(len(arr)-1 -i):  #  j 从0开始 -i 减去轮数
            # 第一个数字和第二个数字比较大小
            # 第一个数字大于第二个数字，则交换位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # 判断数字是否做交换
                swap = True
        if not swap: # 如果swap = not False 为真，执行Break 结束for i循环  swap = not False为假 不执行break
            break

    return arr
# 优化第二版后
def bubble_sort3(arr, key= None, reverse = False):  # key= None key的默认值为None
    # 控制循环次数
    for i in range(len(arr) - 1): # i 从0开始
        print(f'第{i+1}轮数组：{arr}')
        swap = False # 初始化swap= False

        # 数字之间比较大小
        # 取出数组中第一个最大的数字
        for j in range(len(arr)-1 -i):  #  j 从0开始 -i 减去轮数
            if key:
                if key[arr[j]] > key[arr[j+1]]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] # 判断数字是否做交换
                    print(f'交换后的数组为{j}:{arr}')
                    swap = True
            else:
                # 第一个数字和第二个数字比较大小
                # 第一个数字大于第二个数字，则交换位置
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] # 判断数字是否做交换
                    print(f'交换后的数组为{j}:{arr}')
                    swap = True
        if not swap: # 如果swap = not False 为真，执行Break 结束for i循环 ; swap = not False为假 不执行break
            print(f'No swaps in pass {i+1}, exiting early')
            break

    #
    if reverse:
        return arr[::-1] # 为真，倒序 打印
    else:
        return arr #否则 正序 打印
# return arr if reverse else arr[::-1]

# 输入一个要排序的数组
arr = [9, 5, 8,7,9,0]
if __name__ == '__main__':
    print(bubble_sort2(arr))
    print(bubble_sort3(arr, reverse=True))

# print(list(range(3)))