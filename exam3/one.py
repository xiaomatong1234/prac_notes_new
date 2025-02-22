"""编写一个 Python 程序，接收一个包含整数的列表，按照从大到小的顺序排序并输出。"""
def lst():
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

arr =[4,1,3,2]
lst()