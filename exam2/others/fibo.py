
"""
14、编写一个函数，实现斐波那契数列每个数字加 1 的功能。
"""
def fibo(n):
    if n <=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) + 1


for i in range(5):
    print(fibo(i),end=' ')