#!/usr/local/bin/python3
import cv2 as cv
import numpy as np

# Load the aerial image and convert to HSV colourspace
image = cv.imread("/home/fangchao/app/sport-block.jpg")
print("image", type(image))
hsv=cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([0,0, 175])
brown_hi=np.array([0,0, 215])

# Mask image to only select browns
mask=cv.inRange(hsv,brown_lo,brown_hi)

# Change image to red where we found brown
image[mask>0]=(255,255,255)

cv.imwrite("result.png",image)
