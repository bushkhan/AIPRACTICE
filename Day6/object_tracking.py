import cv2
import imutils

blackLower=(0,0,0)
blackUpper=(9360,255,50)

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)