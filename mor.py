import cv2 as cv
import numpy as np

 

img = cv.imread('smarties.png', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((2, 2), np.uint8)
dialation = cv.dilate(mask, kernel, iterations=3)

cv.imshow('Image', img)
cv.imshow('Mask', mask)
cv.imshow('Dialation', dialation)

cv.waitKey(0)
cv.destroyAllWindows()