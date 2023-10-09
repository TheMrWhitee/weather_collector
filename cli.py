import click

import config
from project.db import get_db
from project.domain.collector.collector import WeatherCollector
from project.domain.collector.helper import insert_cities
from project.domain.models import City


@click.group()
def cli():
    pass


@cli.command()
def insert_city():
    cities = (
        'Chongqing', 'Shanghai', 'Beijing', 'Chengdu', 'Delhi', 'Guangzhou',
        'Mumbai', 'Shenzhen', 'Kinshasa', 'Istanbul', 'Karachi', 'Tokyo',
        'Tianjin', 'Zhengzhou', 'São Paulo', 'Tehran', 'Moscow', 'Hangzhou',
        'Lahore', 'Shijiazhuang', 'Suzhou', 'Jakarta', 'Dongguan', 'Qingdao',
        'Changsha', 'Cairo', 'Harbin', 'Seoul', 'Ningbo', 'Hefei', 'Nanjing',
        'Mexico City', 'Jinan', 'Ho Chi Minh City', 'London', 'New York',
        'Xi’an', 'Kunming', 'Chittagong', 'Bengaluru', 'Shenyang', 'Bangkok',
        'Hanoi', 'Lagos', 'Riyadh', 'Changchun', 'Lima', 'Hong Kong', 'Bogotá',
        'Baghdad'
    )

    db = next(get_db())

    count = db.query(City).count()
    if count:
        print('The database already contains {} cities'.format(count))
        return

    insert_cities(cities)


@cli.command()
@click.option('-n', '--number', type=int, default=50)
def collect(number):
    collector = WeatherCollector(config.OPENWEATHER_API_KEY)
    collector.collect_statistics(number)


if __name__ == '__main__':
    cli()
