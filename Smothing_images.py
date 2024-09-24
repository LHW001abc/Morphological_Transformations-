import cv2 as cv
import numpy as np
 
img = cv.imread('early_1800.jpg', 0)

#average = cv.blur(img, (5, 5))
gaussian = cv.GaussianBlur(img, (5, 5), 0)

median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral', bilateral)


cv.imshow('Image', img)
cv.imshow('Median', median)
#cv.imshow('Average', average)
cv.imshow('Gaussian', gaussian)
cv.waitKey(0)
cv.destroyAllWindows()
