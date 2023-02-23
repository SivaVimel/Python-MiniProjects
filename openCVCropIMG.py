import cv2
import argparse

ref_p = []
crop = False

def shape_sele(event,x,y,flags,param):
    global ref_p,crop
    
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_p = [(x,y)]
        
    elif event == cv2.EVENT_LBUTTONUP:
        ref_p.append((x,y))
        
        cv2.rectangle(image,ref_p[0],ref_p[1],(0,255,0),2)
        cv2.imshow('image',image)
        

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True, help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image',shape_sele)

while True:
    cv2.imshow('image',image)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('r'):
        image = clone.copy()
        
    elif k == ord('c'):
        break

if len(ref_p) == 2:
    crop_img = clone[ref_p[0][1]:ref_p[1][1],ref_p[0][0]:ref_p[1][0]]
    cv2.imshow('crop_img',crop_img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
        
        
        
        
        
        
        
        
        
        
        