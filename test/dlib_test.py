import cv2
import dlib
import numpy as np

# 顔検出器とランドマーク検出器を初期化します
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('dlib/shape_predictor_68_face_landmarks.dat')

# 画像を読み込みます
img = cv2.imread('img/face.jpg')

# 画像をグレースケールに変換します
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔を検出します
faces = detector(gray)

for face in faces:
    # ランドマークを検出します
    landmarks = predictor(gray, face)

    # ランドマークを描画します
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(img, (x, y), 1, (255, 0, 0), -1)

# 画像を表示します
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
