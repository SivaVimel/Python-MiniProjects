import cv2 

#Click Event Funtion
def click_Event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN: #for left mouse click
        print(x,' ',y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(x)+','+str(y),(x,y),font,0.5,(255,0,0),2) #putText(src,text,org,font,font_size,colour,thickness)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN: #for right mouse click
        print(x,' ',y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img,str(x)+','+str(y),(x,y),font,0.5,(255,0,0),2) #putText(src,text,org,font,font_size,colour,thickness)
        cv2.imshow('image',img)

if __name__ == "__main__":
    img = cv2.imread('__path__') #Define Image Path
    cv2.imshow('image',img) #shows image as a GUI or displays image
    cv2.setMouseCallback('image',click_Event) #mouse click event call
    cv2.waitKey(0) # 0 - to kill the display of image
    cv2.destroyAllWindows() #Kill funtion
    