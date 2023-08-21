from flask import Flask
from flask import request
from flask import render_template 
import spam_detection as sd

app = Flask(__name__)

@app.route("/")
def detect():
    value = request.args.get('message', '')
    if value:
        result = sd.detect(value)
        return render_template('success_case.html', message=value, result=result)
    return render_template('input_case.html')

@app.route("/detect/<message>")
def detect_message(message):
    return sd.detect(message)