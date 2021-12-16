"""
    MeasureSpeed.py
    Created by Chenxi Qian

    measure the speed of a moving car using two HC-SR04 Ultrasonic Sensors
"""

import time
from MeasureDistance import measureDistance

def measureSpeed():
    # distance between two Ultrasonic Sensors in cm
    SENSOR_DIS = 57

    # define GPIO pins
    LEFT_TRIG_PIN = 23
    LEFT_ECHO_PIN = 24
    RIGHT_TRIG_PIN = 5
    RIGHT_ECHO_PIN = 6

    # initiate ultrasonic sensors
    # first few measurements would be unstable
    # discard these values
    for _ in range(5):
        measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)
        time.sleep(0.001)
        measureDistance(RIGHT_TRIG_PIN, RIGHT_ECHO_PIN)

    # calibrate and get initial distance
    _, initDistanceLeft = measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)
    _, initDistanceRight = measureDistance(RIGHT_TRIG_PIN, RIGHT_ECHO_PIN)

    print("#################### Start Program ####################")
    print("############### Measure Initial Distance ##############")
    print("Left Initial:  ", initDistanceLeft)
    print("Right Initial: ", initDistanceRight)
    print("#######################################################")

    # start timer when the car reached the left sensor
    leftDetected = False
    leftDetectedTime = 0
    while not leftDetected:
        currentTimeLeft, measuredDistanceLeft = measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)
        time.sleep(0.05)
        if measuredDistanceLeft < initDistanceLeft - 5:
            leftDetected = True
            leftDetectedTime = currentTimeLeft

    print("Left Detected! Time:", leftDetectedTime, "Distance:", measuredDistanceLeft)

    # stop timer when the car reached the right sensor
    rightDetected = False
    rightDetectedTime = 0
    while not rightDetected:
        currentTimeRight, measuredDistanceRight = measureDistance(RIGHT_TRIG_PIN, RIGHT_ECHO_PIN)
        time.sleep(0.05)
        if measuredDistanceRight < initDistanceRight - 5:
            rightDetected = True
            rightDetectedTime = currentTimeRight

    print("Right Detected! Time:", rightDetectedTime, "Distance:", measuredDistanceRight)
    print("#######################################################")
    print("################## Calculating Speed ##################")

    # calculate the speed of the car
    speedCM = round(SENSOR_DIS / (rightDetectedTime - leftDetectedTime), 2)
    speedKM = round(speedCM * 0.036, 2)
    speedMI = round(speedCM * 0.022369, 2)
    print("Measured Speed:", speedCM, "cm/s")
    print("Measured Speed:", speedKM, "km/h")
    print("Measured Speed:", speedMI, "mile/h")
    print("#######################################################")
    return speedMI
