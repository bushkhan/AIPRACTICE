from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    success, frame = cam.read()
    frame1 = er.recognise_emotion(frame, return_type='BGR')
    print(frame1)
    cv2.imshow('frame',frame1)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()