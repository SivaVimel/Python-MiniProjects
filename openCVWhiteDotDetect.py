import cv2
path = '/home/anonimouz/Downloads/white-dot.png'

gray = cv2.imread(path,0) #Image -> Gray Image (Black and White)
th, threshed = cv2.threshold(gray,100,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) #Threshold
cnts = cv2.findContours(threshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2] #find number of objects by path making as curve joining points -> Dots

s1=3
s2=20
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt)<s2: #Calculates area and measures
        xcnts.append(cnt)

print("\nDots Number : {}".format(len(xcnts)))