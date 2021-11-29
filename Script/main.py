from MeasureSpeed import measureSpeed
from CaptureLicense import captureLicense
from LicenseDetect import licenseDetect

SPEED_LIMIT = 0  # speed limit 20 mile/h

detectedSpeed = measureSpeed()
if detectedSpeed > SPEED_LIMIT:
    captureTime, originalImagePath = captureLicense()
    captureTime, croppedImagePath = licenseDetect(captureTime, originalImagePath)
