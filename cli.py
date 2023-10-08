import click

from project.domain.collector.helper import insert_cities


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

    insert_cities(cities)


if __name__ == "__main__":
    cli()
