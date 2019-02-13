from .endpoints import *

ROUTES = (
    (["GET"], "/status", status),
    (["GET"], "/find_issues", find_issues),
    (["GET"], "/reload_pins", reload_pins),
    (["GET"], "/doser/<pin_id>/quantity/<int:quantity>", doser),
    (["GET"], "/temperature", temperature),
    (["GET"], "/set_temperature", set_temperature),
    (["GET"], "/pin/<pin_id>/open", open_pin),
    (["GET"], "/pin/<pin_id>/open/<int:expire_delta>", open_pin_time),
    (["GET"], "/pin/<pin_id>/close", close_pin),
    (["GET"], "/set_procedure/<procedure>", set_procedure),

    (["GET"], "/get_temperatures", get_temperatures),
    (["GET", "POST"], "/temperature", temperature),
)
