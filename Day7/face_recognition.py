import numpy, os
import cv2
haar_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
datasets = 'datasets'
print("Training...")
(images, labels, names, id) = ([],[],{},0)

for(subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir

        subjectpath = os.path.join(datasets,subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
            print(labels)
        id +=1
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
print(images, labels)
(width,height) = (130,100)
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(images, labels)

webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cnt = 0

while True:
    (_,im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(im, (x,y), (x+w,y+h), (255,255,0), 2)

        faceOnly = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(faceOnly,(width,height))

        prediction = recognizer.predict(face_resize)
        cv2.rectangle(im, (x,y), (x + w, y+ h), (0, 255, 0), 3)
        if prediction[1]<800:
            cv2.putText(im,'%s - %.0f' % (names[prediction[0]], prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 255))
            cnt = 0
        else:
            cnt +=1
            cv2.putText(im,'Unknown', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 0, 255))
            if(cnt>100):
                cv2.imwrite("unknown.jpg",im)
                cnt = 0
    cv2.imshow('FaceRecognition',im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
