"""
面向对象跑步减肥
小明和小美都爱跑步
小明体重 75 公斤
小美体重 45 公斤
每次跑步会减肥 0.5 公斤
每次吃东西体重增加 1 公斤
请根据打印出跑完步之后的体重
"""
# 定义一个跑步减肥类
class RunWeightLoss:
    # 定义类属性 小明、小美的初始体重
    ming_weight = 75
    mei_weight = 45
    # 定义跑步减肥方法
    def run(self):
        self.ming_weight -= 0.5
        self.mei_weight -= 0.5
        print(f"跑完步后，小明体重：{self.ming_weight}, 小美体重： {self.mei_weight}\n")
    # 定义吃东西方法
    def eat(self):
        self.ming_weight += 1
        self.mei_weight += 1
        print(f"吃完东西后，小明体重：{self.ming_weight}, 小美体重： {self.mei_weight}\n")

# 创建对象
r1 = RunWeightLoss()
# 调用方法
r1.run()
r1.eat()

