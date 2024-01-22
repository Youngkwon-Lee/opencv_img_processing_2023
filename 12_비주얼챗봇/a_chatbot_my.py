import os
import cv2
import openai
from datetime import datetime

# OpenAI API 키 설정
openai.api_key = "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"
results = []
# Haar Cascade를 이용한 얼굴 인식을 위한 준비
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def get_gpt_response(face_count):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"프레임에 {face_count}개의 얼굴이 있습니다."}
      ]
    )
    return completion.choices[0].message['content']

# 웹캠 캡처
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # 얼굴 인식
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    face_count = len(faces)

    # 얼굴 영역에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # GPT-3.5 Turbo로부터 설명 받기
    response = get_gpt_response(face_count)
    print("GPT-3.5 Turbo Response:", response)
    results.append(response)

    # 결과 프레임 출력
    cv2.imshow('Frame', frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 결과를 파일에 저장
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(f"res/{current_time}.txt", "w") as f:
    for result in results:
        f.write(f"{result}\n")