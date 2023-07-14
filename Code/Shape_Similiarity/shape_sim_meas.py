import numpy as np

def calc_shape_similarity(options):

    calc_shape_similarity_compare_polygons(options)
    calc_shape_similarity_angles(options)




def calc_shape_similarity_angles(options):
    shape_similarity_val = 0
    for i in range(len(options["angle_sums_images"])-1):
         temp =  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]
         if(temp<0):
                    temp = temp * -1
         shape_similarity_val = shape_similarity_val + temp
    options["shape_similarity_measure"] = shape_similarity_val




def calc_shape_similarity_compare_polygons(options):
    """
    function that calculates the difference from the total angle sum of one image to the next. This difference is summed up and is the 'shape_similarity_measures'

    @param options: Dictionary with options set in main
    """
    shape_similarity_val = 0
    polygon_array = options["list_of_all_polygons"]

    write_results_file(polygon_array)
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
    print("shape_similarity_measures_compare_polys calculated")
    print(" ")
    print("Sum of the angle differences over all frames and polygons: "+str(round(shape_similarity_val,2)) + " rad / " + str(round(np.rad2deg(shape_similarity_val),2)) + " Degree ")
    print("Average Angular deviation (Sum divided by Number of Polygons): " + str(round((shape_similarity_val / options["number_of_polygons"]),2)) +" / "+  str(round(np.rad2deg(shape_similarity_val / options["number_of_polygons"]),2)) + " Degree ")
    print(" ")
    print("detected angles/points: "+str(options["number_of_angles"]))
    print("deviation per angle (Sum divided by number of angles): " + str(round((shape_similarity_val / options["number_of_angles"]),2))+ " rad / " + str(round(np.rad2deg(shape_similarity_val / options["number_of_angles"]),2)) + " Degree")
    print(" ")
    print("detected polygons: "+str(options["number_of_polygons"]))
    print("number of compared polygons: " + (str(number_of_compared_polygons)))
    print("Counter for same detected objects in two consecutive frames per frame: " + str(iterator)) #Counter for the number of the same detected objects in two consecutive frames 
    print(" ")
    print(" ")



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




def write_results_file(results):
    """
    write a txt file with the given result variable at a path.

    @param results: string
    """
    f = open( r'Code\YOLO\temp\temp_polyarr_indiv.txt', 'w' )
    f.write(repr(results))
    f.close()
