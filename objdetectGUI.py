import cv2
import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

# Haar cascade 파일 경로 설정
face_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'
# 초기 이미지 파일 및 기본 설정
file_name = r'C:\Users\kmg00\Desktop\image-20231011T114902Z-001\image\marathon_01.jpg'
title_name = 'Haar cascade object detection'
frame_width = 500


def selectFile():
    # 파일 대화상자를 사용하여 이미지 파일 선택
    file_name = filedialog.askopenfilename(initialdir="./image", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print('File name : ', file_name)
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    read_image = cv2.resize(read_image, dimension, interpolation=cv2.INTER_AREA)
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detectAndDisplay(read_image)


def detectAndDisplay(frame):
    # 얼굴 및 눈을 감지하고 그 결과를 GUI에 표시
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # -- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:

        center = (x + w // 2, y + h // 2)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y + h, x:x + w]
        # -- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
    # cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detection.config(image=imgtk)
    detection.image = imgtk

# 메인 GUI 생성
main = Tk()
main.title(title_name)
main.geometry()

read_image = cv2.imread(r'C:\Users\kmg00\Desktop\image-20231011T114902Z-001\image\marathon_01.jpg')
(height, width) = read_image.shape[:2]
# 초기 이미지 로드 및 크기 조절
ratio = frame_width / width
dimension = (frame_width, int(height * ratio))
read_image = cv2.resize(read_image, dimension, interpolation=cv2.INTER_AREA)

image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(image=image)

# Haar cascade 분류기 로드
face_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_cascade_name=r'C:\Users\kmg00\PycharmProjects\opencv\venv\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

# -- 1. Load the cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
# GUI 요소 (라벨, 스핀박스, 버튼 등) 설정
label = Label(main, text=title_name)
label.config(font=("Courier", 18))
label.grid(row=0, column=0, columnspan=4)
sizeLabel = Label(main, text='Frame Width : ')
sizeLabel.grid(row=1, column=0)
sizeVal = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal, from_=0, to=2000, increment=100, justify=RIGHT)
sizeSpin.grid(row=1, column=1)
Button(main, text="File Select", height=2, command=lambda: selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))
detection = Label(main, image=imgtk)
detection.grid(row=2, column=0, columnspan=4)
detectAndDisplay(read_image)

# 메인 GUI 이벤트 루프 실행
main.mainloop()



