import cv2
import numpy as np


txt=np.loadtxt('../res/B.txt')
max_val=np.amax(txt)
txt=txt/max_val*255
txt=txt.astype('uint8')


cv2.imwrite('../res/output.jpg',txt)