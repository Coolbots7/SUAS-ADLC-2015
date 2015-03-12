import numpy as np
import cv2

def getAveVal(img,mask):
    v1,v2,v3,_ = cv2.mean(img,mask = mask)
    
    print v1,v2,v3
    return v1,v2,v3

def getColorHSV(h,s,v):
    if v<75:
        return 'Black'
    elif v>190 and s<27:
        return 'White'
    elif v<185 and s>53:
        return 'Gray'
    else:
        if h<14:
            return 'Red'
        elif h<25:
            return 'Orange'
        elif h<34:
            return 'Yellow'
        elif h<73:
            return 'Green'
        elif h<102:
            return 'Aqua'
        elif h<127:
            return 'Blue'
        elif h<149:
            return 'Purple'
        elif h<175:
            return 'Pink'
        else:
            return 'Red'
    
def getAngle(img,cnt):
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img,ellipse,(0,255,0),2)

    (x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

    print angle
    return img, angle

def getContours(img, mask):
    _,contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 2)

    print len(contours)
    return img, contours

def fitLine(img,cnt):
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

    return img
