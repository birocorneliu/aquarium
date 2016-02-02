import os
import jinja2
import endpoints
import webapp2
from protorpc import message_types, remote
from google.appengine.api import mail
from app import parser, presenter, db_calls


###################################################################################################
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


###################################################################################################
class MainPage(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        classes = [
            "hex col-sm-6", "hex col-sm-6", "hex col-sm-6  templatemo-hex-top2",
            "hex col-sm-6  templatemo-hex-top3", "hex col-sm-6  templatemo-hex-top3",
            "hex col-sm-6 hex-offset templatemo-hex-top1 templatemo-hex-top2",
            "hex col-sm-6 templatemo-hex-top1 templatemo-hex-top3",
            "hex col-sm-6 templatemo-hex-top1 templatemo-hex-top3",
            "hex col-sm-6 templatemo-hex-top1 templatemo-hex-top2"]
        models = db_calls.get_temps()
        items = [{
            "date": model.date,
            "temp": model.temperature,
            } for model in models]
        template_values = {
            "rows": items,
            "images1": [(cls, index+1) for index, cls in enumerate(classes)],
            "images2": [(cls, index+10) for index, cls in enumerate(classes)]
        }


        template = JINJA_ENVIRONMENT.get_template('templates/home.jinja2')
        self.response.write(template.render(template_values))


###################################################################################################
class Charts(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        models = db_calls.get_temps()
        from datetime import datetime
        import random
        time = datetime.now().replace(second=0, microsecond=0)
        temps = []
        hour = 0
        minute = 0
        for i in range(120):
            temps.append({
            "date": time.replace(hour=hour, minute=minute),
            "temp": round(26 + random.random() * 2, 2)
            })
            minute += 10
            if minute == 60:
                hour += 1
                minute = 0

        #temps = db_calls.get_temps()
        #temps = [{"date": temp.date, "temp": temp.date} for temp in temps]

        light_intensity = 0
        lights = [
            [30, {"on": [ 7, 00], "off": [ 7, 20]}],
            [39, {"on": [ 7, 20], "off": [10, 00]}],
            [39, {"on": [ 7, 50], "off": [ 9, 30]}],
            [30, {"on": [10, 00], "off": [10, 20]}],

            [30, {"on": [17, 20], "off": [17, 40]}],
            [39, {"on": [17, 40], "off": [22, 00]}],
            [39, {"on": [18, 00], "off": [21, 35]}],
            [30, {"on": [22, 00], "off": [22, 30]}],
        ]
        co2 = [
            [50, {"on": [ 6, 00], "off": [ 9, 30]}],
            [50, {"on": [15, 00], "off": [20, 30]}],
        ]
        hour = 5
        minute = 30
        watts = []
        co2_stat = 0

        for i in range(1080):
            for watt, status in lights:
                if status["on"] == [hour, minute]:
                    light_intensity += watt
                if status["off"] == [hour, minute]:
                    light_intensity -= watt
            for watt, status in co2:
                if status["on"] == [hour, minute]:
                    co2_stat += watt
                if status["off"] == [hour, minute]:
                    co2_stat -= watt

            watts.append({
                "date": time.replace(hour=hour, minute=minute),
                "light_intensity": light_intensity,
                "co2_stat": co2_stat
            })
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0



        template_values = {
            "temps": temps,
            "watts": watts
        }

        template = JINJA_ENVIRONMENT.get_template('templates/temp_chart.jinja2')
        self.response.write(template.render(template_values))



###################################################################################################
class Contact(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.jinja2')
        self.response.write(template.render({}))


###################################################################################################
class Commands(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/commands.jinja2')
        self.response.write(template.render({}))



###################################################################################################
class Config(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/config.jinja2')
        self.response.write(template.render({}))



###################################################################################################
class CheckFishStatus(webapp2.RequestHandler):

    #--------------------------------------------------------------------------
    def get(self):
        #get_config
        #message = get_fish_status_warning()
        message = "ai o buba gogule"
        if message:
            subject = "O problema la acvariu!!!"
            sender_address = "FishAPP Support <corneliu.biro@gmail.com>"
            for user_address in ["corneliu.biro@gmail.com"]: #config.emails
                mail.send_mail(sender_address, user_address, subject, message)


###################################################################################################
class Temperature(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        models = db_calls.get_temps()
        items = [presenter.copyTempPresenter(model) for model in models]
        self.response.write({"items": items})


    #----------------------------------------------------------------------------------------------
    def post(self):
        model = db_calls.add_temp(self.request)

        self.response.write({
            "date": model.date,
            "temperature": model.temperature
        })


@endpoints.api(name='FishAPI', version='v1', description="Fishy app")
###################################################################################################
class FishAPI(remote.Service):


    @endpoints.method(parser.TempParser, presenter.TempPresenter,
                      path='add_temp', http_method='POST', name='add_temp')
    #----------------------------------------------------------------------------------------------
    def add_temp(self, request):
        model = db_calls.add_temp(request)

        return presenter.copyTempPresenter(model)



    @endpoints.method(message_types.VoidMessage, presenter.TempsPresenter,
                      path='get_temps', http_method='GET', name='get_temps')
    #----------------------------------------------------------------------------------------------
    def get_temps(self, request):
        models = db_calls.get_temps()
        items = [presenter.copyTempPresenter(model) for model in models]

        return presenter.TempsPresenter(items=items)

