import numpy as np
import time

def calc_shape_similarity(options):
    options["timestamp_prog_end"] = time.time()
    results_dictionary = { }
    calc_timestamps(options, results_dictionary)
    calc_shape_similarity_compare_polygons(options, results_dictionary)
    calc_shape_sim_compare_classes_in_one_frame(options, results_dictionary)
    write_settings(results_dictionary, options)
    write_results_file(results_dictionary, options["path_write_timestamps"])




def calc_shape_sim_compare_classes_in_one_frame(options, rD):
    shape_similarity_val = 0
    polygon_array = options["list_of_all_polygons"]
    fps = len(polygon_array)
    temp = 0
    iterator = 0
    val_arr_cars = []
    val_arr_motorcycle = []
    val_arr_trucks = []
    val_arr_oO = []
    for frame in range(len(polygon_array)):
        res = compare_polygons_in_frame(polygon_array[frame],rD)
        # print(res)
    
        # print(res[0][0])
        # print(res[1][0])
        # print(res[2][0])
        # print(res[3][0])
   
        val_arr_cars.append(sum(res[0][0]))
    
        val_arr_motorcycle.append(sum(res[1][0]))
       
        val_arr_trucks.append(sum(res[2][0]))
        print(frame)
        print("detectet oO")
        print(calc_SSM_oO(res[3][0], polygon_array[frame]))
        val_arr_oO.append(calc_SSM_oO(res[3][0], polygon_array[frame]))
        # print(frame)
        # print("oO")
       # print(res[3][0])
        
        # print("val_arr_cars")
        # print(val_arr_cars)
        # print("val_arr_trucks")
        # print(val_arr_trucks)
   
    # print("sum over frmaes")
    # print(val_arr_cars)
    # print("summe")
    # print(sum(val_arr_cars))
    # print(sum(val_arr_motorcycle))
    # print(sum(val_arr_trucks))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    #print(val_arr_oO)
    print("vallar")
    sorted_array_OO = sort_oO_arr(val_arr_oO)
    write_SSM_CPF(val_arr_cars,2,rD,fps)
    write_SSM_CPF(val_arr_motorcycle,3,rD,fps)
    write_SSM_CPF(val_arr_trucks,7,rD,fps)

    for e in range(len(sorted_array_OO)):
        write_SSM_CPF([sorted_array_OO[e][1]], sorted_array_OO[e][0],rD,fps)
    rD["el17"] = "emptyline"
    rD["el18"] = "emptyline"
    return 0   

def sort_oO_arr(val_arr_OO):
    print(val_arr_OO[0])
    buckets = []
    for i in range(len(val_arr_OO)):
        for c in range(len(val_arr_OO[i])):
             if classbucket_exists(buckets, val_arr_OO[i][c][0]):
                buckets.append([val_arr_OO[i][c][0]])

    # print("buckets")
    # print(buckets)
    # print("start filling buckets")
    for i in range(len(val_arr_OO)):
        for c in range(len(val_arr_OO[i])):
            for b in range(len(buckets)):
                if buckets[b][0] == val_arr_OO[i][c][0]:
                    buckets[b].append(val_arr_OO[i][c][1])
    # print("buckets filled")
    # print(buckets)
    # print("stop")
    for i in range(len(buckets)):
        temp = buckets[i][0]
        temp_sum = sum(buckets[i][1:len(buckets[i])])
        buckets[i] = [temp]
        buckets[i].append(temp_sum)
    # print(buckets)
    # print("stop")
    return buckets
            



def classbucket_exists(buckets_arr, classid):
    for b in range(len(buckets_arr)):
        if buckets_arr[b] == classid:
            return False
    return True

def write_SSM_CPF(arr, classid,rD,fps):
    string = "Shape Similarity Measure (per FPS and Class) " + str(get_text_string(classid)) + " "
    # print("arr")
    # print(arr)
    # print("sumarr")
    # print(sum(arr))
    res = round((sum(arr)/fps),4)
    rD[string] = str(res) + "rad / " + str(round(np.rad2deg(sum(arr)/fps),4)) + " Degree"


def calc_SSM_oO(res, frame):
    piof = get_indizes_and_classes(frame)
   # print(res)
    sum_oO= create_buckets(piof)
    for i in range(len(res)):
        if check_if_class_exists(res[i][1],piof):
            for b in range(len(sum_oO)):
                if sum_oO[b][0] == res[i][1]:
                    sum_oO[b].append(res[i][0]) 
    for i in range(len(sum_oO)):
        temp = sum_oO[i][0]
        temp_sum = sum(sum_oO[i][1:len(sum_oO[i])])
        sum_oO[i] = [temp]
        sum_oO[i].append(temp_sum)
    return sum_oO

def create_buckets(piof):
    buckets = []
    for i in range(len(piof)):
        if piof[i][3] != 2 and piof[i][3] != 3 and piof[i][3] != 7:
            buckets.append([piof[i][3]])
   # print(buckets)
    return buckets

def check_if_class_exists(classid, piof):
    for i in range(len(piof)):
        if piof[i][3] == classid:
            return True
    return False

def compare_polygons_in_frame(frame,rD):
    #print(frame)
    #print(frame[0][2],frame[0][3])
    polys_in_one_frame = get_indizes_and_classes(frame)
    #print(polys_in_one_frame)
    res = calc_measure_in_one_frame(frame,polys_in_one_frame,rD)
    return res

def calc_measure_in_one_frame(frame, polys_in_one_frame,rD):
    # print("measrue in one frame")
    # print(frame[0][3])
    # print(polys_in_one_frame[0][3])
    temp_Cars = get_anglevalue_by_class(2,polys_in_one_frame)
    SSM_Cars = []
    temp_Motorcycle = get_anglevalue_by_class(3,polys_in_one_frame)
    SSM_Motorcycle =[]
    temp_Trucks = get_anglevalue_by_class(7,polys_in_one_frame)
    SSM_Truck = []
    temp_oO = 0
    SSM_oO=[]

    for p in range(len(frame)):
        #if frame[p][3] == polys_in_one_frame[p][3]:
        # if polys_in_one_frame[p][3] == frame[p][3]:
        #     temp = temp + (polys_in_one_frame[p][2]-frame[p][2])
        match frame[p][3]:
            case 2:
              #  print("autovergleich")
                temp_Cars = temp_Cars - frame[p][2]
                if temp_Cars < 0:
                    temp_Cars = temp_Cars *-1
                SSM_Cars.append(temp_Cars)
                temp_Cars = get_anglevalue_by_class(2,polys_in_one_frame)
            case 3:
              #  print("motorradvergleich")
                temp_Motorcycle = temp_Motorcycle - frame[p][2]
                if temp_Motorcycle < 0:
                    temp_Motorcycle = temp_Motorcycle *-1
                SSM_Motorcycle.append(temp_Motorcycle)
                temp_Motorcycle= get_anglevalue_by_class(3,polys_in_one_frame)
            case 7: 
              #  print("truckvergleich")
                temp_Trucks = temp_Trucks - frame[p][2]
                if temp_Trucks < 0:
                    temp_Trucks = temp_Trucks *-1
                SSM_Truck.append(temp_Trucks)
                temp_Trucks = get_anglevalue_by_class(7,polys_in_one_frame)
            case _:
                temp_oO = get_anglevalue_by_class(frame[p][3], polys_in_one_frame)
                if temp_oO == -1:
                    SSM_oO.append(0)
                else:
                    temp_oO = temp_oO - frame[p][2]
                    if temp_oO < 0:
                        temp_oO = temp_oO *-1
                    SSM_oO.append([temp_oO,frame[p][3]])
               # print("andresobjektvergleich")
    # print("SSM")
    # print(SSM_Cars)
    # print(SSM_Truck)
    # print(SSM_Motorcycle)
    # print(SSM_oO) #Muss noch richtig generiert werden!!!
    res = [[SSM_Cars,2],[SSM_Motorcycle,3],[SSM_Truck,7],[SSM_oO]]
    # print(res)
  

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
    for i in range(len(piof)):
        if piof[i][3] == classID:
            return piof[i][2]
    return -1

def get_indizes_and_classes(frame):
    class_and_ind = []
    for poly in range(len(frame)):
        temp = [frame[poly][0],frame[poly][1],frame[poly][2],frame[poly][3]]
        #print(temp)
        if(check_if_in_arr(temp,class_and_ind) == False):
            class_and_ind.append(temp)
    #print(class_and_ind)
    return class_and_ind

def check_if_in_arr(temp, class_and_ind):
    if len(class_and_ind) == 0:
        return False
    else:
        for i in range(len(class_and_ind)):
            if temp[3] == class_and_ind[i][3]:
                return True
        return False    


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


def write_settings(rD, options):
    rD["Path Directory"] = options["path_directory"]
    rD["Path Source Video"] = options["path_source_video"]
    rD["Path Write Video"] = options["path_write_video"]
    rD["Path Timestamps"] = options["path_write_timestamps"]
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
    rD["write_labels"] = options["write_labels"]



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
        rD["Sum of individual variablels (must be the same as 'Duration Programm')"] = str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2))+" sec."
        rD["el5"] = "emptyline"
        rD["Attention"] = "Minimal deviations due to not exact timestamp setting"
        rD["Total sum of the angles"] = str(round(sum(options["angle_sums_images"]),2)) + " Degree"
        rD["el7"] = "emptyline"
        rD["el8"] = "emptyline"
    else:
        rD["Duration Program"] = ret_timestampline(options, "prog")
        rD["Duration YOLO"] = ret_timestampline(options, "yolo") + " ms"
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




def calc_shape_similarity_angles(options):
    shape_similarity_val = 0
    for i in range(len(options["angle_sums_images"])-1):
         temp =  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]
         if(temp<0):
                    temp = temp * -1
         shape_similarity_val = shape_similarity_val + temp
    options["shape_similarity_measure"] = shape_similarity_val