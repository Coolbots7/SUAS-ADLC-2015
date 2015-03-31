import numpy as np
import cv2

def getAveVal(img,mask):
    v1,v2,v3,_ = cv2.mean(img,mask = mask)
    
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

    return contours

def fitLine(img,cnt):
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

    return img

def drawBoundingRect(img,cnt):
    x,y,w,h = cv2.boundingRect(cnt)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img

def cropImage(img,cnt):
    x,y,w,h = cv2.boundingRect(cnt)
    wa = w*0.1
    ha = h*0.1
    crop = img[y-ha:y+h+ha,x-wa:x+w+wa]
    return crop
