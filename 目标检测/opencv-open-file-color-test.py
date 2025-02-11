#!/usr/bin/env python3

"""
File: opencv-open-file-color-test.py
 
This Python 3 code is published in relation to the article below:
https://www.bluetin.io/opencv/opencv-color-detection-filtering-python/
 
Website:    www.bluetin.io
Author:     Mark Heywood
Date:	    8/12/2017
Version     0.1.0
License:    MIT
"""

from __future__ import division
import cv2
import numpy as np

def nothing(*arg):
        pass

# Initial HSV GUI slider values to load on program start.
icol = (36, 202, 59, 71, 255, 255)    # Green
#icol = (18, 0, 196, 36, 255, 255)  # Yellow
#icol = (89, 0, 0, 125, 255, 255)  # Blue
#icol = (0, 100, 80, 10, 255, 255)   # Red
cv2.namedWindow('colorTest')
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'colorTest', icol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'colorTest', icol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'colorTest', icol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'colorTest', icol[3], 255, nothing)
cv2.createTrackbar('highSat', 'colorTest', icol[4], 255, nothing)
cv2.createTrackbar('highVal', 'colorTest', icol[5], 255, nothing)

# Raspberry pi file path example.
#frame = cv2.imread('/home/pi/python3/opencv/color-test/colour-circles-test.jpg')
# Windows file path example.
frame = cv2.imread(r"C:\Users\Maibenben\Desktop\product\buhegepin\20181029.jpg")

while True:
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'colorTest')
    lowSat = cv2.getTrackbarPos('lowSat', 'colorTest')
    lowVal = cv2.getTrackbarPos('lowVal', 'colorTest')
    highHue = cv2.getTrackbarPos('highHue', 'colorTest')
    highSat = cv2.getTrackbarPos('highSat', 'colorTest')
    highVal = cv2.getTrackbarPos('highVal', 'colorTest')

    # Show the original image.
    cv2.imshow('frame', frame)
    
    # Blur methods available, comment or uncomment to try different blur methods.
    frameBGR = cv2.GaussianBlur(frame, (7, 7), 0)
    #frameBGR = cv2.medianBlur(frame, 7)
    #frameBGR = cv2.bilateralFilter(frame, 15 ,75, 75)
    """kernal = np.ones((15, 15), np.float32)/255
    frameBGR = cv2.filter2D(frame, -1, kernal)"""
	
    # Show blurred image.
    cv2.imshow('blurred', frameBGR)
	
    # HSV (Hue, Saturation, Value).
    # Convert the frame to HSV colour model.
    frameHSV = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
    
    # HSV values to define a colour range we want to create a mask from.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    # Show the first mask
    cv2.imshow('mask-plain', mask)

    # Cleanup the mask with Morphological Transformation functions
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

    # Show morphological transformation mask
    cv2.imshow('mask', mask)
    
    # Put mask over top of the original image.
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # Show final output image
    cv2.imshow('colorTest', result)
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()

