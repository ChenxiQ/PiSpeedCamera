"""
    MeasureDistance.py
    Created by Chenxi Qian

    measure the distance using HC-SR04 Ultrasonic Ranging Module
"""

import RPi.GPIO as GPIO
import time

def measureDistance(trig, echo):
    # set up GPIO pins for TRIG and ECHO
    TRIG_PIN = trig
    ECHO_PIN = echo
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    # generate a pulse using TRIG pin
    GPIO.output(TRIG_PIN, False)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = 0
    pulse_end = 0

    # set up timer and wait for ECHO response
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = int(pulse_duration * 17150)

    GPIO.cleanup()

    return time.time(), distance
