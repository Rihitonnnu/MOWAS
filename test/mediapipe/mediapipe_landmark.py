import cv2
import mediapipe as mp

# MediaPipeのFaceMeshモデルを初期化
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# MediaPipeのDrawingSpecを初期化（描画設定）
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# カメラを開く
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # BGR画像をRGBに変換
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 顔のランドマークを検出
    results = face_mesh.process(rgb_image)

    # 検出したランドマークを描画
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)

    # 画像を表示
    cv2.imshow('MediaPipe FaceMesh', frame)

    # 'q'キーでループから抜ける
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# カメラを閉じる
cap.release()
cv2.destroyAllWindows()
