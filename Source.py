import numpy as np
import cv2
from glob import glob
import os
import time

from imageAnalysisFunctions import *
from targetClass import *


#Erode / Dialate Kernel
kernel = np.ones((5,5),np.uint8)

#Erode / Dialate Iterations
nIt = 10

targets = []
targetCnt = 0

while True:
    time.sleep(5)

    #Read all '.JPG' images from main folder
    img_names = glob('*.JPG')

    if len(img_names) > 0:
        for fn in img_names:
            
            #Read image nd convert to HSV colorspace
            img = cv2.imread(fn, 1)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            #Get the mean values for HSV
            mean, _ = cv2.meanStdDev(hsv)

            #Split HSV into individual channels
            h, _, _ = cv2.split(hsv)

            #Remove the average hue value from the h channel
            hMask = cv2.inRange(h, 0, mean[0]+10)

            #Erode / Dialate the mask 'nIt' times to eliminate noise
            dilate = cv2.dilate(hMask, kernel, iterations=nIt)
            erode = cv2.erode(dilate, kernel, iterations=nIt)

            #Invert mask from white to black
            mask = 255 - erode

            #Combine the origional image with the mask
            res = cv2.bitwise_and(img,img, mask= mask)

            #Write the resulting image to the folder Output
            cv2.imwrite(os.path.join('Output', '%s' % fn), res)

            contours = getContours(res, mask)
            #Test for contour
            if len(contours) == 0:
                print ' No contours found'
            else:
                for cnt in contours:

                    #Create object
                    targetCnt +=1
                    targets.append(Target(targetCnt))

                    drawCenter(img,cnt)

                    #isolate target
                    crop = cropImage(img,cnt)
                    cropMask = cropImage(mask,cnt)
                    
                    #save image name
                    targets[targetCnt-1].setImg('Target %i.jpg' % targetCnt)

                    #Get target color
                    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
                    h,s,v = getAveVal(hsv,cropMask)
                    targets[targetCnt-1].setTargetColor(str(getColorHSV(h,s,v)))
                    
                    #get target position
                    cx,cy = getCenter(cnt)
                    targets[targetCnt-1].setPos(cx,cy)

                    #save isolatd image
                    cv2.imwrite(os.path.join('Targets', 'Target %i.jpg' % targetCnt), crop)

                    #Print target
                    targets[targetCnt-1].printObj()
                    
            #Move completed image to folder
            os.rename(fn, "Completed/%s" % fn)
            print ' --Completed %s' % fn
    
cv2.waitKey()
cv2.destroyAllWindows()
