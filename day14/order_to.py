# """
# 实战：客户订单记录管理
# 在一个简单的订单管理系统中，需要将客户的订单信息保存到文件中，并支持读取文件来查看历史订单记录。
# 管理员可以通过系统添加新的订单信息，同时可以查看所有订单内容。
#
# 输入订单信息（包括客户姓名、订单内容、订单金额）。
#
# 将订单保存到 orders.txt 文件中，每条订单占一行。
#
# 支持读取 orders.txt 文件，输出历史订单记录。
#
# 文件不存在时，系统应自动创建文件。
#
# 每次查看订单时，系统读取最新文件内容。
# """
# import os
# from time import time
#
#
# def closure_create(func):
#     """
#     闭包函数，返回一个函数
#     :param func:
#     :return:
#     """
#     def inner():
#         print(f'start{time}')
#         func()
#         print(f'end {time}')
#     return inner  # 不要加()
#
# @closure_create
# def save_orders():
#     """
#     输入订单，保存在文件
#     打开文件，使用追加模式
#     写入订单信息
#     打印成功提示
#     :return:
#     """
#     # with open('orders.txt','a') as file:
#     #     r_file = file.read()
#     #     file.write(r_file)
#     #     print('',r_file)
#     pass
#
# @closure_create
# def read_orders():
#     """
#     读取文件，判断文件是否存在
#     如果文件存在，则返回内容
#     :return:
#     """
#     # with open('orders.txt', "a") as file:
#     #     r_file = file.read()
#     #     print('输出历史订单记录：',r_file)
#     pass
#
#
# def run():
#     """
#     给用户输出一个菜单
#     :return:
#     """
#     while True:
#         user_input = (int(input("1 save_orders\n""2 read_orders\n")))
#         if user_input == 1:
#             save_orders()
#         elif user_input == 2:
#             read_orders()
#         else:
#             break
#
# if __name__ == '__main__':
#     run()
def save_order(file_path):
    # 获取订单信息
    order_info = {}
    order_info["客户姓名"] = input('输入客户姓名：')
    order_info["订单内容"] = input("输入订单内容：")
    order_info["订单金额"] = int(input("输入订单金额："))

    # 将订单信息转换为字符串
    manu = str(order_info)

    # 以追加模式打开文件并写入数据
    with open(file_path, "a") as f1:
        f1.write(manu + "\n")  # 写入数据并换行

    print("订单信息已保存")


# 读取文件
def read_order(file_path):
    with open(file_path, "r") as f2:
        # 以行为单位读取文件所有的内容
        contents = f2.readlines()
        if not contents:
            print("订单信息为空")
            return
        print('*' * 100)
        for i in range(len(contents)):
            print(f"第{i + 1}位客户的订单信息为{contents[i].strip()}")

def order_manage_system():
    file_path = "D:/bilibili-python/orders.txt"
    while True:
        print("请选择操作\n"
              "添加新订单：请按 1\n"
              "查看历史订单：请按 2\n"
              "退出系统：请按 3")
        num = int(input("输入操作按钮："))
        if num == 1:
            save_order(file_path)
        elif num == 2:
            read_order(file_path)
        elif num == 3:
            print("退出系统")
            break
        else:
            print("无效输入，请重新选择！")

# 主程序入口
if __name__ == "__main__":
    order_manage_system()