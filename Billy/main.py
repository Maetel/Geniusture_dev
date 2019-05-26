import cv2 as cv
import numpy as np
import BGR_gradation as Bg
import image_brightness as ib

def make_empty_image(width, height, channels = 3):
    return np.zeros((height, width, channels),np.uint8)

def main():

    #1. create image
    path = "test_image.jpg"

    channels = 3

    width = 800
    height = 600
    buff = make_empty_image(width, height, channels)

    #2. make BGR gradation image
    Bg.BGR_gradation.fill_BGR_gradadation(buff)

    #3. change image brightness
    buff = cv.cvtColor(buff, cv.COLOR_BGR2GRAY)

    multiplier = 1.5
    adder = 30
    buff = ib.image_brightness(buff, multiplier, summer = adder)
    cv.imshow("after", buff)

    cv.waitKey(0)

if __name__=="__main__":
    main()