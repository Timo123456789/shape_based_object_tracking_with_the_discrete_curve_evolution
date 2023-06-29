
def calc_shape_similarity(options):
    calc_shape_similarity_compare_polygons(options)
    calc_shape_similarity_angles(options)




def calc_shape_similarity_angles(options):
    shape_similarity_val = 0
    for i in range(len(options["angle_sums_images"])-1):
         shape_similarity_val = shape_similarity_val +  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]
    options["shape_similarity_measure"] = shape_similarity_val
    print("shape_similarity_measures_anlge calculated")
    print(str(shape_similarity_val))




def calc_shape_similarity_compare_polygons(options):
    """
    function that calculates the difference from the total angle sum of one image to the next. This difference is summed up and is the 'shape_similarity_measures'

    @param options: Dictionary with options set in main
    """
    shape_similarity_val = 0
    polygon_array = options["list_of_all_polygons"]


    for frame in range(len(polygon_array)-1): 
        if(len(polygon_array[frame]) == len(polygon_array[frame+1])):
            for polygon in range(len(polygon_array[frame])):
                temp = (polygon_array[frame][polygon][2]-polygon_array[frame+1][polygon][2])
                shape_similarity_val = shape_similarity_val + temp
    options["shape_similarity_measure"] = shape_similarity_val
    print("shape_similarity_measures_compare_polys calculated")
    print(str(shape_similarity_val))









def write_results_file(results):
    f = open( r'Code\YOLO\temp\temp.txt', 'w' )
    f.write(repr(results))
    f.close()
