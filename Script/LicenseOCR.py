import os
import re
import sqlite3 as lite
import sys

def licenseOCR(captureTime, imagePath):
    print("OCR Image", imagePath)
    cmd = "tesseract " + imagePath + " /home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_5OCRResult" + " -l eng -psm 7 >> /dev/null"
    os.system(cmd)

    OCRPath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_5OCRResult.txt"
    with open(OCRPath) as f:
        # read the OCR result into one line and remove spaces
        OCRMsg = f.read().replace(" ", "").replace("\n", "")
        
        # only preserve capital letters and digits
        detectedPlate = re.sub(u"([^\u0030-\u0039\u0041-\u005a])", "", OCRMsg)
    
    print("OCR Result:", detectedPlate)
    return detectedPlate
