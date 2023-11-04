import cv2
import numpy as np
from matplotlib import pyplot as plt

win = 'win'
def onChange(x):
    userOFCSb = cv2.getTrackbarPos('OFCS',win)

ori_img = cv2.imread('img/testImg.jpg')
img=ori_img.copy()
img_fixed=img.copy()
cv2.imshow(win, img)

# userOFCS = int(input())
userOFCS = 0.2
userOFCSb = 10


cv2.createTrackbar('OFCS', win,0,1, onChange)
cv2.waitKey()
cv2.destroyAllWindows()
