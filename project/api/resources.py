from datetime import datetime, timedelta

from fastapi import APIRouter

import config
from project.db import get_db
from project.domain.collector.collector import WeatherCollector
from project.domain.collector.helper import \
    get_coordinates_and_population_of_city
from project.domain.models import Weather, City

router = APIRouter()


@router.get('/collect')
def collect(amount: int = 50):
    """
    Collect weather statistics in the largest cities in the world,
    by population.
    Param "amount" - how many cities need to be selected
    """

    collector = WeatherCollector(config.OPENWEATHER_API_KEY)
    collector.collect_statistics(amount)
    return 'Statistics collected'


@router.get('/weather/{city}')
def get_current_weather_by_city(city: str):
    """
    Get current weather in a city by name
    """

    city_info = get_coordinates_and_population_of_city(city)
    collector = WeatherCollector(config.OPENWEATHER_API_KEY)
    weather = collector.get_weather(city_info[0], city_info[1])
    return {'weather': weather}


@router.get('/statistics/{city}')
def get_statistics(city: str):
    """
    Get weather statistics in a selected city for the last 12 hours
    """
    db = next(get_db())
    time = datetime.now() - timedelta(hours=12)

    city = db.query(City).filter(City.name == city).scalar()
    weather_statistics = db.query(Weather).filter(
        Weather.city_id == city.id,
        Weather.created_at >= time
    )

    statistics = []
    for statistic in weather_statistics:
        stat = {
            'timestamp': statistic.created_at.strftime('%Y-%m-%d %H:%M'),
            'temp': statistic.temp,
            'pressure': statistic.pressure,
            'humidity': statistic.humidity,
        }
        statistics.append(stat)

    return {'statistics': statistics}
