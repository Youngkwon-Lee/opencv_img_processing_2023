'''
1. 사과 이미지를 채널 분리를 한다:
2. 레나 이미지를 채널 분리를 한다.

3. 두개의 이미지의 사이즈를 동일하게 조정한 후 사과의 B , 레나 R,  사과의 G
값을 병합해서 결과를 확인한다.
'''

import cv2 as cv
import matplotlib.pyplot as plt

im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')

if im1.shape != im2.shape:
    im2 = cv.resize(im2, (im1.shape[1], im1.shape[0]))

r1, g1, b1 = cv.split(im1)
r2, g2, b2 = cv.split(im2)

merged = cv.merge((r2, g1, b1))

cv.imshow("Merged Image", merged)

cv.waitKey(0)
cv.destroyAllWindows()