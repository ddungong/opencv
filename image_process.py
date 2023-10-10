import cv2
import numpy as np


img = cv2.imread('C:/Users/kmg00/Desktop/apple.jpg')

print(format(img.shape[1])) #넓이
print(format(img.shape[0])) #높이
print(format(img.shape[2])) # 컬러 색상 갯수

(b,g,r)=img[0,0] # b g r 순서로 해야 함 이미지 0,0의 rgb를 가져온다
print(r,g,b)

(height,width)=img.shape[:2]
center=(width//2,height//2)

move=np.float32([[1,0,100],[0,1,100]])#up down의 100만큼 다운 right ,left 의 오른쪽으로 100만큼 움직임 +=up,right - down left
moved=cv2.warpAffine(img,move,(width,height))# width와 height의 크기만큼 움직임


move=cv2.getRotationMatrix2D(center,90,1.0)
rotation=cv2.warpAffine(img,move,(width,height))


ratio=200.0/width
dimension=(200,int(height*ratio))

resized=cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)

mask=np.zeros(img.shape[0:2],dtype='uint8')
cv2.circle(mask,center,300,(255,255,255),-1)

masked=cv2.bitwise_and(img,img,mask=mask)


(Blue,Green,Red)=cv2.split(img)

cv2.imshow('Red',Red)
cv2.imshow('Green',Green)
cv2.imshow('Blue',Blue)

zeros=np.zeros(img.shape[0:2],dtype='uint8')
cv2.imshow('Red1',cv2.merge([zeros,zeros,Red]))
cv2.imshow('Green1',cv2.merge([zeros,Green,zeros]))
cv2.imshow('Blue1',cv2.merge([Blue,zeros,zeros]))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",gray)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()