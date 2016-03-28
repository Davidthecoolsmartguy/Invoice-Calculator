"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#get flask
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

from routes import *

#run server and this is the ip server
if __name__ == '__main__':
    import os
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
