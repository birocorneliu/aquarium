from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Temperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    register_date = Column(DateTime, default=datetime.now)


class CronConfig(Base):
    __tablename__ = "cron_config"

    id = Column(Integer, primary_key=True)
    pin_id = Column(String(16), nullable=False)
    on_hour = Column(Integer, nullable=False)
    on_minute = Column(Integer, nullable=False)
    off_hour = Column(Integer)
    off_minute = Column(Integer)
    quantity = Column(Integer)



engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
