"""
课堂练习
编写一个函数，根据用户的年龄使用三目运算符判断是否成年。若年龄大于等于18，则返回 "成年人"，否则返回 "未成年人"。
编写一个函数，接受一个数字参数，使用三目运算符判断它是否为正数、负数或零。
"""
import random

# def adult():
#     age = int(input("Enter your age: "))
#     r = "成年人" if age >= 18 else "未成年人"
#     return r
#
# print(adult())
#
#
# def num():
#    number = int(input("Enter a number: "))
#    r = "正数" if number >0 else "负数或零"
#    return r
# print(num())

"""
课堂练习
计算平方数：编写一个匿名函数，计算一个数的平方，并将其应用于一个列表中的每个元素。
筛选偶数：编写一个匿名函数，筛选出一个列表中的所有偶数。
排序：编写一个匿名函数，按照列表中每个元组的第二个元素对一个元组列表进行排序。
"""

# lst = [1,2,3,4,5,6]
# square = lambda n: n * n
# for num in lst:
#     print(f'{num}的平方数为：',square(num))
#
# evn_lst = []
# even = lambda n: n % 2 == 0
# for num in lst:
#     if even(num):
#         evn_lst.append(num)
# print("\n列表中所有偶数为：",evn_lst,"\n")
#
#
# tuple_lst = [(0,7),(4,8),(9,1)]
# sort_tuple = sorted(tuple_lst, key=lambda tup: tup[1])
#
# print('元组中第二个元素排序结果为：',sort_tuple)
"""
课堂练习
编写一个 Python 程序，实现一个计数器函数。
该函数能够记录特定函数的调用次数。
需要使用闭包和装饰器来实现这个功能。
"""
# import time
# def decorate(func):
#     def outer():
#         if not hasattr(outer, 'count'):
#             outer.count = 0
#         outer.count += 1
#         print('当前函数开始调用：')
#         func()
#         print(f'调用了:{outer.count}次')
#
#     return outer
#
# @decorate
# def times():
#     time.sleep(1)
#
# for _ in range(10):
#     times()

"""
课堂练习：数字列表的处理
从给定的学生成绩数据中，使用列表推导式 筛选出所有及格的学生（成绩大于或等于 60）。
使用字典推导式 构建一个新的字典，字典的键是学生的名字，值是他们的成绩。
"""
# # 学生成绩数据
# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 55},
#     {"name": "Charlie", "score": 95},
#     {"name": "David", "score": 45},
#     {"name": "Eve", "score": 72}
# ]
# # pass_stu = []
# # for stu in students:
# #     if stu["score"] >= 60:
# #         pass_stu.append(stu)
# # print(pass_stu)
# pass_stu = [stu for stu in students if stu["score"] >= 60]
# print('及格的学生：',pass_stu)
#
# new_dict = {stu['name']:stu['score'] for stu in students }
# print(f'名字-成绩新字典：{new_dict}')
"""
编写一个 Python 程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来。
"""
# with open('file.txt','a+') as file:
#     file.write('写入一些东西')
# with open('file.txt','r') as file:
#     r_data = file.read()
#     print(r_data)

"""
课堂练习
编写程序，让用户输入两个整数 start 和 end,然后输出这两个整数之间的一个随机数。
要求考虑用户输入不是整数的情况，以及 start>end 的情况。使用异常处理的方式，根据实际情况进行适当提示或输出。
"""
# try:
#     start = int(input('请输入起始值：'))
#     end = int(input('请输入结束值：'))
#     if start >= end:
#         print('起始值不能比结束值大')
#
#     else:
#         choice_num = random.randint(start, end)
#         print(f'随机数为：{choice_num}')
# except ValueError:
#     print('请输入整数！！！')

























