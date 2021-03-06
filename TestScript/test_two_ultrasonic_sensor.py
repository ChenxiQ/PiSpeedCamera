import RPi.GPIO as GPIO
import time

def measureDistance(trig, echo):
    TRIG_PIN = trig
    ECHO_PIN = echo
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    GPIO.output(TRIG_PIN, False)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = 0
    pulse_end = 0

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = int(pulse_duration * 17150)

    GPIO.cleanup()

    return time.time(), distance

LEFT_TRIG_PIN = 23
LEFT_ECHO_PIN = 24
RIGHT_TRIG_PIN = 5
RIGHT_ECHO_PIN = 6

for i in range(100):
    currentTimeLeft, measuredDistanceLeft = measureDistance(LEFT_TRIG_PIN, LEFT_ECHO_PIN)
    time.sleep(0.001)
    currentTimeRight, measuredDistanceRight = measureDistance(RIGHT_TRIG_PIN, RIGHT_ECHO_PIN)
    print(i)
    print("Left:  ", currentTimeLeft, "\t", measuredDistanceLeft)
    print("Right: ", currentTimeRight, "\t", measuredDistanceRight)
    time.sleep(0.1)
