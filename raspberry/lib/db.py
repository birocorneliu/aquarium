import json
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


###################################################################################################
class Temperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    register_date = Column(DateTime, default=datetime.now)


###################################################################################################
class CronConfig(Base):
    __tablename__ = "cron_config"

    id = Column(Integer, primary_key=True)
    pin_id = Column(String(16), nullable=False)
    on_hour = Column(Integer, nullable=False)
    on_minute = Column(Integer, nullable=False)
    off_hour = Column(Integer)
    off_minute = Column(Integer)
    quantity = Column(Integer)


###################################################################################################
class TempCommands(Base):
    __tablename__ = "temp_commands"

    id = Column(Integer, primary_key=True)
    raw_statuses = Column(String(254), nullable=False)
    expire_date = Column(DateTime, default=datetime.now)

    @property
    #----------------------------------------------------------------------------------------------
    def statuses(self):
        return json.loads(self.raw_statuses)


    @classmethod
    #----------------------------------------------------------------------------------------------
    def add_entry(cls, new_statuses):
        obj = cls.get()
        if obj:
            statuses = obj.statuses
        else:
            obj = cls()
            statuses = {}
        statuses.update(new_statuses)
        obj.raw_statuses = json.dumps(statuses)
        obj.expire_date = datetime.now() + timedelta(hours=2)
        session.add(obj)
        session.commit()
        return obj


    @classmethod
    #----------------------------------------------------------------------------------------------
    def get(cls):
        cls.clean()
        query = session.query(cls)
        query = query.filter(cls.expire_date > datetime.now())
        query = query.order_by(desc(cls.expire_date))
        return query.first()


    @classmethod
    #----------------------------------------------------------------------------------------------
    def clean(cls):
        items = session.query(cls).filter(cls.expire_date < datetime.now())
        items.delete()


    @classmethod
    #----------------------------------------------------------------------------------------------
    def clear_all(cls):
        session.query(cls).delete()



engine = create_engine('sqlite:///lib/aquarium.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
