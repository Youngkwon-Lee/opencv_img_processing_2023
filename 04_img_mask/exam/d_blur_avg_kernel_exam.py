import cv2
import numpy as np

img = cv2.imread('../../img/apple.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1/4, 1/4],
                    [1/4, 1/4]] )
# 필터 적용
blured = cv2.filter2D(img, -1, kernel)

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('avrg blur', blured)
cv2.waitKey()
cv2.destroyAllWindows()