import cv2
import numpy as np

# 이미지를 불러옵니다.
image = cv2.imread('your_image_path.jpg')


# 원본 이미지의 특정 위치 좌표
pts1 = np.float32([[0,0], [1,0], [0,1]])


pts2 = np.float32([[0,0], [1,1], [1,0]])

# 변환 행렬을 구합니다.
matrix = cv2.getAffineTransform(pts1,pts2)

result = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow('Transformed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
