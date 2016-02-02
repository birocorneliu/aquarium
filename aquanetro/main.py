import endpoints
import webapp2
import handlers


application = webapp2.WSGIApplication([
    ('/', handlers.MainPage),
    ('/charts', handlers.Charts),
    ('/contact', handlers.Contact),
    ('/commands', handlers.Commands),
    ('/config', handlers.Config),
    ('/check_status', handlers.CheckFishStatus),
    ('/temperature', handlers.Temperature),
], debug=True)


api = endpoints.api_server([
    handlers.FishAPI
])

