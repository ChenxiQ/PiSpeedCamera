"""
    LicenseDetect.py
    Created by Chenxi Qian and Kuan Lu

    detect the license plate and crop corresponding area as output
"""

import cv2
import numpy as np
import imutils

### import used for test code ###
import glob
from LicenseOCR import licenseOCR
#################################

# helper sort function
# given four (x, y) coordinate points
# sort four points in the following order
# A -> B -> C -> D
# ------------------
# ----A--------C----
# ----|        |----
# ----|        |----
# ----B--------D----
# ------------------
def sort(location):
    ySorted = sorted(location, key=(lambda x: x[1]))
    xSorted0 = sorted(ySorted[0:2], key=(lambda x: x[0]))
    xSorted1 = sorted(ySorted[2:4], key=(lambda x: x[0]))
    return xSorted0 + xSorted1

def licenseDetect(captureTime, imagePath):
    # prepare intermediate image file name and path
    originalPath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_0Original.jpg"
    noiseReducedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_1NoiseReduced.jpg"
    edgedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_2Edged.jpg"
    transformedPath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_3Transformed.jpg"
    croppedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_4Cropped.jpg"

    # crop the captured image to reduce computation
    img = cv2.imread(imagePath)[400:1024, :]
    cv2.imwrite(originalPath, img)
    
    # convert color to grayscale and perform noise reduction
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert color
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) # Noise reduction
    cv2.imwrite(noiseReducedImagePath, bfilter)

    # edge detection using canny filter
    edged = cv2.Canny(bfilter, 30, 200)
    cv2.imwrite(edgedImagePath, edged)

    # find rectangles from the image
    # trying to match the area of a license plate
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    try:
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break

        # transform the titled rectangle to a vertical horizontal rectangle
        originalPoints = np.float32(sort([location[0][0], location[1][0], location[2][0], location[3][0]]))
        mappedPoints = np.float32([[0, 0], [800, 0], [0, 400], [800, 400]])
        transformMatrix = cv2.getPerspectiveTransform(originalPoints, mappedPoints)
        # transformed = cv2.warpPerspective(img, transformMatrix, (800, 400))[95:305, 0:800]  # parameter used for real road test
        transformed = cv2.warpPerspective(img, transformMatrix, (800, 400))[95:305, 30:770]  # parameter used for lab test environment
        cv2.imwrite(transformedPath, transformed)
        transformedGray = cv2.cvtColor(transformed, cv2.COLOR_BGR2GRAY)
        
        # histogram equalization and final color convert
        equalized = cv2.equalizeHist(transformedGray)
        # _, cropped = cv2.threshold(equalized, 60, 255, cv2.THRESH_BINARY)  # parameter used for real road test
        _, cropped = cv2.threshold(equalized, 40, 255, cv2.THRESH_BINARY)  # parameter used for lab test environment
        cv2.imwrite(croppedImagePath, cropped)
        return captureTime, croppedImagePath
    
    except:
        return

################################# TEST CODE #################################

# for img in glob.glob(r"/home/pi/PiSpeedCamera/PiCameraImage/*.jpg"):
#     capturedTime, croppedImagePath = licenseDetect(img[37:-4], img)
#     licenseOCR(capturedTime, croppedImagePath)

#############################################################################
