import cv2
import os
import glob
import numpy as np


labels=os.listdir('Images')
imgnum=0
for l in labels:
    #print(l)
    path=os.path.join('Images/',l)
    print(path)

    for img in glob.glob('{}/*.JPG'.format(path)):

        image=cv2.imread(img)
        image=cv2.resize(image,(500,500))
        greyimage=cv2.imread(img,0)
        greyimage=cv2.resize(greyimage,(500,500))
        retval,thresh=cv2.threshold(greyimage,130,255,cv2.THRESH_BINARY)
        kernel = np.ones((5,5),np.uint8)
        thresh = cv2.dilate(thresh,kernel,iterations = 1)
        im2,contours,hier=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h=cv2.boundingRect(cnt)
            if w>50 and h>50:
                output=image[y:y+h,x:x+w]
                cv2.imwrite(str(imgnum)+'.png',output)
        imgnum+=1
