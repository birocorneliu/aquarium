from .endpoints import *

ROUTES = (
    (["GET"], "/", home),
    (["GET"], "/temperature", temperature),
    (["GET"], "/temperature/save", temperature_save),
    (["GET"], "/pin/<int:pin_no>/open", open_pin),
    (["GET"], "/pin/<int:pin_no>/close", close_pin),
    (["GET"], "/dose_pump/pump_id/<int:pump_id>/ml_quantity/<float:ml_quantity>", dose_pump),
)
