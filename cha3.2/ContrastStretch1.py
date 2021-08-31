import cv2
import numpy as np

image = cv2.imread(r'../DIP3E_Original_Images_CH03/Fig0312(a)(kidney).tif')
cv2.imshow('origin image', image)

shape = image.shape
height = shape[0]
width = shape[1]
channels = shape[2]
for row in range(height):
    for col in range(width):
        for cn in range(channels):
            pv = image[row,col,cn]
            if pv > 120:
                pv = 255
                image[row,col,cn] = pv
            else:
                pv = 30
                image[row,col,cn] = pv

cv2.imshow('new image', image)
cv2.waitKey(0)
