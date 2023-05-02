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
    p = readtxtfile()

   
  
    print("get index where highest k is")
    print(get_highest_k(p))
    print("get index where lowest k is")
    index_lowest_k = get_lowest_k(p)
    print(index_lowest_k, "kvalue", calc_k_with_points(p,index_lowest_k,(index_lowest_k+1),(index_lowest_k-1)))
    print(get_selected_point(p,get_lowest_k(p)))
    delete_point_from_polygon(p, get_lowest_k(p))


    # print(calc_k_with_points(p,2,1,3))
    # print(calc_k_with_points(p,3,4,1))


    



   
    
 
    #print(p[0].exterior.coords[0].distance())
    plot_GS_polygon(p)

    return 0 










def delete_point_from_polygon(p,index_of_point):
        d_point = get_selected_point(p, index_of_point)
        array = p[0].exterior.coords
        print("array vorher")
        print(array)
        # print("array nachher")
        # print(array)
        # plot_GS_polygon(shrinked_p)
        print("--------------------------")
        print(get_array_with_points(p))
        array = get_array_with_points(p)
        print("--------------------------")
     
      
        array.pop(index_of_point)
        shrink_poly = create_Polygon_from_array(array)
        print(create_Polygon_from_array(array))
        plot_GS_polygon(shrink_poly)
        print(array)


        # test = gpd.GeoDataFrame(geometry=gpd.GeoSeries(p))
        # print(test)
        # print("index_of_point")
        # print(index_of_point)
        # #p2 = test[0].pop(index_of_point)
        # #print(p2)
        return False
        return p

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
    for i in range(NoP):
        if i==0:
            k_value = calc_k_with_points(p,i,NoP,1) 
            point_on_k = get_selected_point(p,i)        
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
    return index_for_point_on_k


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




def readtxtfile():

    #readgeodataFrame.from_file benutzen? siehe https://stackoverflow.com/questions/27606924/count-number-of-points-in-multipolygon-shapefile-using-python



    f = open(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt")
    #polygon_from_txt = np.loadtxt(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt", comments="#", delimiter=";")
    #print(polygon_from_txt)
    polygon1 = Polygon([   (1,1),
                    (0,3),
                    (2,4),
                    (5,5),
                    (4,3),
                    (4,1)
                    ])
    polygon2 = Polygon([   (1,2),
                    (2,1),
                    (3,1),
                    (4,1),
                    (5,2),
                    (4,3),
                    (3,6),
                    (2,3)
                    ])

    p = gpd.GeoSeries(polygon2)
    # p = gpd.GeoDataFrame(polygon2)
    return p
    
def plot_GS_polygon(p):
    p.plot()
    plt.show()



def calc_k_with_points(polygon,p,s1,s2):
    angle = (get_angle(polygon,p,s1) + get_angle(polygon,p,s2))
    dist_between_p_s1 = calc_distance_between_two_points(polygon,p,s1)
    dist_between_p_s2 = calc_distance_between_two_points(polygon,p,s2)

    
    

    k =  (angle*dist_between_p_s1*dist_between_p_s2)     /    (dist_between_p_s1+dist_between_p_s2)
    
    

    # print("angle",angle, "dist p s1 ",dist_between_p_s1, "dist p s2",dist_between_p_s2, "k", k)
    # print("Summe Distanz zw. 2 Punkten","  p: ", p," s1: ", s1," s2: ", s2)
    # print( (calc_distance_between_two_points(polygon,p, s1)+calc_distance_between_two_points(polygon,p, s2)))
    if k<0:                 #Muss das so? Bei negativen Winkel kommen immer negative Werte raus die je höher ja kleiner sind, als andere.
        return k*(-1)
    else:
        return k





main()