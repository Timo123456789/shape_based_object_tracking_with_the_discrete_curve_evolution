import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import math
import pandas




def simplify_polygon_k_with_angle(arr, final_number_of_points):
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
        calc_lowest_k = get_lowest_k(DCE_Polygon) # get index and  calculated value for the lowest k value wiht angles and distances
        index_lowest_k = calc_lowest_k[0]    

        if i == (NoP-3): #Exception if Polygon is only triangle
            return polygon_to_pixels(DCE_Polygon)
        
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k) #Overwrite DCE Polygon with new Polygon, where is point on index k deleted

        if final_number_of_points == get_number_of_points(DCE_Polygon): #if statement for return the simplified polygon at desired number of points
            return polygon_to_pixels(DCE_Polygon)
        



def simplify_polygon_k_with_dist(arr, final_number_of_points):
    """
    returns a polygon, which is simplified to a given number of points
    K Calculation with using distances

    @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
    @param final_number_of_points: int for the number of points of the returned polygon
    @return array:  which was simplified to the given number of points
    """
    DCE_Polygon = create_Polygon_from_array(arr) #transform array to polygon for further calculations
    NoP = get_number_of_points(DCE_Polygon) # variable to save the total numbers of points in the polygon
    if final_number_of_points >= NoP: #direct return, if desired number of points is less than or equal to total number of points
        return polygon_to_pixels(DCE_Polygon)

    for i in range(NoP): #iterate over all polygonpoints
        calc_lowest_k = get_lowest_k_dist_calc(DCE_Polygon) # get index and  calculated value for the lowest k value with distances
        index_lowest_k = calc_lowest_k[0]

        if i == (NoP-3): #Exception if Polygon is only triangle
            return polygon_to_pixels(DCE_Polygon)
            
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k) #Overwrite DCE Polygon with new Polygon, where is point on index k deleted
        
        if final_number_of_points == get_number_of_points(DCE_Polygon): #if statement for return the simplified polygon at desired number of points
            return polygon_to_pixels(DCE_Polygon)




def get_lowest_k(p):
    """
    returns lowest k value for polygon p

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return k: calculated lowest k value in p as int
    """
    NoP = get_number_of_points(p)
    k_value = 0
    index_for_point_on_k = -1
    for i in range(NoP):
        if i==0:
            k_value = calc_k_with_points(p,i,(NoP-1),1) 
            index_for_point_on_k = 0       
        else:
            if i==NoP:
                break
            scnd_k_value = calc_k_with_points(p,i,(i+1),(i-1))
            if scnd_k_value<=k_value:        
                k_value = scnd_k_value
                index_for_point_on_k = i  
    return [index_for_point_on_k,k_value]




def get_lowest_k_dist_calc(p):
    """
    returns lowest k value for polygon p
    K Calculation only with distances

    @param p: Polygon (as Geopanda.Geoseries Object)
    @return k: calculated lowest k value in p as int
    """
    NoP = get_number_of_points(p)
    k_value = 0
    index_for_point_on_k = -1
    for i in range(NoP):
        if i==0:
            k_value = calc_k_dist(p,i,(NoP-1),1) 
            index_for_point_on_k = 0       
        else:
            if i==NoP:
                break
            scnd_k_value = calc_k_dist(p,i,(i+1),(i-1))
            if scnd_k_value<=k_value:        
                k_value = scnd_k_value
                index_for_point_on_k = i  
    return [index_for_point_on_k,k_value]




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
    return k




def calc_k_dist(p,p1,s1,s2):
    """
    returns K Value calculated based on Latecki, Lakaemper and Wolter, with three Points.

    @param p: Polygon, created with Geopanda
    @param p1: Point for which k is calculated
    @param s1: Point which describes the end of the first line from p
    @param s2: Point which describes the end of the second line from p
    @returns k: as int; only positiv
    """
    k = calc_distance_between_two_points(p,s1,p1)+calc_distance_between_two_points(p,s2,p1) - calc_distance_between_two_points(p,s1,s2)
    if k < 0:
        return k * -1
    else:
        return k


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




def get_angle_two_lines(polygon,p,s1,s2):  #https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2
    """
    returns angle in degree between two lines

    @param polygon: Polygon (as Geopanda.Geoseries Object)
    @param p1: Point Object from there the angle would be calculated
    @param s1: Point Object from p1 to s1 from there the angle would be calculated
    @param s2: Point Object from p1 to s2 from there the angle would be calculated
    @return pointcounter: Number of points in Polygon p as int
    """
    p = polygon[0].exterior.coords[p]
    s1 = polygon[0].exterior.coords[s1]
    s2 = polygon[0].exterior.coords[s2]

    x = np.array([p[0],p[1],s1[0],s1[1]])
    y = np.array([p[0],p[1],s2[0],s2[1]])

    val_arr = np.arctan2(y,x)*180/np.pi
    val_arr_sum = 0
    for i in range(len(val_arr)):
        val_arr_sum = val_arr_sum + val_arr[i]
    return np.deg2rad(val_arr_sum)




def get_angle_two_points(p,point1,point2):
    """
    returns angel between two points (point1 and point2)

    @param p: Polygon (as Geopanda.Geoseries Object)
    @param point1: point1 from there the angle would be calculated
    @param point2: point2 from there the angle would be calculated
    @return: angle between point1 and point2 on Polygon p in radiant
    """
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    
    return math.radians(math.atan2((p2.x-p1.x),(p2.y-p1.y)))
    



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




def readtextfile(path):  #Quelle https://www.opengeodata.nrw.de/produkte/geobasis/vkg/dvg/dvg2/
    """
    read a given textfile from path

    @param path: Path where the reading file is located
    @returns Geoseries Polygon: which are created from array
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

    #write_path = r"Code\DCE\TestRuns\SimplePolygons\testpng"
    
    read_path = read_path_very_small_NRW
    write_path = write_path_temp
    print_limiter = 5 #Limiter for saving file intervall
    p = readtextfile(read_path)
    polygon_in_arr = get_array_with_points(p)

    final_number_poly = simplify_polygon_k_with_angle(polygon_in_arr,10) #simplify polygon to 10 points
    plot_GS_polygon(create_Polygon_from_array(final_number_poly),-20,write_path) #write polygon
  
    NoP = get_number_of_points(p)
    print("____________________________________")
    print_limiter_var = 0
    plot_GS_polygon(p, 0, write_path)
    DCE_Polygon = p
    
    for i in range(NoP):  #iterate over all points in polygon
       # print("Punkt", get_selected_point(p,i) )
        calc_lowest_k = get_lowest_k(DCE_Polygon)
        index_lowest_k = calc_lowest_k[0]
        k_value=calc_lowest_k[1]
        if index_lowest_k==-1:
            print("Error; k = -1")
            break
        print(get_selected_point(p,i),"i: ",i," limiter:", (print_limiter-print_limiter_var), "verbl. P.:", (NoP-i), "kvalue", k_value)
       
        print_limiter_var = print_limiter_var +1
        # if i == (NoP-800): #set limit with fixed number of points remaining (must be comment IN!)
        #     print_limiter = 150
        #     print_limiter_var = 150
        # if i == (NoP-500):
        #     print_limiter = 100
        #     print_limiter_var = 100
        # if i == (NoP-300):
        #     print_limiter = 50
        #     print_limiter_var = 50
        # if k_value ==(NoP-100):
        #     print_limiter = 10
        #     print_limiter_var = 10
        if i == (NoP-3):
            plot_GS_polygon(DCE_Polygon,i,write_path)
            print("finished")
            break
        if print_limiter_var == print_limiter:
            plot_GS_polygon(DCE_Polygon,i, write_path)
            print_limiter_var = 0
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k)
        #plot_GS_polygon(DCE_Polygon)  
 
    #print(p[0].exterior.coords[0].distance())
    #plot_GS_polygon(p)

    return 0 




#test()