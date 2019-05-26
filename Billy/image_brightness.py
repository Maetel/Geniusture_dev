#first made on 2019.05.26, JAM

import numpy as np

def image_brightness(img, multiplier = 1.0, summer = 0.0, max_intensity = 255, min_intensity = 0 ):
    img = img.astype(float)
    return np.clip( \
        (img*multiplier) + summer,\
        min_intensity, max_intensity).astype(np.uint8)