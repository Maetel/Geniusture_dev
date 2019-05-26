#first made on 2019.05.26, JAM
import numpy as np

def color_convergence(img, step = 16):
     return ((img//step)*step)+(step//2)
