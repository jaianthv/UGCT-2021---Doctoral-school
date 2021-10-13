import numpy as np
import cv2 as cv
import os
import time
import porespy as ps
import matplotlib.pyplot as plt


def seperate_regions(masked_img, I_min, I_max, show_img):
    
    x = (cv.findNonZero(masked_img))
    x = np.array(x)
    #print (x)
    temp = masked_img
   
    for i in range(0,len(x)):
        coordinate_temp = x[i]
        coordinate_x = coordinate_temp[0][0]
        coordinate_y = coordinate_temp[0][1]
        if temp[coordinate_y][coordinate_x] >= I_min and temp[coordinate_y][coordinate_x] <= I_max:   #33788 - 38000 #38000 - 70000
           temp[coordinate_y][coordinate_x] = 1
        else:
           temp[coordinate_y][coordinate_x] = 0
        coordinate =[]
    if show_img != 0:
       plt.matshow(temp)
       plt.show()
    
    #### calculate the number of non-zero pixels


    #### total area is mask of 1 

  
    
    return temp


folder = "C:/UGCT_doctoral_course/Codes/sequence/"
os.chdir(folder);
New_folder_name = "Threshold"
os.mkdir(New_folder_name)

List_of_files = os.listdir();
    
for i in range(len(List_of_files)):
    
    Is_it_tif=".tif" in List_of_files[i]
    print (List_of_files[i])
    if Is_it_tif==True:
       image = cv.imread(List_of_files[i],-1)
       Threshold_image = seperate_regions(image, 17500, 45000, 0)
       os.chdir(folder+New_folder_name)
       cv.imwrite("Threshold_image_"+List_of_files[i]+"f",Threshold_image)
       os.chdir(folder)


       
       




