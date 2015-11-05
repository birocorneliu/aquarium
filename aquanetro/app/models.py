from google.appengine.ext import ndb


###############################################################################
class FishTemp(ndb.Model):

    date = ndb.DateTimeProperty(indexed=True)
    humidity = ndb.FloatProperty()
    temperature = ndb.FloatProperty()



###############################################################################
class FishConfig(ndb.Model):

    min_temp = ndb.FloatProperty()
    max_temp = ndb.FloatProperty()
    temps_per_chart = ndb.IntegerProperty()
    emails = ndb.StringProperty(repeated=True)


