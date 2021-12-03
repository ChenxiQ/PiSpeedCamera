import cv2
import numpy as np
import imutils

import glob

def sort(location):
    ySorted = sorted(location, key=(lambda x: x[1]))
    xSorted0 = sorted(ySorted[0:2], key=(lambda x: x[0]))
    xSorted1 = sorted(ySorted[2:4], key=(lambda x: x[0]))
    return xSorted0 + xSorted1

def licenseDetect(captureTime, imagePath):
    noiseReducedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_1NoiseReduced.jpg"
    edgedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_2Edged.jpg"
    croppedImagePath = "/home/pi/PiSpeedCamera/ProcessImage/" + captureTime + "_3Cropped.jpg"

    img = cv2.imread(imagePath)[540:1080, 0:1020]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) # Noise reduction
    cv2.imwrite(noiseReducedImagePath, bfilter)
    edged = cv2.Canny(bfilter, 30, 200) # Edge detection
    cv2.imwrite(edgedImagePath, edged)

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

        originalPoints = np.float32(sort([location[0][0], location[1][0], location[2][0], location[3][0]]))
        mappedPoints = np.float32([[0, 0], [800, 0], [0, 400], [800, 400]])
        transformMatrix = cv2.getPerspectiveTransform(originalPoints, mappedPoints)
        transformed = cv2.warpPerspective(img, transformMatrix, (800, 400))
        cv2.imwrite(croppedImagePath, transformed)
    
    except:
        return

for img in glob.glob(r"/home/pi/PiSpeedCamera/PiCameraImage/*.jpg"):
    licenseDetect(img[37:-4], img)

# tesseract /home/pi/PiSpeedCamera/ProcessImage/2021-11-30_19:16:22_3Cropped.jpg /home/pi/PiSpeedCamera/ProcessImage/ocr -l eng -psm 7
