import os
import sys
from flask import Flask, redirect
try:
    from flask.ext.cors import CORS
except:
    from flask_cors import CORS

from app import ROUTES
from lib.exceptions import APPException


#Start app engine
app = Flask(__name__)
app.secret_key = "Super secret KEY"
CORS(app)


#Add rules to the app
for methods, path, func in ROUTES:
    app.add_url_rule(path, view_func=func, methods=methods)


#Add exception handler
@app.errorhandler(APPException)
def exception_handler(error):
    base_url = "/error?code={}&message={}"
    url = base_url.format(error.status_code, error.message)
    return redirect(url)


#Add current path to sys paths
PATH = os.path.realpath('.')
sys.path.append(PATH)



###################################################################################################
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)


