from MeasureSpeed import measureSpeed
from CaptureLicense import captureLicense
from LicenseDetect import licenseDetect
from LicenseOCR import licenseOCR
from AddOCRToDatabase import addOCRToDatabase

SPEED_LIMIT = 0  # speed limit 20 mile/h

detectedSpeed = measureSpeed()
if detectedSpeed > SPEED_LIMIT:
    captureTime, originalImagePath = captureLicense()
    captureTime, croppedImagePath = licenseDetect(captureTime, originalImagePath)
    detectedPlate = licenseOCR(captureTime, croppedImagePath)
    addOCRToDatabase(detectedSpeed, detectedPlate)
