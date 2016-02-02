from datetime import datetime
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
def get_temps(limit=50):
    query = FishTemp.query()
    #query = query.filter(FishTemp.date < datetime.now().replace(hour=19, minute=0))
    query = query.order(-FishTemp.date)
    models = query.fetch(limit=limit)
    models.reverse()

    return models



