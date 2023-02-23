import cv2
import numpy as np

kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

cam = cv2.VideoCapture(0)

while(1):
    ret, img = cam.read()
    #First GMG with noise
    mask = fgbg.apply(img)
    cv2.imshow('GMG noise',mask)
    
    #GMG without noise using morphology
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
    cv2.imshow('GMG',mask)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWIndows()