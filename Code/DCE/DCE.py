"""
DCE Code File for a prototypical implementation for the combination of "You Only Look Once" (YOLO) (Redmon, 2016, doi: 10.1109/CVPR.2016.91 ) (Vers. YOLOv8x, Ultralytics, 2023) and Discrete Curce Evolution (DCE) (Latecki, 1999, doi: 10.1006/cviu.1998.0738 ); based on hypothesis by Dorr, Latecki and  Moratz (2015, doi: 10.1007/978-3-319-23374-1_7 )

Calculate the Discrete Curve Evolution for polygon up to a fixed limit

Must be used with the files: Main.py, yolo_every_frame.py, yolo_result_version.py, yolo_segementation.py, shape_sim_meas.py

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
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import math
import pandas
import time




def simplify_polygon_k_with_angle(arr, final_number_of_points, options):
    """
    choose the given DCE run method, standard method is the fast way
    K Calculation with using angles and distances

    @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
    @param final_number_of_points: int for the number of points of the returned polygon
    @return array:  which was simplified to the given number of points
    """
    #return simplify_polygon_k_with_angle_old(arr, final_number_of_points, options)
    return simplify_polygon_fast_sec(arr, final_number_of_points)




def simplify_polygon_fast_sec(arr, fNoP):
    """
    faster method for calculating the DCE; here are calcualted the k values only for the considered point and the point before. 
    Decrease the points of the polygon with the DCE Method to the given number of points

    @param arr: Polygon (as Geopanda.Geoseries Object)
    @param fNoP: final number of points, if the polygon has this number of points this method terminate
    @return array: 2-dim array, with pixel values
    """
    DCE_Polygon = create_Polygon_from_array(arr) #create a Geopanda.Geoseries Object from the given array; to calculate the k value with the DCE Method
    NoP = get_number_of_points(DCE_Polygon) #get the actual number of points from the polygon
   
    if NoP <= fNoP: #if clause to return the polygon directly when the given polygon has fewer points than required
        return polygon_to_pixels(DCE_Polygon)
    k_val_arr = calc_k_for_all_points(DCE_Polygon) #init the k value array with calculate the k value for all points on the polygon
    sort_arr = np.asarray(k_val_arr, dtype="float") #cast the k value array to a numpy array for further calculations
    sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="quicksort")] #sort this array to get the lowest k value and their index

    while(len(sort_arr)>= fNoP): #if the polygon has more points than required by fNoP; the loop must be run
        indic = int(sort_arr[0][0]) #indic is always the first element of the sorted array
 
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic) #delete the point with the lowest k value from the polygon
        NoP_temp = get_number_of_points(DCE_Polygon) #get the actual number of points from the polygon 

        if indic == 0: # if the index is 0; the k value for the before point must be the last point on the polygon; the actual point is the first 
            k_bef = calc_k_with_points(DCE_Polygon, (NoP_temp-1),0, (NoP_temp-2)) #calculate the k value for the last point on polygon  #scheme: (Polygon, Index of (considered) last point on the polygon, 0 for the first neighbour at this point, and the index for the second neigbour at this point (the point 2 indices before last point))
            k_act = calc_k_with_points(DCE_Polygon, 0,(NoP_temp-1), 1 ) #calculate the k value for the considerd/actual point of the polygon #scheme: (Polygon, Index of the (considered) first point on the polygon, index from the last point of the polygon (as first neighbour), 1 as index for the second neighbour (point after the considered point))
        else: #if index is not 0; there would be calculate normally

            if indic-1 == 0: #if index decreased by 1 is 0; the k_value for the point before must be the last point on the polygon
                k_bef = calc_k_with_points(DCE_Polygon, 0,1, (NoP_temp-1))  #calculate k for the point before the considered point  #scheme: (Polygon, 0 as the considered/acutal point of the polygon, 1 as the index for the first neigbour (point after the considered point); and the last point on the polygon as second neigbour)
            else: #other case if indic+1 is bigger than the number of points at the polygon / in the array
                if indic+1 > NoP_temp: #if case when indic+1 is bigger than the number of points at the polygon / in the array
                    k_bef = calc_k_with_points(DCE_Polygon, indic-1, 0, indic) #calculate k for the point before the considered point #Schema: (Polygon, indic-1 for the actual/considered point, who would be k calculated, 0 for the first neighbour (after the considered point indic-1), indic for the point before the considered point (as seocnd neighbour))
                else: #if this is not the case k_bef would be calculated normaly 
                    k_bef = calc_k_with_points(DCE_Polygon, indic-1, indic, indic-2) #calculate k for the point before the considered point #Schema: (Polygon, indic-1 for the actual/considered point, who would be k calculated; indic for the first neighbour (after the considered point indic-1), indic-2 for the second neigbour (before the considered point))

            if indic+1 > NoP_temp: #if case if indic increase by 1 is bigger than the number of points at the polygon / in the array
                k_act = calc_k_with_points(DCE_Polygon,indic-1, 0, indic-2) #calculate k for the point, which is the considered point #Schema: (Polygon, indic-1 for the actual/considered point, who would be k calculated; 0 for the first neigbour (after the considered point indic-1), indic -2 for the second neigbour (before the considered point))
            else: #if this is not the case, k would be calculated normally
                k_act = calc_k_with_points(DCE_Polygon,indic, indic-1, indic+1) #calculate k for the point, which is the considered point #Schema: (Polygon, indic for the actual/considered point, who would be k calculated; indic-1 for the first neigbour (before the considered point), indic+1 for the second neighbour (after the considered point))     
   
        sort_arr = update_sort_array_sec(sort_arr,indic,k_bef[0], k_act[0],DCE_Polygon) #update the sort array with the calculated k values

        if (get_number_of_points(DCE_Polygon) == fNoP): #exception if the polygon has reached the final number of points fNoP
            return polygon_to_pixels(DCE_Polygon) #convert the polygon to a array with pixels and return

    return polygon_to_pixels(DCE_Polygon) #convert the polygon to a array with pixels and return




def update_sort_array_sec(sort_arr, indic, k_bef, k_act, p):
    """
    Update the array with the given variables and at the given indices

    @param sort_arr: 2-dim Array, with all k values and indices for the polygon p
    @param indic: actual index for the calculated k value on the polygon p
    @param k_bef: k value for the point (index-1) before index; calulated in other method
    @param k_act: k value for the point (index) at index; calulated in other method
    @param p: Polygon (as Geopanda.Geoseries Object)
    @return arr: 2 dim array, with updatet values on 2 indices
    """
    NoP_Poly = get_number_of_points(p) #get the actual number of points from the polygon
   
    sort_arr = np.delete(sort_arr, 0, axis = 0) #delete the lowest k value from the (sorted) array
    temp = sort_arr[np.argsort(sort_arr[:,0], kind="quicksort")] #temp variable, where the 'new' sorted array with the lowest value at the top is saved
    
    new_val_arr = np.array([indic, k_act]) #variable for the new k_value at the considered index
    sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0) #add the considered index and their k value to the temp variable
    temp = sort_arr[np.argsort(sort_arr[:,0], kind="quicksort")] #sort the temp variable, to get the lowest value at the top
    
    #if clause for updating the values
    if indic == 0:  #if clause, for the case that index is the first point in the polygon 
        temp[NoP_Poly-1][1] = k_bef #the k value before the index in this case, is the last point on polygon p
    else: #if this is not the case, there values updatet normally
        upd_indic = np.where(np.isin(temp[:,0], indic-1)) #search the index on the temp array, where the value (index-1) is saved
        upd_indic = int(upd_indic[0][0]) #cast this value to an int
        temp[upd_indic][1] = k_bef #update the k value to the given  new k value
    
    #if clause for deleting the redundant value
    if indic+1 == NoP_Poly: #if clause, for the case that the index is teh last point of the polygon
        del_ind = len(sort_arr)-1 #get the index of the last value in the array
        temp = np.delete(temp, del_ind, axis = 0) #delete the last value from array
    else: #if this is not the case, the value are deleted normally
        del_ind = np.where(np.isin(temp[:,0], indic+1)) #search the index where the value is, that would be deleted
        
        if del_ind[0].size == 0: #if there is no value found, the last element of the array would be deleted
            temp = np.delete(temp, (len(sort_arr)-1), axis = 0)
        else: #case for found a value
            del_ind = del_ind[0][0] #cast the founded value to an int
            temp = np.delete(temp, del_ind, axis = 0) #delete the founded value on this index

    if indic != (len(sort_arr)-1): #if clause to decrease the index on all values in the sort array, if there index is bigger than the deleted index
        for i in range(len(temp)): #iterate over the whole array
            if temp[i][0]>del_ind: #if the index is bigger than the deleted index
                temp[i][0] = temp[i][0]-1 #decrease the index value by 1
   
    if len(temp) != get_number_of_points(p): #exception handler; the array and the polygon must be have the same number of values always
        print("Error; Array and Number of points in the polygon must be have the same number of values always")
        quit()
    return temp[np.argsort(temp[:,1], kind="quicksort")] #return the updated array




def calc_k_for_all_points(p):
    """
    returns an array with the k value for every point/index on the polygon p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return array: 2-dim array with [[index, k_value],...]
    """
    NoP = get_number_of_points(p)
    temp_k_val_arr = []
    for i in range(NoP):
        if i == 0:
            temp = calc_k_with_points(p,i,1, (NoP-1))
            temp_k_val_arr.append([i,temp[0]])
        else:
            temp = calc_k_with_points(p,i,i+1,i-1)
            temp_k_val_arr.append([i,temp[0]])
    return temp_k_val_arr






def get_lowest_k(p, options):
    """
    returns lowest k value for polygon p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return k: calculated lowest k value in p as int
    """
    NoP = get_number_of_points(p)
    k_array = 0
    index_for_point_on_k = -1
    for i in range(NoP):
        if i==0:
            k_array = calc_k_with_points(p,i,(NoP-1),1)
            index_for_point_on_k = 0
        else:
            if i==NoP:
                break
            scnd_k_array = calc_k_with_points(p,i,(i+1),(i-1))

            if scnd_k_array[0]<=k_array[0]:
                k_array[0] = scnd_k_array[0]
                index_for_point_on_k = i
    return [index_for_point_on_k,k_array[0]]




def calc_k_with_points(polygon,p,s1,s2):
    """
    returns K Value calculated based on Latecki and Lakaemper, with three Points.
    The first linesegment is from p to s1 (p,s1) and the second linesegment is form p to s2 (p,s2)
    Angle calculation must be sum up, because there are two angles to get the hole angle from s1 to s2.

    @param polygon: Polygon, created with Geopanda
    @param p: Point for which k is calculated
    @param s1: Point which describes the end of the first line from p
    @param s2: Point which describes the end of the second line from p
    @returns k: as Int

    Source Code; simliar implementation by Latecki/Opfer, 2002 : https://cis.temple.edu/~latecki/Software/Evo.zip
    """
    angle = get_angle_two_lines(polygon,p,s1,s2)
    dist_between_p_s1 = calc_distance_between_two_points(polygon,p,s1)
    dist_between_p_s2 = calc_distance_between_two_points(polygon,p,s2)

    k =  (angle*dist_between_p_s1*dist_between_p_s2)/(dist_between_p_s1+dist_between_p_s2)
    return [k, angle]




def get_sum_of_angles(outline):
    """
    returns the sum of all angles in a given polygon

    @param outline: 2 dim array, as tupel eg. [[2,1],[3,6],[5,8],..]
    @returns sum_of_angles: as Int
    """
    sum_of_angles = 0
    cop_outline = np.array(outline, dtype=  'int')
    cop_outline = cop_outline[0]
    angle_separated = []

    p = create_Polygon_from_array(cop_outline)

    NoP = get_number_of_points(p)
    for i in range(NoP):
        if i==0:
            temp = get_angle_two_lines(p,i, (NoP-1),1)
            sum_of_angles = sum_of_angles + temp
            angle_separated.append([i, temp])
        else:
            temp2 = get_angle_two_lines(p,i, (i+1), (i-1))
            sum_of_angles = sum_of_angles + temp2
            angle_separated.append([i, temp2])


    return [sum_of_angles, angle_separated]




def delete_point_from_polygon(p,index_of_point):
    """
    returns a polgyon p, where a point has been deleted

    @param p: Polygon (as Geopanda.Geoseries Object)
    @param index_of_point: Index for the point, which would be deleted
    @return shrink_poly: Polygon (as Geopanda.Geoseries Object) without point on index 'index_on_point'
    """
    array = get_array_with_points(p) 
    array.pop(index_of_point)
    shrink_poly = create_Polygon_from_array(array)

    return shrink_poly




def create_Polygon_from_array(arr):
    """
    create a Geopanda Geoseries Object from an given array

    @param arr: 2 dim Array of points (as tupel); like [[0,1],[0,2],..]
    @return p: Geopanda.Geoseries Object

    """
    polygon = Polygon(arr)
    p = gpd.GeoSeries(polygon)
    return p




def get_array_with_points(p):
    """
    returns an Array of Points in p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return array of points: which are in given Polygon p

    """
    NoP = get_number_of_points(p)
    array_of_points = []
    k_value = 0
    for i in range(NoP):
        array_of_points.append(p[0].exterior.coords[i])

    return array_of_points




def get_number_of_points(p):
    """
    returns number of points in a polygon p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return pointcounter: Number of points in Polygon p as int
    """
    pointcounter = 0
    for i in p[0].exterior.coords:
        pointcounter = pointcounter + 1
    pointcounter = pointcounter-1
    return pointcounter




def get_angle_two_lines(polygon,p,s1,s2):
    """
    returns angle in degree between two lines

    @param polygon: Polygon (as Geopanda.Geoseries Object)
    @param p1: Point Object from there the angle would be calculated
    @param s1: Point Object from p1 to s1 from there the angle would be calculated
    @param s2: Point Object from p1 to s2 from there the angle would be calculated
    @return radiant in int

    Source: https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2
    """
    p = polygon[0].exterior.coords[p]
    s1 = polygon[0].exterior.coords[s1]
    s2 = polygon[0].exterior.coords[s2]

    #Following is the answer of Bing Bot for get a python function to calculate Angels between two poinst (minor changes for this use case)
    # v1 = [s1[0]-p[0],s1[1]-p[1]]
    # v2 = [s2[0]-p[0],s2[1]-p[1]]
    # angle = np.degrees(np.arctan2(np.cross(v1,v2), np.dot(v1,v2)))
    # if angle < 0:
    #     angle = angle * -1

    #this code is from Source above
    x = np.array([p[1],p[0],s1[1],s1[0]])
    y = np.array([p[1],p[0],s2[1],s2[0]])

    val_arr = np.arctan2(y,x)*180/np.pi
    val_arr_sum = sum(val_arr)

    #here you can change which method is used
    #return np.deg2rad(angle)
    return np.deg2rad(val_arr_sum)




def get_selected_point(p,i):
    """
    returns  point at index i from a given Polgon

    @param p = Polygon (as Geopanda.Geoseries Object)
    @return Point = Tuple from Point at index i on p
    """
    return Point(p[0].exterior.coords[i])




def calc_distance_between_two_points(p, point1, point2):
    """
    calculate distance between two Points

    @param p: Polygon (as Geopanda.Geoseries Object)
    @param point1: Point 1 which calculate distance from
    @param point2: Point 2 which calculate distance to
    @return dist: Distance between Point1 and Point2 in p
    """
    p1 = Point(p[0].exterior.coords[point1])
    p2 = Point(p[0].exterior.coords[point2])
    dist = p1.distance(p2)
    return dist




def readtextfile(path):  #
    """
    read a given textfile from path

    @param path: Path where the reading file is located
    @returns Geoseries Polygon: which are created from array

    Source data:  https://www.opengeodata.nrw.de/produkte/geobasis/vkg/dvg/dvg2/
    """
    test = pandas.read_table(path, delimiter=';')
    array = convert_table_in_array(test)
    return create_Polygon_from_array(array)




def convert_table_in_array(t):
    """
    Convert a given table to an arrray

    @param t: table with columns, which are named with 'x' and 'y'
    @return a: array with points from table as tuple
    """
    RowCount = len(t)
    a = []
    for i in range(RowCount):
        a.append((t.iloc[i]["x"], ((t.iloc[i]["y"]))))
    return a




def choosePolygon(x):
    """
    Function which is used, when a simple Polygon is choosen for testrun

    @param x: Selected the Polygon with this number
    @return p: return p as geopanda.geoseries object which includes one Polygon Object
    """
    polygon1 = Polygon([    (1,1),(0,3),(2,4),
                            (5,5),(4,3),(4,1)
                    ])
    polygon2 = Polygon([    (1,2),(2,1),(3,1),
                            (4,1),(5,2),(4,3),
                            (3,6),(2,3)
                    ])
    polygon3= Polygon([     (3,1),(4,1),(5,1), (6,1),(7,1),(8,1), (9,2),(8,3),(7,4),
                            (8,5),(9,6),(10,7),(11,8),(8,7),(6,7),(5,9),(8,10),(7,11),
                            (6,12),(5,11),(4,11),(3,11),(2,11),(0,10),(2,9),(2,8),(2,7),
                            (1,6),(1,5),(3,4),(1,3),(2,2)
    ])
    if x == 1:
        p = gpd.GeoSeries(polygon1)

    if x == 2:
        p = gpd.GeoSeries(polygon2)
    if x == 3:
        p = gpd.GeoSeries(polygon3)
    return p




def plot_GS_polygon(p, index, write_path):
    """
    Plot a given Polygon at the folderpath 'path' with the indexnumber 'index' in the filename.
    Plot the polygon as PNG File

    @param p: Polygon, created with Geopanda, which would be saved as file
    @param index: index to make saved file unique
    @param writepath: Path, where would be file written
    """
    p.plot()
    plt.savefig( write_path + str(index)+".png")
    plt.close




def polygon_to_pixels(p):
    """
    returns a numpy array, which includes all points as pixel values

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return array: numpy array with pixels
    """
    NoP = get_number_of_points(p) # variable to save the total numbers of points in the polygon
    array_of_points = []
    for i in range(NoP):
        located_pixel = [p[0].exterior.coords[i][0], p[0].exterior.coords[i][1]]
        array_of_points.append(located_pixel)
    return np.array(array_of_points, np.int32) #cast to get a integer and not floats




def simplify_polygon_k_with_angle_old(arr, final_number_of_points, options):
    """
    returns a polygon, which is simplified to a given number of points
    K Calculation with using angles and distances
    this method is not so efficient in compare to the method above

    @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
    @param final_number_of_points: int for the number of points of the returned polygon
    @return array:  which was simplified to the given number of points
    """
    DCE_Polygon = create_Polygon_from_array(arr)  #transform array to polygon for further calculations

    NoP = get_number_of_points(DCE_Polygon) # variable to save the total numbers of points in the polygon
   
    if final_number_of_points >= NoP: #direct return, if desired number of points is less than or equal to total number of points
        return polygon_to_pixels(DCE_Polygon)

    for i in range(NoP): #iterate over all polygonpoints
        calc_lowest_k = get_lowest_k(DCE_Polygon, options) # get index and  calculated value for the lowest k value wiht angles and distances
        index_lowest_k = calc_lowest_k[0]
    
        if i == (NoP-3): #Exception if Polygon is only triangle
            return polygon_to_pixels(DCE_Polygon)
        
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k) #Overwrite DCE Polygon with new Polygon, where is point on index k deleted
 
        if final_number_of_points == get_number_of_points(DCE_Polygon): #if statement for return the simplified polygon at desired number of points
            return polygon_to_pixels(DCE_Polygon)




def test():
    """
    testfunction for DCE.py;
    use only when you would run DCE.py without main.py

    write some testdata
    """

    #Paths for write and read files
    read_path_very_small_NRW = r"Code\DCE\examples\dvg2bld_nw_vsmall.txt"
    read_path_small_NRW = r"Code\DCE\examples\dvg2bld_nw_small.txt"
    read_path_big_NRW = r"Code\DCE\examples\dvg2bld_nw.txt"

    write_path_very_small_NRW = r"Code\DCE\TestRuns\NRWPolyVSmall\testpng"
    write_path_small_NRW = r"Code\DCE\TestRuns\NRWPolySmall\testpng"
    write_path_big_NRW = r"Code\DCE\TestRuns\NRWPoly_big\testpng"
    write_path_simplePolygon = r"Code\DCE\TestRuns\SimplePolygons\testpng"
    write_path_temp = r"Code\DCE\TestRuns\temp\testpng"

    write_path = r"Code\DCE\TestRuns\SimplePolygons\temp"

    read_path = read_path_very_small_NRW
    #write_path = write_path_temp
    print_limiter = 10 #Limiter for saving file intervall
    p = choosePolygon(1) #readtextfile(read_path)
    p = readtextfile(read_path)
    polygon_in_arr = get_array_with_points(p)
    options = {"test":2}
    fnop= 10
    timestamp_old_a = time.time()
    plot_GS_polygon(create_Polygon_from_array(polygon_in_arr),"Ursprung"+str(fnop),write_path)

    old_poly = simplify_polygon_k_with_angle_old(polygon_in_arr,fnop,options)

    plot_GS_polygon(create_Polygon_from_array(old_poly)," Alte Methode 15 P"+str(fnop),write_path) #write polygon
    timestamp_old_e = time.time()
    print("erstes fertig")

    print("laeuft")
    timestamp_new_a = time.time()
    #final_number_poly = simplify_polygon_k_with_angle(polygon_in_arr,4, options) #simplify polygon to 10 points
    #final_number_poly = simplify_polygon_second(polygon_in_arr,4, options)
    #ref(polygon_in_arr,5,options)
    #final_number_poly = simplify_polygon_k_immer_neu(polygon_in_arr, fnop, options)
    final_number_poly = simplify_polygon_fast_sec(polygon_in_arr, fnop, options, write_path_temp)

    #temp = simplify_polygon_k_immer_neu(polygon_in_arr, fnop, options)
    #plot_GS_polygon(create_Polygon_from_array(temp),"temp k immer neu"+str(fnop),write_path) #write polygon

    plot_GS_polygon(create_Polygon_from_array(final_number_poly),"Neue Mehtode10 P"+str(fnop),write_path) #write polygon
    timestamp_new_e = time.time()

   # print("laenge alt: "+ str(len(old_poly)) + "laenge neu: " + str(len(final_number_poly)))
    print("Alte Methode: " + str(timestamp_old_e-timestamp_old_a) + "neue Methode: "+ str(timestamp_new_e-timestamp_new_a))
    print("____________________________________________________________________________________________________")
    print("stop")


#test()