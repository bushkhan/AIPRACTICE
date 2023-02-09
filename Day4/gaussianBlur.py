import cv2
import imutils
img = cv2.imread('../Resources/girl.png')
gaussianBlurImg = cv2.GaussianBlur(img, (21,21),0)
cv2.imwrite("../Resources/gaussianImage.jpg",gaussianBlurImg)
