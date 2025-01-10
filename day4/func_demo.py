# my_tuple = (1, 2, 3, 4, 5)
# print(list(my_tuple))
# 1、定义最简单的函数
# def func1():
#     """
#     定义一个函数
#     :return:返回值
#     """
#     return "func1"
#
# print(func1())

# 2、定义有返回值的函数
# def func2():
#     """
#     输出没有返回值的函数
#     :return:
#     """
#     print("hogwarts")
# def func3():
#     """
#     输出有返回值的函数
#     :return:
#     """
#     return "hogwarts"
#
# print('返回有返回值的函数：',func3())
# def get_number():
#     """
#     输入一个数字
#     :return: 返回数字的值
#     """
#     num = int(input('请输入一个数字：'))
#     return num
#
# # 打印hello返回次数
# print("hello" * get_number())

# 3、调用可以接收参数的函数
# def add(a,b):
#     """
#     计算a+b
#     :param a:
#     :param b:
#     :return: 返回a+b的值
#     """
#     return a+b
#
#
# print('a + b=',add(1,2))
# def show():
#     """
#     返回0-10中的值
#     返回除2之外0-10中的值
#     :return:
#     """
#     print("循环前的内容")
#     for i  in range(10):
#         print(i)
#         if i == 3:
#             return
#     print("循环后的内容")
#
#
# print("函数调用前的内容：")
# print("函数调用后的内容：",show())
# # def show():
#     print("循环前输出内容")
#     for i in range(10):
#         print(i)
#         if i == 3:
#             return
#     print("循环后输出内容")
#
# print("函数调用前输出内容")
# show()
# print("函数调用后输出内容")
# # 从键盘获取一个字符串，并返回给了调用者。调用者得到结果后进行了大写处理
# def get_str():
#     """
#     从键盘获取一个字符串，并返回给了调用者。调用者得到结果后进行了大写处理
#     :return:
#     """
#     result = input('获取一个字符串：')
#     return result
#
#
# print(get_str().upper())

# 4、函数返回多个值

# 5、组包、解包操作

# 6、不同条件下多个返回值
# def multiReturn():
#     return 1
#     return 2
#     return 3
#     return 4
#     return 5
#
# print(multiReturn())
# print(multiReturn())
# print(multiReturn())
# print(multiReturn())
# print(multiReturn())

# 7、位置参数与关键字参数
# def printMsg(n, msg):
#     for i in range(n):
#         print(f'第{i+1}次输出{msg}')
#
# # 关键字参数
# printMsg(n=5, msg="Hogworts")
# printMsg(msg="Hogworts", n=5)

# 8、默认值函数

# 9、可变参数 *args


# 10、不确定的关键字参数 **kwargs

# 11、多种参数的顺序
# def info(name1, name2, *args, age1=18, age2=21, **kwargs):
#     print("Positional Arguments:")
#     print("name1:", name1)
#     print("name2:", name2)
#     print("args:", args)
#     print("Keyword Arguments:")
#     print("age1:", age1)
#     print("age2:", age2)
#     print("kwargs:", kwargs)
#
# info("Alice", "Bob", "Charlie", "Dave", age2=30, occupation="Engineer", city="New York")
# info("Alice", "Bob", "Charlie", "Dave", age1=25, age2=30, occupation="Engineer", city="New York")
'''
对数字列表中数字的求和，求平均值，求最大值，求最小值。

nums = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]

'''
# def num(nums):
#
#     return sum(nums), max(nums), min(nums), sum(nums)/len(nums)
#
#
#
# nums =  [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]
# if __name__ == '__main__':
#     print(list(num(nums)))


# nums = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]
# # lens=len(nums)
# # print(lens)
# def num_list_count(num_list):
#     # 定义要返回结果的初始值
#     n_sum = 0
#     n_avg = None
#     n_max = None
#     n_min = None
#
#     # 求和
#     for n in num_list:
#         n_sum += n
#
#         # 最大值
#         if n_max == None or n_max < n:
#             n_max = n
#
#         # 最小值
#         if n_min == None or n_min > n:
#             n_min = n
#
#     #  平均值
#         n_avg = n_sum / len(num_list)
#
#     return n_sum,n_max,n_min,n_avg
#
#
# n_sum,n_max,n_min,n_avg = num_list_count(nums)
# # print(num_list_count(nums))
# print(n_sum,n_max,n_min,n_avg)
#
#
