# from time import time
#
# a = time()
#
# # 三目运算符
# r = True if a > 156 else False
# # if a > 156:
# #     r = True
# # else:
# #     r = False
# print(r)
# 定义一个简单的装饰器
# def simple_decorator(func):
#     def wrapper():
#         print("在原函数执行之前做一些事情")
#         func()
#         print("在原函数执行之后做一些事情")
#     return wrapper
#
# # 使用装饰器
# @simple_decorator
# def hello():
#     print("Hello, World!")
#
# # 调用被装饰的函数
# hello()
# 模拟用户数据
users = [
    {'role': 'staff', "username": "ben", "password": 1234},
    {'role': 'manager', "username": "admin", "password": 1234}
]

# 定义 auth 装饰器
def auth(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 从 kwargs 中获取用户名
            username = kwargs.get('username')
            current_user = None
            # 遍历用户列表，查找当前用户
            for user in users:
                if user["username"] == username:
                    current_user = user
                    break
            # 检查用户角色是否匹配
            if current_user and current_user["role"] == role:
                # 如果角色匹配，调用原函数
                return func(*args, **kwargs)
            else:
                # 如果角色不匹配，打印提示信息
                print(f'该用户角色没有权限执行此操作。')
        return wrapper
    return decorator

# 使用 auth 装饰器
@auth('manager')
def get_commodities(db_file, username):
    print(f"查询 {db_file} 中的商品库存，当前用户是 {username}")

# 调用被装饰的函数
get_commodities(db_file='orders.json', username='admin')