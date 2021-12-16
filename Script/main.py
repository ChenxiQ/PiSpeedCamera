from MeasureSpeed import measureSpeed
from CaptureLicense import captureLicense
from LicenseDetect import licenseDetect
from LicenseOCR import licenseOCR
from AddOCRToDatabase import addOCRToDatabase
import time

import warnings
warnings.filterwarnings("ignore")

SPEED_LIMIT = 0  # speed limit 20 mile/h

detectedSpeed = measureSpeed()
if detectedSpeed > SPEED_LIMIT:
    startTime = time.time()
    captureTime, originalImagePath = captureLicense()
    captureTime, croppedImagePath = licenseDetect(captureTime, originalImagePath)
    detectedPlate = licenseOCR(captureTime, croppedImagePath)
    print("Total Processing Time:", round(time.time()-startTime, 2))
    addOCRToDatabase(detectedSpeed, detectedPlate)
