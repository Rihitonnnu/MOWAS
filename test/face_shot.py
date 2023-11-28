import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

# カメラを開く
cap = cv2.VideoCapture(0)

# 画像をキャプチャする
ret, frame = cap.read()

# 画像を保存する
cv2.imwrite("img/face.jpg", frame)

# カメラを閉じる
cap.release()
