import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/trail.jpg')
histogram = []

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    histogram.append(histr[:, 0])
    plt.plot(histr,color = col)
    plt.xlim([0,256])



print("==== B ====")
print(histogram[0])
print("==== G ====")
print(histogram[1])
print("==== R ====")
print(histogram[2])

plt.title('Wall Image')
plt.show()
