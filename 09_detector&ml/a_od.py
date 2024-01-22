import cv2

# XML 파일을 로드하여 Haar Cascade 분류기 객체를 생성합니다.
face_cascade = cv2.CascadeClassifier(
    '../../Users/이영권/Downloads/09_detector&ml/09_detector&ml/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 분류기를 사용하여 얼굴을 감지합니다.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 감지된 각 얼굴에 대하여 Bounding Box를 그립니다.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y),  (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
