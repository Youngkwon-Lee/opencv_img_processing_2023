# 사과이미지에  +50   -50 ,  *2 , /2
import cv2
import numpy as np
apple_image = cv2.imread('../img/apple.jpg')

#  + ,  -  = 밝기 조절
#  * , /  = 대비조절
add_img  =  cv2.add(apple_image, np.array([100.0]) )
sub_img  = cv2.subtract(apple_image, np.array([100.0])   )
mul_img  =cv2.multiply(apple_image, 2)
div_img = cv2.divide(apple_image, 2)
scaled_image = cv2.convertScaleAbs(div_img, alpha=2, beta=0)



cv2.imshow("add" , add_img)
cv2.imshow("sub" , sub_img)
cv2.imshow("mul" , mul_img)
cv2.imshow("div" , scaled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
