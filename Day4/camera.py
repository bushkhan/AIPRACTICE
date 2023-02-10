import cv2
import time
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

time.sleep(1)

while True:
    _,img = cam.read()
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        break

cam.release()
cv2.destroyAllWindows()

