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

            # roi 선택
            w = x - x0
            h = y - y0
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:

                # height, width = img.shape[:2]
                # # img = cv2.resize(img, (int(width), int(height)), interpolation=cv2.INTER_AREA)
                # 전경
                # img_fg = img[y0:y0 + h, x0:x0 + w]
                #
                # # resize를 통한 블러링
                # # img_cp = cv2.resize(img, (int(width*userOFCS), int(height*userOFCS)), interpolation=cv2.INTER_AREA)
                # # img_cp = cv2.resize(img_cp, (int(width), int(height)), interpolation=cv2.INTER_AREA)
                # # img_cp[y0:y0 + h, x0:x0 + w] = img_fg
                #
                # #blur() 함수로 블러링
                # img_af = cv2.blur(img,(userOFCSb,userOFCSb))
                # img_af[y0:y0 + h, x0:x0 + w] = img_fg
                #
                # 수정된 이미지 show
                # cv2.imwrite('./img/fixed.jpg', img_af)
                # cv2.imshow('img_cp',img_af)
                # print("fixed")

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
