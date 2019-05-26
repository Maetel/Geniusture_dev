import cv2 as cv
import numpy as np
import BGR_gradation as Bg
import image_brightness as ib
import color_convergence as cc
import resize_image as ri
import random_convergence as rc
import create_points as cp

def make_empty_image(width, height, channels = 3):
    return np.zeros((height, width, channels),np.uint8)

def main():

    #1. create image
    path = "test_image.jpg"

    channels = 3

    width = 800
    height = 600
    image = make_empty_image(width, height, channels)

    #2. make BGR gradation image
    Bg.BGR_gradation.fill_BGR_gradadation(image)

    #3. change image brightness
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    multiplier = 1.5
    adder = 30
    gray = ib.image_brightness(gray, multiplier, summer = adder)
    #cv.imshow("brightness change", gray)

    #4, 5. converge colors & resize image
    image = cv.imread("lena.jpg")
    step = 70;
    image = cc.color_convergence(image, step)
    resize_ratio = 0.3; resize_width = 800; resize_height = 600
    #image = ri.resize_image(image, resize_ratio, resize_ratio, mode = ri.RESIZE_BY_RATIO)
    image = ri.resize_image(image, resize_width, resize_height, mode = ri.RESIZE_BY_SIZE)
    #cv.imshow("color convergence", image)

    #6. random convergence
    image = make_empty_image(width, height, channels)

    divider = 100
    points = cp.create_points(width, height, divider, divider)

    subdiv = cv.Subdiv2D((0,0,image.shape[1], image.shape[0]));

    for p in points: subdiv.insert(p)
    image = rc.draw_voronoi(image, subdiv)
    cv.imshow("rc", image)

    cv.waitKey(0)

if __name__=="__main__":
    main()