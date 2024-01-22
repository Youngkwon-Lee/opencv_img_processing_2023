import cv2  as cv   # -  as   별칭      :    cv2모듈을  cv라는 별칭으로 사용하겠다.

img_file = "../img/Lenna.png" # 표시할 이미지 경로
img = cv.imread(img_file,-1)  # 이미지를 읽어서 img 변수에 할당

#print(img)
#print(type(img))
print(dir(img))
(h,w,ch) =img.shape
print(f"{h} , {w} , {ch}")
print(len(img.shape))
cv.imwrite("res.jpg", img)