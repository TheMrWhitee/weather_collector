from sqlalchemy import Column, BigInteger, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB

from project.db import Base
from project.domain.mixins import TimestampMixin


class City(Base, TimestampMixin):
    __tablename__ = 'city'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    population = Column(BigInteger)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class Weather(Base, TimestampMixin):
    __tablename__ = 'weather'

    id = Column(BigInteger, primary_key=True)
    city_id = Column(BigInteger, ForeignKey('city.id'), nullable=False)
    temp = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    all_info = Column(JSONB, nullable=False, default={}, server_default='{}')
