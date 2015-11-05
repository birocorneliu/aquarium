import endpoints
import webapp2
import handlers


application = webapp2.WSGIApplication([
    ('/', handlers.MainPage),
    ('/charts', handlers.Charts),
    ('/contact', handlers.Contact),
    ('/config', handlers.Config),
    ('/check_status', handlers.CheckFishStatus),
], debug=True)


api = endpoints.api_server([
    handlers.FishAPI
])

