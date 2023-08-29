import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import math
import pandas
import time




def simplify_polygon_k_with_angle(arr, final_number_of_points, options):
    """
    returns a polygon, which is simplified to a given number of points
    K Calculation with using angles and distances

    @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
    @param final_number_of_points: int for the number of points of the returned polygon
    @return array:  which was simplified to the given number of points
    """
    return simplify_polygon_third(arr, final_number_of_points, options)






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
    #write_path_temp = r"Code\DCE\TestRuns\temp\testpng"

    write_path = r"Code\DCE\TestRuns\SimplePolygons\temp"

    read_path = read_path_very_small_NRW
    #write_path = write_path_temp
    print_limiter = 10 #Limiter for saving file intervall
    p = choosePolygon(1) #readtextfile(read_path)
    p = readtextfile(read_path)
    polygon_in_arr = get_array_with_points(p)
    options = {"test":2}
    fnop= 5
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
    final_number_poly = simplify_polygon_k_immer_neu(polygon_in_arr, fnop, options)

    #temp = simplify_polygon_k_immer_neu(polygon_in_arr, fnop, options)
    #plot_GS_polygon(create_Polygon_from_array(temp),"temp k immer neu"+str(fnop),write_path) #write polygon

    plot_GS_polygon(create_Polygon_from_array(final_number_poly),"Neue Mehtode ohne letzten Punkt aktualisieren 15 P"+str(fnop),write_path) #write polygon
    timestamp_new_e = time.time()

    


   # print("laenge alt: "+ str(len(old_poly)) + "laenge neu: " + str(len(final_number_poly)))
    print("Alte Methode: " + str(timestamp_old_e-timestamp_old_a) + "neue Methode: "+ str(timestamp_new_e-timestamp_new_a))
    print("____________________________________________________________________________________________________")
    print("stop")




def simplify_polygon_k_immer_neu(arr, fNoP, options):
    DCE_Polygon = create_Polygon_from_array(arr)
    NoP = get_number_of_points(DCE_Polygon)
    indic_arr = []

    while(get_number_of_points(DCE_Polygon) != fNoP):
        k_val_arr = calc_k_for_all_points(DCE_Polygon)
        sort_arr = np.asarray(k_val_arr, dtype="float64")
        sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="quicksort")]
        

        indic = int(sort_arr[0][0])
        indic_arr.append(indic)
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)

    print("__________________K IMMER NEU___________________")
    #DCE_Polygon.plot()
    #plt.show()
    #print(indic_arr)
    return polygon_to_pixels(DCE_Polygon)


def simplify_polygon_third(arr, fNoP, options):
    DCE_Polygon = create_Polygon_from_array(arr)
    NoP = get_number_of_points(DCE_Polygon)

    k_val_arr = calc_k_for_all_points(DCE_Polygon)
    sort_arr = np.asarray(k_val_arr, dtype="float64")
    sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="quicksort")]


    indic_gleich_NoPTemp = 0
    indicM1_gleich_Null = 0
    indicP1_gr_NoPTemp_bef = 0
    indicP1_gr_NoPTemp_act = 0
    indic_norm_bef = 0
    indic_norm_act = 0
    indic_arr = []

    #print("erstes Sort Array")
   # print(sort_arr)
    while(len(sort_arr)>= fNoP):
        indic = int(sort_arr[0][0])
        indic_arr.append(indic)
       # print(len(sort_arr))
        #Entferne Punkt
        NoP_before_delete_Polygon = get_number_of_points(DCE_Polygon)
        NoP_before_delete_sortarray = len(sort_arr)
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
        entfernter_Punkt = sort_arr[0]
        #sort_arr = np.delete(sort_arr, 0, axis = 0)

        #print("len sort arr" + str(len(sort_arr)) + "NOP Polygon" + str(get_number_of_points(DCE_Polygon)))
        #print("calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))")
       # print(" ")
        # if indic == len(sort_arr):
        #     indic = indic -1
        NoP_temp = get_number_of_points(DCE_Polygon)

       # if indic >= NoP_temp:
            #print("indic"+ str(indic))
            #print("Punktanzahl Polygon" + str(NoP_temp))
           # print("entfertner Punkt" + str(entfernter_Punkt))
            #print(sort_arr[0])
           # print(get_selected_point(DCE_Polygon, NoP_temp))
            #print("stop")


        if indic == NoP_temp:
            #indic_gleich_NoPTemp = indic_gleich_NoPTemp +1
            k_bef = calc_k_with_points(DCE_Polygon,indic-1,0,indic-2)
            k_act = calc_k_with_points(DCE_Polygon, 0,1,indic-1)

        else:
            if indic-1 == 0:
            # print("kbef_vals (indic =0)" + str(indic-1) + ", "+ str(1) + ", "+ str(get_number_of_points(DCE_Polygon)-1))
               # print("indic-1 ist 0")
               # print("0, 1, " + str(NoP-2))
                k_bef = calc_k_with_points(DCE_Polygon, 0, 1,(NoP_temp-1) )
                #indicM1_gleich_Null = indicM1_gleich_Null +1
            else:
            # print("kbef_vals" + str(indic-1) + ", "+ str(indic) + ", "+ str(indic+1))
                if indic+1 > NoP_temp:
                    k_bef = calc_k_with_points(DCE_Polygon, indic-1, 0, indic) #RICHTIG??
                    #indicP1_gr_NoPTemp_bef = indicP1_gr_NoPTemp_bef +1
                else:
                    k_bef = calc_k_with_points(DCE_Polygon, indic-1, indic+1, indic) #muss es nicht indic-1,indic, indic-2 heissen?
                   # indic_norm_bef = indic_norm_bef +1
        # print("kbef_res "+ str(k_bef))
            #print("kact_vals" + str(indic) + ", "+ str(indic+1) + ", "+ str(indic-1))
            if indic+1 > NoP_temp:
               # print("indic + 1 ist groesser als NoP temp")
                k_act = calc_k_with_points(DCE_Polygon,indic, 0, indic-1) #RICHTIG??
                #indicP1_gr_NoPTemp_act = indicP1_gr_NoPTemp_act +1
            else:
                k_act = calc_k_with_points(DCE_Polygon,indic, indic+1, indic-1)
                #indic_norm_act = indic_norm_act +1
            #print("kact_res "+ str(k_act))


        # print("kbef" + str(k_bef[0]) + "kact" + str(k_act[0]))
        # print("sort_arr vor aktualisierung" +str(len(sort_arr)) +  " Polygonpunktanzahl nach entfernt " + str(get_number_of_points(DCE_Polygon)))
        # print(sort_arr)
        # print("punkt an stelle " + str(indic) + " entfernt")
   
        sort_arr = update_sort_array(sort_arr,indic,k_bef[0], k_act[0],DCE_Polygon)
    
        # print("sort_arr nach aktualisierung")
        # print(sort_arr)
        # print(calc_k_with_points(DCE_Polygon,4,0,3))
        # print(" ")
        # print("Reference:")
        # print(calc_k_for_all_points(DCE_Polygon))
        # print("Reference 2:")
        # print(get_lowest_k(DCE_Polygon, options))
        # print(get_number_of_points(DCE_Polygon))


        # if len(sort_arr) != get_number_of_points(DCE_Polygon):
        #     print("Punktanzahl Polygon vor Entfernung: "+ str(NoP_before_delete_Polygon) + "  IST Zahl: "+ str(get_number_of_points(DCE_Polygon)))
        #     print("Punktanzahl array vor Entfernung: "+ str(NoP_before_delete_sortarray) + "  IST Zahl: "+ str(len(sort_arr)))
        #     print("Fehler; Gesamtpunktanzahl ist verschieden")

        if (get_number_of_points(DCE_Polygon) == fNoP):
            print("statistik:")
            print(indic_arr)
            DCE_Polygon.plot()
            plt.show()
            return polygon_to_pixels(DCE_Polygon)
    #print(sort_arr)
    # sort_arr = update_element(sort_arr, indic-1, k_bef[0])
    # sort_arr = update_element(sort_arr, indic, k_act[0])


    # print("sort_arr")
    # print(sort_arr)
    # DCE_Polygon.plot()
    # plt.show()
    print("indic_arr")
    print(indic_arr)
    return polygon_to_pixels(DCE_Polygon)





def update_sort_array(sort_arr, indic, k_bef, k_act, p):
    NoP_Poly = get_number_of_points(p)
    overwritten_act = False
    overwritten_bef = False
   # print(sort_arr[0])
   # print("indic"+ str(indic))
   # if indic == 156:
     #   sort_temp = sort_arr[np.argsort(sort_arr[:,0], kind="mergesort")]
        #print("stop")
  #  print(sort_arr[0][0])
   # print(len(sort_arr))
    sort_arr = np.delete(sort_arr, 0, axis = 0)

    sort_array_indic_bef = np.where(np.isin(sort_arr[:,0], indic-1))
    sort_array_indic_act = np.where(np.isin(sort_arr[:,0], indic))
    #print("indic: " + str(indic) + "sort array indic bef" + str(sort_array_indic_bef[0][0]))
    #print("indic: " + str(indic) + "sort array indic act" + str(sort_array_indic_act[0].size))
    a_temp_test = sort_arr[np.argsort(sort_arr[:,0], kind="quicksort")]
    

    sort_array_indic_aft = np.where(np.isin(sort_arr[:,0], indic+1))
    if indic == 0 or sort_array_indic_aft[0].size == 0:
        sort_arr = np.delete(sort_arr, 0, axis = 0)
    else:
        sort_arr = np.delete(sort_arr, int(sort_array_indic_aft[0][0]), axis = 0)


    #print("bef indic" + str(sort_array_indic_bef))
   # print("act indic" + str(sort_array_indic_act))
    # if indic !=0:
        if sort_array_indic_bef[0].size == 0:
         #   print("hinzugefuegt indic" + str(indic-1))
            overwritten_bef = True
            new_val_arr = np.array([indic, k_bef])
            sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0)
        else:
            sort_array_indic_bef = int(sort_array_indic_bef[0][0])
            #print(sort_array_indic_bef)

        if sort_array_indic_act[0].size ==0:
            #print("hinzugefuegt indic" + str(indic))
            overwritten_act = True
            new_val_arr = np.array([indic, k_act])
            sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0)
        else:
            sort_array_indic_act = int(sort_array_indic_act[0][0])


    # else:
    #     sort_array_indic_bef = len(sort_arr)-1
    #     sort_array_indic_act = 0

   
    # print(indic)
    # print(str(sort_array_indic_bef) + " " + str(sort_array_indic_act))
    if indic == 0:
        sort_arr[(len(sort_arr)-1)][1] = k_bef
        sort_arr[0][1] = k_act
    else:
        if overwritten_bef == False:
            if indic-1 >= len(sort_arr):
                sort_array_indic_bef = len(sort_arr)-1
            sort_arr[sort_array_indic_bef][1] = k_bef
        if overwritten_act == False:
            if indic >= len(sort_arr):
                sort_array_indic_act = len(sort_arr)-1
            sort_arr[sort_array_indic_act][1] = k_act


    #berechen letztes Element neu
    #last_element = calc_k_with_points(p,len(sort_arr)-1,0, len(sort_arr)-2)
    #print("last_element")
    #print(last_element)

 
    sort_by_num = sort_arr[np.argsort(sort_arr[:,0], kind="quicksort")]
    #print("indic" + str(indic))

    #print("vor neu nummierung")
    #print(sort_by_num)
    for i in range(len(sort_by_num)):
       sort_by_num[i][0]=i
 #   print("neusortiert")
    #print(sort_by_num)
    #print("stop")
#
    #sort_by_num[len(sort_by_num)-1][1] = last_element[0]

    #print(sort_by_num)
    # print(sort_by_num)
    # print("stop")

    sort_by_k =sort_by_num[np.argsort(sort_by_num[:,1], kind="quicksort")]
    # print(sort_by_k)
    return(sort_by_k)



def ref(arr, FNoP, options):
        print("REFERENCE--BEGIN------------------------------------------------------------------")
        DCE_Polygon = create_Polygon_from_array(arr)
        NoP = get_number_of_points(DCE_Polygon)
        k_val_arr = calc_k_for_all_points(DCE_Polygon)
        sort_arr = np.asarray(k_val_arr, dtype="float64")
        sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
        indic = int(sort_arr[0][0])
        print(sort_arr)
        print(get_lowest_k(DCE_Polygon, " "))
        # DCE_Polygon.plot()
        # plt.show()
        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
        print("puntk an stelle " + str(indic)  + "entfertn")
        k_val_arr = calc_k_for_all_points(DCE_Polygon)
        sort_arr = np.asarray(k_val_arr, dtype="float64")
        sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
        print(sort_arr)
        print("REFERENCE---END-----------------------------------------------------------------")
        # DCE_Polygon.plot()
        # plt.show()




def sort_arr_func(sort_arr):
    sort_by_num = sort_arr[np.argsort(sort_arr[:,0], kind="mergesort")]
    for i in range(len(sort_by_num)):
        sort_by_num[i][0]=i

 
    sort_by_k =sort_by_num[np.argsort(sort_by_num[:,1], kind="mergesort")]
   
    return sort_by_k



def del_indic(arr, indic):
    indic_del = np.where(np.isin(arr[:,0], indic))
    arr = np.delete(arr, indic_del[0][0], axis = 0)
    return arr




def calc_k_for_all_points(p):
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
    sum_of_angles = 0
    cop_outline = np.array(outline, dtype=  'int')
    cop_outline = cop_outline[0]

    p = create_Polygon_from_array(cop_outline)

    NoP = get_number_of_points(p)
    for i in range(NoP):
        if i==0:
            sum_of_angles = sum_of_angles + (get_angle_two_lines(p,i, (NoP-1),1))
        else:
            sum_of_angles = sum_of_angles + (get_angle_two_lines(p,i, (i+1), (i-1)))


    return sum_of_angles




def delete_point_from_polygon(p,index_of_point):
    """
    returns a polgyon p, where a point has been deleted

    @param p: Polygon (as Geopanda.Geoseries Object)
    @param index_of_point: Index for the point, which would be deleted
    @return shrink_poly: Polygon (as Geopanda.Geoseries Object) without point on index 'index_on_point'
    """
    array = get_array_with_points(p)

    #if len(array) >= 3:
  #  if len(array) <= index_of_point:  #irgendwie auch merkwuerdig!

      #  p.plot()
      #  plt.show()
        #index_of_point = len(array)-1
  
    array.pop(index_of_point)
    shrink_poly = create_Polygon_from_array(array)
    #else:
    #    shrink_poly = create_Polygon_from_array(array)
    #plot_GS_polygon(p, 1, r'Code\vid_examples')




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
    v1 = [s1[0]-p[0],s1[1]-p[1]]
    v2 = [s2[0]-p[0],s2[1]-p[1]]
    angle = np.degrees(np.arctan2(np.cross(v1,v2), np.dot(v1,v2)))
    if angle < 0:
        angle = angle * -1

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



def simplify_polygon_k_with_angle_old(arr, final_number_of_points, options):
    """
    returns a polygon, which is simplified to a given number of points
    K Calculation with using angles and distances
    this method is not so efficient in compare to the method above

    @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
    @param final_number_of_points: int for the number of points of the returned polygon
    @return array:  which was simplified to the given number of points
    """


    indic_gleich_NoPTemp = 0
    indicM1_gleich_Null = 0
    indicP1_gr_NoPTemp_bef = 0
    indicP1_gr_NoPTemp_act = 0
    indic_norm_bef = 0
    indic_norm_act = 0

    index_arr = []
    point_arr = []
    k_val_arr_end = []
    DCE_Polygon = create_Polygon_from_array(arr)  #transform array to polygon for further calculations

    NoP = get_number_of_points(DCE_Polygon) # variable to save the total numbers of points in the polygon
    if final_number_of_points >= NoP: #direct return, if desired number of points is less than or equal to total number of points
        return polygon_to_pixels(DCE_Polygon)

    for i in range(NoP): #iterate over all polygonpoints
        calc_lowest_k = get_lowest_k(DCE_Polygon, options) # get index and  calculated value for the lowest k value wiht angles and distances
        index_lowest_k = calc_lowest_k[0]
       # print("index_lowest_k"+ str(index_lowest_k))
        #point_arr.append(get_selected_point(DCE_Polygon,i))
        if index_lowest_k == get_number_of_points(DCE_Polygon): indic_gleich_NoPTemp = indic_gleich_NoPTemp +1
        else:    indic_norm_bef = indic_norm_bef +1
        if index_lowest_k-1 == 0: indicM1_gleich_Null = indicM1_gleich_Null +1
        if index_lowest_k+1 > get_number_of_points(DCE_Polygon) : indicP1_gr_NoPTemp_bef = indicP1_gr_NoPTemp_bef +1


        if i == (NoP-3): #Exception if Polygon is only triangle
            return polygon_to_pixels(DCE_Polygon)

        DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k) #Overwrite DCE Polygon with new Polygon, where is point on index k deleted
        index_arr.append(index_lowest_k)
        k_val_arr_end.append(calc_lowest_k[1])
        if final_number_of_points == get_number_of_points(DCE_Polygon): #if statement for return the simplified polygon at desired number of points
            print("Reference:")
            print(index_arr)
            # print(point_arr)
            # print(k_val_arr_end)
            # DCE_Polygon.plot()
            # plt.show()
            print("statistik:")
            print("indic = NoP Temp"+ str(indic_gleich_NoPTemp))
            print("indic-1 = 0"+ str(indicM1_gleich_Null))
            print("indic+1 > NoPTemp bef "+ str(indicP1_gr_NoPTemp_bef))
            print(indic_norm_bef)

            print("_________________")
            return polygon_to_pixels(DCE_Polygon)








def insert_element(arr,indic ,elem):
    indic_del = np.where(np.isin(arr[:,0], indic))
    arr = np.delete(arr,indic_del,0)
    new_k_value = np.array([indic, elem])
    arr= np.concatenate((arr,[new_k_value]), axis = 0)
    #arr = sort_arr_func(arr)

    return arr

def update_element(arr, indic, k_val):
    #print("anfangsindic" + str(indic))
    indic_del = np.where(np.isin(arr[:,0], indic))
    # print(indic_del)

    # print(arr[0][1])
    indic_del = indic_del[0]
    # print("indic")
    # print(indic)
    if indic_del.size == 0:
        print("not found" + str(indic))
       # print(arr)
        new_val_arr = np.array([indic, k_val])
        #print(new_val_arr)
        arr = np.concatenate((arr, [new_val_arr]), axis=0)
        #arr = np.append(arr, [new_val_arr], axis= 0)
        # print("nach hinzufuegen")
        # print(arr)
        #print("stop")
    else:
        print("k in sort array wird an stelle " + str(indic_del[0]) + " geupdatet")
        # print("arr vor update")
        # print(arr)
        # print(arr[2][0])
        # print(arr[2][1])
        #print(indic_del[0])
        # print("___________________")
        arr[indic_del[0]][1] = k_val
        #print("arr nach update")
        #print(arr)
    #     print("_________________________")
    # print(arr)

    return arr

test()