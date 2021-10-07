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


### Kernel operation

Kernel operation is nothing but carrying out elementwise matrix mutiplication or convolution on your image pixels. <br>
Covolution = [[a,b,c] [d,e,f] [g,h,i]] (x) [[1,2,3] [4,5,6] [7,8,9]] = a.1 + b.2 + c.3 + d.4 + e.5 + f.6 + g.7 + h.8

For example you can define a kernel as a 3 x 3 matrix such as; <br>
```
0  -1  0 
-1  4  -1 
0  -1  0 
```

and operate this on each pixel of your image, the output of operation is your processed image. Let use see what this kernel can do.

To carry out a kernel operation you can use `cv.filter2D` function. Example is [here](https://learnopencv.com/image-filtering-using-convolution-in-opencv/). Let us try.

```

# create a kernel

kernel_1 = np.array( [[0, -1, 0], 
                    [-1, 4, -1],
                    [0, -1, 0]] )
                    
new_image = cv.filter2D(src=image, ddepth=-1, kernel=kernel_1)

# write your code to plot/visualize the image


```
What do you see? Congratulations you have successfully made a kernel operation!

*Exercise 2* <br>
How about you try another kernel? What does the following kernel do?<br>
```
0  -1  0 
-1  5  -1 
0  -1  0 
```


### Noise filtering
Filtering of noise is important to obtain a clear image. A simple approach to filter the noise is by grey value thresholding. The opencv function is `cv.threshold(Inner_layer,Limit,set_to_value,cv.THRESH_BINARY+cv.THRESH_OTSU) `, here we set a limit and change the pixel value to a user defined value tyically as a binary image to 1 or 0. However this thresholding may not be always suitable, hence we use other form of noise filtering as follows.

#### Gaussian Filtering

Also known as Gaussian blur, approxiate each pixel into a Gaussian function. It typically make the image blurr, but at the same time reduce the noice in some cases. It is also carried out by kernel operation and the Gaussian blur kernel is given as follows;<br>
```
1/16  1/8  1/16 
1/8  1/4  1/8 
1/16  1/8  1/16 
```

One can carry out the Gaussian blur using `cv.filter2D` function as carried out before. However opencv has a seperate Gaussian blur function as `cv.gaussianblur`. The syntax is given as `cv.GaussianBlur(image_name, (i, i), 0)` where "i,i" is the kernel size if it is a 3 x 3 matrix or 5 x 5 matrix and so on. Let us see what the Gaussian blur can do.


*Exercise 3*<br>
How about we try doing gaussian blur with 3x3, 5x5 and 10x10 kernel?? What to do you see?<br>

List of other filters can be found in [link](https://docs.opencv.org/4.5.3/d4/d86/group__imgproc__filter.html)



#### FFT filtering

Fast Fourier transform is one of the important algorithm in image processing. Foruier transform of an image converts your image in a frequency space. One can make your image blurry by removing the high frequency signal and can make the image sharper by removing the low frequency signals. This approach can also be used to smooth and sharpen the image, however the use of FFT on images is broad.

Let us follow the code below, it taken from [here](https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Fourier_Transform_FFT_DFT.php);

```
image_float = np.float32(image)

dft = cv2.dft(image_float32, flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()  


shape_img = np.shape(image)
for_crop = image.copy()
for_crop = for_crop * 0

center_coordinates = (int(shape_img[0]/2), int(shape_img[1]/2)) 
radius = 20
color = (10, 10, 0) 
thickness = 1
image = cv.circle(image, center_coordinates, radius, color, thickness)
flood_fill = cv.floodFill(binary_image,None,(cx,cy),1)
flood_fill_image = flood_fill[1]

plt.matshow(flood_fill_image)
plt.show()

mask = flood_fill_image
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
image_back = cv.idft(f_ishift)
image_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()  
```

### Edge detection
Edge detection is needed as a part of image processing. Edge detection measures the region where there is a slope in the image. One of the edge detection method is canny edge detection method, the syntax is `cv.Canny(image,1,1)`. The numbers represent a threshold value to detect the slope
Other detection method include Sobel and Laplacian.

Let us see which threshold works.

```
Edge_iamge = cv.Canny(image,i,i) # --> change i and see what happens
plt.matshow(Edge_image)
plt.show()

```

[1] Canny, J., 1986. A computational approach to edge detection. IEEE Transactions on pattern analysis and machine intelligence, (6), pp.679-698.


### Segmentation

#### Grey value thresholding 
Grey value thresholding is one of the simplest segmentation techniques, where select the range of pixels to be displayed and discard the remaning regions. One way to carry out the grey value thresholding is by using the function from the opencv, i.e. `cv.threshold`, some examples on different types and implementation can be found here [example](https://learnopencv.com/opencv-threshold-python-cpp/). A typical example can be seen below;

```
cv.threshold(image,Limit,set_to_value,cv.THRESH_BINARY+cv.THRESH_OTSU)

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

#### Erosion/dilation
Before we go to the contour based segmentation it is important to know one more function, which the dilation and erosion of the image objects. From the word, the dilation function dilate the object, i.e. a thin line can be made thicker. The opposite of dilate is erosion where a thicker line is made thinner. In image processing you might use dilation more than erosion. Just like other function, dilation also works by kernel operation. The kernel determine by how many pixels a given pixel must dilate. A nice description of different morphological changing functions along with examples can be found [here](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html).

```
kernel = np.ones((i,i),np.uint8)
binary_image = cv.dilate(image,kernel,iterations=1)
#erosion = cv.erode(image,kernel,iterations = 1)
```

#### Contour based
Contour based segmentation is useful when you have to segment particular objectes from the image. The object can be separated based on the surface area, shape for example. Let us see how it works.
```
contours,_ = cv.findContours(binary_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)

cv.drawContours(binary_image,contours,-1,(0,255,0),3)

plt.matshow(binary_image)
plt.show()

## let us remove some regions of the contour

select_list = []

cv.drawContours(binary_image,contours[select_list],0,(0,255,0),3)
plt.matshow(binary_image)
M = cv.moments(contours[select_list])
cx = (M["m10"] / M["m00"])
cy = (M["m01"] / M["m00"])
center_coordinates = (int(cx), int(cy)) 
flood_fill = cv.floodFill(binary_image,None,(cx,cy),0)
plt.matshow(flood_fill[1])
plt.show()

```

Could you seperate different objects from the image??


Now we have segmented the image. Let us do a quick analysis using one of the porespy function to calculate the local thickness.


## Introduction to Porespy
Porespy is one of the python module used for pore analysis. It has one of the active repository and have many functions suitable for analyzing pores data. During this course we use it to analyze the local thickness of the tomography images.

### Finding local thickness
The local thickness can be computed by "Ray" or "Sphere" method, and porespy and many other local area/volume calculator uses sphere based approach. Let us first find the thickness on a 2D image. 

```
import porespy as ps
image = np.array(image,dtype=np.float32)
thickness_image = ps.filters.local_thickness(image)
```

[1] Hildebrand, T. and Rüegsegger, P., 1997. A new method for the model‐independent assessment of thickness in three‐dimensional images. Journal of microscopy, 185(1), pp.67-75.



### Exporting/saving
```
os.chdir("C:/Users/jaianth/Desktop/unwrapped")
path_name = "Unwrapped_%s.tiff"%image_number
cv.imwrite(path_name,image_array)
```

### looping over a folder
How to we do the same process for a stack of images?
```
folder="H:/Batch_1_07_2020/EEG002_X overview/reconstructed/Processed/"
os.chdir("H:/Batch_1_07_2020/EEG002_X overview/reconstructed/Processed/")

List_of_files = os.listdir();
List_of_files.sort()

for i in range(len(List_of_files)-1):
    #os.chdir(folder)
    Is_it_tif=".tiff" in List_of_files[i]
    #print (List_of_files[i])
    if Is_it_tif==True:
        print (List_of_files[i])

```

### Image registration 
#### Hyperspy 



## Exercise 1: Choose your data set

Now let us segment a full stack of image. Once successful we will do a 3D rendering. 

## Rendering to 3D image
There are many options to visualize a 3D image in python, many libraries in [panda](https://pypi.org/project/panda3d-viewer/), [vedo](https://vedo.embl.es/), [matplotlib](https://matplotlib.org/stable/gallery/pyplots/whats_new_99_mplot3d.html#sphx-glr-gallery-pyplots-whats-new-99-mplot3d-py) or [plotly](https://plotly.com/python/3d-camera-controls/) is available for this purpose. However, for large data sets one of the efficient appraoch to convert the images into a vtk format. VTK refers to visualization tool kit, and is nothing but a text file which has the information of the pixels in the 3D image. With a text file available the 3D image can also rendered by simply writing codes instead of requiring a graphical user interface. In this course we will understand how to create a vtk file. While vtk files can be viewed in python, we use paraview opensource GUI to visualize the 3D rendering. To visualize the vtk file in python, you can use paraview [python libraries](https://kitware.github.io/paraview-docs/latest/python/quick-start.html). The document may not be well written but you can go through if interested. In any case let us understand the vtk format and make a vtk file on our own.

### VTK file
The description of the vtk file can be found in this [link](https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf). 

```
# Example of vtk file
# vtk DataFile Version 2.0
Unstructured Grig EXAMPLE
ASCII
DATASET UNSTRUCTURED_GRID
POINTS 18 float
1 5 0
2 5 0
3 5 0
4 5 0
4 4 0
3 4 0
3 3 0
3 2 0
3 1 0
3 0 0 
2 0 0 
1 0 0 
1 1 0
2 1 0
2 2 0
2 3 0
2 4 0
1 4 0

CELLS 3 26
8 0 1 2 3 4 5 16 17
9 16 5 6 7 8 9 13 14 15 
6 8 9 10 11 12 13

CELL_TYPES 3
7
7
7


POINT_DATA 18
SCALARS scalars float 1
LOOKUP_TABLE default

1.0   
1.0   
2.0   
3.0   
4.0   
5.0
6.0   
7.0   
8.0   
9.0   
10.0   
11.0
12.0   
13.0   
14.0   
15.0   
16.0   
17.0
  



```

### VTK file description
### python script to create VTK file
