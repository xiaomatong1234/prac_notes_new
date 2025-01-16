class RunWeightLoss:
    """跑步减肥类"""
    def __init__(self, name, weight):
        """初始化每个人的姓名和体重"""
        self.name = name
        self.weight = weight

    def run(self):
        """跑步减肥，每次跑步减0.5公斤"""
        self.weight -= 0.5
        print(f"{self.name} 跑步后体重：{self.weight} 公斤")

    def eat(self):
        """吃东西增加体重，每次增加1公斤"""
        self.weight += 1
        print(f"{self.name} 吃东西后体重：{self.weight} 公斤")

# 创建小明和小美的对象
ming = RunWeightLoss("小明", 75)
mei = RunWeightLoss("小美", 45)

# 模拟小明和小美跑步和吃东西
ming.run()
mei.run()

ming.eat()
mei.eat()