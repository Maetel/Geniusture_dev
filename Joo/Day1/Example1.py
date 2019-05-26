import cv2 as cv
import numpy as np

path = "testImage.jpg"

width = 800
height = 600
buff = np.zeros((height, width, 3), np.uint8) # BGR이므로 3차원인 가로세로 배열이다. 모든 값에 0을 넣는다.

print(np.shape(buff)) # (행:600,열:800,높이:3)이다.
print(np.shape(buff[0]))
print(np.shape(buff[:, : width//3]))
buff[:, width//3 : width] = (100,150,255) #★★★ 각각 한 필셀에 (100,150,255) 값이 들어간거다!! 이것만 기억하면 됨
print(np.shape(buff[:, width//3 : width]))

for i in range(0,2) :
    for j in range(0, width) :
        if ( i == 0) :
            buff[:, j: width // 2 * (j + 1)] = (j*255/400 - j, 0, 0)
        else :
            buff[:, width // 2 + j : width // 2 * (j + 1)] = (0, j*255/400, 0)

# for i in range(0, width) :
#     buff[:, i] = (255 - i * 255 / 800, i * 255 / 800, 0)

# for i in range(0,3) :
#     for j in range(0, width) :
#         if ( i == 0) :
#             buff[:, j: width // 3 * (j + 1)] = (j*255/400 - j, 0, 0)
#         elif ( i == 1) :
#             buff[:, width // 3  * i + j : width // 3 * i + j+1] = (j * 255 / 400 - j, 0, 0)
#         else :
#             buff[:, width // 3 + j : width // 3 * (j + 1)] = (0, j*255/400, 0)


cv.imwrite(path, buff)
j