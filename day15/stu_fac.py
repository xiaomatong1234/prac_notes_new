"""
课堂练习：计算正整数的阶乘
编写一个 Python 程序，使用递归算法，计算给定正整数 n 的阶乘。
阶乘的定义是从 1 到 n 所有正整数的乘积。
例如 3 的阶乘为 1*2*3=6。
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
if __name__ == '__main__':
    f = factorial(3)
    print('阶乘为：',f)

"""
课堂练习：字符串反转
使用递归函数反转一个字符串，例如将 "hello" 变为 "olleh"。
"""
def rollback(s):
    length = len(s)
    if length == 0:
        return " "
    return s[-1] + rollback(s[:-1])
if __name__ == '__main__':
    string = rollback("hello")
    print('反转后的字符串为：',string)
"""
课堂练习：数组求和
使用递归计算一个列表中所有元素的和，例如列表 [1,2,3,4,5] 的和为 15
"""
def num_sum(lst):
    length = len(lst)
    if length == 0:
        return 0
    return lst[0] + num_sum(lst[1:])
if __name__ == '__main__':
    lsts = num_sum([1,2,3,4,5])
    print('列表元素的和为：',lsts)

"""
实战思路
编写一个 Python 程序，使用递归算法，生成并输出斐波那契数列的前 n 项，其中 n 是用户指定的正整数。
斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....从第三个数开始，每个数字都是前两个数字之和。
"""
def fibonacci(n):
    lst = []
    if n <0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    num = fibonacci(3)
    print(f'第{num}斐波那契数为：',num)

"""
返回斐波那契数列
"""
def fibonacci_lst(n):
    if n <0:
        return
    elif n==1:
        return [1]
    elif n==2:
        return [1,1]
    else:
        # 先获取前面的数列
        f_list = fibonacci_lst(n-1)
        # 把当前位置的值添加到数列中
        f_list.append(f_list[-1]+f_list[-2])
        return  f_list
if __name__ == '__main__':
    num = fibonacci_lst(3)
    print('斐波那契数列：',num)