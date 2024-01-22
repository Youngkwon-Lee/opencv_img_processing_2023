import cv2
 #https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga89e7806b0a616f6f1d502bd8c183ad3e
title = 'mouse event'                   # 창 제목
img = cv2.imread('../img/bg.jpg') # 백색 이미지 읽기
cv2.imshow(title, img)

def onMouse(event, x, y, flags, param):
    print(event, x, y, )
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (0,0,0), -1)
        cv2.imshow(title, img)
    elif   event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 30, (0, 0, 255), -1)
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)


while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()