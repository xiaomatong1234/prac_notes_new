from datetime import datetime


class WeatherFixture:
    def __init__(self):
        self.weather_data = {
            "Beijing":
            {"2023-10-01":
                 {"temp": 20,"humidity": 60,"windspeed": 10},

                str(datetime.today().strftime("%Y-%m-%d")): {
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
    # 获取当前天气
    def get_current_weather(self,city):
        if city not in self.weather_data:
            raise ValueError(f"{city} not found in weather data")
        # 获取今天天气信息
        today = datetime.today().strftime("%Y-%m-%d")
        print(f'{city},{self.weather_data[city]}')
        return self.weather_data[city]

    # 获取历史天气
    def get_history_weather(self,city,date):
        if city not in self.weather_data or date not in self.weather_data[city]:
            raise ValueError(f"{city} or {date}not found in weather data")
        print(f'{city},{date},{self.weather_data[city][date]}')
        return self.weather_data[city][date]

# w = WeatherFixture()
# w.get_current_weather('Shanghai')
# w.get_history_weather('Beijing','2023-10-01')
