import flask
from flask import Flask, request, json,render_template,redirect,url_for,jsonify,json
import mysql.connector
import mysql
import datetime
import os
from decrypt import *

with open(r'database_auth.json','r') as readfile:
    db_auth = json.load(readfile)

""" decrypt the database details"""
main_dir = os.getcwd()
os.listdir(os.path.join(main_dir,'auth'))

db_auth = {'dbname.txt':'key_dbname.txt',
           'db_pass.txt':'key_db_pass.txt',
           'host.txt':'key_host.txt',
           'dbuser.txt':'key_dbuser.txt'}
filename = {}
for i in db_auth.keys():
    with open(os.path.join('auth',i), 'r') as readfile:
        filename['{}'.format(i.split('.')[0])]= json.load(readfile)

file_key = {}
for i in db_auth.keys():
    with open(r'auth/' +db_auth[i], 'r') as readfile:
        file_key['{}'.format(db_auth[i].split('.')[0])]= json.load(readfile)

db_auth = {}
for i in filename.keys():
    db_auth[i] = decrypt(eval(filename[i]),eval(file_key['key_'+i])).decode("utf-8")

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
