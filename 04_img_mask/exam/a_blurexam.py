import numpy as np
import cv2

# 흰색 이미지 생성
image = np.ones((20, 20, 3), dtype=np.uint8) * 255

width, height = 5,5
kernel = np.ones((width, height), np.float32) / (width * height)
print(kernel)

filtered_image = cv2.filter2D(image, -1, kernel)
print(filtered_image)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

