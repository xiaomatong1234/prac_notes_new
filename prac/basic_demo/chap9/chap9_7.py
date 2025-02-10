from prac.basic_demo.chap9.chap9_5 import User


class Admin(User):
    """编写一个adimin类"""
    def __init__(self, first_name, last_name, age): # 调用父类的构造方法
        """重写父类初始化方法"""
        super().__init__(first_name, last_name, age)
        self.privileges = [] # 创建一个privileges列表

    def show_privileges(self):
        """显示权限"""
        for privilege in self.privileges:
            msg =f'显示管理员权限：{privilege}'
            print(msg)

# 创建一个管理员富相
admin = Admin('fuxiang', 'li', 18)
admin.privileges=["can add post", "can delete post", "can ban user"]
# 调用 show_privileges方法
admin.show_privileges()