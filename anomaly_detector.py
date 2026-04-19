
import cv2

cap = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    anomaly = False

    for (x, y, w, h) in faces:
        anomaly = True
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anomaly:
        cv2.putText(frame, "IRON MAN ALERT: THREAT DETECTED",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2)

    cv2.imshow("Anomaly Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
