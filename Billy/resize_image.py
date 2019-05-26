#first made on 2019.05.26, JAM
import cv2 as cv

RESIZE_BY_SIZE = 0
RESIZE_BY_RATIO = 1

def resize_image(img, width, height, mode = RESIZE_BY_SIZE):
    if(mode is RESIZE_BY_SIZE):
        img = cv.resize(img, (height,width))
    elif(mode is RESIZE_BY_RATIO):
        img = cv.resize(img, (int(img.shape[0]*height), int(img.shape[1]*width)) )
    return img