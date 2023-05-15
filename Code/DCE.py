import numpy as np
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString
import math
import pandas

#WICHTIG: y Koordinate wird beim Einlesen noch *-1 genommen (muss wieder abgeändert werden)
#NoP muss wieder -10 genommen werden, damit am Ende kein leeres Polygon ausgegeben wird


#Main Method
#
def main():
    read_path_very_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\examples\dvg2bld_nw_vsmall.txt"
    read_path_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\examples\dvg2bld_nw_small.txt"
    read_path_big_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\examples\dvg2bld_nw.txt"
    
  
    write_path_very_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\NRWPolyVSmall\testpng"
    write_path_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\NRWPolySmall\testpng"
    write_path_big_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\NRWPoly\testpng"
    write_path_simplePolygon = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\SimplePolygons\testpng"
    write_path_temp = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\temp\testpng"

    #write_path = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\SimplePolygons\testpng"
    
    #p = choosePolygon(2)

    
    read_path = read_path_very_small_NRW
    write_path = write_path_temp
    print_limiter = 10
    p = readtextfile(read_path)

   
  

    NoP = get_number_of_points(p)
    print("____________________________________")
    print_limiter_var = 0
    plot_GS_polygon(p, 0, write_path)
    DCE_Polygon = p
    

    for i in range(NoP):
       # print("Punkt", get_selected_point(p,i) )
        calc_lowest_k = get_lowest_k_dist_calc(DCE_Polygon)
        index_lowest_k = calc_lowest_k[0]
        k_value=calc_lowest_k[1]
        if index_lowest_k==-1:
            print("Error; k = -1")
            break
        print(get_selected_point(p,i),"i: ",i," limiter:", (print_limiter-print_limiter_var), "verbl. P.:", (NoP-i), "kvalue", k_value)
       
        print_limiter_var = print_limiter_var +1
        # if i == (NoP-800):
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
        if i == (NoP-10):
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






def get_lowest_k_dist_calc(p):
    NoP = get_number_of_points(p)
    k_value = 0
    index_for_point_on_k = -1
    for i in range(NoP):
        if i==0:
            k_value = calc_k_dist(p,i,NoP,1) 
            point_on_k = get_selected_point(p,i) 
            index_for_point_on_k = 0       
        else:
            if i==NoP:
                break
            scnd_k_value = calc_k_dist(p,i,(i+1),(i-1))
           # print("Punkt", get_selected_point(p,i), "K Wert:", scnd_k_value)
            if scnd_k_value<=k_value:        
                # print("k neu setzen")
                # print("i",i, "i+1", i+1,"i-1", i-1)
                k_value = scnd_k_value
                index_for_point_on_k = i  
            
   
    return [index_for_point_on_k,k_value]



#gibt Polygon ohne Punkt zurück

"""
returns a polgyon p, where a point has been deleted

@param p: Polygon (as Geopanda.Geoseries Object)
@param index_of_point: Index for the point, which would be deleted
@return: Polygon (as Geopanda.Geoseries Object) without point on index 'index_on_point'
"""
def delete_point_from_polygon(p,index_of_point):
        d_point = get_selected_point(p, index_of_point)
        array = p[0].exterior.coords
        array = get_array_with_points(p)
        array.pop(index_of_point)
        shrink_poly = create_Polygon_from_array(array)
        return shrink_poly
       
"""
create a Geopanda Geoseries Object from an given array

@param arr: 2 dim Array of points (as tupel); like [[0,1],[0,2],..]
@return p: Geopanda.Geoseries Object

"""
def create_Polygon_from_array(arr):
    polygon = Polygon(arr)
    p = gpd.GeoSeries(polygon)
    return p


"""
Returns an Array of Points in p

@param p: Polygon (as Geopanda.Geoseries Object)
@return: array of points, which are in given Polygon p

"""
def get_array_with_points(p):
    NoP = get_number_of_points(p)
    array_of_points = []
    k_value = 0
    for i in range(NoP):
        array_of_points.append(p[0].exterior.coords[i]) 
        # array_of_points.append(get_selected_point(p,i)) 

    return array_of_points


"""
returns lowest k value for polygon p

@param p: Polygon (as Geopanda.Geoseries Object)
@return k: calculated lowest k value in p as int

"""
def get_lowest_k(p):
    NoP = get_number_of_points(p)
    k_value = 0
    index_for_point_on_k = -1
    for i in range(NoP):
        if i==0:
            k_value = calc_k_with_points(p,i,NoP,1) 
            point_on_k = get_selected_point(p,i) 
            index_for_point_on_k = 0       
        else:
            if i==NoP:
                break
            scnd_k_value = calc_k_with_points(p,i,(i+1),(i-1))
            print("Punkt", get_selected_point(p,i), "K Wert:", scnd_k_value)
            if scnd_k_value<=k_value:        
                # print("k neu setzen")
                # print("i",i, "i+1", i+1,"i-1", i-1)
                k_value = scnd_k_value
                index_for_point_on_k = i  
            
   
    return [index_for_point_on_k,k_value]

"""
returns number of points in a polygon p

@param p: Polygon (as Geopanda.Geoseries Object)
@return pointcounter: Number of points in Polygon p as int

"""
def get_number_of_points(p):
    pointcounter = 0
    for i in p[0].exterior.coords:
       # print(i)
        pointcounter = pointcounter + 1 
       # print (p[0].exterior.coords[i])
    pointcounter = pointcounter-1
    return pointcounter


"""
returns angel between two points (point1 and point2)

@param p: Polygon (as Geopanda.Geoseries Object)
@param point1: point1 from there the angle would be calculated
@param point2: point2 from there the angle would be calculated
@return: angle between point1 and point2 on Polygon p in radiant

"""
#return angle in radiant
def get_angle(p,point1,point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    angle = math.degrees(math.atan2(-(p2.y-p1.y), p2.x-p1.x))
    print(p1,p2)
    print("angle", angle, "angle in radians", math.radians(angle))
    angle_radians = math.radians(angle)
    # return angle
    if angle_radians < 0:
        return angle_radians*-1
    else:
        return angle_radians
    return math.radians(angle)

    #return math.degrees(math.atan2(y2-y1, x2-x1))
    

"""
returns  point at index i from a given Polgon 

@param p = Polygon (as Geopanda.Geoseries Object)
@return Point = Tuple from Point at index i on p
"""
def get_selected_point(p,i):
       return Point(p[0].exterior.coords[i])


"""
calculate distance between two Points

@param p: Polygon (as Geopanda.Geoseries Object)
@param point1: Point 1 which calculate distance from
@param point2: Point 2 which calculate distance to
@return dist: Distance between Point1 and Point2 in p
"""
def calc_distance_between_two_points(p, point1, point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    dist = p1.distance(p2)
    return dist

"""
read a given textfile from path

@param path: Path where the reading file is located
@returns: Geoseries Polygon, which are created from array
"""
def readtextfile(path):
    p = 0
   # f = open(path) 
    #Quelle https://www.opengeodata.nrw.de/produkte/geobasis/vkg/dvg/dvg2/
    test = pandas.read_table(path, delimiter=';')
    array = convert_table_in_array(test)
    return create_Polygon_from_array(array) 

"""
Convert a given table to an arrray

@param t: table with columns, which are named with 'x' and 'y'
@return a: array with points from table as tuple
"""
def convert_table_in_array(t):
    RowCount = len(t)
    #print(RowCount)
    a = []
    for i in range(RowCount):
        a.append((t.iloc[i]["x"], (-1*(t.iloc[i]["y"]))))
    #print("a")
    #print(a)
    return a
    

    return a 

"""
Function which is used, when a simple Polygon is choosen for testrun

@param x: Selected the Polygon with this number
@return p: return p as geopanda.geoseries object which includes one Polygon Object 
"""
def choosePolygon(x):
   
    polygon1 = Polygon([    (1,1),(0,3),(2,4),
                            (5,5),(4,3),(4,1)
                    ])
    polygon2 = Polygon([(1,2),
                    (2,1),
                    (3,1),
                    (4,1),
                    (5,2),
                    (4,3),
                    (3,6),
                    (2,3)
                    ])
    polygon3= Polygon([(3,1),
        (4,1),(5,1),(6,1),(7,1),(8,1),(9,2),(8,3),(7,4),(8,5),(9,6),(10,7),(11,8),(8,7),(6,7),(5,9),(8,10),(7,11),(6,12),(5,11),(4,11),
        (3,11),(2,11),(0,10),(2,9),(2,8),(2,7),(1,6),(1,5),(3,4),(1,3),(2,2)
    ])
    if x == 1:
        p = gpd.GeoSeries(polygon1)
        
    if x == 2:
        p = gpd.GeoSeries(polygon2)
    if x == 3:
        p = gpd.GeoSeries(polygon3)
        
   
    # p = gpd.GeoDataFrame(polygon2)
    return p


"""
Plot a given Polygon at the folderpath 'path' with the indexnumber 'index' in the filename.
Plot the polygon as PNG File

@param p = Polygon, created with Geopanda, which would be saved as file
@param index = index to make saved file unique
@param writepath = Path, where would be file written
"""
def plot_GS_polygon(p, index, write_path):
    p.plot()
    #plt.savefig("testtiff" + str(index)+".tiff")
    #plt.savefig(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\NRWPolyVSmall\testpng" + str(index)+".png")
    plt.savefig( write_path + str(index)+".png")
    plt.close
    #plt.show()


"""
Returns K Value calculated based on Latecki and Lakaemper, with three Points.
The first linesegment is from p to s1 (p,s1) and the second linesegment is form p to s2 (p,s2)
Angle calculation must be sum up, because there are two angles to get the hole angle from s1 to s2.

@param polygon: Polygon, created with Geopanda
@param p: Point for which k is calculated
@param s1: Point which describes the end of the first line from p
@param s2: Point which describes the end of the second line from p
@returns: K as Int
"""
def calc_k_with_points(polygon,p,s1,s2):
    angle = (get_angle(polygon,p,s1) + get_angle(polygon,p,s2))

    dist_between_p_s1 = calc_distance_between_two_points(polygon,p,s1)
    dist_between_p_s2 = calc_distance_between_two_points(polygon,p,s2)

    
    

    k =  (angle*dist_between_p_s1*dist_between_p_s2)/(dist_between_p_s1+dist_between_p_s2)
    
    
    print("point", p)
    print("angle",angle, "dist p s1 ",dist_between_p_s1, "dist p s2",dist_between_p_s2, "k", k)
    # print("Summe Distanz zw. 2 Punkten","  p: ", p," s1: ", s1," s2: ", s2)
    # print( (calc_distance_between_two_points(polygon,p, s1)+calc_distance_between_two_points(polygon,p, s2)))
    # print("k", k)
    if k == 0:
        print("angle")
        print(angle, dist_between_p_s1, dist_between_p_s2)
    return k


def calc_k_dist(p,p1,s1,s2):
    k = calc_distance_between_two_points(p,p1,s1)+calc_distance_between_two_points(p,p1,s2) - calc_distance_between_two_points(p,s1,s2)
    if k < 0:
        return k *-1
    else:
        return k 

main()