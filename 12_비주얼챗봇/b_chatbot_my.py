import cv2
import openai
from datetime import datetime

openai.api_key = "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"
# 결과를 저장할 리스트
results = []

# 초기 객체 위치 설정을 위한 플래그
initBB = None

# OpenCV의 KCF 트래커 인스턴스 생성
tracker = cv2.TrackerKCF_create()

def get_gpt_response(x, y):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"얼굴은 좌표 ({x}, {y})에 위치하고 있습니다."}
      ]
    )
    return completion.choices[0].message['content']

# 웹캠 캡처
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if initBB:
        # 객체 추적
        (success, box) = tracker.update(frame)

        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # GPT-3.5 Turbo로부터 설명 받기
            response = get_gpt_response(x, y)
            print("GPT-3.5 Turbo Response:", response)
            results.append(response)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # 's'를 눌러 객체 위치 설정
    if key == ord("s"):
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        tracker.init(frame, initBB)

    # 'q'를 누르면 종료
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# 결과를 파일에 저장
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(f"res/{current_time}.txt", "w") as f:
    for result in results:
        f.write(f"{result}\n")
