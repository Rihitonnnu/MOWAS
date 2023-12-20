import cv2

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

# カスケード分類器の読み込み
face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_alt2.xml')

# 画像の取得と処理
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 画像を保存
cv2.imwrite('face.jpg', frame)

# カメラのキャプチャを終了
cap.release()
