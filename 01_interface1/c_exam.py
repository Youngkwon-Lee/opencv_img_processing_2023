import cv2  as cv   # -  as   별칭      :    cv2모듈을  cv라는 별칭으로 사용하겠다.

img_file = "../img/apple.jpg" # 표시할 이미지 경로
img_dec = cv.imread(img_file ,cv.IMREAD_UNCHANGED)  # 이미지를 읽어서 img 변수에 할당
img= cv.cvtColor(img_dec,cv.COLOR_RGB2YCrCb)

if img is not None:
  cv.imshow('MyImg', img)   # 읽은 이미지를 화면에 표시
  cv.waitKey()           # 키가 입력될 때까지 대기
  cv.destroyAllWindows()  # 창 모두 닫기
else:
    print('No image file.')


#   'scn' is 1  -> 입력 이미지  채널확인
#   'dcn'       -> 출력 이미지   채널확인