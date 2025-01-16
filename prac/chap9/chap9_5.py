class User:
    """表示用户的类"""
    def __init__(self,first_name, last_name, age):
        """
        初始化用户
        :param first_name: 用户姓
        :param last_name: 用户名
        :param age: 年龄
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1 # 将login_attempts属性值加1
        print('增加用户登陆次数：', self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0 # 设置login_attempts属性为0
        print('重置用户登陆次数：',self.login_attempts)


# 创建User的实例
user1 = User('张','三',18)
# 增加用户登陆次数
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


# 重置用户登陆次数
user1.reset_login_attempts()



