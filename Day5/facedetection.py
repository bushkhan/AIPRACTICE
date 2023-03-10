import cv2
import os

dataset = "dataset"
name = "champ"
path = os.path.join(dataset,name)
if not os.path.isdir(path):
    print(path)
    os.makedirs(path,exist_ok=True)

(width,height) = (130,100)


alg = 'haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

count = 1

while count < 31:
    print(count)
    _,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in face:
        cv2.rectangle( img, (x,y), (x+w,y+h), (0,255,0), 2)

        faceOnly = gray[y:y+h, x:x+w]
        resizeimg = cv2.resize(faceOnly,(width,height))

        cv2.imwrite("%s/%s.jpg" %(path,count),resizeimg)
        count+=1

    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image captured")
cam.release()
cv2.destroyAllWindows()

