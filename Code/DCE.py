import numpy as np
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon


def testdurchlauf():
    testpolygon = [[0,0],[2,0],[2,2],[3,4],[1,2]]
    #Alternativ Import einer Textdatei mit Punkten (gleiches Schema wie oben?)
    readtxtfile()
    return 0        

def readtxtfile():
    f = open(r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\testpolygon.txt")
    print(f.read())
    polygon1 = Polygon([(0,5),
                    (1,1),
                    (3,0),
                    ])

    p = gpd.GeoSeries(polygon1)
    p.plot()
    plt.show()
    return 0
    

def calc_k(s1,s2):
    k = (calc_betha(s1,s2)*calc_length(s1)*calc_length(s2))/(calc_length(s1)+calc_length(s2))
    return k


def calc_betha(s1,s2):
    foo = 0
    return foo

def calc_length(ls):
    return ls


testdurchlauf()