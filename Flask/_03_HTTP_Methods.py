'''
Running on widows:
  $env:FLASK_APP = "_03_HTTP_Methods"
  flask run
'''

from flask import Flask, request
from flask.json import jsonify
app = Flask(__name__)

'''
http://127.0.0.1:5000/get_data
'''
@app.route("/get_data", methods=['GET'])
def get_data():
    response_body = {
      "method": request.method,
      "name": "Jose Santos",
      "email": "jose.santos@noemail.com",
      "phone": "(999) 111-2233"
    }
    return jsonify(response_body) # Returning the response as a JSON

'''
http://127.0.0.1:5000/get_data_with_params?name=Jose Santos&email=jose.santos@noemail.com&phone=(999) 111-2233
'''
@app.route("/get_data_with_params", methods=['GET'])
def get_data_with_params():
    params = request.args # Accessing the query string
    response_body = {
      "Method": request.method,
      "name": params['name'],
      "email": params['email'],
      "phone": params['phone']
    }
    return jsonify(response_body)

'''
http://127.0.0.1:5000/post_data
{
    "email": "jose.santos@noemail.com",
    "name": "Jose Santos",
    "phone": "(999) 111-2233"
}
'''
@app.route("/post_data", methods=['POST'])
def hello_world():
    params = request.json # Acessing the request body as JSON
    response_body = {
      "Method": request.method,
      "name": params['name'].upper(),
      "email": params['email'].upper(),
      "phone": params['phone'].upper()
    }
    return jsonify(response_body)