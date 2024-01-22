import cv2

img = cv2.imread('../../Users/이영권/Downloads/09_detector&ml/09_detector&ml/img/shape.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 외곽선
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 찾은 외곽선을 화면에 그리기
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Shape Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()