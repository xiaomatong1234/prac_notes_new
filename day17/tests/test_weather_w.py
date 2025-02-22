# from time import sleep
#
# import allure
# import yaml
# import pytest
#
#
# weather_data = {
#     "Beijing": {
#         "2023-10-01": {
#             # 温度
#             "temp": 20,
#             # 湿度
#             "humidity": 60,
#             # 风速
#             "windspeed": 10
#         },
#     },
#     "Shanghai": {
#         "2023-10-01": {
#             "temp": 25,
#             "humidity": 40,
#             "windspeed": 5
#         }
#     }
# }
#
# def setup_module():
#     with open("weather.yaml", "w") as file:
#         yaml.safe_dump(weather_data, file)
#
# def get_yaml(f):
#     with open(f, "r") as file1:
#         datas = yaml.safe_load(file1)
#     return datas
#
# @allure.feature("测试天气预测系统")
# class TestWeather:
#     def setup_class(self):
#         self.weather_data = WeatherSystem(weather_data)
#
#     @allure.story("获取当前天气")
#     @allure.title("获取当前天气正常情况")
#     # 获取当前天气正常情况 标记
#     @pytest.mark.run(order=2)
#     def test_get_current(self):
#         sleep(1)
#         result = self.weather_data.get_weather("Beijing")
#         assert result == weather_data["Beijing"]
#         print(result)
#
#     @allure.story("获取当前天气")
#     @allure.title("获取当前天气异常情况")
#     # 获取当前天气异常情况 标记
#     @pytest.mark.run(order=1)
#     def test_get_current_error(self):
#         sleep(1)
#         with pytest.raises(ValueError, match="城市名不存在"):
#             self.weather_data.get_weather("City")
#
#     @allure.story("获取历史天气")
#     @allure.title("获取历史天气正常情况")
#     # 获取历史天气正常情况
#     @pytest.mark.run(order=4)
#     def test_history_current(self):
#         sleep(1)
#         result = self.weather_data.get_history_weather("Beijing", "2023-10-01")
#         assert result == weather_data["Beijing"]["2023-10-01"]
#         print(result)
#
#     @allure.story("获取历史天气")
#     @allure.title("获取历史天气异常情况")
#     # 获取历史天气异常情况
#     @pytest.mark.run(order=3)
#     def test_history_current_error(self):
#         sleep(1)
#         with pytest.raises(ValueError, match="城市名不存在或者日期不存在"):
#             self.weather_data.get_history_weather("City", "2023-10-01")
#
#     @allure.title("预期失败,跳过查询未来天气")
#     # 跳过查