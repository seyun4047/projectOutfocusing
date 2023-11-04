import sys
maxX = -1
minX = sys.maxsize
maxY = -1
minY = sys.maxsize
def updateRoi(x,y):
    def isMaxX(x):
        global maxX
        if maxX<x:
            maxX=x
    def isMaxY(y):
        global maxY
        if maxY<y:
            maxY=y
    def isMinX(x):
        global minX
        if minX>x:
            minX=x
    def isMinY(y):
        global minY
        if minY>y:
            minY=y
    isMaxX(x)
    isMaxY(y)
    isMinX(x)
    isMinY(y)