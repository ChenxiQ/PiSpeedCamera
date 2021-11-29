from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def captureLicense():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    camera.capture(rawCapture, format="bgr")
    capturedImage = rawCapture.array

    style = "%Y-%m-%d_%H:%M:%S"
    captureTime = str(time.strftime(style, time.localtime(time.time())))
    imagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "Original.jpg"

    cv2.imwrite(imagePath, capturedImage)

    return captureTime, imagePath
