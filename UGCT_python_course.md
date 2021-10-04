# Python - Data analysis and 3D rendering

Welcome to the course page for python data analysis for UGCT - Doctoral school 2021 on "Introduction to Micro computer tomography". This course is suitable for everyone with prerequisite on python needed. All you need is your interest and motivation. The advatange of using python or anyother open soure software is that you can use it today, tomorrow till the end of time. You can not relying on any software lincense or its expiration date and that is also my motivation to go full opensource. In this practical session, we will learn how to handle reconstructed tomography images from UGCT. The images are typically generated as ".tiff" or ".tif" files/format. Tipically they are about 1000 of them with a total size ranging from 5 Gb to 10 Gb depending on the size of your sample. Hence, handling can be tricky when you dont have a computer with GPU for example. However, there are some tricks you can use such as splitting up of your data or looping over all imagesso you dont load all the images in your memory. We will learn such tricks and techniques during this course. We begin this course by having a general hands on session so everyone can have a feel on how to handle python and it can be followed by a seesion where data analysis can be tailored to individual data sets measured during the course or in the past.

Let us start first from python installation.

## Python installation
Here I assume most of you have a windows system, if you have a linux or Mac python would already be installed. For windows user, please visit the [link](https://www.python.org/downloads/) Choose the latest version or any version (preferable above 3.4) as you prefer and download the executible (.exe) file. Once the file has been downloaded, open and follow the instruction to install python. It is quite straight forward. Once python is installed you will see an app call "IDLE" in your desktop or the "Start". The IDLE is basically your python virtual terminal where the python program that you write will be executed. However, one can also run in the terminal in command prompt but let us not go there and comlicate things. So if you like next to ">>" sign you can type "print ("Hellow world")" and see the output below. Does python print Hello world in blue. Congratulations you wrote your first script. In order to carry out our image processing we require additional functions called modules. Therefore these modules are separately installed from the terminal (command promt) which is described in the next section.

Note: There are many other way one can use python in windows, other platforms include [Jypyter notebook](https://jupyter.org/), [anaconda](https://www.anaconda.com/products/individual), [Ipython](https://ipython.org/) and so on. However, we use simple one such as IDlE or terminal approach for this course. If you are interested feel free to use other platforms of python.

## Module installation
The list of modules needed for our course are listed below;
- Matplotlib.py
- numpy
- os
- sys
- opencv
- porespy

Go to command prompt in your windows system. Then type the following one at a time;

1. pip install matplotlib.py  - press enter ---> wait until the installation is complete, then go to the next point 
2. pip install numpy          - press enter ---> wait until the installation is complete, then go to the next point
3. pip install os             - press enter ---> wait
4. pip install sys            - press enter ---> wait
5. pip install cv2            - press enter ---> wait
6. pip install porespy        - press enter ---> wait

Phew!!! Finally it is done but still some more to install. A description of each module and its purpose will be explained after all the installations are over.


## Paraview installation
Paraview is an interactive 3D visualization, one can combine it python and it can be very efficient. However, in this course we will use it as a graphical user interface. 
You can download the software from the [link](https://www.paraview.org/download/), choose the .exe file after you scroll down under "get the software". Follow the instructions and complete is installation.

## ImageJ installation
Although this is optional, but it can be good to have some quick feedback. Go to this [link](https://imagej.net/software/fiji/). Dowload the .zip file, extract and you are done. A plugin suitable for 3D analysis is MorphoLibJ under the plugin IJPB. To install this plug in, open imagej go to help --> press "update.." it will check for the updates and another window will appear. Press "Manage update sites". Under name find "FIJI", "3D imageJ suite" and "IJPB plugins"; and check the boxes on the left. Then close the current window and press "Apply changes" in the previous window and let it install, once done restart and imageJ is ready. You can open imageJ and under plugin check if you can see MorphLibJ.

Now you are ready with everything needed for this course. In case you had any trouble during the installation, you ask the person in charge of the course or better ask google :) From the following sections the actual course begins starting with a brief description of different modules and function we use in python analysis.

## Description about different python modules

#### Matplotlib
It is one of the many plotting tool used in python and probably one of the oldest. In this course we will use this library, however if you know of other plotting libraries feel free to use them. We will use the plot function "matplotlib.pyplot" for all our plotting. The documentation for matplotlib can be found [here](https://matplotlib.org/).

#### numpy
Numpy is a python function used for handling arrays and data sets. It is quite helpful in handling 2D and 3D images in the form of arrays. Documentation for numpy can be found [here](https://numpy.org/doc/stable/).

#### os 
os refers to operating system. This module is needed to direct the python to a particular folder or location in your computer. The documentation is [here](https://docs.python.org/3/library/os.html).

#### sys

sys module provides the possibility to send arguments in the commandline as you execute your python script. We may not be using this during the course, but is something good to know. You can check the [documentation](https://docs.python.org/3/library/sys.html) to know more about it.

#### cv2/opencv
This is an important module, which people use of image processing. It is one of the important module in image processing and we will a lot of function from this module during the course. It is something you may want to study/read through yourself if you want to make use of this module to process your images. It have good a good documentation and this [link](https://learnopencv.com/) has many examples explaining almost all the functions available in the module. The OpenCV documentation can be found [here](https://docs.opencv.org/4.5.3/).

#### porespy
While Opencv can do most of the image processing, it is more suitable for 2D images. However, tomography images, working with 3D volume images is important as each pixels are interdependent. Neverthelss, for computational reasons one can still split the images into slices to carry out the analysis. In Porsepy one have the possibility anlyze the 3D image data in the volume form. The Porespy is mainly used to analyze the local thickness of the tomography images during this course.

## Let the coding begin

We will firat do some small python programs so you get used to coding. In idle, go to top corner "File" and press "New file". A new window will appear, here is where you are going to write your python script. Let start by first loading the image.

### Load image
```
import numpy
import cv2 as cv
import matplotlib.pyplot as plt

folder="Enter/folder/path"
os.chdir(folder)
filename = "xxx.tif"
image = cv.imread(filename,-1)
print ("Image successfully read")
```
After this, press ctrl+s to save, give a name to your file. By default it will save as .py as ending. So you can just give a name here. Once saved, press F5 to run the script. Or you can go to "Run" on the top and press "Run Module". Was the script executed without any error, did the program print "Image successfully read"?? Then all is good.

### Open image in python
Your image is loaded in the script, now let us take a look at it. There are two ways you can view your image let us try first by using opencv function. In the same program. start a new line. Write the following.

```
# in the line below - give a fancy name to the "window name" and enter the name you have given to your image

cv.imshow('Window name',your image variable)
# the line below will wait until you press escape after which it will close the image window
cv.waitKey(0)
cv.destroyAllWindows()

```

Did it work, were you able to see the image? One disadvantage of using the `cv.imshow` function is that you cannot adjust the grey scale value to be displayed or it has a scale bar to see the pixel values. So to be able to view those, we use matplotlib function as below. 

```
plt.matshow(Type your image name)
plt.show()

```
Then run the script, how does the image appear?? Here you can zoom in place the mouse on top of your pixel of interest and know what value it has. 

*Exercise 1* <br>
While loading the image you used the syntax `cv.imread(filename,-1)` what does the "-1" corresponds to? How about you try entering "0" and "1" and how does the image change? Can you use any other value?? Don't google your answer immediately :) <br>
Alright, let us do some operation on the image. 


### Grey value thresholding 
Grey value thresholding is one of the simplest segmentation techniques, where select the range of pixels to be displayed and discard the remaning regions. One way to carry out the grey value thresholding is by using the function from the opencv, i.e. `cv.threshold`, some examples on different types and implementation can be found here [example](https://learnopencv.com/opencv-threshold-python-cpp/). A typical example can be seen below;

```
cv.threshold(Inner_layer,Limit,set_to_value,cv.THRESH_BINARY+cv.THRESH_OTSU)

```
This code typically functions as the following <br>
```
if pixel value < Limit
   set pixel value to set_to_value
else 
   set pixel value to zero

```
Imagine you have a pixel range of 0 - 100, and you want to separate or segment the pixels from 50 - 75, then this function cannot be used. There might be other possibilities but let us do it in the hard way. Let us write this operation as a python function.


```
def seperate_regions(input_image, I_min, I_max, show_img):
    
    x = (cv.findNonZero(input_image))
    x = np.array(x)
    #print (x)
    temp = input_image
   
    for i in range(0,len(x)):
        coordinate_temp = x[i]
        coordinate_x = coordinate_temp[0][0]
        coordinate_y = coordinate_temp[0][1]
        if temp[coordinate_y][coordinate_x] >= I_min and temp[coordinate_y][coordinate_x] <= I_max:   
           temp[coordinate_y][coordinate_x] = 1
        else:
           temp[coordinate_y][coordinate_x] = 0
        coordinate =[]
    if show_img == 1:
       plt.matshow(temp)
       plt.show()
       
    return temp
```
*Exercise 2* <br>
Copy the function in your python script and you need to write one more line in order to execute this function. Are you able to get the segmented image?<br>
Now we have segmented the image. Let us do a quick analysis using one of the porespy function to calculate the local thickness.



## Introduction to Porespy
Porespy is one of the python module used for pore analysis. It has one of the active repository and have many functions suitable for analyzing pores data. During this course we use it to analyze the local thickness of the tomography images.

### Finding local thickness

[1] Hildebrand, T. and Rüegsegger, P., 1997. A new method for the model‐independent assessment of thickness in three‐dimensional images. Journal of microscopy, 185(1), pp.67-75.



### Exporting and saving


### looping over a folder



## Exercise 1: Choose your data set

## Rendering to 3D image
### VTK file
### VTK file description
### python script to create VTK file
