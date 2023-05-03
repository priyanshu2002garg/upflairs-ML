import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_.xml')
#vid=cv2.VideoCapture(0)
vid=cv2.VideoCapture(0)
while True:
    flag,img=vid.read()
    if flag:
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=fd.detectMultiScale(
           img_gray,
           scaleFactor=1.1,
           minNeighbors=5,
           minSize=(50,50)
        )
        np.random.seed(50)
        colors=[np.random.randint(0,255,3).tolist()
                for i in faces]
        i=0
        #th,img_bw=cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY)
        for x,y,w,h in faces:
        #x,y,w,h=(350,300,300,200)
        #img_cropped=img[y:y+h,x:x+w,:]
            cv2.rectangle(
                    img,pt1=(x,y), pt2=(x+w,y+h), color=colors[i],
                    thickness=8
                
            )
            i=i+1
        cv2.imwrite('myself.png',img)
        cv2.imshow('preview',img)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
     print('no frame')
     break
sleep(0.1)    
vid.release()
cv2.destroyAllWindows()