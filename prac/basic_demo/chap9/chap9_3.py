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
    def describe_user(self):
        """
        打印用户信息摘要
        :return:
        """
        user_info = '用户姓名为：' + self.first_name + self.last_name + f'\t年龄为：{self.age}'
        print(user_info)

    def greet_user(self):
        """
        向用户发出个性化问候语
        :return:
        """
        greet_msg  = '您好，'+ self.first_name + self.last_name + '，欢迎您使用本系统！'
        print(greet_msg)

# 创建User的实例
user1 = User('张','三',18)
user1.describe_user()
user1.greet_user()

