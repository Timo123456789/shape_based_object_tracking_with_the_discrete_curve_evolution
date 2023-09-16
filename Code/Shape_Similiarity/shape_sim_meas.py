"""
Shape Similarity Measure Code File for a prototypical implementation for the combination of "You Only Look Once" (YOLO) (Redmon, 2016, doi: 10.1109/CVPR.2016.91 ) (Vers. YOLOv8x, Ultralytics, 2023) and Discrete Curce Evolution (DCE) (Latecki, 1999, doi: 10.1006/cviu.1998.0738 ); based on hypothesis by Dorr, Latecki and  Moratz (2015, doi: 10.1007/978-3-319-23374-1_7 )

Calculate a Shape Similarity Measure and write this to a text file

Must be used with the files: Main.py, DCE.py, yolo_every_frame.py, yolo_segementation.py, yolo_result_version.py

Implementation for bachelor thesis: "Formbasiertes Objekttracking mit der Discrete Curve Evolution"
                                    "Shape-based object tracking with the Discrete Curve Evolution"

                                    at Westfaelische Wilhelms Universitaet Muenster
                                    First Supervisor: Prof. Dr. Ing. Reinhard Moratz
                                    Second Supervisor: Dr. Christian Knoth

@author: Timo Lietmeyer, 11.09.2023
@contact: timolietmeyer@uni-muenster.de (for question, etc.)

supported by Vocavit GmbH, Hamburg

"""
import numpy as np
import time
import datetime
from YOLO.yolo_result_version import *




def calc_shape_similarity(options):
    """
    main method for calcualte SSM
    runs all other methods
    calc_shape_similarity_compare_polygons and calc_shape_sim_compare_classes_in_one_frame are comparing methods for Shape Similarity, where inner angle radiant sums would be compared; there are deprecated

    @param options: Dictionary with options set in main
    """
    options["timestamp_prog_end"] = time.time()
    results_dictionary = { }

    create_first_lines(options, results_dictionary)
   
    #calc_shape_similarity_compare_polygons(options, results_dictionary) # calc SSM_old by compare every polygon to the next exact same polygon in the next frame
    #calc_shape_sim_compare_classes_in_one_frame(options, results_dictionary) #calc SSM_old by compare Polygon to the polygons with the same class in one frame
    
    calc_SSM_illustration(options, results_dictionary)
    calc_timestamps(options, results_dictionary) #set timestamps
    write_settings(results_dictionary, options) #write settings to result dictionary
    write_results_file(results_dictionary, options["path_write_timestamps"]) #write results dictionary

  


def calc_SSM_illustration(options, rD):
    """
    calculate the shape similarity measure by using different methods; write the results direct to the results dictionary

    @param options: Dictionary with options set in main
    @param rD: results dictionary, where all results would be saved

    """
    #init different variables
    polygon_array = options["list_of_all_polygons"]
    fps = len(polygon_array)
    temp = 0

    val_arr_cars = []
    val_arr_motorcycle = []
    val_arr_trucks = []
    val_arr_oO = []

    val_arr_compared_ind_cars = []
    val_arr_compared_ind_motorcycle = []
    val_arr_compared_ind_trucks = []
    val_arr_compared_ind_oO = []

    number_of_compared_polygons = 0
    compare_polys = 0

    compared_polygons_cars = 0
    compared_polygons_motorcycle = 0
    compared_polygons_trucks= 0

    for frame in range(fps-1): #first loop to iterate over all frames (-1, because the actual frame must be compared with the next frame)

        if (len(polygon_array[frame])<= len(polygon_array[frame+1])): #if in the next frame more polygons than in the actual frame, the length must be setted to the minor number
                compare_polys = len(polygon_array[frame])
                number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame])
        else: 
            if (len(polygon_array[frame])> len(polygon_array[frame+1])): #if in the actual frame more polygons than in the next frame, the length must be setted to the minor number
                compare_polys = len(polygon_array[frame+1])
                number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame+1])

        for polygon in range(compare_polys): #second loop to iterate over all polygons in the frame

            if polygon_array[frame][polygon][3] == polygon_array[frame+1][polygon][3]: # if the class for the detected polygons are the same in the next frame; the SSM could be calculated
                match polygon_array[frame][polygon][3]:
                    case 2: #car
                        temp = calc_minor_SSM(polygon_array[frame][polygon][5], polygon_array[frame+1][polygon][5], options) #calculate the lowest SSM (classes must be the same for both frames)
                        val_arr_cars.append(temp[0]) #append the lowest SSM to an result array
                        val_arr_compared_ind_cars.append(temp[1]) # add the index of the lowest SSM to an result array
                        compared_polygons_cars = compared_polygons_cars + 1 #increase compared polygons cars by 1
                    case 3: #motorcycle, same to case 2
                        temp = calc_minor_SSM(polygon_array[frame][polygon][5], polygon_array[frame+1][polygon][5], options)
                        val_arr_motorcycle.append(temp[0])
                        val_arr_compared_ind_motorcycle.append(temp[1])
                        compared_polygons_motorcycle = compared_polygons_motorcycle + 1
                    case 7: #truck, same to case 2
                        temp = calc_minor_SSM(polygon_array[frame][polygon][5], polygon_array[frame+1][polygon][5], options)
                        val_arr_trucks.append(temp[0])
                        val_arr_compared_ind_trucks.append(temp[1])
                        compared_polygons_trucks = compared_polygons_trucks + 1
                    case _: # other class
                        temp = calc_minor_SSM(polygon_array[frame][polygon][5], polygon_array[frame+1][polygon][5],options) # the classes must be the same for both frames 
                        val_arr_oO.append([temp[0], polygon_array[frame][polygon][3]])
                        val_arr_compared_ind_oO.append([temp[1], polygon_array[frame][polygon][3]]) #append the values by an array; to differentiate between all other classes
                temp = 0    # for new iteration the temp variable must be set to 0

    detected_cars = len(val_arr_cars) #get the number of detected cars (car polygons) for all frames
    detected_motorcycle = len(val_arr_motorcycle) #same to line above only for motorcycle
    detected_trucks = len(val_arr_trucks) #same to line above only for trucks

    sorted_array_OO = sort_oO_arr_new(val_arr_oO) #sort oO Array and return sorted SSM sorted at class id

    write_statistics(rD, number_of_compared_polygons,ret_NoP(polygon_array), options["number_of_angles_bef_DCE"], options["number_of_compared_angles"]) #write statistics to result dictionary

    write_SSM_new(val_arr_cars,2,rD,fps, detected_cars, compared_polygons_cars) #write results to Dictionary
    write_SSM_new(val_arr_motorcycle,3,rD,fps, detected_motorcycle, compared_polygons_motorcycle) #write results to Dictionary
    write_SSM_new(val_arr_trucks,7,rD,fps, detected_trucks, compared_polygons_trucks) #write results to Dictionary

    for e in range(len(sorted_array_OO)): #iterate over all oO classes and write for every class the SSM to results dictionary
        write_SSM_new([sorted_array_OO[e][2]], sorted_array_OO[e][0],rD,fps,sorted_array_OO[e][1],sorted_array_OO[e][1])

    rD["el17"] = "emptyline"
    rD["el18"] = "emptyline"
    return 0   




def write_statistics(rD, number_of_compared_polygons, res_ret_NoP, NoP_bef_DCE, NoCP):
    """
    write calculated statistics at the result dictionary

    @param rD: results dictionary, where all results would be saved
    @param number_of_compared_polygons: int, which saved the number of all compared polygons in the program
    @param res_ret_NoP: array, which represent the numbers of all polygons and points/angles which are used in the program
    @param NoP_bef_DCE: int, which represent all points from all polygons, before DCE simplificated the polygons
    @param NoCP: int, which saved the number of all coompared angles/points while SSM is calculated
    """
    rD["el_T1"] = "emptyline"
    rD["Number of compared Polygons"] = number_of_compared_polygons
    rD["Number of all Polygons"] = res_ret_NoP[0]
    rD["el_T2"] = "emptyline"
    rD["number of compared angles/points"] = NoCP
    rD["number of angles/points"] = res_ret_NoP[1]
    rD["number of angles/points before DCE"] = NoP_bef_DCE
    rD["el_T3"] = "emptyline"

    


def write_SSM_new(arr, classid,rD,fps, detected, NoCP):
    """
    write calculated results at the results dictionary

    @param arr: array with results
    @param classid: int, which class id would be written
    @param rD: results dictionary, where all results would be saved
    @param fps: whole number of frames in the source video
    @param detected: number of detected objects
    @param NoCP: number of compared polygons for every class
    """
    if sum(arr) == 0 or detected == 0: #if detected or sum(arr) is 0; the following calcucated measures are wrong; would be printet as string as note
        string_not_right = " (Result is WRONG, because SSM is 0) "
    else:
        string_not_right = " "

    string_1 = "Shape Similarity Measure " + str(get_text_string(classid)) + " " + string_not_right
    string_2 = "Shape Similarity Measure (per FPS and Class) " + str(get_text_string(classid)) + " " + string_not_right #set text string for SSM divided by fps
    string_3 = "Shape Similarity Measure (per detected " + str(get_text_string(classid)) + ")" + string_not_right  #set text string for SSM divided by detections
    string_4 = "detected " + str(get_text_string(classid)) + string_not_right 

    if detected != 0: #if clause if detection = 0; dividing by 0 is not allowed
        res_raw = round(sum(arr),4)
        res_per_frame = round((sum(arr)/fps),4) #calculate SSM divided by fps round on 4 places
        res_per_obj = round((sum(arr)/detected),4) #calculate SSM divided by  detected objects round on 4 places
        string_empty_1 = str(np.random.randint(10000)) #set string for empty line
        string_empty_2 = str(np.random.randint(10000))

        rD[string_1] = str(res_raw)
        rD[string_2] = str(res_per_frame) #write calculated value at results dictionary,
        rD[string_3] = str(res_per_obj)  #write calculated value at results dictionary, 
        rD[string_4] = str(detected) + " per frame:"+ str(round(detected/fps,2)) 
        rD[string_empty_1] = "emptyline"
        rD[string_empty_2] = "emptyline"




def sort_oO_arr_new(val_arr_OO):
    """
    sorted a val array from other Object detections to different buckets, to calculate one SSM for every class
    simply method for the new SSM Calculate Method, cause there not so complex arrays;
    inspired by Bucket Sort

    @param val_arr_OO: all SSM for all oO Detections in all frames and over all oO classes
    @return buckets: 1 dim Array
    """
    buckets = []
    for i in range(len(val_arr_OO)): #iterate buckets, for every class which is in val_arr_OO
        if classbucket_exists(buckets, val_arr_OO[i][1]):
            buckets.append([val_arr_OO[i][1]])

    for i in range(len(val_arr_OO)): #fill buckets with all sum uped detected Objects from val_arr_oO array at the expected bucket
        for b in range(len(buckets)):
            if buckets[b][0] == val_arr_OO[i][1]:
                buckets[b].append(val_arr_OO[i][0])
    
    for i in range(len(buckets)): #iterate over buckets; and sum up all different detection numbers to one value
        temp = buckets[i][0]
        temp_sum = sum(buckets[i][1:len(buckets[i])])
        temp_range = len(buckets[i])-1
        buckets[i] = [temp, temp_range, temp_sum]
        
    return buckets #return buckets, example [[2,10,78.25]]; [Class, Detections, SSM]




def calc_minor_SSM(Poly1, Poly2, options):
    """
    function to calculate the minorist SSM value; permute the second array to get all possibilities of permutation between the two given polygons. Returns the lowest SSM value by all permutation and the index, (compared permutation index), where the lowest SSM is

    @param Poly1: 1-dim array
    @param Poly2: 1-dim array
    @param [min,ind]: 1-dim array 
    """
    SSM_arr = []  
    for ref in range(len(Poly1)):
        if len(Poly1) != 0 and len(Poly2) !=0:
            temp = compare_arrays(Poly1,Poly2, options)
            SSM_arr.append(temp[0])
            Poly2 = permute_arr(Poly2)
    if len(Poly1) != 0 and len(Poly2) !=0:
        min = np.min(SSM_arr)  
    else:
        return [0,0]
    ind = np.where(SSM_arr == min)

    if ind[0].size == 0:
        print("Error; minor SSM indic is not found (shape_sim_meas.py, calc minor SSM Method)")
        quit()
    else:
        ind = ind[0][0]
    return [min, ind]
    



def compare_arrays(arr1, arr2, options):
    """
    compare 2 given array arr1 and arr2. Calculate first the minor length of the two arrays, to get no 'out of bounce error'; at the FOR Loop it calculate the absolute difference between all values in the arrays. Appends the mathematic way of this calculation to an array

    @param arr1: 1 dim array
    @param arr2: 1 dim array
    @param options: Dictionary with options set in main
    @return: 2-dim array
    """
    value = 0
    val_arr = []
    arr_range = 0
    if len(arr1) != len(arr2): #if clause to get the lowest length by the two arrays
        if len(arr1) <= len(arr2):
            arr_range = len(arr1)
        elif len(arr2)<= len(arr1):
            arr_range = len(arr2)
    else:
        arr_range = len(arr1)
     
    options["number_of_compared_angles"] =  options["number_of_compared_angles"] + arr_range #add a statistics variable; to count all compared angles
 
    for i in range(arr_range):
        value = value + (np.abs(arr1[i][1]-arr2[i][1])) #calculate the SSM for one comparing between this arrays; absolute function to get a value that converge against 0
        val_arr.append([(str(arr1[i][0])+ "-" + str(arr2[i][0])),arr1[i][1]-arr2[i][1]])
  
    return [value, val_arr]




def permute_arr(arr):
    """
    function to permute an given array; copy the last element to the beginning of the given array to permute this

    @param arr: array with values
    @return arr: permuted array
    """
    len_arr = len(arr)-1
    temp = arr[len_arr]
    arr = np.delete(arr, len_arr, axis = 0)
    arr = np.insert(arr,0, temp, axis = 0)
    return arr




def calc_shape_similarity_compare_polygons(options, rD):
    """
    function that calculates the difference from the total angle sum of one image to the next. This difference is summed up and is the 'shape_similarity_measures' at the results dictionary.
    This difference is calculated from the comparision from every polygon to exact this polygon on the next frame.

    @param options: Dictionary with options set in main
    @param rD: Dictionary with all statistics data by the result video
    """
    shape_similarity_val = 0
    polygon_array = options["list_of_all_polygons"]

    temp = 0
    iterator = 0
    number_of_compared_polygons = 0
    for frame in range(len(polygon_array)-1): #iterate over all frames
        
        if (len(polygon_array[frame])<= len(polygon_array[frame+1])): #if in the next frame more polygons than in the actual frame, the length must be setted to the minor number
             compare_polys = len(polygon_array[frame])
             number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame])
        else: 
             if (len(polygon_array[frame])> len(polygon_array[frame+1])): #if in the actual frame more polygons than in the next frame, the length must be setted to the minor number
                  compare_polys = len(polygon_array[frame+1])
                  number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame+1])

        for polygon in range(compare_polys): #iterate over all polygon, range at the minor polygons numb er
            if polygon_array[frame][polygon][3] == polygon_array[frame+1][polygon][3]: #check if class id is the same
                temp = (polygon_array[frame][polygon][2]-polygon_array[frame+1][polygon][2]) #calculate Shape sim Mesaure
                iterator += 1
            if(temp<0): #set SSM to positive if its negative
                temp = temp * -1
            shape_similarity_val = shape_similarity_val + temp #sum up all differences for SSM
    #save the results at the result Dictionary        
    options["number_of_angles"]=  ret_NoP(polygon_array) 
    options["shape_similarity_measure"] = shape_similarity_val 

    rD["number of angles/points"] = str(ret_NoP(polygon_array)) 
    rD["Sum of the angle differences over all frames and polygons"] = str(round(shape_similarity_val,2)) + " rad / " + str(round(np.rad2deg(shape_similarity_val),2)) + " Degree " 
    rD["Average Angular deviation (SSM/Number_of_Polygons)"] =  str(round((shape_similarity_val / options["number_of_polygons"]),2)) +" / "+  str(round(np.rad2deg(shape_similarity_val / options["number_of_polygons"]),2)) + " Degree " 
    rD["deviation per angle (SSM/Number_of_angles)"] =  str(round((shape_similarity_val / options["number_of_angles"]),2))+ " rad / " + str(round(np.rad2deg(shape_similarity_val / options["number_of_angles"]),2)) + " Degree" 
    rD["el1"] = "emptyline"
    rD["detected polygons"] = str(options["number_of_polygons"]) 
    rD["number of compared polygons"] = str(number_of_compared_polygons)
    rD["Counter for same detected objects in two consecutive frames per frame"]: str(iterator)
    rD["el2"] = "emptyline"
    rD["el3"] = "emptyline"  




def calc_shape_sim_compare_classes_in_one_frame(options, rD):
    """
    calculate SSM in (one) Frame. iterate over all frames and runs other methods to calculate the SSM

    @param options: Dictionary with options set in main
    @param rD: Dictionary with all statistics data by the result video
    """
    polygon_array = options["list_of_all_polygons"]
    fps = len(polygon_array)

    val_arr_cars = []
    val_arr_motorcycle = []
    val_arr_trucks = []
    val_arr_oO = []
    detected_cars = []
    detected_motorcycle = []
    detected_trucks = []

    for frame in range(len(polygon_array)): #iterate over all array, which includes all polygons in all frames of the source video
        res = compare_polygons_in_frame(polygon_array[frame]) #runs the compare method
   
        val_arr_cars.append(sum(res[0][0])) #add the SSM to the val arr for class car (2)
        detected_cars.append(len(res[0][0]))
    
        val_arr_motorcycle.append(sum(res[1][0])) # same to case car
        detected_motorcycle.append(len(res[1][0]))       

        val_arr_trucks.append(sum(res[2][0])) #same to case car
        detected_trucks.append(len(res[2][0]))
      
        val_arr_oO.append(calc_SSM_oO(res[3][0], polygon_array[frame])) #another structure for array for other object detections
    
    detected_cars = sum(detected_cars) #sum up SSM Value Array to one value
    detected_motorcycle = sum(detected_motorcycle)
    detected_trucks = sum(detected_trucks)

    sorted_array_OO = sort_oO_arr(val_arr_oO) #sort oO Array and return sorted SSM sorted at class id

    write_SSM_CPF(val_arr_cars,2,rD,fps, detected_cars) #write results to Dictionary
    write_SSM_CPF(val_arr_motorcycle,3,rD,fps, detected_motorcycle) #write results to Dictionary
    write_SSM_CPF(val_arr_trucks,7,rD,fps, detected_trucks) #write results to Dictionary

    for e in range(len(sorted_array_OO)): #iterate over all oO classes and write for every class the SSM to results dictionary
        write_SSM_CPF([sorted_array_OO[e][2]], sorted_array_OO[e][0],rD,fps,sorted_array_OO[e][1])
    rD["el17"] = "emptyline"
    rD["el18"] = "emptyline"
    return 0   




def sort_oO_arr(val_arr_OO):
    """
    sorted a val array from other Object detections to different buckets, to calculate one SSM for every class

    @param val_arr_OO: all SSM for all oO Detections in all frames and over all oO classes
    @return buckets: 2 dim Array
    """
    buckets = []
    for i in range(len(val_arr_OO)): #iterate buckets, for every class which is in val_arr_OO
        for c in range(len(val_arr_OO[i])):
             if classbucket_exists(buckets, val_arr_OO[i][c][0]):
                buckets.append([val_arr_OO[i][c][0]])

    for i in range(len(val_arr_OO)): #fill buckets with all sum uped detected Objects from val_arr_oO array at the expected bucket
            for c in range(len(val_arr_OO[i])):
                for b in range(len(buckets)):
                    if buckets[b][0] == val_arr_OO[i][c][0]:
                        buckets[b].append(val_arr_OO[i][c][1])

    for i in range(len(buckets)): #iterate over buckets; and sum up all different detection numbers to one value
        temp = buckets[i][0]
        temp_sum = sum(buckets[i][1:len(buckets[i])])
        buckets[i] = [temp]
        buckets[i].append(temp_sum)

    for i in range(len(val_arr_OO)): #fill buckets with all sum uped SSMs from val_arr_oO array to the expected bucket
        for c in range(len(val_arr_OO[i])):
            for b in range(len(buckets)):
                if buckets[b][0] == val_arr_OO[i][c][0]:
                    buckets[b].append(val_arr_OO[i][c][2])

    for i in range(len(buckets)): #iterate over buckets and sum up all SSMs for every class
        temp = buckets[i][0]
        number_obj = buckets[i][1]
        temp_sum = sum(buckets[i][2:len(buckets[i])])
        buckets[i] = [temp, number_obj]
        buckets[i].append(temp_sum)
    return buckets #return buckets, example [[2,10,78.25]]; [Class, Detections, SSM]
            



def write_SSM_CPF(arr, classid,rD,fps, detected):
    """
    write calculated results at the results dictionary

    @param arr: array with results
    @param classid: int, which class id would be written
    @param rD: results dictionary, where all results would be saved
    @param fps: whole number of frames in the source video
    @param detected: number of detected objects
    """
    if sum(arr) == 0 or detected == 0: #if detected or sum(arr) is 0; the following calcucated measures are wrong; would be printet as string as note
        string_not_right = " (Result is WRONG, because SSM is 0) "
    else:
        string_not_right = " "

    string = "Shape Similarity Measure (per FPS and Class) " + str(get_text_string(classid)) + " " + string_not_right #set text string for SSM divided by fps
    string_2 = "Shape Similarity Measure (per detected " + str(get_text_string(classid)) + ")" + string_not_right  #set text string for SSM divided by detections
    string_3 = "detected " + str(get_text_string(classid)) + string_not_right 

    if detected != 0: #if clause if detection = 0; dividing by 0 is not allowed
        res_per_frame = round((sum(arr)/fps),4) #calculate SSM divided by fps round on 4 places
        res_per_obj = round((sum(arr)/detected),4) #calculate SSM divided by  detected objects round on 4 places
        string_empty_1 = str(np.random.randint(10000)) #set string for empty line
        string_empty_2 = str(np.random.randint(10000))

        rD[string] = str(res_per_frame) + "rad / " + str(round(np.rad2deg(sum(arr)/fps),4)) + " Degree" #write calculated value at results dictionary, in rad and degree
        rD[string_2] = str(res_per_obj) + "rad / " + str(round(np.rad2deg(sum(arr)/detected),4)) + " Degree" #write calculated value at results dictionary, in rad and degree
        rD[string_3] = str(detected) + " per frame:"+ str(round(detected/fps,2)) 
        rD[string_empty_1] = "emptyline"
        rD[string_empty_2] = "emptyline"




def calc_SSM_oO(res, frame):
    """
    calculates SSM at the other Objects Array

    @param  res: array from OO Method, which includes sum uped diffences for every class in every frame; would be sorted in this method
    @param frame:  array with all detected classids and objects
    """
    piof = get_indizes_and_classes(frame) #get example anglesums
    sum_oO= create_buckets(piof) #create buckes for sorting elements
    for i in range(len(res)): #iterate over result array
        if check_if_class_exists(res[i][1],piof): #if class exists
            for b in range(len(sum_oO)): #iterate over buckets and add all elements to the given bucket
                if sum_oO[b][0] == res[i][1]:
                    sum_oO[b].append(res[i][0]) 

    for i in range(len(sum_oO)): # sum up all SSMs in sumOO Array
        temp = sum_oO[i][0] #first element is the classid
        temp_sum = sum(sum_oO[i][1:len(sum_oO[i])])
        sum_oO[i] = [temp, calc_number(temp, res)] #first element is the classid, second the counter for with this class detected objects
        sum_oO[i].append(temp_sum)

    return sum_oO 




def calc_measure_in_one_frame(frame, polys_in_one_frame):
    """
    calculate all SSM in one frame for Cars, Motorcycles and Trucks, append this to an array and return; SSM is calculated by comparison of every anglesum with a example (first) anglesum of polygon for every another polygon

    @param frame: array with all detected polygons from this frame
    @param polys_in_one_frame: array with values  FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID at the example polygon
    @return result: as moredimensional array
    """
    temp_Cars = get_anglevalue_by_class(2,polys_in_one_frame)
    SSM_Cars = []

    temp_Motorcycle = get_anglevalue_by_class(3,polys_in_one_frame)
    SSM_Motorcycle =[]

    temp_Trucks = get_anglevalue_by_class(7,polys_in_one_frame)
    SSM_Truck = []

    temp_oO = 0
    SSM_oO=[]

    for p in range(len(frame)): #iterate over all elements/polygons in frame
        match frame[p][3]:
            case 2: #if class in frame = 2, the detected polygon is a car
                temp_Cars = temp_Cars - frame[p][2] #calc SSM
                if temp_Cars < 0: #Set SSM to positive value
                    temp_Cars = temp_Cars *-1
                SSM_Cars.append(temp_Cars) # append SSM to Array, which be sum up later
                temp_Cars = get_anglevalue_by_class(2,polys_in_one_frame) # set temp variable back to example anglesum value
            case 3: #same to case 2
                temp_Motorcycle = temp_Motorcycle - frame[p][2]
                if temp_Motorcycle < 0:
                    temp_Motorcycle = temp_Motorcycle *-1
                SSM_Motorcycle.append(temp_Motorcycle)
                temp_Motorcycle= get_anglevalue_by_class(3,polys_in_one_frame)
            case 7: #same to case 2
                temp_Trucks = temp_Trucks - frame[p][2]
                if temp_Trucks < 0:
                    temp_Trucks = temp_Trucks *-1
                SSM_Truck.append(temp_Trucks)
                temp_Trucks = get_anglevalue_by_class(7,polys_in_one_frame)
            case _: #if there is no car, motorcycle detected, the algorithm get the anglesum from this detected class, if it is available
                temp_oO = get_anglevalue_by_class(frame[p][3], polys_in_one_frame) #get anglesum from detected class if it is available
                if temp_oO == -1: #if there is not avalaible the method returns -1 and to the array get be append a 0 value
                    SSM_oO.append(0)
                else: #another case the calculate from SSM is the same at case 2
                    temp_oO = temp_oO - frame[p][2]
                    if temp_oO < 0:
                        temp_oO = temp_oO *-1
                    SSM_oO.append([temp_oO,frame[p][3]])
        
    res = [[SSM_Cars,2],[SSM_Motorcycle,3],[SSM_Truck,7],[SSM_oO]] #set a moredimensional array for results, with classids at the end
    return res #return this array




def write_settings(rD, options):
    """
    write the settings from the main.py file in the result dictionary

    @param options: Dictionary with options set in main
    @param rD: Dictionary with all statistics data by the result video
    """
    fps = int(get_fps(options["path_source_video"]))
    vid_in_s = len(options["list_of_all_polygons"])
    string_6 = str(vid_in_s/fps) + " / " + str(fps) + " / " + str(vid_in_s)
    
    rD["Path Directory"] = options["path_directory"]
    rD["Path Source Video"] = options["path_source_video"]
    rD["Path Write Video"] = options["path_write_video"]
    rD["Path Timestamps"] = options["path_write_timestamps"]
    rD["Videolength (in Sec.) / Frames per Second / Total Number of Frames"] = string_6
    rD["el14"] = "emptyline"
    rD["DCE Number of Points for Cars"] = options["NoP_Cars"]
    rD["DCE Number of Points for Motorcylce"] = options["NoP_Motorcycle"]
    rD["DCE Number of Points for Trucks"] = options["NoP_Truck"]
    rD["DCE Number of Points for other Objects"] = options["NoP_other_Object"]
    rD["el15"] = "emptyline"
    rD["YOLO Model"] = options["YOLO_model"]
    rD["YOLO Every Frame Version"] = options["yolo_every_frame"]
    rD["el16"] = "emptyline"
    rD["Save Timestamps"] = options["save_timestamps"]
    rD["Black Video"] = options["black_video"]
    rD["Black Boxes"] = options["black_bboxes"]
    rD["write_labels"] = options["write_labels"]
    rD["el17"] = "emptyline"
 



def calc_timestamps(options, rD):
    """
    calculte timestamps for the duration of the program parts, two different calculate methods must be used for every yolo method

    @param options: Dictionary with options set in main
    @param rD: Dictionary with all statistics data by the result video
    """
    if options["yolo_every_frame"] == True:
        rD["Duration Program"] = ret_timestampline(options, "prog")
        rD["Duration YOLO"] = str(round(options["timestamp_yolo_dur"],2)) + " ms"
        rD["Duration write_Outline(exclude DCE Calculation)"] = str(round((options["timestamp_write_outline_dur"]),2)) + " ms"
        rD["Duration DCE"] = str(round(options["timestamp_DCE_dur"],2)) + " ms"
        rD["Duration write_video"] = str(round((options["timestamp_write_video_dur"]),2)) + " ms"
        rD["el4"] = "emptyline"
        rD["Sum of individual variablels (must be the same as 'Duration Programm')"] = str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2))+" sec."
        rD["el5"] = "emptyline"
        rD["Attention"] = "Minimal deviations due to not exact timestamp setting"
        rD["Total sum of the angles"] = str(round(sum(options["angle_sums_images"]),2)) + " Degree"
        rD["el7"] = "emptyline"
        rD["el8"] = "emptyline"

    else:

        rD["Duration Program"] = ret_timestampline(options, "prog")
        rD["Duration YOLO"] = ret_timestampline(options, "yolo") 
        rD["Duration write_Outline(include DCE Calculation)"] = str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms"
        rD["Duration DCE"] = str(round(options["timestamp_DCE_dur"],2)) + " ms"
        rD["Duration write_video"] = ret_timestampline(options, "write_video")
        rD["el4"] = "emptyline"
        rD["Sum of individual variablels (must be the same as 'Duration Programm')"] =str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + " sec." 
        rD["el5"] = "emptyline"
        rD["Attention"] = "Minimal deviations due to not exact timestamp setting"
        rD["el6"] = "emptyline"
        rD["Total sum of the angles"] = str(round(sum(options["angle_sums_images"]),2)) + " Degree"
        rD["el7"] ="emptyline"
        rD["el8"] = "emptyline"
        



def calc_procent_deviation(options):
    """
    calculate the procent deviation and return this as string

    @param options: Dictionary with options set in main
    @return string
    """
    G = sum(options["angle_sums_images"]) #ground value
    W = options["shape_similarity_measure"]
    p = (W/G)*100
    value = round(p, 4)
    if value < 0:
        value = value*-1        
    string = str(value) + " %"
    return string




def ret_timestampline(options, string):
    """
    function that returns a timestamp string; transform timestamps to ms and minutes 

    @param options: Dictionary with options 
    @param string: Value for given options variable 
    @return string
    """
    time_in_ms = round((options["timestamp_"+string+"_end"]-options["timestamp_"+string+"_start"]) * 100, 2)
    time_in_s = round((time_in_ms /100), 2)
    time_in_min = round((time_in_s/60),2)
    if (time_in_s > 180):
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec /" + str(time_in_min)+" min," 
    else:
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec," 
    


    
def calc_number(classid, res):
    """
    calculates number of classids in a given result array (for counting the number of tracked objects)

    @param classid: int
    @param: res: result array with all detected classids and objects
    @returns temp: int 
    """
    temp = 0
    for i in range(len(res)):
        if classid == res[i][1]:
            temp = temp + 1
    return temp




def create_buckets(piof):
    """
    create buckets in a 2 dim array; a bucket for every classid; not for 2 (car), 3 (motorcycle), 7 (truck)

    @param piof: array with FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID
    @returns buckets: 2 dim array
    """
    buckets = []
    for i in range(len(piof)):
        if piof[i][3] != 2 and piof[i][3] != 3 and piof[i][3] != 7:
            buckets.append([piof[i][3]])
    return buckets




def check_if_class_exists(classid, piof):
    """
    check if a class in polygon_in_one_frame exists and returns a bool

    @param classid: int; selected class which anglesum would be returned
    @param piof: array with FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID
    @returns boolean
    """
    for i in range(len(piof)):
        if piof[i][3] == classid:
            return True
    return False




def compare_polygons_in_frame(frame):
    """
    this method calculates the example polygons for further calculation and gives this value to another method, that calculate this

    @param frame: frame array
    @return: res array from another method
    """
    polys_in_one_frame = get_indizes_and_classes(frame)
    res = calc_measure_in_one_frame(frame,polys_in_one_frame)
    return res




def get_text_string(class_id):
    """
    return a text string from a given class id with the individual score for every polygon 

    @param class_id = int to identify the class
    @return: string
    """
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category)




def get_anglevalue_by_class(classID, piof):
    """
    returns anglesum from a given class for a polygon_in_one_frame array

    @param classid: int; selected class which anglesum would be returned
    @param piof: array with FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID
    @returns int: anglesum
    """
    for i in range(len(piof)):
        if piof[i][3] == classID:
            return piof[i][2]
    return -1




def get_indizes_and_classes(frame):
    """
    returns example/first element of every class from a given frame 

    @param frame: array with classes and another values (FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID, outline [for polygon])
    @return: array with following values FrameNumber, Polygonnumer [at selected Frame], Anglesum, ClassID
    """
    class_and_ind = []
    for poly in range(len(frame)):
        temp = [frame[poly][0],frame[poly][1],frame[poly][2],frame[poly][3]]
        if(check_if_in_arr(temp,class_and_ind) == False):
            class_and_ind.append(temp)
    return class_and_ind




def check_if_in_arr(temp, class_and_ind):
    """
    returns false if an integer (class_id) is already in array, else return true

    @param: class_and_ind: array with data from frame, classid is at the third element
    @param: temp: int; classid, which would be checked if it available in class_and_ind param
    @return: boolean
    """
    if len(class_and_ind) == 0:
        return False
    else:
        for i in range(len(class_and_ind)):
            if temp[3] == class_and_ind[i][3]:
                return True
        return False    
    



def classbucket_exists(buckets_arr, classid):
    """
    check if a class in buckets array exists and returns a bool

    @param classid: int; selected class which anglesum would be returned
    @param buckets: array with different classids
    @returns boolean
    """
    for b in range(len(buckets_arr)):
        if buckets_arr[b] == classid:
            return False
    return True




def ret_NoP(polygon_array):
    """
    returns Number of points from all polygons in polygon array
    
    @param polygon_array: multidimensional array with data
    @return: NoP: integer
    """
    NoP = 0
    number_of_polygons = 0
    for frame in range(len(polygon_array)):
         number_of_polygons = number_of_polygons + len(polygon_array[frame])
         for polygon in range(len(polygon_array[frame])):
              NoP = NoP + len(polygon_array[frame][polygon][4])
    return [number_of_polygons, NoP]




def create_first_lines(options, rD):
    """
    write the first lines to the result dictionary

    @param options: Dictionary with options set in main
    @param rD: results dictionary
    """
    string_empty_1 = str(np.random.randint(10000)) #set string for empty line
    string_empty_2 = str(np.random.randint(10000))

    current_dateTime = datetime.datetime.now() #creates variable to save the finished time for the program

    if current_dateTime.day <10: #add to the beginning a zero, for better reading
        day = "0"+str(current_dateTime.day)
    else:
        day = str(current_dateTime.day)

    if current_dateTime.month <10: #similar above
        month = "0"+str(current_dateTime.month)
    else:
        month = str(current_dateTime.month)

    if current_dateTime.hour <10: #similar above
        hour = "0"+str(current_dateTime.hour)
    else:
        hour = str(current_dateTime.hour)

    if current_dateTime.minute <10: #similar above
        minute = "0"+str(current_dateTime.minute)
    else:
        minute = str(current_dateTime.minute)
    
    if current_dateTime.second <10: #similar above
        second = "0"+str(current_dateTime.second)
    else:
        second = str(current_dateTime.second)

    date = str(day)+"."+str(month)+"."+str(current_dateTime.year)
    time = str(hour)+":"+str(minute) + ":" + str(second)
    rD["Processed on"] = " "+  date + " at " + time
    rD[string_empty_1] = "emptyline"
    rD[string_empty_2] = "emptyline"




def write_results_file(results_dictionary, path):
    """
    write a txt file with the given result variable at a path.

    @param results_dictionary: dictionary
    @param path: Path, where the file would be written
    """
    with open(path, 'w') as f: 
        for key, value in results_dictionary.items(): 
            if value == "emptyline":
                f.write('\n')
            else:
                f.write('%s:%s\n' % (key, value))
    print("result successfully written")