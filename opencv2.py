import numpy as np
import cv2

def myfunc(i):
    pass 

title='video camera'
cv2.namedWindow(title) 
cv2.createTrackbar('reset', title, 0, 1, myfunc)
cv2.createTrackbar('R', title, 0, 100, myfunc)
cv2.createTrackbar('G', title, 0, 100, myfunc)
cv2.createTrackbar('B', title, 0, 100, myfunc)
cv2.createTrackbar('gamma', title, 0, 100, myfunc)
cv2.setTrackbarPos('R', title, 10)
cv2.setTrackbarPos('G', title, 10)
cv2.setTrackbarPos('B', title, 10)
cv2.setTrackbarPos('gamma', title, 10)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)


while(True):

    ret, frame = cap.read()
    if not ret: continue
    
    h,w,c=frame.shape
    r = cv2.getTrackbarPos('R',title)
    g = cv2.getTrackbarPos('G',title)
    b = cv2.getTrackbarPos('B',title)
    gamma = cv2.getTrackbarPos('gamma',title)
    reset=cv2.getTrackbarPos('reset',title)
    
    frame[:,:,0] = ( ( frame[:,:,0] / 255 ) ** ( 11 / (b+1) ) ) *255
    frame[:,:,1] = ( ( frame[:,:,1] / 255 ) ** ( 11 / (g+1) ) ) *255
    frame[:,:,2] = ( ( frame[:,:,2] / 255 ) ** ( 11 / (r+1) ) ) *255
    frame[:,:,:] = ( ( frame[:,:,:] / 255 ) ** ( gamma / 10 ) ) *255
    if(reset==1):
        cv2.setTrackbarPos('R', title, 10)
        cv2.setTrackbarPos('G', title, 10)
        cv2.setTrackbarPos('B', title, 10)
        cv2.setTrackbarPos('gamma', title, 10)
        cv2.setTrackbarPos('reset', title, 0)
        
    cv2.imshow(title, frame)  

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
