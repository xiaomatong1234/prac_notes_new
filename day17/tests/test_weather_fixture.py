from datetime import datetime

import pytest
import yaml

from day17.src.weather_fixture import WeatherFixture

# 将fixture移入conftest文件中
# @pytest.fixture(autouse=True) #autouse=True 自动调用
# def fixture():
#      return WeatherFixture()

# 获取yaml文件
def get_yaml():
    # filename = '../data/weather_fixture_data.yml'
    filename = '../data/weather_data.yml'
    with open(filename) as f:
        data = yaml.safe_load(f)
    print('data',data)
    return data

class TestWeatherFixture:
    @pytest.mark.parametrize(
        "city,expected", get_yaml().items()
    )
    def test_current_weather_parametrize(self, fixture, city, expected):
        result = fixture.get_current_weather(city)
        assert result == expected

    @pytest.mark.run(order=1) # 控制用例执行顺序
    def test_current_weather(self,fixture):
        """获取当前天气"""
        result = fixture.get_current_weather('Beijing')
        expected_weather = {
            '2023-10-01': {'humidity': 60, 'temp': 20, 'windspeed': 10},
            str(datetime.today().strftime("%Y-%m-%d")): {'humidity': 60, 'temp': -7, 'windspeed': 10}}
        assert result == expected_weather


    def test_history_weather(self,fixture):
        """获取历史天气"""
        result = fixture.get_history_weather('Beijing','2023-10-01')
        print(result)
        assert result == {'humidity': 60, 'temp': 20, 'windspeed': 10}


    @pytest.mark.skip(reason='Future weather data is not available')
    def test_get_future_weather(self,fixture):
        """跳过测试用例"""
        result = fixture.get_history_weather('Beijing','2023-12-01')
        assert result['temp'] is not None

    @pytest.mark.xfail(reason='Case is expected to fail')
    def test_get_weather_for_non_existent_city(self,fixture):
        """用例预期失败"""
        try:
            result = fixture.get_current_weather('Shenzhen')
            assert False, f"Expected {result}city not found"
        except Exception as e:
            print('捕捉到异常',e)

    # @pytest.mark.run(order=2)  # 控制用例执行顺序
    def test_get_weather_for_invalid_date(self,fixture):
        """获取不存在日期的天气"""
        with pytest.raises(ValueError) as e:
            fixture.get_history_weather('Beijing','2023-12-00')
        assert str(e.value) == 'Beijing or 2023-12-00not found in weather data'



