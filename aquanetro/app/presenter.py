from protorpc import messages


###################################################################################################
class TempPresenter(messages.Message):

    temperature = messages.FloatField(1)
    date = messages.StringField(3)



###################################################################################################
class TempsPresenter(messages.Message):
    items = messages.MessageField(TempPresenter, 1, repeated=True)


#--------------------------------------------------------------------------------------------------
def copyTempPresenter(model):
    tp = TempPresenter()

    for field in tp.all_fields():
        value = getattr(model, field.name)
        if field.name == "date":
            value = str(value)
        setattr(tp, field.name, value)

    return tp


###################################################################################################
def dictTempPresenter(obj):
    return {
        "date": obj.date,
        "temperature": obj.temperature
    }


###################################################################################################
def chartTempPresenter(obj):
    return {
        "date": obj.date,
        "temp": obj.temperature
    }

