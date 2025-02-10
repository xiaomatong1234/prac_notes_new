"""
练习10-13：验证用户　
最后一个remember_me.py版本假设用户要么已输入用户名，要么是首次运行该程序。
我们应该修改这个程序，以防当前用户并非上次运行该程序的用户。

为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。
如果不对，就调用get_new_username()让用户输入正确的用户名。
"""
import json

filename = "username.json"
def get_stored_username():
    """如果存储了用户，就获取它"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示输入用户名"""
    username = input('请输入你的姓名：')
    with open(filename, 'w') as f:
        json.dump(username, f)  # type:ignore
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        correct = input(f'请确认用户名{username}是否正确y/n：')
        if correct == 'y':
            print(f'Welcome back, {username}')
        else:
            username = get_new_username()
            print(f'We\'ll remember you when you come back, {username}!')
    else:
        username = get_new_username()
        print(f'We\'ll remember you when you come back, {username}!')

greet_user()



