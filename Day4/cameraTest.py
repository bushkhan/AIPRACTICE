import cv2
import time
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

time.sleep(1)
_,img = cam.read()
#returns two values 1 is true or false and other
#one is where we actually get the frame!

cv2.imwrite("../Resources/imagefromcamera.jpg",img)
cam.release()
cv2.destroyAllWindows()

