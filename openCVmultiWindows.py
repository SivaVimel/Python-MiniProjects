import cv2

cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    cv2.imshow('Normal',img)
    cv2.imshow('Gray',gray)
    cv2.imshow('HSV',hsv)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cam.release()
cv2.destroyAllWIndows()