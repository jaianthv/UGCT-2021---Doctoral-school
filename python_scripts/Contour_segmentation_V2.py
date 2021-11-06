import numpy as np
import cv2 as cv
import os
import time
import porespy as ps
import matplotlib.pyplot as plt


def clean_extra_contours(contours, val):

    # draw contours
    # dilate contours
    # check len of contours
    # if you have to dilate 
 
    No_of_contours = len(contours)
    #print (No_of_contours)
    Individual = []
    
    for i in range(No_of_contours):
        Individual.append(len(contours[i]))
        
   
    #print (Individual)
    
    Max_Con = max(Individual)
    #print (Max_Con)
    idx = Individual.index(Max_Con)
    #print (idx)
       
    del_item = []

    for j in range(len(contours)):
        #if Max_Con - len(contours[j]) > 1506:
        if len(contours[j])/Max_Con < val: ### change this value
           #print (Max_Con - len(contours[j]))
           del_item.append(len(contours[j]))
    
    #print (del_item)

    for j in range(0,len(del_item)):
        no_of_contour = len(contours)
        
        for k in range(0,no_of_contour):
            if len(contours[k]) == del_item[j] :
                del(contours[k])
                break
    return contours


def segment_remaining(contours,image, original):
    Temp = image.copy()
    
    kernel = np.ones((5,5),np.uint8)
    Temp = cv.dilate(Temp,kernel,iterations=1)
    for i in range(0,len(contours)):
        M = cv.moments(contours[i])
        cx = (M["m10"] / M["m00"])
        cy = (M["m01"] / M["m00"])
        center_coordinates = (int(cx), int(cy)) 

        flood_fill = cv.floodFill(Temp,None,(center_coordinates[0],center_coordinates[1]),1)
        Temp = Temp + flood_fill[1]
    #retval,  Temp = cv.threshold(Temp,5,1,cv.THRESH_BINARY)
    #plt.matshow(Temp*original)
    #plt.show()
    return Temp*original





folder = "C:/Lin/Cropped/Threshold/"
os.chdir(folder);
New_folder_name = "segmented"
os.mkdir(New_folder_name)

List_of_files = os.listdir();
    
for i in range(len(List_of_files)):
    
    Is_it_tif=".tiff" in List_of_files[i]
    print (List_of_files[i])
    if Is_it_tif==True:
       image = cv.imread(List_of_files[i],-1)
       image_temp = image.copy()
       image = np.array(image,dtype=np.uint8)
       retval, image = cv.threshold(image,1,1,cv.THRESH_BINARY)
       contours,_ = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)
       
       contours = clean_extra_contours(contours, 0.015) ## change this value it represents the size of contours to be removed
       # 0.015 says remove all contours less than 1.5 percent the size of the biggest contours

       #x = cv.drawContours(image,contours,-1, (5,5,0), 1)
       #plt.matshow(x)
       #plt.show()

 #      print ((contours))
       
       
       x = segment_remaining(contours,image, image_temp)
       


       
       
       os.chdir(folder+New_folder_name)
       cv.imwrite("Segment_"+List_of_files[i],x)
       os.chdir(folder)

