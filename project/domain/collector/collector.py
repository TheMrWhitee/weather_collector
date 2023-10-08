import requests

import config
from project.db import get_db, transaction
from project.domain.models import City, Weather


class WeatherCollector:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, lat, lon):
        url = f'{config.OPENWEATHER_URL}?lat={lat}&lon={lon}'
        url += f'&appid={self.api_key}&units=metric'

        weather = requests.get(url).json()
        return weather

    def _iter_large_cities(self, amount):
        db = next(get_db())
        cities = db.query(City).order_by(City.population.desc()).limit(amount)

        for city in cities:
            yield city

    def run(self, amount):
        db = next(get_db())
        weather_in_cities = []

        for city in self._iter_large_cities(amount):
            city_weather = self.get_weather(city.latitude, city.longitude)
            weather = Weather(
                city_id=city.id,
                temp=city_weather['main']['temp'],
                pressure=city_weather['main']['pressure'],
                humidity=city_weather['main']['humidity'],
                all_info=city_weather,
            )
            weather_in_cities.append(weather)

        with transaction(db):
            db.add_all(weather_in_cities)
