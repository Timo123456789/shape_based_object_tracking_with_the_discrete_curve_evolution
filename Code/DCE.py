import numpy as np
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point


def main():
    #testpolygon = [[0,0],[2,0],[2,2],[3,4],[1,2]]
    #Alternativ Import einer Textdatei mit Punkten (gleiches Schema wie oben?)
    p = readtxtfile()
    print(p)
    print(distance_between_two_points(p,1,3))
 
    #print(p[0].exterior.coords[0].distance())
    plot_GS_polygon(p)
    

    return 0        

def distance_between_two_points(p, point1, point2):
    p1 = Point(p[0].exterior.coords[point1])  
    p2 = Point(p[0].exterior.coords[point2])
    dist = p1.distance(p2)
    return dist

def readtxtfile():
    f = open(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt")
    #polygon_from_txt = np.loadtxt(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt", comments="#", delimiter=";")
    #print(polygon_from_txt)
    polygon1 = Polygon([(1,1),
                    (0,3),
                    (2,4),
                    (5,5),
                    (4,3),
                    (4,1)
                    ])

    p = gpd.GeoSeries(polygon1)
    return p
    
def plot_GS_polygon(p):
    p.plot()
    plt.show()

def calc_k(s1,s2):
    k = (calc_betha(s1,s2)*calc_length(s1)*calc_length(s2))/(calc_length(s1)+calc_length(s2))
    return k


def calc_betha(s1,s2):
    foo = 0
    return foo

def calc_length(ls):
    return ls


main()