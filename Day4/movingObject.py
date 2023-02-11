import cv2
import time
import imutils
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

time.sleep(1)

firstFrame = None
area = 500

while True:
    _,img = cam.read()
    text = "Normal"

    img = imutils.resize(img,width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21,21),0)


    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        break

cam.release()
cv2.destroyAllWindows()

