# _*_ coding: utf-8 _*_
# @Time     : 2019/8/14 16:46
# @Author   : Ole211
# @Site     : 
# @File     : face_recognition.py    
# @Software : PyCharm

import os
import numpy as np
import cv2
import time


# 图片马赛克效果
def imageMosaic(img):
    w, h = img.shape[:2]
    step = 5
    for i in range(w - step):
        for j in range(h - step):
            if i % step == 0 and j % step == 0:
                for m in range(step):
                    for n in range(step):
                        img[i + m, j + n] = img[i, j]

    return img


# 人脸检测
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if len(faces) == 0:
        return None, None, None
    x, y, w, h = faces[0]
    return gray[y:y + w, x:x + h], faces[0], faces


def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dir_name in dirs:
        label = int(dir_name)
        subject_dir_path = data_folder_path + '/' + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            image_path = subject_dir_path + '/' + image_name
            image = cv2.imread(image_path)
            image = cv2.resize(image, (520, 340))
            cv2.imshow('Training on image...', image)
            cv2.waitKey(10)
            face, rect, _ = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels


def draw_rectangle(img, rect):
    x, y, w, h = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (150, 150, 0), 2)


def paint_chinese_opencv(img, chinese, position, fontsize, color):  # opencv输出中文
    from PIL import Image, ImageFont, ImageDraw
    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 图像从OpenCV格式转换成PIL格式
    font = ImageFont.truetype('./simhei.ttf', fontsize, encoding="utf-8")
    # color = (255,0,0) # 字体颜色
    # position = (100,100)# 文字输出位置
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, chinese, font=font, fill=color)  # PIL图片上打印汉字 # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    img = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)  # PIL图片转cv2 图片
    cv2.imshow('PIL_opencv', img)


def draw_text(img, text, x, y):
    paint_chinese_opencv(img, text, (x, y), 28, (0, 150, 150))

    # cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 0), 2 )


# subjects = ['帅斌', '帅旗', '子轩', '妈']
subjects = ['shuaibin', 'shuaiqi', 'zixuan', 'ma']


def predict(test_img):
    img = test_img.copy()
    _, _, faces = detect_face(img)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 150, 150), 5)
        face_rect = img[y:y + w, x:x + h]
        # 马赛克化
        face_rect = imageMosaic(face_rect)
        face_rect = cv2.cvtColor(face_rect, cv2.COLOR_BGR2GRAY)
        label = face_recognizer.predict(face_rect)
        label_text = subjects[label[0]]
        cv2.putText(img, label_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 0), 2)
        # draw_text(img, label_text, face[0], face[1] - 5)
    #     x, y, w, h = face
    #     rect = img[y:y+w, x:x+h]
    #     label = face_recognizer.predict(rect)
    #     label_text = subjects[label[0]]
    #     draw_rectangle(img, face)
    #     img = draw_text(img, label_text, face[0], face[1]-5)
    #     cv2.imshow('predict', img)

    return img


if __name__ == '__main__':
    faces, labels = prepare_training_data('./train_data/')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))

    # 预测
    test_images = [i for i in os.listdir('./test_data/') if i.endswith('.JPG') or i.endswith('.jpg')]
    print(test_images)
    for img in test_images:
        try:
            o = cv2.imread('./test_data/' + img)
            o = cv2.resize(o, (520, 340))
            im = predict(o)
            cv2.imshow(os.path.splitext(img)[0], im)
        except Exception as e:
            print(e)

    cv2.waitKey()
    cv2.destroyAllWindows()
