import pytest
import yaml

from day17.src.weather import Weather


def setup_module(self):
    print('\n【测试开始】\n')


def teardown_module(self):
    print('\n【测试结束】')

# 获取yaml文件
def get_yaml_humidity():
    with open('../data/weather_humidity.yml', 'r') as f:
        data = yaml.safe_load(f)
    return data
# 获取温度
def get_yaml_temperature():
    with open('../data/weather_temperature.yml', 'r') as f:
        data = yaml.safe_load(f)
    return data


class TestWeather:
    def setup_class(self):
        # 实例化
        self.weather = Weather()

    @pytest.mark.parametrize(
        "city,expected",get_yaml_humidity(),
        ids=['Beijing_humidity_60']
    )
    def test_now_weather(self,city,expected):
        humidity = self.weather.query_now_weather(city)
        assert humidity['humidity'] == expected

    @pytest.mark.parametrize(
        "city,date,expected",get_yaml_temperature(),
    )
    def test_history_weather(self,city,date,expected):
        temp = self.weather.query_history_weather(city,date)
        assert temp['temp'] == expected
