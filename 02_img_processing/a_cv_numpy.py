import numpy as np

# np.zeros() - 모든 값이 0인 배열 생성
zeros_array = np.zeros((3, 3))
print("Zeros Array:\n", zeros_array, "\n")

# np.ones() - 모든 값이 1인 배열 생성
ones_array = np.ones((3, 3))
print("Ones Array:\n", ones_array, "\n")

# np.full() - 모든 값이 특정 값으로 채워진 배열 생성
full_array = np.full((3, 3), 7)
print("Full Array with 7:\n", full_array, "\n")

# np.eye() - 단위 행렬 생성
eye_array = np.eye(3)
print("Eye Array:\n", eye_array, "\n")

# np.fliplr() - 행렬의 왼쪽과 오른쪽을 뒤집기
flipped_eye_array = np.fliplr(eye_array)
print("Flipped Eye Array:\n", flipped_eye_array, "\n")

# np.linspace() - 선형 간격의 배열 생성
linspace_array = np.linspace(0, 10, 5)
print("Linspace Array from 0 to 10 with 5 elements:\n", linspace_array, "\n")

# np.arange() - 주어진 간격으로 배열 생성
arange_array = np.arange(0, 10, 2)
print("Arange Array from 0 to 10 with step 2:\n", arange_array, "\n")
