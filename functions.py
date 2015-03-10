import numpy as np
import cv2

def getContours(img, mask):
    _,contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 2)

    print len(contours)
    return contours

def getAveColor(img,mask):
    aveColor = cv2.mean(img,mask = mask)
    
    print aveColor
    return aveColor
    
def getAngle(cnt):
    (x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

    print angle
    return angle
