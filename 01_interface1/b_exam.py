import cv2
img_file = "../img/apple.jpg"

def ImRead_attr():
    for attr in dir(cv2):
        if 'IMREAD' in attr:
            print(f"{attr} = {getattr(cv2, attr)} ")
            img = cv2.imread(img_file, getattr(cv2, attr))
            cv2.imshow('IMG', img)
            cv2.waitKey()

def Imwrite_attr():
    for attr in dir(cv2):
        if 'IMWRITE' in attr:
            print(f"{attr} = {getattr(cv2, attr)} ")

if __name__ == '__main__':
    ImRead_attr()
    #Imwrite_attr()