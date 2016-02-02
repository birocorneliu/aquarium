from protorpc import messages


###################################################################################################
class TempParser(messages.Message):
    temperature = messages.FloatField(1)


