#edg detection using   laplacian
import cv2 as cv
import numpy as np
img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F , ksize=3)
lap = np.uint8(np.absolute(lap))

cv.imshow('Image', img)
cv.imshow('Laplacian', lap)
cv.waitKey(0)
cv.destroyAllWindows()

#using sobelx sobely
import cv2 as cv
import numpy as np

img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
cv.imshow('Image', img)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.waitKey(0)
cv.destroyAllWindows()





