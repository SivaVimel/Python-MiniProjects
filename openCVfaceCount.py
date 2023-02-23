import cv2

cam =  cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/anonimouz/Documents/python projects/cascade/face.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,1.1,3)
    count = 0
    
    for x,y,w,h in face:
        count +=1
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,'Face'+str(count),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
        
    cv2.imshow('Face',frame)
    
    if cv2.waitKey(33) == 27:
        break
cam.release()
cv2.destroyAllWindows()