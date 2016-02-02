from .endpoints import *

ROUTES = (
    (["GET"], "/", home),
    (["GET"], "/reload_pins", reload_pins),
    (["GET"], "/doser/<pin_id>/quantity/<int:quantity>", doser),
    (["GET"], "/temperature", temperature),
    (["GET"], "/temperature/save", temperature_save),
    (["GET"], "/pin/<pin_id>/open", open_pin),
    (["GET"], "/pin/<pin_id>/close", close_pin),
    (["GET"], "/set_times_to_cron", set_times_to_cron),
    (["GET"], "/set_procedure/<procedure>", set_procedure),
)


from app.cron import Cron

#Set CronTab
#Cron.clean_cron()
#Cron.set_times()
