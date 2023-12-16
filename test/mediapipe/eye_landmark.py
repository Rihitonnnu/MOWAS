import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe's FaceMesh model
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Initialize MediaPipe's DrawingSpec (drawing settings)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Open the camera
cap = cv2.VideoCapture(0)

# 現在のカメラの解像度を取得
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'frame_width: {frame_width}')
print(f'frame_height: {frame_height}')

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Convert BGR image to RGB
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face landmarks
        results = face_mesh.process(rgb_image)

        # Draw the detected landmarks and calculate eyelid distances
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, c = frame.shape
                for id, lm in enumerate(face_landmarks.landmark):
                    # Eye landmarks have IDs from 33 to 145
                    if 33 <= id <= 145:
                        x, y = int(lm.x * w), int(lm.y * h)
                        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                # Calculate the distance between upper and lower eyelids for left eye
                left_eye_top = np.array(
                    [face_landmarks.landmark[159].x * w, face_landmarks.landmark[159].y * h])
                left_eye_bottom = np.array(
                    [face_landmarks.landmark[145].x * w, face_landmarks.landmark[145].y * h])
                left_eye_distance = np.linalg.norm(
                    left_eye_top - left_eye_bottom)

                # Calculate the distance between upper and lower eyelids for right eye
                right_eye_top = np.array(
                    [face_landmarks.landmark[386].x * w, face_landmarks.landmark[386].y * h])
                right_eye_bottom = np.array(
                    [face_landmarks.landmark[374].x * w, face_landmarks.landmark[374].y * h])
                right_eye_distance = np.linalg.norm(
                    right_eye_top - right_eye_bottom)

                # Display the distances on the frame
                cv2.putText(frame, f"Left eye distance: {left_eye_distance}", (
                    10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Right eye distance: {right_eye_distance}", (
                    10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the image
        cv2.imshow('MediaPipe FaceMesh', frame)

        # Exit the loop when 'q' key is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Release the camera and destroy OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
