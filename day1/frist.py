# print("测试开发进阶，首选霍格沃茨")

# 接收键盘输入，并输出到控制台
# name = input("请输入您的姓名：")
# print("您好，" + name + "!")

# 输出不同类型的字符
# print("hogwarts", 99, False, sep='--')
#
# #指定不同的结束符
# print("Hello", end="")
# print("World", end="")
#
# name = input("请输入用户名：")
# print("欢迎用户:", name )

# 获取变量地址
# print(id("hogwarts"))
#
# school = 'hogwarts'
# print(id(school))

#
# b1 = True
# print(type(b1))
#
# s2 = "hogwarts"
# print(type(s2))
#
# s2 = """
# python
# java
# php
# """
# print(type(s2))
#整数与浮点数运算
# # 布尔值与整数运算
# result = False + 1
# print(result)
# print(type(result))

# 布尔值与整数运算

# # 将字符串转换为整数
# x = int("hogwarts")
# print(x)
# print(type(x))
# a = 11
# b = 30
# c = b // a
# print("b % a 的值为：", c)
# 整除运算符 //
a,b,c = 1,2,3
# c1 = b / a
# c2 = b ** a
# c3 = b // a
# c4 =b * a
# print(c1,c2,c3,c4,sep='-----')
#
# a += b
# b -= c
#
# print(a,b,sep= '\n', end='\n————————😈😈😈😈😈赋值运算结束😈😈😈😈😈————————\n' )
#
# e,f,g,h = 4,5,6,7
# print(e == f, f != g, g >= h, e <= f, sep= '\n', end='\n————————🥹🥹🥹🥹🥹关系运算结束🥹🥹🥹🥹🥹————————\n')

'''
课堂练习：
从键盘中输入一个3位数字字符串，将其转换为数字，并逆序，不允许使用切片，不需要做判断
'''
name = input('请从键盘中输入一个3位数字字符串：')
A = int(name)

#  百位 取余
B = A % 10
# 十位 取商 取余
C = A // 10 % 10
# 个位 取商
D = A // 100
print(B,C,D, sep="")





