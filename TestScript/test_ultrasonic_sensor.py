import RPi.GPIO as GPIO
import time

def measureDistance():
    TRIG_PIN = 23
    ECHO_PIN = 24
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    GPIO.output(TRIG_PIN, False)
    # time.sleep(2)

    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = int(pulse_duration * 17150)
    print("Distance", distance, "cm")

    GPIO.cleanup()

for _ in range(1000):
    measureDistance()
    time.sleep(0.01)
