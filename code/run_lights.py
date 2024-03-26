import Jetson.GPIO as GPIO
import time

# Define the GPIO pin numbers for each LED
red_led = [7,13,7,13]
yellow_led = [12,15,12,15]
green_led = [11,16,11,16]

#18,19,21/22,23,24 >for the other 2 trafic lights

# Set up the GPIO pins as outputs
GPIO.setmode(GPIO.BOARD) 

for i in range(len(red_led)):
    GPIO.setup(yellow_led[i], GPIO.OUT)
    GPIO.setup(green_led[i], GPIO.OUT)
    GPIO.setup(red_led[i], GPIO.OUT)

 #To prevent one light to run before the rest.and before calling the function 
for i in range(len(red_led)):
    GPIO.output(red_led[i], GPIO.LOW)
    GPIO.output(yellow_led[i], GPIO.LOW)
    GPIO.output(green_led[i], GPIO.LOW)

#initially all traffic lights are red
def initialize():
    for i in range(len(red_led)):
        GPIO.output(red_led[i], GPIO.HIGH)  
    

# Define the traffic light sequence
def light(Vcam_id,v_num):

    if (v_num==0): #define minimum time for green light
        sinterval=0.5
    elif(v_num>5):#define maximum time for green light
        sinterval=6
    else:
        sinterval=v_num*1 #Avg time to pass traffic light #s/vehicle


    #Turn off the red light of the current traffic light
    GPIO.output(red_led[Vcam_id], GPIO.LOW)

    # Run the traffic light sequence 
    GPIO.output(yellow_led[Vcam_id], GPIO.HIGH)                                                                                                                                                                                                                                                                                                                                                                                                                 
    time.sleep(2)
    GPIO.output(yellow_led[Vcam_id], GPIO.LOW)
    
    GPIO.output(green_led[Vcam_id], GPIO.HIGH)                                                                                                                                                                                                                                                                                                                                                                                                                 
    time.sleep(sinterval)
    GPIO.output(green_led[Vcam_id], GPIO.LOW)

    initialize()

#GPIO.cleanup()
'''
while True:
 
    traffic_light()
    '''

#light()