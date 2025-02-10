# # 操作文件
# try:
#     with open('data.txt', 'r') as f:
#         datas = f.read()
# except FileNotFoundError as e:  # e 堆栈消息
#     print(f'文件不存在{e}')
"""
课堂练习
编写程序，让用户输入两个整数 start 和 end,然后输出这两个整数之间的一个随机数。
要求考虑用户输入不是整数的情况，以及 start>end 的情况。使用异常处理的方式，根据实际情况进行适当提示或输出。
"""
import json
import os
import random
from datetime import datetime
import sys
import yaml


def num():
    try:
        start_num = int(input('请输入一个起始值：'))
        end_num = int(input('请输入一个结束值：'))

        if start_num >= end_num:
            raise Exception(f'起始值{start_num}小于或等于结束值{end_num}')

        choice_num = random.randint(start_num, end_num)
        print(f'随机数为：{choice_num}')

    except ValueError:
        print('起始值或结束值不是正整数\n')
"""
课堂练习
sys 模块
获取并打印所有命令行参数。
输出当前 Python 解释器的版本信息。

os 模块
获取并打印当前工作目录。
创建一个新目录，验证是否成功创建。

datetime 模块
获取当前日期和时间并打印。
将当前时间格式化为 YYYY-MM-DD HH:MM:SS 并打印。
"""
def sys_demo():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    print(f'脚本名称：{script_name}')
    print(f'参数名称：{arguments}')
def os_demo():
    # 获取当前目录
    directory = os.getcwd()
    print(f'当前目录为：{directory}')
    # 创建新目录
    # os.mkdir('/Volumes/software/warehouse/python_practice/python_prac0107/day15/new_directory')
    # 验证新目录是否创建成功
    path = '/Volumes/software/warehouse/python_practice/python_prac0107/day15/new_directory'
    if os.path.exists(path):
        print('新目录创建成功')
    else:
        print('新目录没有创建成功')
def datetime_demo():
    # 获取当前日期和时间并打印
    date_now = datetime.now()
    print('当前日期&时间为：',date_now)
    # 格式化当前时间
    date = date_now.strftime('%Y-%m-%d %H:%M:%S')
    print('格式化后的时间为：',date)
"""
{
    "app_name": "TestApp",
    "version": "0.1",
    "libraries": ["numpy", "pandas"]
}

课堂练习
JSON 文件操作
创建一个 test_config.json 文件。
保存配置到文件
从文件中加载配置并打印。

YAML 文件操作
将相同的配置转换为 YAML 格式保存到 test_config.yaml 文件。
从文件中加载 YAML 配置并打印。
"""
datas ={
    "app_name": "TestApp",
    "version": "0.1",
    "libraries": ["numpy", "pandas"]
}
def json_demo():
    # 写入json文件
    with open('test_config.json', 'w', encoding='utf-8') as f:
        json.dump(datas,f)
    # 读取json文件
    with open(r'test_config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('加载test_config.json文件内容：',data)
def yaml_demo():
    # 写入yml文件
    with open(r'test_config.yaml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(datas,f)
    # 读取yml文件
    with open(r'test_config.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print('加载test_config.yml文件内容：',data)
"""
课堂练习：数字列表的处理
从给定的学生成绩数据中，使用列表推导式 筛选出所有及格的学生（成绩大于或等于 60）
。
使用字典推导式 构建一个新的字典，字典的键是学生的名字，值是他们的成绩。

# 学生成绩数据

"""
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 45},
    {"name": "Eve", "score": 72}
]
def pass_stu():
   lst = [stu['name'] for stu in students if stu['score']>=60]
   print('及格的学生为：',lst)

def new_dic():
    dic = {stu['name']:stu['score'] for stu in students}
    print('新的字典为：',dic)

if __name__ == '__main__':
    # sys_demo()
    # os_demo()
    # datetime_demo()
    # json_demo()
    # yaml_demo()
    # pass_stu()
    new_dic()