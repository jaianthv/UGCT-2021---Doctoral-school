import cv2 as cv
import numpy as np
import os
import porespy as ps
import sys
import matplotlib.pyplot as plt


folder="C:/UGCT_doctoral_course/Codes/"
os.chdir(folder)
filename = 'cn_example.tif'
image = cv.imread(filename,-1)
image = np.array(image,dtype=np.uint8)

retval, image = cv.threshold(image,200,1,cv.THRESH_BINARY)
Temp = image.copy()
plt.matshow(image)
plt.show()
contours,_ = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)
print (contours)
x = cv.drawContours(image,contours,-1, (5,5,0), 1)

plt.matshow(x)
plt.show()


## let us remove some regions of the contour

number=4

cv.drawContours(image,contours[number],0,(0,255,0),3)

M = cv.moments(contours[number])
cx = (M["m10"] / M["m00"])
cy = (M["m01"] / M["m00"])
center_coordinates = (int(cx), int(cy)) 
flood_fill = cv.floodFill(image,None,(center_coordinates[0],center_coordinates[1]),0)
plt.matshow(flood_fill[1])
plt.show()


## let us just keep 1

Number = 4

for i in range(0,len(contours)-1):
    if i != 6:
        M = cv.moments(contours[i])
        cx = (M["m10"] / M["m00"])
        cy = (M["m01"] / M["m00"])
        center_coordinates = (int(cx), int(cy)) 

        flood_fill = cv.floodFill(Temp,None,(center_coordinates[0],center_coordinates[1]),0)
        Temp = flood_fill[1]

plt.matshow(Temp)
plt.show()




