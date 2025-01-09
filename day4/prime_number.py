'''
实战：素数
编写一个 Python 程序，输入一个正整数，判断这个数是否为素数（质数）。

素数是指只能被 1 和它本身整除的正整数。
'''
import math

# def is_prime(num):
#     # 判断是不是正整数
#     if num <= 1:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def prime_numbers(num):
#     if is_prime(num):
#         print(f'{num}是一个素数')
#     else:
#         print(f'{num}不是一个素数')
#
#
#
# num = int(input('请输入一个正整数：'))
# if __name__ == '__main__':
#     prime_numbers(num)

'''
优化  数的平方根
'''
def is_prime(num):
    # 判断是不是正整数
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) +1): #sqrt 计算一个数的平方根  int 遇到小数向下取整
            if num % i == 0:
                return False
    return True

def prime_numbers(num):
    if is_prime(num):
        print(f'数字 {num} 是一个素数')
    else:
        print(f'数字 {num} 不是一个素数')


num = int(input('请输入一个正整数：'))
if __name__ == '__main__':
    prime_numbers(num)