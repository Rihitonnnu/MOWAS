import cv2
import datetime

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 現在の日時でファイルを作成
now = datetime.datetime.now()
filename = now.strftime('%Y%m%d_%H%M%S')
out = cv2.VideoWriter('face_image/'+filename + '.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Write the captured frame into the video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video writer, video capture, and destroy any open windows
out.release()
cap.release()
cv2.destroyAllWindows()
