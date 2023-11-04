import cv2
import numpy as np

isDragging = False
isRDragging = False

# 창 설정
def win_con():
    cv2.imshow('img',img)
    cv2.imshow('img_fixed',img)
    cv2.imshow('mask_img', mask_img)

    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.namedWindow('img_fixed', cv2.WINDOW_NORMAL)
    cv2.namedWindow('mask_img', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('img', 500, 500)
    cv2.resizeWindow('img_fixed', 500, 500)
    cv2.resizeWindow('mask_img', 500, 500)

    cv2.moveWindow('img', 0, 0)
    cv2.moveWindow('img_fixed', 500, 0)
    cv2.moveWindow('mask_img', 1000, 0)


def onMouse(event, x, y, flags, param):
    global isDragging, isRDragging, x0, y0, img, userOFCSb
    if event == cv2.EVENT_RBUTTONDOWN:
        isRDragging = True
        eraseDot()
        cv2.circle(mask_img, (x, y), penSize, (0, 0, 0), -1)
        cv2.imshow('img', img)
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        cv2.circle(img, (x, y), penSize, (255, 0, 0), -1)
        cv2.circle(mask_img, (x, y), penSize, (255, 255, 255), -1)
        cv2.imshow('img', img)

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            #draw mask
            cv2.circle(img, (x, y), penSize, (255, 0, 0), -1)
            cv2.circle(mask_img, (x,y), penSize, (255,255,255), -1)
            cv2.imshow('img',img)
            cv2.imshow('mask_img', mask_img)
        elif isRDragging:
            #draw mask
            cv2.circle(mask_img, (x, y), penSize, (0, 0, 0), -1)
            eraseDot()
            cv2.imshow('img',img)
            cv2.imshow('mask_img', mask_img)

    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False

    elif event == cv2.EVENT_RBUTTONUP:
        if isRDragging:
            isRDragging = False
            eraseDot()

    if userOFCSb > 0: outfocusing()

#TrackBar
def onChange(x):
    global userOFCSb
    global penSize
    userOFCSb = cv2.getTrackbarPos('OFCS','img')
    penSize = cv2.getTrackbarPos('PenSize', 'img')
    if userOFCSb > 0 : outfocusing()


def outfocusing():
    # blured
    blued_img = cv2.blur(ori_img, (userOFCSb, userOFCSb))
    # masked img
    mask_img_inv = cv2.bitwise_not(mask_img)
    # Blured img에서 마스킹된 부분 제외하기
    masked_fg = cv2.bitwise_and(ori_img, mask_img)
    # 마스킹된 img에서 배경 제외하기
    masked_bg = cv2.bitwise_and(blued_img, mask_img_inv)
    # 위 두 이미지 합치기
    img_fixed = masked_fg + masked_bg

    # 수정된 이미지 show
    cv2.imshow('img_fixed', img_fixed)

def eraseDot():
    global img
    # masked img
    mask_img_inv = cv2.bitwise_not(mask_img)
    # Blured img에서 마스킹된 부분 제외하기
    masked_fg = cv2.bitwise_and(img, mask_img)
    # 마스킹된 img에서 배경 제외하기
    masked_bg = cv2.bitwise_and(ori_img, mask_img_inv)
    # 위 두 이미지 합치기
    img = masked_fg + masked_bg

    # 수정된 이미지 show
    cv2.imshow('img', img)

ori_img = cv2.imread('img/testImg.jpg')
img = ori_img.copy()
img_fixed=img.copy()
mask_img = np.zeros_like(img)

win_con()

userOFCSb = 0 # 아웃포커싱 정도 조절
penSize = 0 # 펜사이즈 조절
win_controller = "Controller"
cv2.setMouseCallback('img', onMouse)
cv2.createTrackbar('OFCS', 'img',0,100, onChange)
cv2.createTrackbar('PenSize', 'img',0,100, onChange)




cv2.waitKey()
cv2.destroyAllWindows()
