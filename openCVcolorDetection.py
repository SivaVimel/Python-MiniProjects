                                #Colour Detection
    
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while(1):
    _,img = cam.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)
    red_mask = cv2.inRange(hsv,red_lower,red_upper)
    
    green_lower = np.array([25,52,72],np.uint8)
    green_upper = np.array([102,255,255],np.uint8)
    green_mask = cv2.inRange(hsv,green_lower,green_upper)
    
    blue_lower = np.array([94,80,2],np.uint8)
    blue_upper = np.array([102,255,255],np.uint8)
    blue_mask = cv2.inRange(hsv,blue_lower,blue_upper)
    
    kernal = np.ones((5,5),"uint8")
    
    red_mask = cv2.dilate(red_mask,kernal)
    res_red = cv2.bitwise_and(img,img,mask=red_mask)
    
    green_mask = cv2.dilate(green_mask,kernal)
    res_green = cv2.bitwise_and(img,img,mask=green_mask)
    
    blue_mask = cv2.dilate(blue_mask,kernal)
    res_blue = cv2.bitwise_and(img,img,mask=blue_mask)
    
    #Red
    contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic,contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            
            cv2.putText(img,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255))
            
    #Green
    contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            
            cv2.putText(img,"Green",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))
            
    #Blue
    contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            cv2.putText(img,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            
    cv2.imshow("Colour Detection",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break
        
    