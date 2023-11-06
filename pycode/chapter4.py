import cv2
import numpy as np

isDragging = False
isRDragging = False
w,h=0,0

# 창 설정
def win_con():
    global w,h
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
    h, w, _ = img.shape

#fill 함수구현
def fillRoi(x,y,dh,dw):
    lx, rx, ty, dy = -1, -1, -1, -1
    print(x,y)
    i = 0
    for i in range(y,0,-1):
        if mask_img[i][x][0]==255:
            ty=i
            break
    # if i<=1:
    #     ty=0
    # j=dh
    print("ty:"+str(ty))
    for j in range(y,dh):
        # print(j)
        if mask_img[j][x][0]==255:
            dy=j
            break
    # if j==dh-1:
    #     dy=dh
    print("dy:"+str(dy))

    for cy in range(ty,dy,1):
        for lx in range(x,0,-1):
            if mask_img[cy][lx][0] == 255:
                break
        for rx in range(x,dw,1):
            if mask_img[cy][rx][0] == 255:
                break
        mask_img[cy,lx:rx]=[255,255,255]
        img[cy, lx:rx] = [255, 0, 0]

def onMouse(event, x, y, flags, param):
    global isDragging, isRDragging, x0, y0, img, userOFCSb
    if event == cv2.EVENT_RBUTTONDOWN:
        isRDragging = True
        eraseDot()
        cv2.circle(mask_img, (x, y), penSize, (0, 0, 0), -1)
        cv2.imshow('img', img)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if fillTog:
           fillRoi(x, y, w, h)
        else :
            isDragging = True
            cv2.circle(img, (x, y), penSize, (255, 0, 0), -1)
            cv2.circle(mask_img, (x, y), penSize, (255, 255, 255), -1)
        cv2.imshow('mask_img',mask_img)
        cv2.imshow('img', img)

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            #draw mask
            cv2.circle(img, (x, y), penSize, (255, 0, 0), -1)
            cv2.circle(mask_img, (x,y), penSize, (255,255,255), -1)
            drawMotion(x,y)
            cv2.imshow('mask_img', mask_img)
        elif isRDragging:
            #draw mask
            cv2.circle(mask_img, (x, y), penSize, (0, 0, 0), -1)
            eraseDot()
            drawMotion(x,y)
            cv2.imshow('mask_img', mask_img)
        else:
            drawMotion(x,y)


    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False



    elif event == cv2.EVENT_RBUTTONUP:
        if isRDragging:
            isRDragging = False
            eraseDot()

    if userOFCSb > 0: outfocusing()

def drawMotion(x,y):
    pre = img.copy()
    cv2.imshow('img', img)
    cv2.circle(pre, (x, y), penSize, (0, 255, 0))
    cv2.imshow('img', pre)

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

fillTog = False # fill toggle
userOFCSb = 0 # 아웃포커싱 정도 조절
penSize = 0 # 펜사이즈 조절
win_controller = "Controller"
cv2.setMouseCallback('img', onMouse)
cv2.createTrackbar('OFCS', 'img',0,100, onChange)
cv2.createTrackbar('PenSize', 'img',0,100, onChange)
while True:
    key = cv2.waitKey(0)
    if key == ord('q') or key == 27 :
        cv2.destroyAllWindows()
    elif key == ord('f'):
        fillTog = True
    elif key == ord('g'):
        fillTog = False
