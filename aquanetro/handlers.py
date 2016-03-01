import os
import jinja2
import json
import endpoints
import webapp2
from webapp2_extras import sessions
from protorpc import message_types, remote
from google.appengine.api import mail, users
from app import parser, presenter, db_calls, utils



###################################################################################################
class BaseHandler(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)


    @webapp2.cached_property
    #----------------------------------------------------------------------------------------------
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()



###################################################################################################
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


###################################################################################################
class MainPage(BaseHandler):

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
class Charts(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template_values = {
            "temps": db_calls.get_dict_temps(),
            "watts": utils.get_light()
        }
        template = JINJA_ENVIRONMENT.get_template('templates/temp_chart.jinja2')
        self.response.write(template.render(template_values))


###################################################################################################
class ApiCharts(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        days = int(self.request.params.get("range", 3))
        template_values = {
            "temps": db_calls.get_dict_temps(days),
        }
        self.response.write(json.dumps(template_values))


###################################################################################################
class Contact(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.jinja2')
        self.response.write(template.render({}))


###################################################################################################
class Commands(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        #import pdb; pdb.set_trace()
        template = JINJA_ENVIRONMENT.get_template('templates/commands.jinja2')
        self.response.write(template.render({}))



###################################################################################################
class Config(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/config.jinja2')
        self.response.write(template.render({}))



###################################################################################################
class CheckFishStatus(BaseHandler):

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
class Temperature(BaseHandler):

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


###################################################################################################
class Connect(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        #import pdb;pdb.set_trace()
        template = JINJA_ENVIRONMENT.get_template('templates/login.jinja2')
        self.response.write(template.render({}))
        print self.session


    #----------------------------------------------------------------------------------------------
    def post(self):
        data = utils.connect_user_through_facebook(self.request.body)
        self.session.update(data)
        self.response.write({})



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


