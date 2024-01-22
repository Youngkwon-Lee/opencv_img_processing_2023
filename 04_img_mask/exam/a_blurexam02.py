#이미지를 읽어서 각 RGB에 해당하는 픽셀값을 파일에 데이터를 저장한다.
import cv2
file_name= '../../img/apple.jpg'
pic=cv2.imread(file_name)
h,w=pic.shape[:2]
pic=cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
RGB=['../res/R.txt','../res/G.txt','../res/B.txt']
for k in range(3):
    txt=open(RGB[k],'w')
    array=pic[:,:,k]
    for j in range(h):
        for i in range(w):
            txt.write(str(array[j,i])+' ')
        txt.write('\n')
    txt.close()