from flask import Flask
from flask import request
from flask import render_template 
import spam_detection as sd

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Welcome to the Spam Detection System</p>"

@app.route("/detect")
def detect():
    return render_template('input_case.html')

@app.route("/detect/<message>")
def detect_message(message):
    return sd.detect(message)