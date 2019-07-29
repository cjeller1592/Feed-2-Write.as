# server.py
# where your python app starts

# init project
from flask import Flask, jsonify, redirect

from stuff import update, read, convert
app = Flask(__name__)

# A placeholder home page
# This way you don't call the Write.as API EVERY time the app loads
@app.route('/')
def home():
  return "Use '/xml' to get a feed of recent posts as a simple Write.as post!"
  
@app.route('/xml')
def hello():
  return redirect(update())
  
 
# listen for requests :)
if __name__ == "__main__":
    from os import environ
    app.run(host='0.0.0.0', port=int(environ['PORT']))