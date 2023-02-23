import numpy as np
import cv2

def emptyWin():
    pass

def main():
    image = np.zeros((512,512,3),np.uint8)
    windowName = "Color Palette"
    
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Blue',windowName,0,255,emptyWin)
    cv2.createTrackbar('green',windowName,0,255,emptyWin)
    cv2.createTrackbar('red',windowName,0,255,emptyWin)
    
    while(True):
        cv2.imshow(windowName,image)
        
        if cv2.waitKey(1)==27:
            break
        
        blue = cv2.getTrackbarPos('blue',windowName)
        green = cv2.getTrackbarPos('green',windowName)
        red = cv2.getTrackbarPos('red',windowName)
        
        image[:] = [blue,green,red]
        print(blue,green,red)
        
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()