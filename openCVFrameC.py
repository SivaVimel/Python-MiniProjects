import cv2 

vid = cv2.VideoCapture('/home/anonimouz/Downloads/test.mp4')

if vid.isOpened():
    count = 0
    success = 1
    
    while success:
        success,image = vid.read()
        if success == 1:
            print("frame%d.jpg"%count)
            cv2.imwrite("frame%d.jpg"%count,image)
            count+=1