import cv2

# 이미지 불러오기
image = cv2.imread('../img/apple.jpg')

# 컬러 영상 (변경 없음)
color_image = image

# 회색조 영상
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진 영상
_, binary_image = cv2.threshold(grayscale_image, 128, 255, cv2.THRESH_BINARY)

# 인덱스 영상
indexed_image = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_JET)


cv2.imshow('Color Image', color_image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Indexed Image', indexed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
