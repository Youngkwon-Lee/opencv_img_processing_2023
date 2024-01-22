import cv2 as cv
import numpy as np

#200*200 사이즈의 빨강색으로 채운 이미지를 생성해 보자
#np.zeros() - 모든 값이 0인 배열 생성
blue_img = np.zeros((200, 200,3))
#빨강색으로 인덱스에 데이터를 저장해보자. BGR [0,0,255]
blue_img[:, :] = [255, 0, 0]  # 모든행 모든 열 [:, :]
blue_img[75:125 , 50:150] = [0, 0, 255]

cv.imwrite('img_res/blue_img', blue_img)

cv.imshow("red_img", blue_img)
cv.waitKey(0)
cv.destroyAllWindows()