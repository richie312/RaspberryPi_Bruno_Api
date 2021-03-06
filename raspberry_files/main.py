import flask
from flask import Flask, request, json,render_template,redirect,url_for,jsonify,json
import datetime
import os

app = Flask(__name__)
app.config['DEBUG'] = True

""" read the list of users"""
@app.route("/get_temperature")        # Standard Flask endpoint
def get_temperature():
    import RPi.GPIO as GPIO
    import dht11    
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
     
    # read data using pin 14
    instance = dht11.DHT11(pin = 23)
    result = instance.read()    
    if result.is_valid():
        response = {"Temperature":str(result.temperature) + " Celsius",
                    "Humidity":result.humidity}        
    else:
        response = {"Error":result.error_code}
    GPIO.cleanup()   
    return jsonify(response)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True,port=5001)
