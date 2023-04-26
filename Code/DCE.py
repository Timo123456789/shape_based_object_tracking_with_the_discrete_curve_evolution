import numpy as np
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString
import math


def main():
    #testpolygon = [[0,0],[2,0],[2,2],[3,4],[1,2]]
    #Alternativ Import einer Textdatei mit Punkten (gleiches Schema wie oben?)
    p = readtxtfile()
   #  p_lines = convert_polygon_to_linestrings(p)
    print(p)
    print("-------------------------------------------------------")
    #print(p_lines)
    print(calc_distance_between_two_points(p,0,1))
    print("getangle")
    print(get_angle(p,4,5))
    print("getboundary")
    print(p.boundary)
    #print(p.boundary[0])

    print("k")
    print(calc_k_with_points(p,0,5,1))
    print(calc_k_with_points(p,1,0,2))
    print(calc_k_with_points(p,2,1,3))
    print("dreier")
    print(calc_k_with_points(p,3,2,4))
    print(calc_k_with_points(p,4,3,5))
    print(calc_k_with_points(p,5,4,0))
   
    
 
    #print(p[0].exterior.coords[0].distance())
    plot_GS_polygon(p)
    

    return 0 


def convert_polygon_to_linestrings(p):
    print("p in convertlinestring")
    print(p)
    print("p[0].boundary in convertlinestring")
    print(p[0].boundary)
    b = p.boundary.coords
    linestrings = [LineString(b[k:k+2]) for k in range(len(b) - 1)]
    p_lines = [list(ls.coords) for ls in linestrings]
    return p_lines

#return angle in radiant
def get_angle(p,point1,point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    angle = math.degrees(math.atan2(p2.y-p1.y, p2.x-p1.x))
    return math.radians(angle)
    #return math.degrees(math.atan2(y2-y1, x2-x1))
    


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
    f = open(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt")
    #polygon_from_txt = np.loadtxt(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt", comments="#", delimiter=";")
    #print(polygon_from_txt)
    polygon1 = Polygon([   (1,1),
                    (0,3),
                    (2,4),
                    (7,7),
                    (4,3),
                    (4,1)
                    ])

    p = gpd.GeoSeries(polygon1)
    return p
    
def plot_GS_polygon(p):
    p.plot()
    plt.show()


#not finished
def calc_k_with_points(polygon,p,s1,s2):
    k = (get_angle(polygon,s1,s2)*calc_distance_between_two_points(polygon,p, s1)*calc_distance_between_two_points(polygon,p, s2))/(calc_distance_between_two_points(polygon,p, s1)+calc_distance_between_two_points(polygon,p, s2))
    return k

def calc_k(s1,s2):
    k = (calc_betha(s1,s2)*calc_length(s1)*calc_length(s2))/(calc_length(s1)+calc_length(s2))
    return k

def calc_betha(s1,s2):
    foo = 0
    return foo

def calc_length(ls):
    return ls


main()