import numpy as np
import cv2

#본 py code의 img 는 프로젝트의 masked_img와 같은 지휘를 얻음

#마우스 클릭이 up될 때 그곳의 색상이 (255,255,255)면 fill함수를 실행하면 됨.
isDragging = False

#fill 함수의 구현
def fillRoi(x,y,dh,dw):
    lx, rx, ty, dy = -1, -1, -1, -1
    print(x,y)
    i = 0
    for i in range(y,0,-1):
        if img[i][x]==255:
            ty=i
            break
    if i<=1:
        ty=0
    j=dh
    print("ty:"+str(ty))
    for j in range(y,dh):
        # print(j)
        if img[j][x]==255:
            dy=j
            break
    if j==dh-1:
        dy=dh
    print("dy:"+str(dy))

    for cy in range(ty,dy,1):
        for lx in range(x,0,-1):
            if img[cy][lx] == 255:
                break
        for rx in range(x,dw,1):
            if img[cy][rx] == 255:
                break
        img[cy,lx:rx]=255
def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img, userOFCSb
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        # cv2.circle(img, (x, y), penSize, (255, 255, 255), -1)
        cv2.imshow('img', img)
        fillRoi(x, y,w,h)

    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
        print(img[y][x])


w = 500
h = 500
img = np.zeros((w,h), dtype=np.uint8)
# cv2.circle(img, (w//2,h//2), 100, (255,255,255) , 10)
cv2.rectangle(img, (200,200), (400,400), 255, 10)
# cv2.imwrite('./blank_img.jpg',empty_img)
cv2.imshow('img', img)
penSize = 100  # 펜사이즈 조절
cv2.setMouseCallback('img', onMouse)

cv2.waitKey()
cv2.destroyAllWindows()