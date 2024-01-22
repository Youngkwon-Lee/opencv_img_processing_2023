# 4-3    높이가  다른 이미지를 가로로 연결해보자   cv.hconcat()
import cv2 as cv

im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')




im_h = cv.hconcat([im1, im2, im1])

cv.imshow("res", im_h)
cv.waitKey(0)
cv.destroyAllWindows()

