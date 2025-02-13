"""
课堂练习：天气预测系统测试
设计一个天气预测系统
获取当前天气：输入城市名称，返回该城市的当前天气，包括温度、湿度、风速等。
获取历史天气：输入城市名称和日期，返回历史上的天气数据（温度、湿度、风速）。
异常处理：如果查询的城市名无效（不存在），系统应抛出异常。

测试要求：
Pytest 标记测试用例：使用 @pytest.mark 对不同场景的测试进行标记，区分正常情况和异常情况。
Pytest 设置跳过、预期失败用例：对一些特定的测试用例进行跳过（例如，查询未来天气的用例），使用 @pytest.mark.skip 和 @pytest.mark.xfail 设置跳过或预期失败的用例。
Pytest 异常处理：测试查询不存在城市或日期的情况，验证异常是否按照预期抛出。
Pytest 结合数据驱动-yaml：使用 YAML 文件提供不同的城市和日期数据，进行参数化测试。
"""
from datetime import datetime


import yaml

class Weather:
    def __init__(self,filename= '../data/weather_data.yml'):
        self.filename = filename
        # 显示去调用读取yaml文件的方法，获取类的实例时，自动调用读取文件的方法
        self.datas = self.read_file()
    # 写入天气
    def write_file(self):
        weather_data = {
            "Beijing": {
                "2023-10-01": {
                    # 温度
                    "temp": 20,
                    # 湿度
                    "humidity": 60,
                    # 风速
                    "windspeed": 10
                },
                "2025-02-12": {
                    # 温度
                    "temp": -7,
                    # 湿度
                    "humidity": 60,
                    # 风速
                    "windspeed": 10
                }
            },
            "Shanghai": {
                "2023-10-02": {
                    "temp": 25,
                    "humidity": 40,
                    "windspeed": 5
                }
            }
        }
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump(weather_data, file)
        print('weather数据已写入')
    # 读取天气
    def read_file(self):
        # 读取yaml文件
        with open(self.filename, 'r', encoding='utf-8') as file:
            datas = yaml.safe_load(file)
        return datas

    # 获取当前天气
    def query_now_weather(self, city):
        try:
            if city in self.datas:
                today = datetime.now().strftime('%Y-%m-%d')
                # 获取今天天气
                if today in self.datas[city]:
                    print(f'city：{city}，date：{today}，weather：{self.datas[city][today]}')
                    # print('获取天气：',self.datas[city][today])
                    # print('获取humidity：', self.datas[city][today]["humidity"])
                    return self.datas[city][today]
                else:
                    print(f'{today}天气在weather_data文件中不存在')
            else:
                print('当前城市在weather_data文件中不存在！！！')
        except Exception as e:
            print('获取当前天气出错','【错误信息】：',e)

    # 获取历史天气
    def query_history_weather(self, city,date):
        try:
            if city in self.datas:
                if date in self.datas[city]:
                    print(f'city：{city}，date：{date}，weather：{self.datas[city][date]}')
                    print('历史天气：',self.datas[city][date])
                    return self.datas[city][date]
                else:
                    print(f'city：{city}，{date}天气在weather_data文件中不存在')
            else:
                print(f'当前城市{city}在weather_data文件中不存在！！！')

        except Exception as e:
            print('获取当前天气出错', '【错误信息】：', e)


# filename = '../data/weather_data.yml'
# w = Weather()
# w.write_file()
# print(w.read_file())
# w.query_now_weather('Beijing')
# w.query_history_weather('Beijing','2023-10-01')


