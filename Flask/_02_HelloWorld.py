'''
https://flask.palletsprojects.com/en/2.0.x/quickstart/
Running on widows:
  $env:FLASK_APP = "_02_HelloWorld"
  flask run
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"