#Libraries
import RPi.GPIO as GPIO
import pymysql
import time
import datetime

host="richie-database.cml5lvgzqjbw.us-east-1.rds.amazonaws.com"
port=3306
dbname="RDS_MySql"
user="richie31"
password="Nirvikalpa!123"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)

cursor = conn.cursor()
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 20
GPIO_ECHO = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
 
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if dist < 10.0:
                msg = 'too close'
                print(msg)
                sql_query = "INSERT INTO readings_sonar_dist (dateofreading, distance) VALUES (%s,%s)"
                now_time = datetime.datetime.now()
                sql_date_format = now_time.strftime('%Y-%m-%d %H:%M:%S')
                dateofreading = sql_date_format
                distance_reading = dist
                val = (dateofreading,distance_reading)
                cursor.execute(sql_query,val)
                conn.commit()                 
            else:
                msg = 'Safe Distance'
                print(msg)
                  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()