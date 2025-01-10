"""
实战：字符串逆序
编写一个 Python 程序，对字符串进行逆序操作。
"""
# def str_demo():
#         return str[: : -1]
#
# # 输入一个字符串
# # 切片对字符串进行逆序操作
# str = input('请输入一个字符串：')
# if __name__ == '__main__':
#     print(str_demo())
#
#
# def str_demo2():
#     new_str = ''
#     for s in str:
#         new_str = s + new_str
#     return new_str
#
# # 输入一个字符串
# # 字符串拼接
# # 对字符串进行逆序操作
# str = input('请输入一个字符串：')
# if __name__ == '__main__':
#     print(str_demo2())

#
def str_demo3(str:list):
    print(str)
    str.reverse()
    str= "".join(str)
    return str




if __name__ == '__main__':
    str = list(input('请输入一个字符串：'))
    print(str_demo3(str))