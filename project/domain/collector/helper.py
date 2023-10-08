import requests

import config
from project.db import get_db, transaction
from project.domain.models import City

cities = (
    'Chongqing', 'Shanghai', 'Beijing', 'Chengdu', 'Delhi', 'Guangzhou',
    'Mumbai', 'Shenzhen', 'Kinshasa', 'Istanbul', 'Karachi', 'Tokyo',
    'Tianjin', 'Zhengzhou', 'São Paulo', 'Tehran', 'Moscow', 'Hangzhou',
    'Lahore', 'Shijiazhuang', 'Suzhou', 'Jakarta', 'Dongguan', 'Qingdao',
    'Changsha', 'Cairo', 'Harbin', 'Seoul', 'Ningbo', 'Hefei', 'Nanjing',
    'Mexico City', 'Jinan', 'Ho Chi Minh City', 'London', 'New York', 'Xi’an',
    'Kunming', 'Chittagong', 'Bengaluru', 'Shenyang', 'Bangkok', 'Hanoi',
    'Lagos', 'Riyadh', 'Changchun', 'Lima', 'Hong Kong', 'Bogotá', 'Baghdad'
)


def get_coordinates_and_population_of_city(city_name: str):
    url = f'{config.GEONAMES_URL}&name={city_name}'
    url += f'&username={config.GEONAMES_USERNAME}'

    response = requests.get(url).json()['geonames'][0]
    lat, lng, ppl = response['lat'], response['lng'], response['population']

    return lat, lng, ppl


def insert_cities(city_names: tuple):
    db = next(get_db())
    cities_to_insert = []

    for name in city_names:
        lat, lng, ppl = get_coordinates_and_population_of_city(name)
        city = City(name=name, latitude=lat, longitude=lng, population=ppl)
        cities_to_insert.append(city)

    with transaction(db):
        db.add_all(cities_to_insert)


insert_cities(cities)
