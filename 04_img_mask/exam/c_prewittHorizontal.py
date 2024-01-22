import numpy as np

image_5x5 = np.array([[5, 10, 15, 20, 25],
                      [30, 35, 40, 45, 50],
                      [55, 60, 65, 70, 75],
                      [80, 85, 90, 95, 100],
                      [105, 110, 115, 120, 125]])

prewitt_horizontal = np.array([[-1, 0, 1],
                               [-1, 0, 1],
                               [-1, 0, 1]])


output_5x5 = np.zeros_like(image_5x5)

for i in range(1, image_5x5.shape[0] - 1):
    for j in range(1, image_5x5.shape[1] - 1):
        sub_matrix = image_5x5[i-1:i+2, j-1:j+2]
        output_5x5[i, j] = np.sum(prewitt_horizontal * sub_matrix)

print(output_5x5)
