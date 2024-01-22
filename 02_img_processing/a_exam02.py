import cv2 as cv
import numpy as np

#1. 200*200 사이즈의 파랑색에 빨강색 사각형으로 채운 이미지를 생성해 보자
#2. 빨강색 추출해보자. 마스크를 생성해서 마스크값에 해당되면 추출해 보자.

#200*200 사이즈의 빨강색으로 채운 이미지를 생성해 보자
#np.zeros() - 모든 값이 0인 배열 생성
blue_img = np.zeros((200, 200,3))
#빨강색으로 인덱스에 데이터를 저장해보자. BGR [0,0,255]
blue_img[:, :] = [255, 0, 0]  # 모든행 모든 열 [:, :]
blue_img[75:125 , 50:150] = [0, 0, 255] # = BGR 빨간색 설정

#1.빨강색 범위를 BGR형식으로 정의
lower_red = np.array([0,0,200])
upper_red = np.array([50,50,255])
#2.범위에 해당되는 마스크 설정
mask = cv.inRange(blue_img , lower_red , upper_red  )
print(mask)

#3. 마스크를 사용해서 원본이미지에서 빨간색 부분만 추출
red_part = cv.bitwise_and(blue_img, blue_img, mask=mask)
red_part = red_part[75:125 , 50:150]

cv.imshow("red_img", red_part)
cv.imwrite('img_res/red_part.jpg', red_part)
cv.waitKey(0)
cv.destroyAllWindows()