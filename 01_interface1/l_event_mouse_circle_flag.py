import cv2

title = 'mouse event'                   # 창 제목
img = cv2.imread('../img/bg.jpg') # 백색 이미지 읽기
cv2.imshow(title, img)                  # 백색 이미지 표시

colors = {'black':(0,0,0),
         'red' : (0,0,255),
         'blue':(255,0,0),
         'green': (0,255,0) } # 색상 미리 정의

def onMouse(event, x, y, flags, param): # 콜백 함수 구현
    print(event, x, y, flags)                # 파라미터 출력
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누름인 경우
        # 컨트롤키와 쉬프트 키를 모두 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY : 
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : # 쉬프트 키를 누른 경우
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY : # 컨트롤 키를 누른 경우
            color = colors['red']
        # 지름 30 크기의 검은색 원을 해당 좌표에 그림
        cv2.circle(img, (x,y), 30, color, -1) 
        cv2.imshow(title, img)          # 그려진 이미지를 다시 표시

cv2.setMouseCallback(title, onMouse)    # title 이란 창에다가 마우스이벤트를 onmouse를 통해서 진행을 함.

while True:
    if cv2.waitKey(0) & 0xFF == 27:     # esc로 종료
        break
cv2.destroyAllWindows()