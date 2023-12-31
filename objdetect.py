import  cv2
import  numpy as np

def detectAnDisplay(frame):
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray=cv2.equalizeHist(frame_gray)
    faces=face_cascade.detectMultiScale(frame_gray)
    for(x,y,w,h) in faces:
        center=(x+w//2,y+h//2)
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        faceROI=frame_gray[y:y+h,x:x+w]
        eyes=eyes_cascade.detectMultiScale(faceROI)
        for(x2,y2,w2,h2) in eyes:
            eye_center=(x+x2+w2//2,y+y2+h2//2)
            radius=int(round(w2+h2)*0.25)
            frame=cv2.circle(frame,eye_center,radius,(255,0,0),4)
        cv2.imshow('Capture',frame)
img=cv2.imread(r'C:\Users\kmg00\Desktop\image-20231011T114902Z-001\image\marathon_02.jpg')

(height,width)=img.shape[0:2]


cv2.imshow("Ori",img)

face_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'

face_cascade=cv2.CascadeClassifier()
eyes_cascade=cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('Error face')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('Error eyes')

detectAnDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
