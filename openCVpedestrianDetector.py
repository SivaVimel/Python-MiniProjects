import cv2
import imutils 

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    ret, img = cam.read()
    if ret:
        img = imutils.resize(img,width = min(400,img.shape[1]))
        (region, _) = hog.detectMultiScale(img, winStride=(4,4),padding =(4,4),scale=1.05)
        
        for x,y,w,h in region:
            cv2.rectangle(img,(x,y),(x+w,h+y),(0,0,255,2))
            
        cv2.imshow('Pedestrian',img)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
cam.release()
cv2.destroyAllWindows()