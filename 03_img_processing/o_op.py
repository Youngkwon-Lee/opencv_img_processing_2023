# 사과이미지에 +50 -50 *2 /2


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

apple_image = cv.imread('../img/apple.jpg')


# +, - = 밝기 조절
# *, / = 대비 조절

add_img = cv.add(apple_image, np.array([50.0]))

sub_img = cv.subtract(apple_image, np.array([50.0]))

mul_img = cv.multiply(apple_image, 2)

div_img = cv.divide(apple_image, 2)

cv.imshow("add_img", add_img)
cv.imshow("sub_img", sub_img)
cv.imshow("mul_img", mul_img)
cv.imshow("div_img", div_img)

cv.waitKey(0)
cv.destroyAllWindows()

