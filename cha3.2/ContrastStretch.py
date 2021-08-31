import cv2
import numpy as np

image = cv2.imread(r'../DIP3E_Original_Images_CH03/Fig0310(b)(washed_out_pollen_image).tif')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 在灰度图进行分段线性对比度拉伸
# 此种方式变换函数把灰度级由原来的线性拉伸到整个范围[0, 255]
r_min, r_max = 255, 0
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if gray_img[i, j] > r_max:
            r_max = gray_img[i, j]
        if gray_img[i, j] < r_min:
            r_min = gray_img[i, j]
r1, s1 = r_min, 0
r2, s2 = r_max, 255

precewise_img = np.zeros((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
k1 = s1 / r1
k3 = (255 - s2) / (255 - r2)
k2 = (s2 - s1) / (r2 - r1)
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if r1 <= gray_img[i, j] <= r2:
            precewise_img[i, j] = k2 * (gray_img[i, j] - r1)
        elif gray_img[i, j] < r1:
            precewise_img[i, j] = k1 * gray_img[i, j]
        elif gray_img[i, j] > r2:
            precewise_img[i, j] = k3 * (gray_img[i, j] - r2)

cv2.imshow('origin image', image)
cv2.imshow('precewise image', precewise_img)
cv2.waitKey(0)