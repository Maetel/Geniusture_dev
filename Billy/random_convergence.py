#first made on 2019.05.26, JAM
import cv2
import numpy as np
import random


# Draw voronoi diagram from below link
#https://www.learnopencv.com/delaunay-triangulation-and-voronoi-diagram-using-opencv-c-python/
def draw_voronoi(img, subdiv):
    (facets, centers) = subdiv.getVoronoiFacetList([])

    for i in range(len(facets)):
        ifacet_arr = []
        for f in facets[i]:
            ifacet_arr.append(f)

        ifacet = np.array(ifacet_arr, np.int)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        cv2.fillConvexPoly(img, ifacet, color, cv2.LINE_AA, 0);
        ifacets = np.array([ifacet])
        cv2.polylines(img, ifacets, True, (0, 0, 0), 1, cv2.LINE_AA, 0)
        #cv2.circle(img, (centers[i][0], centers[i][1]), 3, (0, 0, 0), -1, cv2.LINE_AA, 0)
    return img