import numpy as np
import time

def calc_shape_similarity(options):
    options["timestamp_prog_end"] = time.time()
    results_dictionary = { }
    calc_timestamps(options, results_dictionary)
    calc_shape_similarity_compare_polygons(options, results_dictionary)
    calc_shape_similarity_angles(options)
    write_results_file(results_dictionary, r'Code\vid_examples\evaluation\test3.txt')




def calc_shape_similarity_angles(options):
    shape_similarity_val = 0
    for i in range(len(options["angle_sums_images"])-1):
         temp =  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]
         if(temp<0):
                    temp = temp * -1
         shape_similarity_val = shape_similarity_val + temp
    options["shape_similarity_measure"] = shape_similarity_val




def calc_shape_similarity_compare_polygons(options, rD):
    """
    function that calculates the difference from the total angle sum of one image to the next. This difference is summed up and is the 'shape_similarity_measures'

    @param options: Dictionary with options set in main
    """
    shape_similarity_val = 0
    polygon_array = options["list_of_all_polygons"]

    temp = 0
    iterator = 0
    number_of_compared_polygons = 0
    for frame in range(len(polygon_array)-1):
        
        if (len(polygon_array[frame])<= len(polygon_array[frame+1])):
             compare_polys = len(polygon_array[frame])
             number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame])
        else: 
             if (len(polygon_array[frame])> len(polygon_array[frame+1])):
                  compare_polys = len(polygon_array[frame+1])
                  number_of_compared_polygons = number_of_compared_polygons + len(polygon_array[frame+1])
        for polygon in range(compare_polys):
            if polygon_array[frame][polygon][3] == polygon_array[frame+1][polygon][3]:
                temp = (polygon_array[frame][polygon][2]-polygon_array[frame+1][polygon][2])
                iterator += 1
            if(temp<0):
                temp = temp * -1
            shape_similarity_val = shape_similarity_val + temp
            
    options["number_of_angles"]=  ret_NoP(polygon_array) 
    options["shape_similarity_measure"] = shape_similarity_val 

    rD["number of angles/points"] = str(ret_NoP(polygon_array)) 
    rD["Sum of the angle differences over all frames and polygons"] = str(round(shape_similarity_val,2)) + " rad / " + str(round(np.rad2deg(shape_similarity_val),2)) + " Degree " 
    rD["Average Angular deviation (Sum divided by Number of Polygons)"] =  str(round((shape_similarity_val / options["number_of_polygons"]),2)) +" / "+  str(round(np.rad2deg(shape_similarity_val / options["number_of_polygons"]),2)) + " Degree " 
    rD["deviation per angle (Sum divided by number of angles)"] =  str(round((shape_similarity_val / options["number_of_angles"]),2))+ " rad / " + str(round(np.rad2deg(shape_similarity_val / options["number_of_angles"]),2)) + " Degree" 
    rD["el1"] = "emptyline"
    rD["detected polygons"] = str(options["number_of_polygons"]) 
    rD["number of compared polygon"] = str(number_of_compared_polygons)
    rD["Counter for same detected objects in two consecutive frames per frame"]: str(iterator)
    rD["el2"] = "emptyline"
    rD["el3"] = "emptyline"  





def ret_NoP(polygon_array):
    """
    returns Number of points from all polygons in polygon array
    
    @param polygon_array: multidimensional array with data
    @return: NoP: integer
    """
    NoP = 0
    for frame in range(len(polygon_array)):
         for polygon in range(len(polygon_array[frame])):
              NoP = NoP + len(polygon_array[frame][polygon][4])
    return NoP




def write_results_file(results_dictionary, path):
    """
    write a txt file with the given result variable at a path.

    @param results: string
    """
    print(results_dictionary)
    with open(path, 'w') as f: 
        for key, value in results_dictionary.items(): 
            if value == "emptyline":
                f.write('\n')
            else:
                f.write('%s:%s\n' % (key, value))
    print("result successfully written")







def calc_timestamps(options, rD):
    if options["yolo_every_frame"] == True:
        rD["Duration Program"] = ret_timestampline(options, "prog")
        rD["Duration YOLO"] = str(round(options["timestamp_yolo_dur"],2)) + " ms"
        rD["Duration write_Outline(exclude DCE Calculation)"] = str(round((options["timestamp_write_outline_dur"]),2)) + " ms"
        rD["Duration DCE"] = str(round(options["timestamp_DCE_dur"],2)) + " ms"
        rD["Duration write_video"] = str(round((options["timestamp_write_video_dur"]),2)) + " ms"
        rD["el4"] = "emptyline"
        rD["Sum of individual variablels (must be the same as 'Duration Programm'):"] = str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2))+" sec."
        rD["el5"] = "emptyline"
        rD["Attention"] = "Minimal deviations due to not exact timestamp setting"
        rD["Total sum of the angles:"] = str(round(sum(options["angle_sums_images"]),2)) + " Degree"
        rD["el7"] = "emptyline"
        rD["el8"] = "emptyline"
    else:
        rD["Duration Program"] = ret_timestampline(options, "prog")
        rD["Duration YOLO"] = ret_timestampline(options, "yolo") + " ms"
        rD["Duration write_Outline(include DCE Calculation)"] = str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms"
        rD["Duration DCE"] = str(round(options["timestamp_DCE_dur"],2)) + " ms"
        rD["Duration write_video"] = ret_timestampline(options, "write_video")
        rD["el4"] = "emptyline"
        rD["Sum of individual variablels (must be the same as 'Duration Programm'):"] =str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + " sec." 
        rD["el5"] = "emptyline"
        rD["Attention"] = "Minimal deviations due to not exact timestamp setting"
        rD["el6"] = "emptyline"
        rD["Total sum of the angles:"] = str(round(sum(options["angle_sums_images"]),2)) + " Degree"
        rD["el7"] ="emptyline"
        rD["el8"] = "emptyline"
        
def save_timestamps_as_file_yolo_result(options):
    """
    function to save timestamps when 'yolo_result_version' is selected

    @param options: Dictionary with options set in main
    """
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " +ret_timestampline(options, "yolo")+ '\n'+"Duration write_Outline(include DCE Calculation) "+str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ +ret_timestampline(options, "write_video") + '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n'+ calc_procent_deviation(options) + '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2)) +'\n' 
        
    f.write(str(results))
    print("timestamps saved")
    print("Processing Time:"+ ret_timestampline(options, "prog"))
    f.close()
    return 0

def save_timestamps_as_file_yolo_every_frame(options):
    """
    function to save timestamps when 'yolo_every_frame' is selected

    @param options: Dictionary with options set in main
    """
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " + str(round(options["timestamp_yolo_dur"],2))+" ms" +'\n'+"Duration write_Outline(exclude DCE Calculation) "+str(round((options["timestamp_write_outline_dur"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ + str(round((options["timestamp_write_video_dur"]),2))+ '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n' +calc_procent_deviation(options)+ '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2)) +'\n' 
        
    f.write(str(results))
    print("timestamps saved")
    print("Processing Time:"+ ret_timestampline(options, "prog"))
    f.close()
    return 0


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

