from datetime import datetime, timedelta
from google.appengine.ext import ndb

from .models import FishTemp


#--------------------------------------------------------------------------------------------------
def add_temp(request):
    time = datetime.now().replace(microsecond=0)
    if hasattr(request, "temperature"):
        temperature = request.temperature
    else:
        temperature = float(request.get("temperature"))

    key = ndb.Key(FishTemp, str(time))
    model = FishTemp(key=key, date=time, temperature=temperature)
    model.put()

    return model


#--------------------------------------------------------------------------------------------------
def get_temps(days=3):
    date = datetime.now() - timedelta(days=days)
    query = FishTemp.query()
    query = query.filter(FishTemp.date > date)
    query = query.order(-FishTemp.date)
    models = query.fetch()
    models.reverse()

    return models


#--------------------------------------------------------------------------------------------------
def get_date(date):
    return {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
        "minute": date.minute,
    }


#--------------------------------------------------------------------------------------------------
def get_dict_temps(days=3):
    models = get_temps(days)
    return [{"date": get_date(row.date), "temperature": row.temperature} for row in models]


