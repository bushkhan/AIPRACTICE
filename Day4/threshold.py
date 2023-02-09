import cv2
import imutils
img = cv2.imread('../Resources/girl.png')
grayImg = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
threshImg = cv2.threshold(grayImg,120,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("../Resources/ThresholdImg.jpg", threshImg)

