import cv2
import numpy as np


img = cv2.imread('C:/Users/kmg00/Desktop/apple.jpg')

print(format(img.shape[1])) #넓이
print(format(img.shape[0])) #높이
print(format(img.shape[2])) # 컬러 색상 갯수

(b,g,r)=img[0,0] # b g r 순서로 해야 함 이미지 0,0의 rgb를 가져온다
print(r,g,b)

dot=img[50:100,50:100] #가로 픽셀 50에서 100 세로픽셀 50에서 100 짤라서 보여줌


img[50:100,50:100]=(0,0,255) #가로 픽셀 50에서 100 세로픽셀 50에서 100 빨간색으로 채워줌

cv2.rectangle(img,(150,50),(200,100),(0,255,0),5)# 좌표를 이용한
cv2.circle(img,(275,75),25,(0,255,255),-1)
cv2.line(img,(350,100),(400,100),(255,0,0),5)
cv2.putText(img,'apple',(450,100),cv2.FONT_HERSHEY_SIMPLEX,-1,(255,255,255),4)
cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()