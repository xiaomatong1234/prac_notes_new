"""
使用 Python 的装饰器机制为函数添加权限校验。

用户输入用户名和权限等级。
- 针对不同权限级别，允许或禁止执行对应功能：
- 普通员工（权限等级为 user）：仅允许查看数据。
- 管理员（权限等级为 admin）：允许查看和修改数据。

提供两个功能函数：
- 查看数据：view_data()
- 修改数据：modify_data()

- 如果权限不足，输出提示信息并禁止操作。
- 使用推导式来筛选所有管理员。
"""
# 模拟员工数据
employees = [
    {"username": "Alice", "role": "user"},
    {"username": "Bob", "role": "admin"},
    {"username": "Charlie", "role": "user"},
    {"username": "David", "role": "admin"},
]


value = ['user','admin']
function_permission = {"view_data":value,"modify_data":value[1]}

def permission_required(func):
    def wrapper(username,*args, **kwargs):
        employee = None
        for emp in employees:
            if emp['username'] == username:
                employee = emp
                break
        if employee is None:
            print(f'{username}员工在管理系统中不存在')
            return

        # 获取功能所需的权限列表
        # func.__name__ 获取被装饰函数的函数名
        require_role = function_permission.get(func.__name__)
        if employee['role'] not in require_role:
            print(f'权限不足，{username} 无法执行此操作')
            return
        return func(username,*args,**kwargs)
    return wrapper


@permission_required
def view_data(username):
    print(f'{username}正在查看数据')

@permission_required
def modify_data(username):
    print(f'{username}正在修改数据')


def main():
    print('欢迎来到员工管理系统\n')
    username = input('请输入用户名：').capitalize()

    while True:
        print('请选择要执行的功能：')
        choice_num = int(input(
                '1.查看数据功能\n'
                '2.修改数据功能\n'
                '3.退出\n'))
        if choice_num == 1:
            view_data(username)
        elif choice_num == 2:
            modify_data(username)
        else:
            print(f"{username}已退出员工管理系统")
            break

        admin_lst = [employee['username'] for employee in employees  if employee["role"] == "admin"]
        print(f"管理员列表:{admin_lst}\n")


if __name__ == '__main__':
    main()

