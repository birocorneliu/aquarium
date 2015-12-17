from .endpoints import *

ROUTES = (
    (["GET"], "/", home),
    (["GET"], "/reload_pins", reload_pins),
    (["GET"], "/doser/<resource>/quantity/<int:quantity>", doser),
    (["GET"], "/temperature", temperature),
    (["GET"], "/temperature/save", temperature_save),
    (["GET"], "/pin/<pin_no>/open", open_pin),
    (["GET"], "/pin/<pin_no>/close", close_pin),
    (["GET"], "/set_times_to_cron", set_times_to_cron),
)
