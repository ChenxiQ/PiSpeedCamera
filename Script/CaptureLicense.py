"""
    CaptureLiscense.py
    Created by Chenxi Qian

    capture the car image using Raspberry Pi Camera Rev 1.3
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def captureLicense():
    # capture an image using Raspberry Pi Camera
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    camera.capture(rawCapture, format="bgr")
    capturedImage = rawCapture.array

    # prepare image file name
    # all the image would be saved in the /ProcessImage directory
    style = "%Y-%m-%d_%H:%M:%S"
    captureTime = str(time.strftime(style, time.localtime(time.time())))
    imagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_0Original.jpg"

    # save the image
    cv2.imwrite(imagePath, capturedImage)

    return captureTime, imagePath
