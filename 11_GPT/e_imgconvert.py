import cv2
import numpy as np
import os

# 이미지 파일 경로
file_path = 'sample_puppy.jpg'
output_path = 'puppy.png'

# 이미지를 OpenCV를 통해 불러옴
image = cv2.imread(file_path)

# PNG로 이미지 저장
cv2.imwrite(output_path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# 파일 크기 확인
file_size = os.path.getsize(output_path)
if file_size < 4 * 1024 * 1024:  # 4MB 미만인지 확인
    print("이미지가 PNG 형식으로 변환되고 4MB 미만입니다. 😡")  # 파일 크기가 요구 사항을 충족하지 못하는 경우
    # OpenAI API 호출 로직
else:
    # 파일 크기가 크면, 이미지 크기를 줄이는 등의 조치가 필요
    print("이미지 파일 크기를 조정해야 합니다.")

# 이미지 크기를 줄이는 추가적인 단계가 필요할 수 있음
# 예를 들어, 이미지의 해상도를 줄이는 경우:
scale_percent = 50  # 예를 들어, 원본 크기의 50%로 줄임
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# 리사이즈된 이미지를 저장
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite(output_path, resized, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# 파일 크기 재확인
file_size = os.path.getsize(output_path)
if file_size < 4 * 1024 * 1024:  # 재확인 후 4MB 미만인지
    print("이미지 크기 조정 후 4MB 미만입니다. 😉")  # 조건 충족시
    # OpenAI API 호출 로직
else:
    print("이미지가 여전히 너무 큽니다. 😡")
