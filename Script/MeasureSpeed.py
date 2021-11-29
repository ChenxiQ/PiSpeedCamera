import time
from MeasureDistance import measureDistance

def measureSpeed():
    SENSOR_DIS = 18
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

    initDistanceLeft = measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)[1]
    initDistanceRight = measureDistance(RIGHT_TRIG_PIN, RIGHT_ECHO_PIN)[1]

    print("#################### Start Program ####################")
    print("############### Measure Initial Distance ##############")
    print("Left Initial:  ", initDistanceLeft)
    print("Right Initial: ", initDistanceRight)
    print("#######################################################")

    leftDetected = False
    leftDetectedTime = 0
    while not leftDetected:
        currentTimeLeft, measuredDistanceLeft = measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)
        time.sleep(0.05)
        if measuredDistanceLeft < initDistanceLeft - 5:
            leftDetected = True
            leftDetectedTime = currentTimeLeft

    print("Left Detected! Time:", leftDetectedTime, "Distance:", measuredDistanceLeft)

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

    speedCM = SENSOR_DIS / (rightDetectedTime - leftDetectedTime)
    speedKM = speedCM * 0.036
    speedMI = speedCM * 0.022369
    print("Measured Speed:", speedCM, "cm/s")
    print("Measured Speed:", speedKM, "km/h")
    print("Measured Speed:", speedMI, "mile/h")
    print("#######################################################")
    return speedMI
