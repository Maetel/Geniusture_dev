import cv2
import numpy as np


def brightnessMuli(picture, ratio) :
    weightLength = np.shape(picture)[0]
    heightLength = np.shape(picture)[1]
    changePicture = (np.clip(picture * ratio, 0 , 255)).astype(np.uint8)
    # print(changePicture)

    # changePicture.astype(np.uint8)

    print(changePicture)



    return changePicture


# cap = cv2.VideoCapture('testHand.mp4')
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

fname = './okinawa.jpg'

original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

original = cv2.resize(original, (960, 540))

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# original = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)

# cv2.imshow('Original', original)
# cv2.imshow('Gray', gray)
# cv2.imshow('Unchange', unchange)

print(np.shape(original))
# print(original[0])
# print(original[0] * 2)
# print(original[0] > 240)
# # original[0,0,0] = 256;
# print(original[0,0,0])

original = brightnessMuli(original, 0.8);
# print(original)
cv2.imshow('Original', original)


cv2.waitKey(0)
cv2.destroyAllWindows()
