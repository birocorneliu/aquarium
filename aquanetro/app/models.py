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



###############################################################################
class Lights(ndb.Model):

    name = ndb.StringProperty(required=True)
    power = ndb.IntegerProperty(required=True)



###############################################################################
class LightsConfig(ndb.Model):

    name = ndb.ReferenceProperty(Lights)
    start = ndb.DateTimeProperty()
    finish = ndb.DateTimeProperty()



###############################################################################
class CO2Config(ndb.Model):

    start = ndb.DateTimeProperty()
    finish = ndb.DateTimeProperty()


