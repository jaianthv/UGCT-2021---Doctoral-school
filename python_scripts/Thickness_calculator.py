import cv2 as cv
import numpy as np
import os
import porespy as ps
import sys
import matplotlib.pyplot as plt


def select_images(**args):
    
    List_args = list(args.items())
    
    Keys =[]
    Values = []
    for i in range(0,len(List_args)):
        Keys.append(List_args[i][0])
        Values.append(List_args[i][1])
  
    if "folder" in Keys:
        folder_index = Keys.index("folder")
        
        
    else:
        print ("Folder argument missing")
    
    if "image_type" in Keys:
        image_type_index = Keys.index("image_type")
    else:
        print ("Image type argument missing")
        
    if "select_images" in Keys:
        Select_images_index = Keys.index("select_images");
        All_images = "No"
    else:
        All_images = "Yes"
        
    
    #Values(folder_index)
    #Values(image_type)
    #Values(Select_images_index)
    if "/" in Values[folder_index]:
        if Values[folder_index][len(Values[(folder_index)])-1] != "/":
           Values[folder_index] = Values[folder_index]+"/"
           
    if '"\"' in Values[folder_index]:
        if Values[folder_index][len(Values[(folder_index)])-1] != '"\"':
           Values[folder_index] = Values[folder_index]+'"\"'

    # folder, imgtype=tiff,png, default:all images, select_images = start from 1 1-10
    
    #option - All, Not_all + range;
    os.chdir(Values[folder_index]);
    List_of_files_selected = [];
    List_of_files = os.listdir();
    
    for i in range(len(List_of_files)):
    
        Is_it_image_type=Values[image_type_index] in List_of_files[i]
        #print (List_of_files[i])
        if Is_it_image_type==True:
           List_of_files_selected.append(Values[folder_index]+List_of_files[i])

    List_of_files_selected.sort()
    if All_images == "No":
       Range = Values[Select_images_index].split("-")
       
       List_out = List_of_files_selected[int(Range[0])-1:int(Range[1])-1]
    else:
       List_out = List_of_files_selected

    return List_out


#def open_single_image():



def store_as_nd_array(Files):

    image = cv.imread(Files[0],-1)
    
    shape = np.shape(image)
    
    Array = np.zeros((len(Files),int(shape[0]),int(shape[1])))
    for i in range(len(Files)):
         image = cv.imread(Files[i],-1)
         image = np.array(image,dtype=np.float32)
         
         Array[i]=image
    print (np.shape(Array))

    return Array


#def display_3D(ND_Array):
def get_thickness(ND_array,resolution):
    
    data = []
    data_std = []
    pos = []
    std = []
    for i in range(len(ND_array)):
        pos.append(i)
        x = (cv.findNonZero(ND_array[i]))
        temp_image = ND_array[i]
        x = np.array(x)
        avg_temp =[]

        if len(x) != 0:
            
            for ii in range(0,len(x)):
                coordinate = x[ii]
                coordinate_x = int(coordinate[0][1])  #change in coordinate
                coordinate_y = int(coordinate[0][0])  #change in coordinate
                avg_temp.append((temp_image[coordinate_x][coordinate_y])*resolution)
                    
            avg=np.mean(avg_temp)
            std=np.std(avg_temp)
        
        
            data.append(avg)
            data_std.append(std)
        
        
    return pos,data,data_std
        


def multiprocess_thickness_calculator(**args):
    #folder, resolution, image_type
    List_args = list(args.items())
    
    Keys =[]
    Values = []
    for i in range(0,len(List_args)):
        Keys.append(List_args[i][0])
        Values.append(List_args[i][1])
  
    if "folder" in Keys:
        folder_index = Keys.index("folder")
    else:
        print ("Folder argument missing")
    
    if "image_type" in Keys:
        image_type_index = Keys.index("image_type")
    else:
        print ("Image type argument missing")

    if "resolution" in Keys:
        resolution_index = Keys.index("resolution")
    else:
        print ("resolution argument missing")
        
    if "save_image" in Keys:
        save_image_index = Keys.index("save_image")
        save_image = "yes"
        if Values[save_image_index] == "yes":
            os.chdir(Values[folder_index])
            #os.mkdir("Processed_thickness")
    else:
        save_image = "No"

    if "overlap" in Keys:
        overlap_no_index = int(Keys.index("overlap"))
        overlap_np = int(Values[overlap_no_index])

    else:
        overlap_no = 5
        

    if "split_images" in Keys:
        split_image_no_index = int(Keys.index("split_images"))
        split_image_no = int(Values[split_image_no_index])
        


    else:
        print ("Enter no of images you want to split")
        
        
        
    
    images = select_images(folder=Values[folder_index],image_type=Values[image_type_index])
    # indices of images into set of 200 slices
    No_of_images = len(images)
    
    Divided_array = create_split_array(No_of_images,overlap_no,split_image_no)
    print (Divided_array)
    '''
    Divide = No_of_images/200
    #print (No_of_images)
    Nos=np.linspace(0,No_of_images-1,No_of_images)
    Divided_array = np.array_split(Nos,round(Divide))
    '''
    #print (Divided_array)
    '''
    for ii in range(len(Divided_array)-2):
        Divided_array[ii]=np.append(Divided_array[ii],Divided_array[ii+1][0:4])
    '''
    data_slices = [];
    data_thickness = []
    data_std_dev = []
    filename_data=open("data_list.txt","a")
    for i in range(0,len(Divided_array)):
        #temp_data = []
        #temp_slices =[]
        #temp_thickness = []
        #temp_std =[]
        print (Divided_array[i])
        start = Divided_array[i][0]
        if i == len(Divided_array)-1:
            end = Divided_array[i][len(Divided_array[i])-1]+1
        
        else:
            end = Divided_array[i][len(Divided_array[i])-1]+overlap_no+1#6
        #end = Divided_array[i][len(Divided_array[i])-1]+6
        #end = Divided_array[i+1][5]
        array = store_as_nd_array(images[int(start):int(end)])
        thickness_image = ps.filters.local_thickness(array)
        thickness_image = np.array(thickness_image, dtype=np.uint16)
        coordinate,data_thickness,data_std = get_thickness(thickness_image,int(Values[resolution_index]))
        '''
        for j in range(len(Divided_array[i])-1):
            filename_data.write("%i %f %f\n"%(Divided_array[i][j],data_thickness[j],data_std[j]))
        '''
        index_z=np.linspace(start,end-1,len(thickness_image))
        print (index_z)
        for j in range(0,len(index_z)-1):
            filename_data.write("%i %f %f\n"%(index_z[j],data_thickness[j],data_std[j]))
            
            
        if save_image == "yes":
           os.chdir(Values[folder_index])
           os.chdir("Processed_thickness")
        for jj in range(len(thickness_image)-1):
            
            temp_split = images[int(index_z[jj])].split("/")
            cv.imwrite("Processed_"+temp_split[len(temp_split)-1],thickness_image[jj])
        
        #temp_data = np.concatenate((Divided_array[i][0:len(Divided_array[i])-5],data_thickness[0:len(Divided_array[i])-5],data_std[0:len(Divided_array[i])-5]),axis=0)
        #Divided_array[i] = np.array(Divided_array[i])
        #data_slices.append(Divided_array[i])#[0:len(Divided_array[i])-5]])
        
        #print (data_slices)
                           
        #data_thickness.append([data_thickness])#([0:len(Divided_array[i])-5]])
        #data_std_dev.append([data_std])#[0:len(Divided_array[i])-5]])
        #data.append([temp_data])
        
        #check if the file is empty
        # if not write
        
            
     

    filename_data.close()

    
    return data_slices,data_thickness,data_std_dev

def plot_thickness_data(folder):
    os.chdir(folder)
    with open('data_list_sorted.txt') as f:
         lines = f.readlines()
         del(lines[0]);
         x = [line.split(" ")[0] for line in lines]
         y = [line.split(" ")[1] for line in lines]
         y_err = [line.split(" ")[2].replace("\n", " ") for line in lines]
         
    
    

    x= np.array(x,dtype=np.uint16)
    
    
    y= np.array(y,dtype=np.float64)
  
    y_err= np.array(y_err,dtype=np.float64)
    
    average = np.mean(y)
    average_error = np.mean(y_err)

    #plt.bar(x,y)
    #plt.plot(x,y)
    plt.errorbar(x, y,yerr=y_err,fmt='o',ecolor='r', capthick=2)
    #plt.ylim(0,40)
    #plt.xscale("log")
    plt.xlabel("No. of slices", fontsize = 15)
    plt.ylabel("Thickness ($\mu$m)", fontsize = 15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    text = 'Average ='+str(round(average,1)) + ' $\pm$' + str(round(average_error,1))+ '($\mu$m) '
    plt.text(0, 10, text , fontsize=15)
    #plt.legend(["thickness","standard deviation"])
    #plt.yscale("linear")
    #plt.xscale("log")
    plt.title("Average thickness per slice", fontsize = 15)
    plt.show()

    return 0

            
def create_split_array(len_of_files,overlap,split_files):
    Divide = len_of_files/split_files #200
    #Divide = split_files
    overlap =int(overlap)
    Nos=np.linspace(0,len_of_files-1,len_of_files)
    
    Divided_array = np.array_split(Nos,round(Divide))

    '''
    print (type(Divided_array[0]))
    
    

    for i in range(0,len(Divided_array)-1):
        temp_len = len(Divided_array[i])
        
        
        start = 0
        end = overlap
        list_temp = Divided_array[i+1][start:end]
        print(list_temp)
        for ii in range(len(list_temp)):
            
            np.append(Divided_array[i],list_temp[ii])
            print (len(Divided_array[i]))
            
    print (Divided_array)
    '''
                                      
    return Divided_array



def sort_sequence():
    with open('data_list.txt') as f:
         lines = f.readlines()
         
         z_value = [line.split(" ")[0] for line in lines]
         thickness = [line.split(" ")[1] for line in lines]
         std = [line.split(" ")[2].replace("\n"," ") for line in lines]
         z_value = np.array(z_value,dtype=np.uint16)
         thickness = np.array(thickness,dtype=np.float32)
         std = np.array(std,dtype=np.float32)
         unique, frequency = np.unique(z_value, return_counts = True)
         
         
    Repeat_number =[]
    
    for i in range(len(frequency)):
        if frequency[i] == 2:
            Repeat_number.append(unique[i])
            
            
    for i in range(len(Repeat_number)):
        coordinates = []
        for j in range(len(z_value)):
            if z_value[j] == Repeat_number[i]:
               coordinates.append(j)
        temp_z_value = []
        temp_thickness =[]
        temp_std = []
        for k in range(len(coordinates)):
            temp_z_value.append(z_value[coordinates[k]])
            
            temp_thickness.append(thickness[coordinates[k]])
            temp_std.append(std[coordinates[k]])

        z_value = list(z_value)
        thickness = list(thickness)
        std = list(std)
        
        z_value[min(coordinates)] = np.average(temp_z_value)
        thickness[min(coordinates)] = np.average(temp_thickness)
        std[min(coordinates)] = np.average(temp_std)

        del(z_value[max(coordinates)])
        del(thickness[max(coordinates)])
        del(std[max(coordinates)])
    #os.remove("data_list.txt")     
    filename_data=open("data_list_sorted.txt","a")
    for i in range(len(z_value)):
        filename_data.write("%i %f %f\n"%(z_value[i],thickness[i],std[i]))
    filename_data.close()
                                







'''
images = select_images(folder="H:/Batch_1_07_2020/EEG002_X overview/reconstructed/Processed/",image_type="tiff",select_images="1-200")
#print (len(images))
array = store_as_nd_array(images)
thickness_image = ps.filters.local_thickness(array)
thickness_image = np.array(thickness_image, dtype=np.uint16)
coordinate,data_thickness = get_thickness(thickness_image)
plt.plot(coordinate,data_thickness)
plt.show()
'''


data = multiprocess_thickness_calculator(folder="C:/UGCT_doctoral_course/Codes/sequence/Threshold/",image_type="tiff",resolution="18", save_image="yes", split_images = "40")
os.chdir("C:/UGCT_doctoral_course/Codes/sequence/Threshold/")
sort_sequence()

#plot_thickness_data("C:/UGCT_doctoral_course/Codes/sequence/Threshold/")













    
