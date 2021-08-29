import math
import numpy as np
import cv2

img = cv2.imread(r'../DIP3E_Original_Images_CH03/Fig0304(a)(breast_digital_Xray).tif', 1)
cv2.imshow("raw img", img)
img = 255 - img
cv2.imshow("new img", img)
cv2.waitKey(0)
