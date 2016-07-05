
admin = "Corneliu Biro"

base_url = "http://raspberry.aquanet.ro"
#base_url = "http://192.168.1.20"

command_mapping = {
    "set_procedure": "set_procedure/{entity}",
    "open_individual": "pin/{entity}/open",
    "close_individual": "pin/{entity}/close",
}

procedures = {
    "movie": "Film",
    "lights_on": "Lumini ON",
    "lights_off": "Lumini OFF",
    "schimb_apa": "Schimb Apa",
    "feed": "Hranire",
    "reset": "Reset"
}
