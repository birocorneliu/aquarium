import endpoints
import webapp2
import handlers

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}


application = webapp2.WSGIApplication([
    ('/', handlers.MainPage),
    ('/charts', handlers.Charts),
    ('/contact', handlers.Contact),
    ('/commands', handlers.Commands),
    ('/config', handlers.Config),
    ('/check_status', handlers.CheckFishStatus),
    ('/temperature', handlers.Temperature),
    ('/api/charts', handlers.ApiCharts),
    ('/fbconnect', handlers.Connect),
], config=config, debug=True)


api = endpoints.api_server([
    handlers.FishAPI
])

