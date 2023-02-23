import cv2

cam = cv2.VideoCapture(0)
cars_cascade = cv2.CascadeClassifier('/home/anonimouz/Documents/python projects/cascade/cars.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    cars = cars_cascade.detectMultiScale(gray,1.1,1)
    
    for x,y,w,h in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow('Cars',frame)
    
    if cv2.waitKey(33) == 27:
        break
cam.release()
cv2.destroyAllWindows()