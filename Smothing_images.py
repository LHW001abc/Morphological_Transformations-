import cv2 as cv
import numpy as np
 
img = cv.imread('early_1800.jpg', 0)

#average = cv.blur(img, (5, 5))
gaussian = cv.GaussianBlur(img, (5, 5), 0)
#cv.imshow('Average', average)
cv.imshow('Gaussian', gaussian)
cv.waitKey(0)
cv.destroyAllWindows()
