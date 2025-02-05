"""
课堂练习：简单的成绩判断
用户输入 3 门课程的成绩，存储到一个列表中。
计算总分和平均分。
如果平均分大于等于 60，则输出“及格”，否则输出“不及格”。
"""
import copy

# lst = []
# for i in range(3):
#     user_input = input('请输入课程成绩：')
#     lst.append(float(user_input))
# sum_num = lst[0]+lst[1]+lst[2]
# avg_num = sum_num/3
# print(f'总分为{sum_num},平均分为{avg_num }')
# if avg_num >=60:
#     print('及格')
# else:
#     print('不及格')

"""
课堂练习：使用 while 实现倒计时
用户输入一个正整数作为起始值，程序每秒输出一个数字，直到倒计时结束并输出 "倒计时结束！"。
"""
# import time
# tim= int(input('请输入一个正整数：'))
# while tim >0:
#     print(f'倒计时{tim}s')
#     time.sleep(1)
#     tim -=1
# print('倒计时结束！！')
"""
课堂练习：使用 for 计算列表中元素的平方
给定一个整数列表 [1, 2, 3, 4, 5]，使用 for 循环计算每个数的平方，并将结果存储到新的列表中，最后输出新列表。
"""
# lsts = [1, 2, 3, 4, 5]
# result = []
# for lst in lsts:
#     result.append(lst*lst)
# print('列表中每个数的平方为：',result)

"""
课堂练习：模拟登录系统
设置一个预定义的用户名和密码，用户最多输入 3 次。
如果用户名和密码正确，输出 "登录成功"；如果失败 3 次，输出 "登录失败"。
"""
# username = 'abc'
# password = 'a1234'
# input_usr = input('请输入用户名：')
# input_pwd = input('请输入密码：')
# if input_usr != username or input_pwd != password:
#     for i in range(3):
#         i += 1
#         print(f'第{i}次，输入错误,请重新输入')
#         input_usr = input('请输入用户名：')
#         input_pwd = input('请输入密码：')
#         if i == 2:
#             break
#     print('登陆失败')
# else:
#     print('登陆成功')
"""
课堂练习：多人分组评分系统
假设有 3 名评委需要给 5 名参赛选手打分（分数范围为 1 到 10）。
使用 for 循环依次处理每个评委对选手的评分。
使用 while 循环管理整个评分流程，直到所有选手都打分完成。
最终，计算每位选手的平均分并显示结果。
"""
# player = 0
# score = 0
# sum_score = 0
#
# while player < 5:
#     for player in range(5):
#         for judge in range(1,4):
#             score = random.randint(1,10)
#             print(f'评委{judge}打分：',score)
#             sum_score += score
#         # print(sum_score)
#         player += 1
#         avg_score = sum_score / 3
#         print(f'选手{player}的平均分为：{round(avg_score,2)}','\n')
"""
课堂练习
创建一个字典，包含以下信息：
姓名（name）
年龄（age）
性别（gender）
城市（city）

添加新的键值对：
国家（country）: “中国”
职业（job）: “软件工程师”

删除字典中的“年龄”项。
检查字典中是否存在“性别”这一键，并输出其对应的值。
遍历字典，打印出所有的键和对应的值。
"""
# person = {"name":'Lili',"age":20,"gender":"female","city":"peking"}
#
# person["country"]= 'China'
# person["job"]= '软件测试工程师'
#
# print('已删除年龄：',person.pop("age"))
#
# print('性别：',person.get("gender"))
#
# for key,value in person.items():
#     print(key,value)
"""
课堂练习：图书借阅管理系统
模拟一个图书馆的借阅管理系统
系统包含以下功能：

使用深拷贝和浅拷贝复制图书信息并演示修改的影响；
检查图书是否在借阅列表中，使用成员运算符 in 和 not in；
使用身份运算符 is 和 is not 比较对象是否为同一本书。

实现以下场景：
借阅列表初始化；
添加图书到借阅列表； 字典
检查某本书是否已被借阅；
复制图书信息并对比深浅拷贝的效果。
"""
# # 初始图书列表
# library_books = [
#     {"title": "Python Programming","author": "John Doe","id": 101},
#     {"title": "Data Science Basics","author": "Jane Smith", "id": 102},
#     {"title": "Machine Learning","author": "Alice Brown","id": 103}]
#
# # 浅拷贝图书信息
# copy_library_books = library_books.copy()
# print('浅拷贝图书信息展示：',copy_library_books)
# print('浅拷贝图书信息内存地址展示：',id(copy_library_books))
# # 深拷贝图书信息
# deep_copy_library_books = copy.deepcopy(copy_library_books)
# print('深拷贝图书信息展示：',deep_copy_library_books)
# print('深拷贝图书信息内存地址展示：',id(deep_copy_library_books))
#
# # 添加图书到借阅列表中
# borrow_lst=[]
# borrow_lst.append(library_books[0])
# print(borrow_lst)
#
# # 检查图书是否在借阅列表中
# check_book = {
# "title": "Python Programming","author": "John Doe","id": 101
# }
# print(f'{check_book["title"]}在图书列表中：',check_book in borrow_lst)
# print(f'{check_book["title"]}在图书列表中：',check_book not in borrow_lst)
#
# # 比较是否是同一本书
# print('为同一本书',check_book is library_books[0]["title"])
# print('为同一本书',check_book is not library_books[0]["title"])
# # 浅拷贝中的第一本书和原始数据的第一本书做比较
# print(copy_library_books[0] is library_books[0])
# # 深拷贝中的第一本书和原始数据的第一本书做比较
# print(deep_copy_library_books is library_books[0])
#
#
# # 检查某本书是否被借阅
# for book in borrow_lst:
#     print(f'已被借阅的图书为：{book}')
"""
课堂练习：图书馆管理系统
创建一个图书馆管理系统，请使用函数实现以下功能：
添加图书到馆藏。
借阅图书时，检查是否存在并更新借阅状态。
使用浅拷贝和深拷贝演示借阅对馆藏的影响。
检查某本书是否在借阅列表中，结合成员运算符。
判断是否为同一本书，结合身份运算符。
"""
def library_manage():
    library_books = [
        {"title": "Python Programming","author": "John Doe","id": 101},
        {"title": "Data Science Basics","author": "Jane Smith", "id": 102},
        {"title": "Machine Learning","author": "Alice Brown","id": 103}]

    # 浅拷贝图书信息
    copy_library_books = library_books.copy()
    print('浅拷贝图书信息展示：',copy_library_books)
    print('浅拷贝图书信息内存地址展示：',id(copy_library_books))
    # 深拷贝图书信息
    deep_copy_library_books = copy.deepcopy(copy_library_books)
    print('深拷贝图书信息展示：',deep_copy_library_books)
    print('深拷贝图书信息内存地址展示：',id(deep_copy_library_books))

    # 添加图书到借阅列表中
    borrow_lst=[]
    borrow_lst.append(library_books[0])
    print(borrow_lst)

    # 检查图书是否在借阅列表中
    check_book = {
    "title": "Python Programming","author": "John Doe","id": 101
    }
    print(f'{check_book["title"]}在图书列表中：',check_book in borrow_lst)
    print(f'{check_book["title"]}在图书列表中：',check_book not in borrow_lst)

    # 比较是否是同一本书
    print('为同一本书',check_book is library_books[0]["title"])
    print('为同一本书',check_book is not library_books[0]["title"])
    # 浅拷贝中的第一本书和原始数据的第一本书做比较
    print(copy_library_books[0] is library_books[0])
    # 深拷贝中的第一本书和原始数据的第一本书做比较
    print(deep_copy_library_books is library_books[0])


    # 检查某本书是否被借阅
    for book in borrow_lst:
        print(f'已被借阅的图书为：{book["title"]}')

library_manage()

"""
课堂练习：使用可变参数
编写一个函数，接受任意数量的数字参数，返回这些数字的和。
编写一个函数，接受任意数量的关键字参数，返回所有键值对组成的字典。
编写一个函数，能够同时处理位置参数（args）和关键字参数（*kwargs），打印包含位置参数的元组和包含关键字参数的字典。
"""
def sum_num(*args):
    result = 0
    for n in args:
        result += n
    return result
print(f'数字的和为：',sum_num(1, 2,3,4))

def dic_num(**kwargs):
    return kwargs
print('组成的字典为：',dic_num(name='John', age=18, address='peking'))

def num(*args, **kwargs):
    return args, kwargs
print('打印位置参数的元组和包含关键字参数的字典',num(1, 2, 3, 4, name='John', age=18, address='peking'))