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
 

