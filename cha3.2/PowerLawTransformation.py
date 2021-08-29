import math
import numpy as np
import cv2

def gammaTransform(c,gamma, image):
    h,w,d = image.shape[0], image.shape[1], image.shape[2],
    new_img = np.zeros((h,w,d),dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j,0] = c*math.pow(image[i,j,0], gamma)
            new_img[i,j,1] = c*math.pow(image[i,j,1], gamma)
            new_img[i,j,2] = c*math.pow(image[i,j,2], gamma)
    cv2.normalize(new_img,new_img,0,255,cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    return new_img

img = cv2.imread(r'../DIP3E_Original_Images_CH03/Fig0309(a)(washed_out_aerial_image).tif', 1)
cv2.imshow("raw img", img)
new_img = gammaTransform(1,4,img)
cv2.imshow('new img',new_img)
cv2.waitKey(0)