import pytest

from day17.src.weather_fixture import WeatherFixture


@pytest.fixture(autouse=True) #autouse=True 自动调用
def fixture():
     return WeatherFixture()