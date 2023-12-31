import cv2 as cv
import numpy as np
import easyocr
from matplotlib import pyplot as plt
import imutils


img = cv.imread('imgees/n2.jpg')

def rescaleframe(frame,scale=0.75):
    width=int(frame.shape[1]*0.2)
    height=int(frame.shape[0]*0.2)
    dimensions =(width,height)

    return cv.resize(frame,dimensions,interpolation =cv.INTER_AREA)

raw_img =rescaleframe(img)
gray_img = cv.cvtColor(raw_img,cv.COLOR_BGR2GRAY)
plt.imshow(cv.cvtColor(gray_img,cv.COLOR_BGR2RGB))


bfilter = cv.bilateralFilter(gray_img,11,17,17)#noise reduction
edged = cv.Canny(bfilter,30,200)#edge detection
plt.imshow(cv.cvtColor(edged,cv.COLOR_BGR2RGB))

keypoints = cv.findContours(edged.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) 
contours = imutils.grab_contours(keypoints)
contours= sorted(contours,key=cv.contourArea,reverse=True)[:10]

location = None
for contour in contours:
    approx = cv.approxPolyDP(contour,10,True)
    if len(approx)==4:
        location =approx
        break

mask = np.zeros(gray_img.shape,np.uint8)
new_image = cv.drawContours(mask,[location],0,255,-1)
new_image = cv.bitwise_and(raw_img,raw_img,mask=mask)
plt.imshow(cv.cvtColor(new_image,cv.COLOR_BGR2RGB))


(x,y) =np.where(mask==255)
(x1,y1) = (np.min(x),np.min(y))
(x2,y2) = (np.max(x),np.max(y))
cropped_img = gray_img[x1:x2+1,y1:y2+1]
plt.imshow(cv.cvtColor(cropped_img,cv.COLOR_BGR2RGB))


reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_img)

text = result[0][-2]
font =cv.FONT_HERSHEY_SIMPLEX
res =cv.putText(raw_img,text=text,org=(approx[0][0][0],approx[1][0][1]+60),fontFace=font,fontScale=1,color=(0,255,0),thickness=1,lineType=cv.LINE_AA)
res = cv.rectangle(raw_img,tuple(approx[0][0]),tuple(approx[2][0]),color=(0,255,0),thickness=3)
plt.imshow(cv.cvtColor(res,cv.COLOR_BGR2RGB))

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

