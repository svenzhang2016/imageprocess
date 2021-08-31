import cv2
import numpy as np
import matplotlib.pyplot as plt

#更改为需要的图片路径
img = cv2.imread(r'../DIP3E_Original_Images_CH03/Fig0314(a)(100-dollars).tif')
h,w = img.shape[0],img.shape[1]

#处理过程
new_img = np.zeros((h,w,8))
for i in range(h):
    for j in range(w):
        n = str(np.binary_repr(img[i,j,0],8))
        for k in range(8):
            new_img[i,j,k] = n[k]

#依次显示
for i in range(8):
    cv2.imshow('image',new_img[:,:,i])
    cv2.waitKey(0)