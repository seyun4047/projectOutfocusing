import cv2
import numpy as np
from matplotlib import pyplot as plt
isDragging = False
x0, y0, w, h = -1,-1,-1,-1
blue, red = (255,0,0),(0,0,255)
def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False

            # #캐니 엣지 검출 함수를 통한 영역 구분
            # w = x - x0
            # h = y - y0
            # print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            # if w > 0 and h > 0:
            #     edges = cv2.Canny(img[y0:y0 + h, x0 :x0 + w],100,360)
            #     cv2.imwrite('./img/canny_edge.jpg', edges)
            #     cv2.imshow('canny_edge', edges)

            # roi 선택
            w = x - x0
            h = y - y0
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:

            # stereo vision 알고리즘을 통한 심도 탐색
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img_depth = img_gray[y0:y0 + h, x0:x0 + w]
                # img_depth2 = cv2.blur(img_depth,(5,5))
                img_depth2 = cv2.GaussianBlur(img_depth, (15,15), 0) #가우시안 필터링
                stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
                disparity = stereo.compute(img_depth, img_depth2)
                plt.imshow(disparity, 'gray')
                plt.show()

            else:
                cv2.imshow('img', img)
                print("error")
img = cv2.imread('img/testImg.jpg')
cv2.imshow('img', img)
# userOFCS = int(input())
userOFCS = 0.2
userOFCSb = 10
cv2.setMouseCallback('img', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
