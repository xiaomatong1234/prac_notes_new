from prac.chap9.chap9_5 import User
class Privileges:
    """创建一个privileges类"""
    def __init__(self):

        self.privileges = []

    def show_privileges(self):
        """显示权限"""
        if self.privileges:
            for privilege in self.privileges:
                msg =f'{privilege}'
                print('展示管理员的私有权限为：',msg)
        else:
            print('管理员没有私有权限！！')

class Admin(User):
    """编写一个adimin类"""
    def __init__(self, first_name, last_name, age): # 调用父类的构造方法
        """重写父类初始化方法"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges() # 将Privileges类作为属性

if __name__ == '__main__':
    # 创建一个管理员实例
    admin = Admin('fang', 'li', 18)

    # 调用 show_privileges方法
    admin.privileges.show_privileges()

    p_privileges = ['can add post', 'can delete post', 'can ban user']
    admin.privileges.privileges = p_privileges # 给管理员添加权限
    admin.privileges.show_privileges() # 展示新添加的管理员权限