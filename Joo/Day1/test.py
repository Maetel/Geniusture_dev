import cv2
import numpy as np

# 사진의 밝기조절을 하는 함수
# picture는 imread로 읽은 변수, ratio는 밝기 조절을 하고 싶은 비율을 입력한다. 단, ratio는 float 형태로 입력할 것!
def brightnessMulti(picture, ratio) :
    changePicture = (np.clip(picture * ratio, 0 , 255)).astype(np.uint8)
    # np.clip은 정해진 범위의 미만 또는 초과할 때 해당 범위 안에 값으로만 유지하도록 만들어줌
    # astype는 배열 요소 값의 타입을 변환시켜준다.
    ## 만약 uint8로 바꾸지 않으면, float형태로 값이 반환된다. 하지만 이미지 파일은 uint8형태가 아니면 제대로 읽지 못하므로 uin8로 변환해야함

    print(changePicture)
    return changePicture


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

original = brightnessMulti(original, 1.5);
cv2.imshow('Original', original)
cv2.waitKey(0)
cv2.destroyAllWindows()


## 동영상을 실행하는 과정
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

