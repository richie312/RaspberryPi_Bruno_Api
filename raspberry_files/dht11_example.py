import RPi.GPIO as GPIO
import dht11
import time
import datetime
import pymysql

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Create the connection between raspbery pi and AWS RDS mysql

host="richie-database.cml5lvgzqjbw.us-east-1.rds.amazonaws.com"
port=3306
dbname="RDS_MySql"
user="richie31"
password="Nirvikalpa!123"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)

cursor = conn.cursor()

# read data using pin 14
instance = dht11.DHT11(pin=23)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        """Insert Data into Raspberry Pi"""

        sql_query = "INSERT INTO readings_temp (dateofreading, temperature, Humidity) VALUES (%s,%s,%s)"
        time = datetime.datetime.now()
        sql_date_format = time.strftime('%Y-%m-%d %H:%M:%S')
        dateofreading = sql_date_format
        temperature = result.temperature        
        Humidity = result.humidity
        val = (dateofreading, temperature, Humidity)
        cursor.execute(sql_query,val)
        conn.commit()
    