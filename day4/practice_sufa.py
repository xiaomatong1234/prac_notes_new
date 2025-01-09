"""
实战：九九乘法表
实战：for 循环实现斐波那契
实战：素数
实战：水仙花数
"""
import math

"""
实战1：九九乘法表
编写一个 Python 程序，生成并输出下面所示的九九乘法表
# 输出示例

1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9
1 * 4 = 4   2 * 4 = 8   3 * 4 = 12  4 * 4 = 16
1 * 5 = 5   2 * 5 = 10  3 * 5 = 15  4 * 5 = 20  5 * 5 = 25
1 * 6 = 6   2 * 6 = 12  3 * 6 = 18  4 * 6 = 24  5 * 6 = 30  6 * 6 = 36
1 * 7 = 7   2 * 7 = 14  3 * 7 = 21  4 * 7 = 28  5 * 7 = 35  6 * 7 = 42  7 * 7 = 49
1 * 8 = 8   2 * 8 = 16  3 * 8 = 24  4 * 8 = 32  5 * 8 = 40  6 * 8 = 48  7 * 8 = 56  8 * 8 = 64
1 * 9 = 9   2 * 9 = 18  3 * 9 = 27  4 * 9 = 36  5 * 9 = 45  6 * 9 = 54  7 * 9 = 63  8 * 9 = 72  9 * 9 = 81
"""
def multiply():
    # 获取列 第一个数
    for i in range(1,10):
        # 获取列 第二个数
        for j in range(1, 10):
            # 输出九九乘法表
            if j <= i:
                print(f'{j}*{i} ={ i*j:^2}', end=' ')

        print()
    return '--------------------------------九九乘法表打印完成------------------------------------------'


if __name__ == '__main__':
    print(multiply())


"""
实战2：for 循环实现斐波那契
编写一个 Python 程序，使用 for 循环，生成并输出斐波那契数列的前 n 项,其中 n 是用户指定的正整数。
斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....从第三个数开始，每个数字都是前两个数字之和。
"""
def febncci():
    # n <= 0 提示用户输入数字类型错误
    feb_lst = [1, 1]
    if nums <= 0:
        return '数字小于0，请重新输入'
    # n = 1 输出1
    elif nums == 1:
        return [1]
    # n = 2 输出1
    elif nums == 2:
        return [1,1]
    # 输入其它数字
    else:
        for i in range(2, nums):
            # next_num = 前两个数相加
            next_num  = feb_lst[i -1] + feb_lst[i -2]
            feb_lst.append(next_num)
        return f'斐波那契数列为：{feb_lst}'

#  用户输入正整数
nums = int(input('请输入一个正整数：'))
if __name__ == '__main__':
    print(febncci())

"""
实战3：素数
编写一个 Python 程序，输入一个正整数，判断这个数是否为素数（质数）。
素数是指只能被 1 和它本身整除的正整数。

"""
# 定义一个函数，判断用户输入的数是不是素数
def is_prime():
    # 判断输入的数是否小于1，小于1输出Fasle
    if nums <= 1:
        return False
    #判断输入的数是否等于2，等于21输出True
    elif nums == 2:
        return True
    #输出其它数字，判断数字能否被2整除
    else:
        for i in range(2, int(math.sqrt(nums))+1):
            if nums % i == 0:
                return False
    return True

def prime_number():
    if is_prime():
        print(f'当前用户输入的{nums}是素数')
    else:
        print(f'当前用户输入的{nums}不是素数')

#问题：两个函数，第一个函数不传参，没有return 接收返回值，执行完后，显示none?


# 用户输入一个正整数
nums = int(input("请输入一个正整数："))
if __name__ == '__main__':
    print(prime_number())

"""
实战4：水仙花数
编写一个 Python 程序，找出 100-999 范围内的水仙花数。
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153 是一个"水仙花数"，因为 153=1^3＋5^3＋3^3
"""
def dafford():
    lst = []
    for num in range(100,999):
        #取出百位数字
        a = num // 100
        #取出十位数字
        b = num // 10 % 10
        #取出个位数字
        c = num % 10
        if num == a**3 + b**3 + c**3:
            lst.append(num)
    return lst

if __name__ == '__main__':
    print(dafford())
