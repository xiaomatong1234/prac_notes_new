"""
实战：客户订单记录管理
在一个简单的订单管理系统中，需要将客户的订单信息保存到文件中，并支持读取文件来查看历史订单记录。
管理员可以通过系统添加新的订单信息，同时可以查看所有订单内容。

输入订单信息（包括客户姓名、订单内容、订单金额）。

将订单保存到 orders.txt 文件中，每条订单占一行。

支持读取 orders.txt 文件，输出历史订单记录。

文件不存在时，系统应自动创建文件。
每次查看订单时，系统读取最新文件内容。
"""
import os


def save_order_to_file(filename,guess_name,order_content,order_amount):
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(f'{guess_name},{order_content},{order_amount}\n')
        print('订单信息添加成功！！')
def read_order_from_file(filename):
    """
    打开文件，读取文件
    检查文件是否为空
    输出文件内容
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as f:
        r_data = f.readlines()
        if not r_data:
            print('暂无订单记录!\n')
            return
        print('打印历史订单记录：')
        for i in range(len(r_data)):
            # 把每行订单信息，去除前后空格，用逗号作为分隔符分隔元素，并分别赋值给 3 个变量
            customer_name, order_content, order_amount = r_data[i].strip().split(",")
            print(f'第{i+1}位，{customer_name}｜,{order_content}｜,{order_amount}')



def order_management_system():
    file_name = 'orders.txt'
    print('欢迎进入客户订单记录管理系统！！')
    while True:
        print('1.查看订单信息\n''2.保存订单信息\n''3.退出系统\n')
        choice_num = int(input('请选择相应的操作：'))
        if choice_num == 1:
            read_order_from_file(file_name)
        elif choice_num == 2:
            guess_name = input('请输入客户姓名：')
            order_content = input('请输入订单信息：')
            order_amount = input('请输入订单金额(元)：')
            save_order_to_file(file_name,guess_name, order_content, order_amount)
        elif choice_num == 3:
            print('退出程序')
            break
        else:
            print('输入无效，请重新输入！')




if __name__ == '__main__':
    order_management_system()
