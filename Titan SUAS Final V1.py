import numpy as np
import cv2
from glob import glob
import os

from functions import *

#Erode / Dialate Kernel
kernel = np.ones((5,5),np.uint8)

#Erode / Dialate Iterations
nIt = 8

#Read all '.JPG' images from main folder
img_names = glob('*.JPG')
for fn in img_names:
    #Read image nd convert to HSV colorspace
    img = cv2.imread(fn, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Get the mean values for HSV
    mean, _ = cv2.meanStdDev(hsv)

    #Split HSV into individual channels
    h, _, _ = cv2.split(hsv)

    #Remove the average hue value from the h channel
    hMask = cv2.inRange(h, 0, m[0])

    #Erode / Dialate the mask 'nIt' times to eliminate noise
    dilate = cv2.dilate(hMask, kernel, iterations=nIt)
    erode = cv2.erode(dilate, kernel, iterations=nIt)

    #Invert mask from white to black
    mask = 255 - erode

    #Combine the origional image with the mask
    res = cv2.bitwise_and(img,img, mask= mask)

    #Write the resulting image to the folder Output
    cv2.imwrite(os.path.join('Output', '%s Output.JPG' % fn), res)

print 'Done!'
cv2.destroyAllWindows()
