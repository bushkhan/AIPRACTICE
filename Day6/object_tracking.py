import cv2
import imutils

blackLower=(0,0,0)
blackUpper=(9360,255,50)

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _,frame = camera.read()
    frame = imutils.resize(frame,width=600)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)



