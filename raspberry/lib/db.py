import json
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime, Float, desc, asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


###################################################################################################
class Temperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    register_date = Column(DateTime, default=datetime.now)


    @classmethod
    #----------------------------------------------------------------------------------------------
    def add_entry(cls, temperature):
        obj = cls()
        obj.temperature = temperature

        session = DBSession()
        session.add(obj)
        session.commit()
        session.close()

        return obj


    @classmethod
    #----------------------------------------------------------------------------------------------
    def get(cls, register_date=None):
        session = DBSession()
        query = session.query(cls)
        #query = query.filter(cls.register_date > register_date)
        query = query.order_by(asc(cls.register_date))

        response = query.all()
        session.close()

        return response



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
    def add_entry(cls, new_statuses, expire_delta=120):
        obj = cls.get()
        if obj:
            statuses = obj.statuses
        else:
            obj = cls()
            statuses = {}
        statuses.update(new_statuses)
        obj.raw_statuses = json.dumps(statuses)
        obj.expire_date = datetime.now() + timedelta(minutes=expire_delta)
        session = DBSession()
        session.add(obj)
        session.commit()
        session.close()

        return obj


    @classmethod
    #----------------------------------------------------------------------------------------------
    def get(cls):
        cls.clean()
        session = DBSession()
        query = session.query(cls)
        query = query.filter(cls.expire_date > datetime.now())
        query = query.order_by(desc(cls.expire_date))

        response = query.first()
        session.close()

        return response


    @classmethod
    #----------------------------------------------------------------------------------------------
    def clean(cls):
        session = DBSession()
        items = session.query(cls).filter(cls.expire_date < datetime.now())
        items.delete()
        session.close()

    @classmethod
    #----------------------------------------------------------------------------------------------
    def clear_all(cls):
        session = DBSession()
        items = session.query(cls)
        print items
        items.delete()

        session.close()



engine = create_engine('sqlite:///lib/aquarium.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
