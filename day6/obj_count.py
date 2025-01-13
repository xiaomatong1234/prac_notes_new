# 定义一个python类
class Counter:
    # 类属性
    # 记录类被实例化的次数
    count_num = 0

    # 构造方法
    def __init__(self):
        Counter.count_num += 1 # 调用类属性 类名

    # 类方法
    @classmethod
    def get_count_num(cls):
        # 访问类属性 类方法中获取类属性的值
        return cls.count_num

    @classmethod
    def reset_count_num(cls):
        cls.count_num = 0


# 使用类方法 对类属性访问
print(f'类属性的初始值为：{Counter.count_num}')

c1 = Counter()
c2 = Counter()
print(f'实例化两次后，类属性的值为：{Counter.count_num}')

# 计数重置
Counter.reset_count_num()
# 重置之后计数的值为
print(f'计数重置后，类属性的值为：{Counter.count_num}')

