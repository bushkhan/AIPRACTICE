import cv2

img = cv2.imread("Resources/girl.png")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",grayImg)

cv2.waitKey(0)