#first made on 2019.05.26, JAM
import random
import numpy as np

CREATE_POINTS_REGULAR_RANDOM = 0

def _regular_random_points(width, height, x_divider, y_divider):
    points = []
    x_interval = width /float(x_divider)
    y_interval = height /float(y_divider)

    for x_idx in range(x_divider):
        for y_idx in range(y_divider):
            x_range = [int(x_idx*x_interval), int((x_idx+1)*x_interval)]
            y_range = [int(y_idx*y_interval), int((y_idx+1)*y_interval)]
            x = random.randint(x_range[0], x_range[1])
            y = random.randint(y_range[0], y_range[1])
            points.append(( x if x<width else width-1, y if y<height else height-1  ))

    return points

def create_points(width, height, x_divider, y_divider, mode = CREATE_POINTS_REGULAR_RANDOM):
    points = []
    if(mode is CREATE_POINTS_REGULAR_RANDOM):
        points = _regular_random_points(width,height,x_divider,y_divider)

    return points