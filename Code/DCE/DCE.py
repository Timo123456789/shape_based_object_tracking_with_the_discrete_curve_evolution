import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import math
import pandas




def simplify_polygon_k_with_angle(arr, final_number_of_points, options):
    """
    returns a polygon, which is simplified to a given number of points
    K Calculation with using angles and distances

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
         
        


def get_lowest_k(p, options):
    """
    returns lowest k value for polygon p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return k: calculated lowest k value in p as int
    """
    NoP = get_number_of_points(p)
    #angle_val_arr = []
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
    #print(outline)
    sum_of_angles = 0
    cop_outline = np.array(outline, dtype=  'int')
    cop_outline = cop_outline[0]
    #cop_outline = [[0,0],[5,0],[5,5],[0,5]]
    # print(cop_outline)
    p = create_Polygon_from_array(cop_outline)
   
    NoP = get_number_of_points(p)
    # print(np.rad2deg(get_angle_two_lines(p,0,3,1)))
    # print(np.rad2deg(get_angle_two_lines(p,1,2,0)))
    # print(np.rad2deg(get_angle_two_lines(p,2,3,1)))
    # print(np.rad2deg(get_angle_two_lines(p,3,4,2)))

    # print(get_angle_two_lines(p,0,2,1))
    # print(get_angle_two_lines(p,1,2,0))
    # print(get_angle_two_lines(p,2,3,1))
    # print(NoP)
    for i in range(NoP):
        if i==0:
            sum_of_angles = sum_of_angles + (get_angle_two_lines(p,i, (NoP-1),1))
        else:
            sum_of_angles = sum_of_angles + (get_angle_two_lines(p,i, (i+1), (i-1)))
    
    # print(sum_of_angles)
    # print(np.rad2deg(sum_of_angles))
    # p.plot()
    # plt.show()
    return sum_of_angles




def delete_point_from_polygon(p,index_of_point):
    """
    returns a polgyon p, where a point has been deleted

    @param p: Polygon (as Geopanda.Geoseries Object)
    @param index_of_point: Index for the point, which would be deleted
    @return shrink_poly: Polygon (as Geopanda.Geoseries Object) without point on index 'index_on_point'
    """
    d_point = get_selected_point(p, index_of_point)
    array = p[0].exterior.coords
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

    # print(p)
    # print(s1)
    # print(s2)
    #Following is the answer of Bing Bot for get a python function to calculate Angels between two poinst (minor changes for this use case)
    v1 = [s1[0]-p[0],s1[1]-p[1]]
    v2 = [s2[0]-p[0],s2[1]-p[1]]
    angle = np.degrees(np.arctan2(np.cross(v1,v2), np.dot(v1,v2)))

    #this code is from Source above 
    x = np.array([p[1],p[0],s1[1],s1[0]])
    y = np.array([p[1],p[0],s2[1],s2[0]])

    val_arr = np.arctan2(y,x)*180/np.pi
    # print(val_arr)
    # print(angle)
    if angle < 0:
        angle = angle * -1
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

    Source: Quelle https://www.opengeodata.nrw.de/produkte/geobasis/vkg/dvg/dvg2/
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