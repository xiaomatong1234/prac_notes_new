"""
实战：选择排序
编写一个 Python 程序，实现择速排序。
对于要排序的数组，第 1 轮比较将找出此时数组中最小的数字。
找到后将该数字与第 1 个数字交换，此时称一个数字已被排序。然后开始第2轮比较，重复上述过程。
每一轮的比较将使得当前未排序数字中的最小者被排序，未排序数字总数减 1。第 arr.length−1 轮结束后排序完成。
"""
def select_demo(arr):
    '''
    1、定义一个最小值下角标 min_idx
      i = 0 ，min_idx = 0


    :param arr:
    :return:
    '''
    #外层循环
    for i in range(len(arr)-1): # i 未排序状态的值
        min_idx = i # 定义最小值下角标index
        # print(f'min_dex的值为：{min_idx}')
        #内层循环
        # 获取到最小值的索引
        for j in range(i+1, len(arr)): #数值从左往右开始比较
            # 判断arr[j]与arr[min_idx]:值的大小
            if arr[j] < arr[min_idx]:
                min_idx = j # 将下角标的值存储起来

        # 交换下角标的位置，min_idx变成已排序状态
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

    return arr

arr=[9,6,1,2]
if __name__ == '__main__':
    print(select_demo(arr))




# # 有问题的代码
# def select_sort():
#     data = [98,56,5,89]
#     length = len(data)
#     for i in range(length-1):
#         small = data[i] # 代码问题的原因：每次玄幻small的值都没有变
#         for j in range(i+1,length):
#             if data[j] < small:
#                 idx = j
#                 data[idx],data[i] = data[i],data[idx]
#                 #
#                 # """
#                 # i = 0 data[i]=98
#                 # j = 1 data[j]=56
#                 #
#                 # """
#     return data
# if __name__ == '__main__':
#     print(select_sort())

