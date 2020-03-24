# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:02:22 2019

@author: aritra.chatterjee
"""

""" Make a dictionary which will contain the 
mapping of direction and GPIO Pin Boolean value"""

import time
import RPi.GPIO as GPIO
import datetime
from sensor3 import *



Direction = ["Forward","Backward","Right","Left","Stop"]
GPIO_Pin=[7,11,13,15]

Forward_map={GPIO_Pin[0]: False,GPIO_Pin[1]:True,GPIO_Pin[2]:False,
                             GPIO_Pin[3]:True}
Backward_map={GPIO_Pin[0]: True,GPIO_Pin[1]:False,GPIO_Pin[2]:True,
                             GPIO_Pin[3]:False}
Right_map={GPIO_Pin[0]: True,GPIO_Pin[1]:False,GPIO_Pin[2]:False,
                             GPIO_Pin[3]:True}
Left_map={GPIO_Pin[0]: False,GPIO_Pin[1]:True,GPIO_Pin[2]:True,
                             GPIO_Pin[3]:False}
Stop_map = {GPIO_Pin[0]: False,GPIO_Pin[1]:False,GPIO_Pin[2]:False,
                             GPIO_Pin[3]:False}

def get_time(dist):
    dist = 2500.00# COming from ultrasonic sensor
    speed = 20.00
    time = dist/speed
    return(time)

time
distance = 2500.00    

while distance > 500:
    gpio_output = []
    for i in range(len(Forward_map)):
        gpio_output.append(GPIO.output(Forward_map[i]))
    gpio_output
    time.sleep(get_time(2500.00))
    