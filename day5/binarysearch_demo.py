"""
实战：二分查找
编写一个 Python 程序，实现二分查找。
二分查找是一种在有序数组中查找元素的算法。
将数组分成两部分，判断目标元素可能在哪一部分。直到找到目标元素或确定目标元素不存在于数组中。
静态数组 有序
"""
def binary_search(arr,target_num):
    left = 0 # 索引左边第一个值
    right = len(arr)-1  #  索引右边的值
    while left <= right:
        mid = (left+right)//2  # 中间指针
        if arr[mid] == target_num: # 中间值和目标值相比较
            return mid
        elif arr[mid] < target_num:
            # 中间值小了，抛弃左边
            left = mid + 1
        else:
            # 中间值大了，抛弃右边
             right = mid - 1
     # 其它特殊情况
    return -1


arr = [1, 2, 3, 4, 5,6]
if __name__ == '__main__':
    print(arr[binary_search(arr, 5)])


