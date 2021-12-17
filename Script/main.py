"""
    main.py
    Created by Chenxi Qian and Kuan Lu

    main function to start the program
    currently needs one start for each speed test
    loop version in future work
"""

from MeasureSpeed import measureSpeed
from CaptureLicense import captureLicense
from LicenseDetect import licenseDetect
from LicenseOCR import licenseOCR
from AddOCRToDatabase import addOCRToDatabase

# SPEED_LIMIT = 20  # speed limit 20 mile/h
SPEED_LIMIT = 0  # debug mode, assuming all cars over speeding

# measure the speed of car
detectedSpeed = measureSpeed()

# if the car is over speeding
# capture the license plate and add to the website database
if detectedSpeed > SPEED_LIMIT:
    captureTime, originalImagePath = captureLicense()
    captureTime, croppedImagePath = licenseDetect(captureTime, originalImagePath)
    detectedPlate = licenseOCR(captureTime, croppedImagePath)
    addOCRToDatabase(detectedSpeed, detectedPlate)
