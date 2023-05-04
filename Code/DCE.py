import numpy as np
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString
import math
import pandas


def main():
    #testpolygon = [[0,0],[2,0],[2,2],[3,4],[1,2]]
    #Alternativ Import einer Textdatei mit Punkten (gleiches Schema wie oben?)
    #p = choosePolygon()
    p = readtextfile()

   
  

    NoP = get_number_of_points(p)
    print_limiter = 10
    print_limiter_var = 0
    plot_GS_polygon(p, 0)
    DCE_Polygon = p
    for i in range(NoP-10):
        calc_lowest_k = get_lowest_k(DCE_Polygon)
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
            plot_GS_polygon(DCE_Polygon,i)
            print("finished")
            break
        if print_limiter_var == print_limiter:
            plot_GS_polygon(DCE_Polygon,i)
            print_limiter_var = 0
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k)
        #plot_GS_polygon(DCE_Polygon)





   
    
 
    #print(p[0].exterior.coords[0].distance())
    #plot_GS_polygon(p)

    return 0 










#gibt Polygon ohne Punkt zurück
def delete_point_from_polygon(p,index_of_point):
        d_point = get_selected_point(p, index_of_point)
        array = p[0].exterior.coords
        array = get_array_with_points(p)
        array.pop(index_of_point)
        shrink_poly = create_Polygon_from_array(array)
        return shrink_poly
       

def create_Polygon_from_array(arr):
    polygon = Polygon(arr)
    p = gpd.GeoSeries(polygon)
    return p

def get_array_with_points(p):
    NoP = get_number_of_points(p)
    array_of_points = []
    k_value = 0
    for i in range(NoP):
        array_of_points.append(p[0].exterior.coords[i]) 
        # array_of_points.append(get_selected_point(p,i)) 

    return array_of_points

def get_highest_k(p):
    NoP = get_number_of_points(p)
    k_value = 0
    for i in range(NoP):
        if i==0:
            k_value = calc_k_with_points(p,i,NoP,1) 
            point_on_k = get_selected_point(p,i)        
        else:
            if i==NoP:
                break
            scnd_k_value = calc_k_with_points(p,i,(i+1),(i-1))
            if scnd_k_value>k_value:        
                # print("k neu setzen")
                # print("i",i, "i+1", i+1,"i-1", i-1)
                k_value = scnd_k_value
                index_for_point_on_k = i  
            
    # print("höchster k Wert", k_value)
    # print("entsprechender Pointindex", index_for_point_on_k)
    # print("entsprechender Punkt", get_selected_point(p,(i-1))) # -1 keine Ahnung warum, sonst springt er einen Punkt zu weit
    return index_for_point_on_k

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
            if scnd_k_value<=k_value:        
                # print("k neu setzen")
                # print("i",i, "i+1", i+1,"i-1", i-1)
                k_value = scnd_k_value
                index_for_point_on_k = i  
            
    # print("höchster k Wert", k_value)
    # print("entsprechender Pointindex", index_for_point_on_k)
    # print("entsprechender Punkt", get_selected_point(p,(i-1))) # -1 keine Ahnung warum, sonst springt er einen Punkt zu weit
    return [index_for_point_on_k,k_value]


def get_number_of_points(p):
    pointcounter = 0
    for i in p[0].exterior.coords:
       # print(i)
        pointcounter = pointcounter + 1 
       # print (p[0].exterior.coords[i])
    pointcounter = pointcounter-1
    return pointcounter

def convert_polygon_to_linestrings(p):
    # print("p in convertlinestring")
    # print(p)
    # print("p[0].boundary in convertlinestring")
    # print(p[0].boundary)
    b = p.boundary.coords
    linestrings = [LineString(b[k:k+2]) for k in range(len(b) - 1)]
    p_lines = [list(ls.coords) for ls in linestrings]
    return p_lines

#return angle in radiant
def get_angle(p,point1,point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    angle = math.degrees(math.atan2(-(p2.y-p1.y), p2.x-p1.x))
    # print(p1,p2)
    # print("angle", angle, "angle in radians", math.radians(angle))
    return math.radians(angle)
    #return math.degrees(math.atan2(y2-y1, x2-x1))
    
def get_selected_point(p,i):
       return Point(p[0].exterior.coords[i])

#Input p = Polygon (as Geopanda.Geoseries Object)
#Input point1 = Point 1 which calculate distance from
#Input point2 = Point 2 which calculate distance to
#return dist = Distance between Point1 and Point2 in p
def calc_distance_between_two_points(p, point1, point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    dist = p1.distance(p2)
    return dist


def readtextfile():
    p = 0
    path = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\examples\dvg2bld_nw_small.txt"
   # f = open(path) 
    #Quelle https://www.opengeodata.nrw.de/produkte/geobasis/vkg/dvg/dvg2/
    test = pandas.read_table(path, delimiter=';')
    array = convert_table_in_array(test)
    return create_Polygon_from_array(array) 


def convert_table_in_array(t):
    RowCount = len(t)
    #print(RowCount)
    a = []
    for i in range(RowCount):
        a.append((t.iloc[i]["x"], t.iloc[i]["y"]))
    #print("a")
    #print(a)
    return a
    

    return a 
def choosePolygon():

    #readgeodataFrame.from_file benutzen? siehe https://stackoverflow.com/questions/27606924/count-number-of-points-in-multipolygon-shapefile-using-python



    f = open(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt")
    #polygon_from_txt = np.loadtxt(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt", comments="#", delimiter=";")
    #print(polygon_from_txt)
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

    p = gpd.GeoSeries(polygon3)
    # p = gpd.GeoDataFrame(polygon2)
    return p
    
def plot_GS_polygon(p, index):
    p.plot()
    #plt.savefig("testtiff" + str(index)+".tiff")
    plt.savefig(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\TestRuns\NRWPolySmallTenStep\testpng" + str(index)+".png")
    #plt.show()



def calc_k_with_points(polygon,p,s1,s2):
    angle = (get_angle(polygon,p,s1) + get_angle(polygon,p,s2))
    dist_between_p_s1 = calc_distance_between_two_points(polygon,p,s1)
    dist_between_p_s2 = calc_distance_between_two_points(polygon,p,s2)

    
    

    k =  (angle*dist_between_p_s1*dist_between_p_s2)     /    (dist_between_p_s1+dist_between_p_s2)
    
    

    # print("angle",angle, "dist p s1 ",dist_between_p_s1, "dist p s2",dist_between_p_s2, "k", k)
    # print("Summe Distanz zw. 2 Punkten","  p: ", p," s1: ", s1," s2: ", s2)
    # print( (calc_distance_between_two_points(polygon,p, s1)+calc_distance_between_two_points(polygon,p, s2)))
    # if k<0:                 #Muss das so? Bei negativen Winkel kommen immer negative Werte raus die je höher ja kleiner sind, als andere.
    #     return k*(-1)
    # else:
    return k





main()