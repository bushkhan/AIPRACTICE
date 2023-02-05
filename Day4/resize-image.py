import cv2
import imutils

img = cv2.imread('../Resources/girl.png')

resizeImg = imutils.resize(img,width=25)
cv2.imwrite("ResizedImage.jpg",resizeImg)
