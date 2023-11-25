# cv2のインポート前にカメラに関する設定を行う
# https://github.com/opencv/opencv/issues/17687
import sys
import time as pf_time
import cv2
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"


cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('xml/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
# 瞬目回数
wink_count = 0

start = pf_time.perf_counter()
wink_flg = False

while True:
    ret, rgb = cap.read()

    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray, scaleFactor=1.11, minNeighbors=3, minSize=(100, 100))

    if len(faces) == 1:
        x, y, w, h = faces[0, :]
        # 四角形描画
        cv2.rectangle(rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 処理高速化のために顔の上半分を検出対象範囲とする
        eyes_gray = gray[y: y + int(h/2), x: x + w]
        eyes = eye_cascade.detectMultiScale(
            eyes_gray, scaleFactor=1.11, minNeighbors=3, minSize=(8, 8))

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(rgb, (x + ex, y + ey), (x + ex +
                          ew, y + ey + eh), (255, 255, 0), 1)

        # 瞬目回数を測定する際に複数回加算してしまうのを防ぐためフラグを用いている
        if len(eyes) == 1:
            wink_flg = False

        # 目が認識されなくなった時
        if len(eyes) == 0:
            if not wink_flg:
                wink_count += 1
                print("count!")
                wink_flg = True

    cv2.imshow('frame', rgb)
    key = cv2.waitKey(10)
    end = pf_time.perf_counter()
    if end-start >= 10:
        break

print(wink_count)
# メモリを解放して終了するためのコマンド
cap.release()
cv2.destroyAllWindows()
