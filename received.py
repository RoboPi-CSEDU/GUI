#!/usr/bin/python
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

speed_left= 10 
speed_right= 11          
rot_left_1= 8  
rot_left_2= 9  
rot_right_1= 12  
rot_right_2= 13

try:
	connection = SerialManager()
	a= ArduinoApi(connection = connection)
except:
	print("Failed to connect")

  
a.pinMode(speed_left,a.OUTPUT)
a.pinMode(speed_right,a.OUTPUT)
    
a.pinMode(rot_left_1,a.OUTPUT)
a.pinMode(rot_left_2,a.OUTPUT)
    
a.pinMode(rot_right_1,a.OUTPUT)
a.pinMode(rot_right_2,a.OUTPUT)


# obstacleDetected()
# wait(time_in_milisec)
# getColorFromSensor()
# getDistanceFromSensor()
# say("text")

def say(str):
	print(str)
	
def go(str,time):
	a='forward'
	b='backward'

	if(str==a):
		move_forward(time)
	elif(str==b):
		move_back(time)
		
def turn(str,time):
	tl='turn_left'
	tr='turn_right'
	if(str==tl):
		turn_left()
	elif(str==tr):
		turn_right()
		
def move_forward(time):
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,255)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,255)
			
    sleep(time)



def move_back(time):
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,255)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,255)
    a.analogWrite(rot_right_2,0)
			
    sleep(time)


def turn_right():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,255)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,255)
			
    sleep(0.5)

def turn_left():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,255)

    a.analogWrite(rot_right_1,255)
    a.analogWrite(rot_right_2,0)
			
    sleep(0.5)

def stop():
    a.analogWrite(speed_left,0)
    a.analogWrite(speed_right,0)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,0)
			
    sleep(1)
	
def run():
	print('hello world')
	

say('hello')

