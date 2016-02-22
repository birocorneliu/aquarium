import os
import jinja2
import json
import endpoints
import webapp2
from protorpc import message_types, remote
from google.appengine.api import mail
from app import parser, presenter, db_calls, utils


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
        template_values = {
            "temps": db_calls.get_dict_temps(),
            "watts": utils.get_light()
        }
        template = JINJA_ENVIRONMENT.get_template('templates/temp_chart.jinja2')
        self.response.write(template.render(template_values))


###################################################################################################
class ApiCharts(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        days = int(self.request.params.get("range", 3))
        template_values = {
            "temps": db_calls.get_dict_temps(days),
        }
        self.response.write(json.dumps(template_values))


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
        items = [presenter.dictTempPresenter(model) for model in models]
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

