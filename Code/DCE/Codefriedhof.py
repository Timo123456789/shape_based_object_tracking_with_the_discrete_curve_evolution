# print("Punkt aus Polygon")
# print(p[0].exterior.coords[5])
 
   
# print("Länge zw. Puntken", p1, p2)
# print("Länge")
# print(p1.distance(p2))

# (3,1),
#         (4,1),(5,1),(6,1),(7,1),(8,1),(9,2),(8,3),(7,4),(8,5),(9,6),(10,7),(11,8),(8,7),(6,7),(5,9),(8,10),(7,11),(6,12),(5,11),(4,11),
#         (3,11),(2,11),(0,10),(2,9),(2,8),(2,7),(1,6),(1,5),(3,4),(1,3),(2,2)


#  plot_GS_polygon(shrink_poly)
#         print(array)


#         # test = gpd.GeoDataFrame(geometry=gpd.GeoSeries(p))
#         # print(test)
#         # print("index_of_point")
#         # print(index_of_point)
#         # #p2 = test[0].pop(index_of_point)
#         # #print(p2)
#         return False
#         return p


#    print("array vorher")
#         print(array)
#         # print("array nachher")
#         # print(array)
#         # plot_GS_polygon(shrinked_p)



        
    # print("get index where highest k is")
    # print(get_highest_k(p))
    # print("get index where lowest k is")
    # index_lowest_k = get_lowest_k(p)
    # print(index_lowest_k, "kvalue", calc_k_with_points(p,index_lowest_k,(index_lowest_k+1),(index_lowest_k-1)))
    # print(get_selected_point(p,get_lowest_k(p)))
    # polytwo = delete_point_from_polygon(p, get_lowest_k(p))
    # plot_GS_polygon(polytwo)

    # print(calc_k_with_points(p,2,1,3))
    # print(calc_k_with_points(p,3,4,1))


#PRINT CALC K with Points
  #angle = (get_angle(polygon,p,s1) + get_angle(polygon,p,s2))
    #angle = get_angle(polygon,s1,s2)
    # print("angle"+ str(angle) + "Punkt P")

  # print("p in calc_k_anlge")
    # print(get_selected_point(polygon, p))


# print(str(angle) + "*"+ str(dist_between_p_s1) + "*"+ str(dist_between_p_s2))
    # print("________________")
    # print(str(dist_between_p_s1)+"+"+str(dist_between_p_s2))
    # print("=="+ str(k))
    
    
    # print("point", p)
    # print("angle",angle, "dist p s1 ",dist_between_p_s1, "dist p s2",dist_between_p_s2, "k", k)
    # # print("Summe Distanz zw. 2 Punkten","  p: ", p," s1: ", s1," s2: ", s2)
    # # print( (calc_distance_between_two_points(polygon,p, s1)+calc_distance_between_two_points(polygon,p, s2)))
    # # print("k", k)
    # if k == 0:
    #     print("angle")
    #     print(angle, dist_between_p_s1, dist_between_p_s2)







# def get_highest_k(p):
#     NoP = get_number_of_points(p)
#     k_value = 0
#     for i in range(NoP):
#         if i==0:
#             k_value = calc_k_with_points(p,i,NoP,1) 
#             point_on_k = get_selected_point(p,i)        
#         else:
#             if i==NoP:
#                 break
#             scnd_k_value = calc_k_with_points(p,i,(i+1),(i-1))
#             if scnd_k_value>k_value:        
#                 # print("k neu setzen")
#                 # print("i",i, "i+1", i+1,"i-1", i-1)
#                 k_value = scnd_k_value
#                 index_for_point_on_k = i  
            
#     # print("höchster k Wert", k_value)
#     # print("entsprechender Pointindex", index_for_point_on_k)
#     # print("entsprechender Punkt", get_selected_point(p,(i-1))) # -1 keine Ahnung warum, sonst springt er einen Punkt zu weit
#     return index_for_point_on_k











# #Funktionsstand vor Bearbeitung 02.06.23 wg. CleanCode


# def get_angle_two_points(p,point1,point2):
#     """
#     returns angel between two points (point1 and point2)

#     @param p: Polygon (as Geopanda.Geoseries Object)
#     @param point1: point1 from there the angle would be calculated
#     @param point2: point2 from there the angle would be calculated
#     @return: angle between point1 and point2 on Polygon p in radiant
#     """
#     p1 = Point(p[0].exterior.coords[point1])  
#     p2 = Point(p[0].exterior.coords[point2])
#     #First Version
  
#     # angle = math.degrees(math.atan2(-(p2.y-p1.y), p2.x-p1.x))
#     # print(p1,p2)
#     # print("angle", angle, "angle in radians", math.radians(angle))
#     # angle_radians = math.radians(angle)
#     # # return angle
#     # if angle_radians < 0:
#     #     return angle_radians*-1
#     # else:
#     #     return angle_radians
#     # return math.radians(angle)

#     # #return math.degrees(math.atan2(y2-y1, x2-x1))

#     #second Version

#     return math.radians(math.atan2((p2.x-p1.x),(p2.y-p1.y)))
 
#     #third version  https://stackoverflow.com/questions/31735499/calculate-angle-clockwise-between-two-points
#     p1 = [p1.x, p1.y]
#     p2 = [p2.x, p2.y]
#     ang1 = np.arctan2(*p1[::-1])
#     ang2 = np.arctan2(*p2[::-1])
#     return np.rad2deg((ang1 - ang2) % (2 * np.pi))




# Main Method Stand 02.06.23

#Main Method
#
# def main():
#     read_path_very_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\examples\dvg2bld_nw_vsmall.txt"
#     read_path_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\examples\dvg2bld_nw_small.txt"
#     read_path_big_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\examples\dvg2bld_nw.txt"
    
  
#     write_path_very_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\NRWPolyVSmall\testpng"
#     write_path_small_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\NRWPolySmall\testpng"
#     write_path_big_NRW = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\NRWPoly_big\testpng"
#     write_path_simplePolygon = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\SimplePolygons\testpng"
#     write_path_temp = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\temp\testpng"

#     #write_path = r"C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\DCE\TestRuns\SimplePolygons\testpng"
    
    
    
#     read_path = read_path_very_small_NRW
#     write_path = write_path_temp
#     print_limiter = 5
#     p = readtextfile(read_path)
#     #p = choosePolygon(2)

   
  

#     NoP = get_number_of_points(p)
#     print("____________________________________")
#     print_limiter_var = 0
#     plot_GS_polygon(p, 0, write_path)
#     DCE_Polygon = p
    

#     for i in range(NoP):
#        # print("Punkt", get_selected_point(p,i) )
#         calc_lowest_k = get_lowest_k(DCE_Polygon)
#         index_lowest_k = calc_lowest_k[0]
#         k_value=calc_lowest_k[1]
#         if index_lowest_k==-1:
#             print("Error; k = -1")
#             break
#         print(get_selected_point(p,i),"i: ",i," limiter:", (print_limiter-print_limiter_var), "verbl. P.:", (NoP-i), "kvalue", k_value)
       
#         print_limiter_var = print_limiter_var +1
#         # if i == (NoP-800):
#         #     print_limiter = 150
#         #     print_limiter_var = 150
#         # if i == (NoP-500):
#         #     print_limiter = 100
#         #     print_limiter_var = 100
#         # if i == (NoP-300):
#         #     print_limiter = 50
#         #     print_limiter_var = 50
#         # if k_value ==(NoP-100):
#         #     print_limiter = 10
#         #     print_limiter_var = 10
#         if i == (NoP-3):
#             plot_GS_polygon(DCE_Polygon,i,write_path)
#             print("finished")
#             break
#         if print_limiter_var == print_limiter:
#             plot_GS_polygon(DCE_Polygon,i, write_path)
#             print_limiter_var = 0
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k)
#         #plot_GS_polygon(DCE_Polygon)





   
    
 
#     #print(p[0].exterior.coords[0].distance())
#     #plot_GS_polygon(p)

#     return 0 


# #third version  https://stackoverflow.com/questions/31735499/calculate-angle-clockwise-between-two-points
#     p1 = [p1.x, p1.y]
#     p2 = [p2.x, p2.y]
#     ang1 = np.arctan2(*p1[::-1])
#     ang2 = np.arctan2(*p2[::-1])
#     return np.rad2deg((ang1 - ang2) % (2 * np.pi))


# def test():
#     """
#     testfunction for DCE.py; 
#     use only when you would run DCE.py without main.py

#     write some testdata
#     """       

#     #Paths for write and read files
#     read_path_very_small_NRW = r"Code\DCE\examples\dvg2bld_nw_vsmall.txt"
#     read_path_small_NRW = r"Code\DCE\examples\dvg2bld_nw_small.txt"
#     read_path_big_NRW = r"Code\DCE\examples\dvg2bld_nw.txt"
    
#     write_path_very_small_NRW = r"Code\DCE\TestRuns\NRWPolyVSmall\testpng"
#     write_path_small_NRW = r"Code\DCE\TestRuns\NRWPolySmall\testpng"
#     write_path_big_NRW = r"Code\DCE\TestRuns\NRWPoly_big\testpng"
#     write_path_simplePolygon = r"Code\DCE\TestRuns\SimplePolygons\testpng"
#     write_path_temp = r"Code\DCE\TestRuns\temp\testpng"

#     #write_path = r"Code\DCE\TestRuns\SimplePolygons\testpng"
    
#     read_path = read_path_very_small_NRW
#     write_path = write_path_temp
#     print_limiter = 5 #Limiter for saving file intervall
#     p = readtextfile(read_path)
#     polygon_in_arr = get_array_with_points(p)

#     final_number_poly = simplify_polygon_k_with_angle(polygon_in_arr,10) #simplify polygon to 10 points
#     plot_GS_polygon(create_Polygon_from_array(final_number_poly),-20,write_path) #write polygon
  
#     NoP = get_number_of_points(p)
#     print("____________________________________")
#     print_limiter_var = 0
#     plot_GS_polygon(p, 0, write_path)
#     DCE_Polygon = p
    
#     for i in range(NoP):  #iterate over all points in polygon
#        # print("Punkt", get_selected_point(p,i) )
#         calc_lowest_k = get_lowest_k(DCE_Polygon)
#         index_lowest_k = calc_lowest_k[0]
#         k_value=calc_lowest_k[1]
#         if index_lowest_k==-1:
#             print("Error; k = -1")
#             break
#         print(get_selected_point(p,i),"i: ",i," limiter:", (print_limiter-print_limiter_var), "verbl. P.:", (NoP-i), "kvalue", k_value)
       
#         print_limiter_var = print_limiter_var +1
#         # if i == (NoP-800): #set limit with fixed number of points remaining (must be comment IN!)
#         #     print_limiter = 150
#         #     print_limiter_var = 150
#         # if i == (NoP-500):
#         #     print_limiter = 100
#         #     print_limiter_var = 100
#         # if i == (NoP-300):
#         #     print_limiter = 50
#         #     print_limiter_var = 50
#         # if k_value ==(NoP-100):
#         #     print_limiter = 10
#         #     print_limiter_var = 10
#         if i == (NoP-3):
#             plot_GS_polygon(DCE_Polygon,i,write_path)
#             print("finished")
#             break
#         if print_limiter_var == print_limiter:
#             plot_GS_polygon(DCE_Polygon,i, write_path)
#             print_limiter_var = 0
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k)
#         #plot_GS_polygon(DCE_Polygon)  
 
#     #print(p[0].exterior.coords[0].distance())
#     #plot_GS_polygon(p)

#     return 0 




# #test()













#NEUE METHODE FÜR DCE





# def simplify_polygon_k_with_angle(arr, final_number_of_points, options):
#     """
#     returns a polygon, which is simplified to a given number of points
#     K Calculation with using angles and distances

#     @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
#     @param final_number_of_points: int for the number of points of the returned polygon
#     @return array:  which was simplified to the given number of points
#     """

   
#     DCE_Polygon = create_Polygon_from_array(arr)  #transform array to polygon for further calculations
#     if final_number_of_points >= len(arr):
#         #print("Finnal NoP kleiner als gegebenes Array")
#         return polygon_to_pixels(DCE_Polygon)
#     # NoP = get_number_of_points(DCE_Polygon) # variable to save the total numbers of points in the polygon
#     # if final_number_of_points >= NoP: #direct return, if desired number of points is less than or equal to total number of points
#     #     return polygon_to_pixels(DCE_Polygon) 
    
#     # for i in range(NoP): #iterate over all polygonpoints
#     #     calc_lowest_k = get_lowest_k(DCE_Polygon, options) # get index and  calculated value for the lowest k value wiht angles and distances
#     #     index_lowest_k = calc_lowest_k[0]    

#     #     if i == (NoP-3): #Exception if Polygon is only triangle
#     #         return polygon_to_pixels(DCE_Polygon)
        
#     #     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, index_lowest_k) #Overwrite DCE Polygon with new Polygon, where is point on index k deleted

#     #     if final_number_of_points == get_number_of_points(DCE_Polygon): #if statement for return the simplified polygon at desired number of points
#     #         return polygon_to_pixels(DCE_Polygon)





#     NoP = get_number_of_points(DCE_Polygon)
#     k_val_arr = calc_k_for_all_points(DCE_Polygon, NoP)
  

#     sort_arr = np.asarray(k_val_arr, dtype="float")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1])]
    
#     while(NoP != final_number_of_points):
#         i = int(sort_arr[0][0])
#         if(i==0):
#             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#             act_NoP = get_number_of_points(DCE_Polygon)
#             NoP = NoP-1
#             sort_arr = np.delete(sort_arr, 0, axis = 0)
#             k_before = calc_k_with_points(DCE_Polygon, 0,act_NoP,1)
#             k_after = calc_k_with_points(DCE_Polygon, act_NoP,act_NoP-1,0)
#             np.insert(sort_arr,0,[0, k_before[0] ])
#             np.insert(sort_arr,act_NoP,[act_NoP, k_after[0]])
#             sort_arr = sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])]
#         else:
#             # print(i)
#             # print(get_array_with_points(DCE_Polygon))
#             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#             # print(get_array_with_points(DCE_Polygon))
#             NoP = NoP-1
#             temp_NoP = get_number_of_points(DCE_Polygon)
#             sort_arr = np.delete(sort_arr, 0, axis = 0)
#            # print("i+1")
#            # print(i+1)
#             #if i == 22:
#            # print("start")
#            # print(len(sort_arr))
#             #print(get_number_of_points(DCE_Polygon))
#             #print(sort_arr)
#            # print("stop")
#             # if i > temp_NoP:
#             #     k_before = calc_k_with_points(DCE_Polygon,i-2,i-3,temp_NoP-1)
#             # else:
#             #     k_before = calc_k_with_points(DCE_Polygon,i-1,i-2,i)
#             # if(i+1)> temp_NoP:
#             #     if (i)> temp_NoP:
#             #         k_after = calc_k_with_points(DCE_Polygon,i-1,i-2, temp_NoP-1)
#             #     else:
#             #         k_after = calc_k_with_points(DCE_Polygon,i,i-1, temp_NoP-1)
#             # else:
#             #     k_after = calc_k_with_points(DCE_Polygon,i,i-1,i+1)


#             k_before = calc_k_with_points(DCE_Polygon,i-1,i-2,i)
#             if i+1>len(sort_arr):
#                 k_after = calc_k_with_points(DCE_Polygon,i,i-1,1)
#             else:
#                 k_after = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
#             np.insert(sort_arr,i-1, [i-1, k_before[0]])
#             np.insert(sort_arr,i, [i, k_after[0]])
#             sort_arr = sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])]
#    # print("raus")    



#    # print("klappt?")





#     # while(NoP != final_number_of_points):
#     #     i = int(sort_arr[0][0])
#     #     if(i == 0):
#     #         DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#     #         NoP = NoP-1
#     #         np.append(sort_arr,[0, calc_k_with_points(DCE_Polygon, 0,NoP,1)])
#     #         np.append(sort_arr,[NoP, calc_k_with_points(DCE_Polygon, NoP,NoP-1,0)])
#     #         sort_arr = sort_arr[np.argsort(sort_arr[:,1])]
#     #     else:
#     #         print("else" + str(i) + "NoP" + str(NoP))

            
#     #         print("Test")
#     #         if(i == get_number_of_points(DCE_Polygon)):
#     #             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,int(i-1))
             
#     #         else:
#     #             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,int(i))
#     #         print(get_number_of_points(DCE_Polygon))

            
#     #         NoP = NoP-1





#     #         temp_NoP = get_number_of_points(DCE_Polygon)










#     #         # if(i+1 > get_number_of_points(DCE_Polygon)):
#     #         #     np.append(sort_arr,[0, calc_k_with_points(DCE_Polygon, 0,NoP,1)])
#     #         #     np.append(sort_arr,[NoP, calc_k_with_points(DCE_Polygon, NoP,NoP-1,0)])
#     #         #     sort_arr = sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])]
#     #         # else:
         
#     #         if (i+1)>temp_NoP or i > temp_NoP:
#     #             print("richitger Fall")
#     #             print(str(i) + " "+ str(i-1) + " " + str (temp_NoP))
#     #             np.append(sort_arr,[i-1, calc_k_with_points(DCE_Polygon, (i-1),(i-2),temp_NoP)])
#     #             np.append(sort_arr,[i, calc_k_with_points(DCE_Polygon, (i-1),(i-2),temp_NoP)])
#     #         else:
#     #             np.append(sort_arr,[i-1, calc_k_with_points(DCE_Polygon, (i-1),(i-2),(i))])
#     #             np.append(sort_arr,[i, calc_k_with_points(DCE_Polygon, (i),(i-1),(i+1))])
#     #         sort_arr =   sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])] #sort_arr_func(sort_arr)

#     #         print("erstes element wieder neu berechnen")
#     #         print((i-1),(i-2),(i))
#     #         print("zweites element wieder neu berechnen")
#     #         print(i,(i-1),(i+1))
#     #         print("number of points in DCE Polygon")
#     #         print(get_number_of_points(DCE_Polygon))

#         # print("______________________________________________________________")
#         # print("i"+ str(i))   
#         # print(sort_arr)
#         # print("_______________________________________________________________")
        
#     # for i in range(NoP-3):
#     #     j = int(sort_arr[0][0])
#     #     if(j == 0):
#     #         DCE_Polygon = delete_point_from_polygon(DCE_Polygon,j)
#     #         NoP = NoP-1
#     #         np.append(sort_arr,[0, calc_k_with_points(DCE_Polygon, 0,NoP,1)])
#     #         np.append(sort_arr,[NoP, calc_k_with_points(DCE_Polygon, NoP,NoP-1,0)])
#     #         sort_arr = sort_arr[np.argsort(sort_arr[:,1])]
#     #     else:
#     #         print("else" + str(j) + "NoP" + str(NoP))
#     #         print("DCE Polygon")
#     #         print(DCE_Polygon)
#     #         DCE_Polygon = delete_point_from_polygon(DCE_Polygon,int(j))
#     #         NoP = NoP-1
#     #         if(j+1 > get_number_of_points(DCE_Polygon)):
#     #             np.append(sort_arr,[0, calc_k_with_points(DCE_Polygon, 0,NoP,1)])
#     #             np.append(sort_arr,[NoP, calc_k_with_points(DCE_Polygon, NoP,NoP-1,0)])
#     #             sort_arr = sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])]
#     #         else:
#     #             np.append(sort_arr,[j-1, calc_k_with_points(DCE_Polygon, (j-1),(j-2),(j))])
#     #             np.append(sort_arr,[j, calc_k_with_points(DCE_Polygon, (j),(j-1),(j+1))])
#     #         sort_arr =   sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])] #sort_arr_func(sort_arr)

#     #     if NoP == final_number_of_points:
#     #         return polygon_to_pixels(DCE_Polygon)


#     return polygon_to_pixels(DCE_Polygon)
#     print("stop")
#     #while()
         


  # DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
    # k_val.append(sort_arr[0][1])
    # sort_arr = np.delete(sort_arr, 0, axis = 0)
    # print(sort_arr)
    # k_before = calc_k_with_points(DCE_Polygon, i-1,i,i+1)
    # k_act = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
    # k_after = calc_k_with_points(DCE_Polygon,i+1,i+2,i-1)
    # print("kbef: "+str(k_before[0]) +"(Stelle:"+str(i-1) + ") kact "+str(k_act[0])+" stelle "+str(i)+" kafter" + str(k_after[0])  + " an stelle:" + str(i+1))
    # sort_arr = update_element(sort_arr,i-1,k_before[0])
    # sort_arr = update_element(sort_arr, i, k_act[0])
    # sort_arr = update_element(sort_arr,i+1,k_after[0])
    # print("nach hinzufügen")
    # print(sort_arr)
    # print("stop2")
    # sort_arr = sort_arr_func(sort_arr)
    # print("nach sortieren")
    # print(sort_arr)
    # print("____________________________________________________________")

    # sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
    # DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
    # k_val.append(sort_arr[0][1])
    # sort_arr = np.delete(sort_arr, 0, axis = 0)
    # print(sort_arr)
    # print(k_val)
    # print("stop 3")
    # k_before = calc_k_with_points(DCE_Polygon, i-1,i,i+1)
    # k_act = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
    # k_after = calc_k_with_points(DCE_Polygon,i+1,i+2,i-1)
    # print("kbef: "+str(k_before[0]) +"(Stelle:"+str(i-1) + ") kact "+str(k_act[0])+" stelle "+str(i)+" kafter" + str(k_after[0])  + " an stelle:" + str(i+1))
    # sort_arr = update_element(sort_arr,i-1,k_before[0])
    # sort_arr = update_element(sort_arr, i, k_act[0])
    # sort_arr = update_element(sort_arr,i+1,k_after[0])
    # print("nach hinzufügen")
    # print(sort_arr)
    # print("____________________________________________________________")

    # sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
    # DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
    # k_val.append(sort_arr[0][1])
    # sort_arr = np.delete(sort_arr, 0, axis = 0)
    # print(k_val)
    # print(sort_arr)
    # print("stop 4")
    # print("--------------------------------------------------")
    # print(calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon)))
    # print("--------------------------------------------------")
    # k_before = calc_k_with_points(DCE_Polygon, i-1,i,i+1)
    # k_act = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
    # k_after = calc_k_with_points(DCE_Polygon,i+1,i+2,i-1)
    # print("kbef: "+str(k_before[0]) +"(Stelle:"+str(i-1) + ") kact "+str(k_act[0])+" stelle "+str(i)+" kafter" + str(k_after[0])  + " an stelle:" + str(i+1))
    # sort_arr = update_element(sort_arr,i-1,k_before[0])
    # sort_arr = update_element(sort_arr, i, k_act[0])
    # sort_arr = update_element(sort_arr,i+1,k_after[0])

    
    # print("stop")
    # print("nach hinzufügen")
    # print(sort_arr)
    # print("____________________________________________________________")


    # sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
    # DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
    # k_val.append(sort_arr[0][1])
    # sort_arr = np.delete(sort_arr, 0, axis = 0)
    # print(k_val)
    # print(sort_arr)
    # print("stop 5")
    # k_before = calc_k_with_points(DCE_Polygon, i-1,i,i+1)
    # k_act = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
    # k_after = calc_k_with_points(DCE_Polygon,i+1,i+2,i-1)
    # k_temp = calc_k_with_points(DCE_Polygon,i-2,i+1,i-1)
    # print("kbef: "+str(k_before[0]) +"(Stelle:"+str(i-1) + ") kact "+str(k_act[0])+" stelle "+str(i)+" kafter" + str(k_after[0])  + " an stelle:" + str(i+1))
    # print("punkt: " + str(get_selected_point(DCE_Polygon,i-1)) + " "+  str(get_selected_point(DCE_Polygon,i)) + "  "+str(get_selected_point(DCE_Polygon,i+1)) )
    # print(get_selected_point(DCE_Polygon,0))
    # print(calc_k_with_points(DCE_Polygon,0,3,1))
    # print(calc_k_with_points(DCE_Polygon,0,get_number_of_points(DCE_Polygon),1))
    # print("--------------------------------------------------")
    # temp = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
    # print(temp)
    # print(get_selected_point(DCE_Polygon,temp[0][0]))
    # test = calc_k_with_points(DCE_Polygon,0,3,2)
    # print("test")
    # print(test)
    # print("--------------------------------------------------")
    # sort_arr = update_element(sort_arr,i-2, k_temp[0])
    # sort_arr = update_element(sort_arr,i-1,k_before[0])
    # sort_arr = update_element(sort_arr, i, k_act[0])
    # sort_arr = update_element(sort_arr,i+1,k_after[0])

    # k_temp = calc_k_with_points(DCE_Polygon,4,3,0)
    # k_temp2 = calc_k_with_points(DCE_Polygon,0,4,1)
    # print(k_temp)
    # print(k_temp2)
    # print(get_lowest_k(DCE_Polygon, options))
    # print("nach hinzufügen")
    # print(sort_arr)
    # print("nach Sortieren")
    # sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")] 
    # print(sort_arr)
    # print("____________________________________________________________")





















################################## Zweiter Versuch

# def simplify_polygon(arr, fNoP, options):
#     DCE_Polygon = create_Polygon_from_array(arr)  #transform array to polygon for further calculations
#     if fNoP >= len(arr):
#         #print("Finnal NoP kleiner als gegebenes Array")
#         return polygon_to_pixels(DCE_Polygon)
#     k_val = []
#     NoP = get_number_of_points(DCE_Polygon)
#     k_val_arr = calc_k_for_all_points(DCE_Polygon, NoP)

#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     #print(sort_arr)
#     index_arr = []
#     k_val_arr_end = []
#     print(sort_arr)
#     i = int(sort_arr[0][0])
#     print(i)
#     print("stop1")

#     for i in range(NoP-fNoP):
#         indic = int(sort_arr[0][0])
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#         k_val.append(sort_arr[0][1])
#         sort_arr = np.delete(sort_arr, 0, axis = 0)
#         if indic == 0:
#             k_before = calc_k_with_points(DCE_Polygon, 1,0,2)
#         else:
#             k_before = calc_k_with_points(DCE_Polygon, indic-1,indic,indic+1)
#         #k_act = calc_k_with_points(DCE_Polygon,indic,indic-1,indic+1)
#         k_after = calc_k_with_points(DCE_Polygon,indic+1,indic+2,indic-1)
#         print("kbef: "+str(k_before[0]) +"(Stelle:"+str(indic-1) + ") kact "+str(k_act[0])+" stelle "+str(indic)+" kafter" + str(k_after[0])  + " an stelle:" + str(indic+1))
#        # k_temp = calc_k_with_points(DCE_Polygon,i-2,i+1,i-1)

#         sort_arr = update_element(sort_arr,indic-1,k_before[0])
#         #sort_arr = update_element(sort_arr, indic, k_act[0])
#         sort_arr = update_element(sort_arr,indic+1,k_after[0])
#         #sort_arr = update_element(sort_arr,i+1,k_temp[0])

#         sort_arr = sort_arr_func(sort_arr)
        
#         print(sort_arr)
#         print(k_val)
#         print("stop")

#     print(k_val)
#     print("stop")

  
#     return(polygon_to_pixels(DCE_Polygon))
    








##manueller Versuch DCE einfach zu implementieren





# def manual(arr):
#     DCE_Polygon = create_Polygon_from_array(arr)
#     NoP = get_number_of_points(DCE_Polygon)

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, NoP)
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     indic = int(sort_arr[0][0])
#     print(sort_arr)
#     print(get_lowest_k(DCE_Polygon, " "))
#     DCE_Polygon.plot()
#     plt.show()
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     print("puntk an stelle " + str(indic)  + "entfertn")
#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()

#     indic = int(sort_arr[0][0])
#     print(sort_arr)
#     print(polygon_to_pixels(DCE_Polygon))
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon.plot()
#     plt.show()


#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     DCE_Polygon.plot()
#     plt.show()
#     print("stop")

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     indic = int(sort_arr[0][0])
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     sort_arr = sort_arr_func(sort_arr) 
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     indic = int(sort_arr[0][0])
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     indic = int(sort_arr[0][0])
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     sort_arr = sort_arr_func(sort_arr)
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     indic = int(sort_arr[0][0])
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     sort_arr = sort_arr_func(sort_arr)
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()


#     k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     print(sort_arr)
#     indic = int(sort_arr[0][0])
#     print(get_selected_point(DCE_Polygon,indic))
#     DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     sort_arr = sort_arr_func(sort_arr)
#     print(sort_arr)
#     DCE_Polygon.plot()
#     plt.show()

















   
# def simplify_polygon_second(arr, fNoP, options):

#     DCE_Polygon = create_Polygon_from_array(arr)
#     NoP = get_number_of_points(DCE_Polygon)

#     k_val_arr = calc_k_for_all_points(DCE_Polygon, NoP)
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     # print(":::::::::D:::::::::::::")
#     # print(get_lowest_k(DCE_Polygon,options))
#     # print(get_selected_point(DCE_Polygon,0))
#     # print(sort_arr)
#     # print(get_selected_point(DCE_Polygon,int(sort_arr[0][0])))
#     # DCE_Polygon = delete_point_from_polygon(DCE_Polygon, int(sort_arr[0][0]))
#     # temp = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#     # temp = np.asarray(temp, dtype="float64")
#     # temp = temp[np.argsort(temp[:,1], kind="mergesort")]
#     # print(temp)
#     # print(get_selected_point(DCE_Polygon,int(temp[0][0])))
#     # print(get_lowest_k(DCE_Polygon,options))
#     # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")



#     actNop = get_number_of_points(DCE_Polygon)

#     del_k_values = [] 
#     del_indic_values = []
#     #print(sort_arr)
#     #print(get_selected_point(DCE_Polygon,(int(sort_arr[0][0])-1)))
#     del_point_val = []

#     while(actNop>= fNoP):
#         indic = int(sort_arr[0][0])
#         #del_point_val.append(get_selected_point(DCE_Polygon,indic))
#        # print("indic" + str(indic) + "Nop Poly" + str(get_number_of_points(DCE_Polygon)))
#         # if indic > get_number_of_points(DCE_Polygon):
#         #     indic = int(sort_arr[1][0])
#             ############################################################################################
#             #Muss noch behandelt werden?
#         #temp = get_lowest_k(DCE_Polygon,options)
#         # if round(sort_arr[0][1],6) != round(temp[1],6):
#         #     print("es ist was falsch gelaufen")
#         #     print("indic" + str(indic) + "  sort arr: " + str(sort_arr))
#         #     print("temp: " + str(temp))
#         #     print(round(sort_arr[0][1],6))
#         #     print(round(temp[0],6))
#         #     print("stop")

        
        
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon,indic)
#         del_k_values.append(sort_arr[0][1])f
#         del_indic_values.append(indic)
#        # print(len(sort_arr))
#         sort_arr = np.delete(sort_arr, 0, axis = 0)
#         #print(len(sort_arr))
#         k_val_arr = calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#         sort_arr_temp = np.asarray(k_val_arr, dtype="float64")
#         sort_arr_temp = sort_arr_temp[np.argsort(sort_arr_temp[:,1], kind="mergesort")]
       
        
#         if(indic == 0):
#            # print("indic 0")
#             temp_NoP = get_number_of_points(DCE_Polygon)
#             k_bef = calc_k_with_points(DCE_Polygon, temp_NoP-1,temp_NoP-2, indic)
#             k_act = calc_k_with_points(DCE_Polygon, indic,temp_NoP-1, indic+1)
#             k_aft = calc_k_with_points(DCE_Polygon,indic+1,indic,indic+2)
#            # print("indic 0")
#            # print("kbef: "+str(k_bef[0]) +"(Stelle:"+str(temp_NoP) + ") kact "+str(k_act[0])+" stelle "+str(indic)+" kafter" + str(k_aft[0])  + " an stelle:" + str(indic+1))
#             sort_arr = update_element(sort_arr, temp_NoP-1,k_bef[0])
#             sort_arr = update_element(sort_arr, indic,k_act[0])
#             sort_arr = update_element(sort_arr, indic+1,k_aft[0])
#         else:
#           #  print("indic NICHT 0")
#             temp_NoP = get_number_of_points(DCE_Polygon)
#            # print(sort_arr)
#             k_bef = calc_k_with_points(DCE_Polygon, indic-1,indic-2, indic)
#             if indic+1 > temp_NoP:
#                 k_act = calc_k_with_points(DCE_Polygon, indic,indic-1, 0)
#             else:
#                 k_act = calc_k_with_points(DCE_Polygon, indic,indic-1, indic+1)
#                 if indic+2 > temp_NoP:
#                     #print(indic+2)
#                    # print("A1")
#                     k_aft = calc_k_with_points(DCE_Polygon,indic+1,indic,1)
#                 else:
#                   #  print("A1 Else")
#                     k_aft = calc_k_with_points(DCE_Polygon,indic+1,indic,indic+2)
#             #print("länge sort array"+ str(len(sort_arr)) +  "  Punkte Polygon" + str(get_number_of_points(DCE_Polygon)))
            
#            # print("indic NICHT 0")
#            # print("kbef: "+str(k_bef[0]) +"(Stelle:"+str(indic-1) + ") kact "+str(k_act[0])+" stelle "+str(indic)+" kafter" + str(k_aft[0])  + " an stelle:" + str(indic+1))
#             sort_arr = update_element(sort_arr, indic-1,k_bef[0])
#             sort_arr = update_element(sort_arr, indic,k_act[0])
#             #sort_arr = update_element(sort_arr, indic+1,k_aft[0])

           
#             #print("_______________________________________________")
#             if fNoP == get_number_of_points(DCE_Polygon):
#                 print(del_indic_values)
#                 print(del_point_val)
#                 print(del_k_values)
#                 return polygon_to_pixels(DCE_Polygon)
#             sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]

#             k_val_arr  =calc_k_for_all_points(DCE_Polygon, get_number_of_points(DCE_Polygon))
#             sort_arr_temp = np.asarray(k_val_arr, dtype="float64")
#             sort_arr_temp = sort_arr_temp[np.argsort(sort_arr_temp[:,1], kind="mergesort")]
#             # print("_______________________________________________")
#             # #print("indic 3 "+str(calc_k_with_points(DCE_Polygon,3,2,4)))
#             # print("indic 4 "+str(calc_k_with_points(DCE_Polygon,4,3,5)))
#             # print("sort_arr")
#             # print(sort_arr)
#             # print("...........................................")
#             # print(sort_arr_temp)
#             actNop = get_number_of_points(DCE_Polygon)
#             #print("___________________________________________________")



#         #sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#         #sort_arr = del_indic(sort_arr,indic)
#         #print("__________________________________________________")
#         #sort_arr = sort_arr_func(sort_arr)
        

        
#         # print(sort_arr)
#         # print(del_k_values)
#         # print("stop")

#     return create_Polygon_from_array(arr)











      
        # if indic-1 == 0:
        #     print("kbef_vals (indic =0)" + str(indic-1) + ", "+ str(1) + ", "+ str(get_number_of_points(DCE_Polygon)-1))
        #     k_bef = calc_k_with_points(DCE_Polygon, 0, 1,(NoP_temp-1) )        
        # else:
        #     print("kbef_vals" + str(indic-1) + ", "+ str(indic) + ", "+ str(indic+1))
        #     if indic+1 > NoP_temp:
        #         if indic >= NoP_temp:
        #             k_bef = calc_k_with_points(DCE_Polygon, indic-1, 0, 1) #RICHTIG??
        #         else:
        #             k_bef = calc_k_with_points(DCE_Polygon, indic-1, 0, indic) #RICHTIG??
        #     elif indic == NoP_temp:
        #         k_bef = calc_k_with_points(DCE_Polygon, indic-1, indic+1, 1)
        #     else:
        #         k_bef = calc_k_with_points(DCE_Polygon, indic-1, indic+1, indic)
        # print("kbef_res "+ str(k_bef))
        # print("kact_vals" + str(indic) + ", "+ str(indic+1) + ", "+ str(indic-1))
        # if indic+1 > NoP_temp:
        #     if indic > NoP_temp:
        #         k_act = calc_k_with_points(DCE_Polygon, NoP_temp, 0, NoP_temp-1) #Richtig???
        #     else:
        #         k_act = calc_k_with_points(DCE_Polygon,indic, 0, indic-1) #RICHTIG??
        # else:
        #     k_act = calc_k_with_points(DCE_Polygon,indic, indic+1, indic-1)
        # print("kact_res "+ str(k_act))










#ganz alter Versuch

# def simplify_polygon_k_with_angle(arr, final_number_of_points, options):
#     """
#     returns a polygon, which is simplified to a given number of points
#     K Calculation with using angles and distances

#     @param arr: 2-dim Array with points as tupel, like [[1,2],[2,1],...]
#     @param final_number_of_points: int for the number of points of the returned polygon
#     @return array:  which was simplified to the given number of points
#     """

   
#     DCE_Polygon = create_Polygon_from_array(arr)  #transform array to polygon for further calculations
#     if final_number_of_points >= len(arr):
#         #print("Finnal NoP kleiner als gegebenes Array")
#         return polygon_to_pixels(DCE_Polygon)
    




#     NoP = get_number_of_points(DCE_Polygon)
#     k_val_arr = calc_k_for_all_points(DCE_Polygon, NoP)
#     #print(k_val_arr) #

#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#     #print(sort_arr)
#     index_arr = []
#     k_val_arr_end = []
    
#     while(NoP > final_number_of_points):
  
#         i = int(sort_arr[0][0])
#         NoP = get_number_of_points(DCE_Polygon)
     
        
#         if(i==0):
#             # print("erster Fall i ist 0")
#             print("richtiger K Wert? IF Fall" + str(i))
#             print(sort_arr[0][1])
#             low_k = get_lowest_k(DCE_Polygon, options)
#             print(low_k)
#             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#             k_val_arr_end.append(sort_arr[0][1])
#             index_arr.append(sort_arr[0][0])
#            # print("i ist 0")
#             act_NoP = get_number_of_points(DCE_Polygon)
#             NoP = NoP-1

#             # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#             # print("sort vor delete i =0")
#             # print(sort_arr)
#             # print(len(sort_arr))
#             sort_arr = np.delete(sort_arr, 0, axis = 0)
#             # print("sort nach delete i=0")
#             # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#             # print(sort_arr)
#             # print(len(sort_arr))
#             # print("i " + str(i)+ "actNop " + str(act_NoP) + "länge sort array "+ str(len(sort_arr)) +" Anzahl PUnkte Polygon " + str(get_number_of_points(DCE_Polygon)) )

#             k_before = calc_k_with_points(DCE_Polygon, (act_NoP-1),(act_NoP-2),0)
#             k_act = calc_k_with_points(DCE_Polygon, 0,(act_NoP),1)
#             k_after = calc_k_with_points(DCE_Polygon,1,0,2)
#             # print("k_before")
#             # print(k_before)
#             # print("k_after")
#             # print(k_after)
#            # if (k_act[0] == 0) or (k_before[0] == 0):
#                 # print("Fehler (if 1 Fall)")
#                 # print("i ist" + str(i))
#             sort_arr = update_element(sort_arr,(act_NoP-1), k_before[0])
#             sort_arr = update_element(sort_arr,0, k_act[0])
#             sort_arr = update_element(sort_arr,1, k_after[0])
#             sort_arr = sort_arr_func(sort_arr)

#             # np.insert(sort_arr,0,[0, k_before[0] ])
#             # np.insert(sort_arr,act_NoP,[act_NoP, k_after[0]])
          
#             #sort_arr = sort_arr[np.argsort(sort_arr[:,1])] #sort_arr_func(sort_arr) #sort_arr[np.argsort(sort_arr[:,1])]
#             test = 0
#             if(final_number_of_points == len(sort_arr)):
#               return polygon_to_pixels(DCE_Polygon)
            
#         else:
#            #print("Ursprung")
#             # print(len(sort_arr))
#             # print(sort_arr[0])
           
#             print("richtiger K Wert? ELSE FALL######################################################################################" + str(i))
#             print(sort_arr[0][1])
#             low_k = get_lowest_k(DCE_Polygon, options)
#             print(low_k)
#             #print(get_array_with_points(DCE_Polygon))
#             DCE_Polygon = delete_point_from_polygon(DCE_Polygon,i)
#             act_NoP = get_number_of_points(DCE_Polygon)
#             if sort_arr[0][1] == 0:
#                 # print("Fehler anfang (if else  Fall)")
#                 # print(sort_arr[0])
#                 test = 0
#             k_val_arr_end.append(sort_arr[0][1])
#             index_arr.append(sort_arr[0][0])
#             # print(get_array_with_points(DCE_Polygon))
#             NoP = NoP-1
#             temp_NoP = get_number_of_points(DCE_Polygon)

#             # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#             # print("sort vor delete ELSE Fall")
#             # print(sort_arr)
#             # print(len(sort_arr))
#             sort_arr = np.delete(sort_arr, 0, axis = 0)
#             # print("sort nach delete ELSE FALL")
#             # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#             # print(sort_arr)
#             # print(len(sort_arr))
            
#             # print("kleinstes Element gelöscht")
#             # print(len(sort_arr))
#             # print(sort_arr[0])


#             k_before = calc_k_with_points(DCE_Polygon,i-1,i-2,i)
            
         


#             if i+1>len(sort_arr):
#                print("i+1 größer als sortarry")
#                k_act = calc_k_with_points(DCE_Polygon,i,i-1,1)
#                k_after = calc_k_with_points(DCE_Polygon,1,i,0) 
           
#             else:
#                 #if i == 3:
#                    # print("i ist 3")
#                 k_act = calc_k_with_points(DCE_Polygon,i,i-1,i+1)
#                 if i+2 > len(sort_arr):
#                     print("i+2 größer als sortarray" )
#                     # print("i+1: " +str(i+1) + "i: "+ str(i)+ " i+2:" +str(i+2))
#                     # print("actnop: " + str(act_NoP) + "acntop-1:  " + str(act_NoP-1))
#                     # print(len(sort_arr))
#                     k_after = calc_k_with_points(DCE_Polygon,(act_NoP-1),(act_NoP-2),0) 
#                     # print(k_after)
#                     # print(get_array_with_points(DCE_Polygon))
#                     # print("stop")
#                 else:
#                     print("i+2 nicht größer als sort array")
#                     print(str(i+1) + "  i: "+ str(i) + "i+2:  " + str(i+2) )
#                     # len(sort_arr)
#                     print("____________________________________________________________________")
#                     k_after = calc_k_with_points(DCE_Polygon,i+1,i,i+2) 
#                     print(str(k_before) + "  " + str(i-1))
#                     print(str(k_act) + "  "+str(i))
#                     print(str(k_after) + "  "+ str(i+1))
#                     print("eigentlich müsste:" + str(get_lowest_k(DCE_Polygon,options))+ " rauskommen")
#                     print("stop")



#                 #print("k_after Else 2. Fall" + "i: "+ str (i))
#                # print(k_after)
#                 #print(k_after[0])
#             # print(i)
#             # print("kanten k s geupdatet")
#             #k_after = calc_k_with_points(DCE_Polygon,i+1,i,i+2) 
#             #if (k_act == 0) or (k_before == 0):
#                 # print("Fehler")
#                 # print("i ist" + str(i))
#             print("k_before"+ str(k_before) +"an Stelle "+ str(i-1))
#             #print("k_act"+ str(k_act)+"an Stelle "+ str(i))
#             print("k_after"+ str(k_after)+"an Stelle "+ str(i+1))
#             print("sort_arr vor aktualisierung ELSE+++++++++++++++++++++++++++++++++++++++++")
#             print(sort_arr)
#             sort_arr = update_element(sort_arr,i-1, k_before[0])
#             sort_arr = update_element(sort_arr,i, k_act[0])
#             #sort_arr = update_element(sort_arr,i+1, k_after[0])
#             print("sort arr nach aktualisierung ELSE +++++++++++++++++++++++++++++++++++")
#             print(sort_arr)
        
#             sort_arr = sort_arr_func(sort_arr)
#             # print(index_arr)
#             # print(k_val_arr_end)
#             # if(final_number_of_points == len(sort_arr)):
#             #     return polygon_to_pixels(DCE_Polygon)

#             # print(sort_arr)
#             # print("stop")
#             # print(sort_arr[0])
#             # print(len(sort_arr))
#             #np.insert(sort_arr,i-1, [i-1, k_before[0]])
#             #np.insert(sort_arr,i, [i, k_after[0]])
#             #sort_arr = sort_arr[np.argsort(sort_arr[:,1])] #sort_arr_func(sort_arr)
#             #print("sort_arr")
#             #print(sort_arr)
#    # print("raus")    
#     print("index arr")
#     print(index_arr)
#     print(k_val_arr_end)


#    # print("klappt?")



# def ref(arr, FNoP, options):
#         print("REFERENCE--BEGIN------------------------------------------------------------------")
#         DCE_Polygon = create_Polygon_from_array(arr)
#         NoP = get_number_of_points(DCE_Polygon)
#         k_val_arr = calc_k_for_all_points(DCE_Polygon)
#         sort_arr = np.asarray(k_val_arr, dtype="float64")
#         sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#         indic = int(sort_arr[0][0])
#         print(sort_arr)
#         print(get_lowest_k(DCE_Polygon, " "))
#         # DCE_Polygon.plot()
#         # plt.show()
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#         print("puntk an stelle " + str(indic)  + "entfertn")
#         k_val_arr = calc_k_for_all_points(DCE_Polygon)
#         sort_arr = np.asarray(k_val_arr, dtype="float64")
#         sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="mergesort")]
#         print(sort_arr)
#         print("REFERENCE---END-----------------------------------------------------------------")
#         # DCE_Polygon.plot()
#         # plt.show()




#     return polygon_to_pixels(DCE_Polygon)
 


# Nun wird der Prozess innerhalb der DCE.py Datei genauer erläutert (s. Listing \ref{cd:DCE_simplify_polygon.py}). Da die DCE in dieser Arbeit mit GeoPandas (s. Kap. \ref{subsec:Geopandas}) implementiert wurde, muss das Array zuerst in ein \lstinline|Geopandas.Geoseries| Objekt transformiert werden. Danach kann von diesem Polygon die Gesamtpunktanzahl berechnet werden, die die Begrenzung des folgenden Iterators in der Schleife darstellt. Zuvor kann der Fall abgefangen werden, dass ein Polygon bereits weniger Punkte als die Punktanzahl auf die das Polygon reduziert werden soll, hat. \\
# 	\lstinputlisting[linerange={11,20-23,25-27,29,30,32,34,35}, caption={Ausschnitt aus \protect\lstinline|simplify_polygon_k_with_angle| Funktion in DCE.py}, label = {cd:DCE_simplify_polygon.py}]{../Code/DCE/DCE.py}
# 	Die Schleife iteriert über alle Punkte im Polygon und berechnet dabei zuerst den niedrigsten K Wert. Diese Funktion wirft auch den Index des niedrigsten Wertes zurück. Dann wird überprüft, ob das Polygon bereits ein Dreieck ist. In diesem Fall wird die Schleife abgebrochen und das Polygon wird als Array zurückgegeben. Falls dies nicht passiert, wird das Polygon mit einem neuen Polygon überschrieben, bei welchem der Punkt an dem Index des geringsten K Wertes entfernt worden ist. Danach wird abgefragt, ob bereits die gewünschte Anzahl der Punkte erreicht worden ist. Wenn in diese Abfrage gegangen wird, wird das Polygon als Array zurückgegeben, ansonsten beginnt die Schleife von vorne. 
# 	Dies \lstinline|get_lowest_k| Funktion ist in Listing \ref{cd:DCE_get_lowest_k.py} abgebildet. Diese Funktion iteriert über alle Punkte des gegebenen Polygons und berechnet für jeden Punkt den K Wert. Wenn der betrachtete Punkt der erste Punkt im Polygon ist, wird der K Wert mit diesem Punkt, dem nächsten Punkt und dem letzten Punkt berechnet. Falls dies nicht der Fall ist, wird überprüft ob \lstinline|i| der Gesamtpunktanzahl entspricht. Dies bedeutet, dass der K Wert für jeden Punkt im Polygon berechnet wurde, woraus folgt, dass die Schleife abgebrochen werden kann. \\
# 	Falls dies nicht der Fall ist, wird der zweite K Wert berechnet, indem der betrachtete Punkt, der nächste und der vorherige Punkt genutzt wird. Dieser zweite K Wert wird mit dem ersten K Wert verglichen um den Geringeren der beiden zu erfassen. Der geringere Wert wird im ersten K Wert gespeichert und der \lstinline|index_for_point_on_k| auf \lstinline|i| gesetzt. \\
# 	\lstinputlisting[linerange={40,47,49-61,63}, caption={Ausschnitt aus \protect\lstinline|get_lowest_k| Funktion in DCE.py}, label = {cd:DCE_get_lowest_k.py}]{../Code/DCE/DCE.py}
# 	Wenn die Schleife abgebrochen worden ist, wird der Index des geringsten K Wertes und der K Wert selbst in einem Array zurückgegeben.\\


# Nun wird der Prozess innerhalb der DCE.py Datei genauer erläutert (s. Listing \ref{cd:DCE_simplify_polygon_A1.py}). Da die DCE in dieser Arbeit mit GeoPandas (s. Kap. \ref{subsec:Geopandas}) implementiert wurde, muss das Array zuerst in ein \lstinline|Geopandas.Geoseries| Objekt transformiert werden. \\
# 	Für dieses Objekt wird dann ein 2 dimensionales Array mit dem Index des jeweiligen Punktes und dem dazugehörigen K Wert erzeugt (s. Listing \ref{cd:DCE_calc_k_for_all_points.py}). Hier wird mit einer IF Abfrage der Sonderfall abgefangen, dass der erste Punkt des Polygons (an Stelle 0) für die K Wert Berechnung genutzt wird.
# 	Das Array, welches diese Funktion zurückgibt, kann mit der Numpy internen Funktion \lstinline|argsort| aufgrund des 1. Wertes im Array sortiert werden. Dadurch gelangt der geringste K Wert mitsamt dem entsprechenden Index im Polygon an die erste Stelle Arrays. Dieses Array wird im folgenden als \lstinline|sort_arr| bezeichnet. Ein Punkt wird immer mit zwei neu berechneten K Werten ersetzt. \\

# 	\lstinputlisting[basicstyle=\ttfamily\scriptsize,firstnumber = 6,linerange={109,115,124,135,137,138,140,141,145,147,149,150,152,153,157,159,161,162,172,190,200,210}, caption={Ausschnitt 2 aus \protect\lstinline|simplify_polygon| Funktion in DCE.py}, label = {cd:DCE_simplify_polygon_A2.py}]{../Code/DCE/DCE.py}

# 	Es folgt danach eine While Schleife (s. Listing \ref{cd:DCE_simplify_polygon_A2.py}) mit der Abbruchbedingung, dass die Länge von \lstinline|sort_arr| größer gleich der gewünschten Endpunktzahl (\lstinline|fNoP|, final Number of Points) ist. \\
# 	In dieser Schleife wird der Index des Punktes mit dem geringsten K Wert (\lstinline|indic|) aus dem \lstinline|sort_arr| gelesen und zur Löschung des Punktes an dieser Stelle im Polygon genutzt. Dieses um einen Punkt reduzierte Polygon überschreibt dann das ursprüngliche Polygon. In einer weiteren Variable wird dann die aktuelle Punktzahl des neuen Polygons gespeichert, um die Sonderfälle bei der Berechnung der K Werte abzufangen. \\
	
# 	Wenn \lstinline|indic| der aktuellen Punktanzahl im Polygon entspricht, werden als vorheriger Punkt der letzte Punkt und als aktueller Punkt der erste Punkt im Polygon genutzt. \\
# 	Da die Berechnung von K in dieser Implementierung drei Punkte erfordert, müssen die Fälle behandelt werden, wenn \lstinline|indic-1| oder \lstinline|indic+1| außerhalb des Polygons oder \lstinline|sort_arr| liegen. \\
# 	Wenn \lstinline|indic-1| den Wert 0 hat, muss der vorherige Punkt der erste Punkt im Polygon sein. Diese Funktion wird dann mit den Werten 0, als Punkt für den K berechnet wird, 1 für den nächsten Punkt, und \lstinline|NoP - 1| für den letzten Punkt im Polygon gestartet. \\
# 	Im Else Teil dieser Abfrage wird mit einer weiteren IF Abfrage abgefragt, ob \lstinline|indic+1 > NoP_temp| ist. Dies ist der Fall, wenn \lstinline|indic| der letzte Punkt im Polygon ist. Dann wird \lstinline|k_bef| mit den Werten \lstinline|indic-1, 0, indic| berechnet, da der letzte Punkt im Polyon betrachtet werden muss.
# 	Wenn dies nicht der Fall ist, kann \lstinline|indic-1| ohne Beachtung von Sonderfällen berechnet werden, indem der betrachtete Punkt (\lstinline|indic-1|), der nachfolgende Punkt (\lstinline|indic|) und der vorherige Punkt (\lstinline|indic-2|) in der Funktion genutzt wird.
# 	Außerhalb von diesem Else Teil existiert in der While Schleife eine weitere If Abfrage, die ebenfalls den Fall abdeckt, dass \lstinline|indic+1 > NoP_temp| ist. Dies ist auch für die Berechnung von dem K Wert des aktuellen (neuen) K Wertes an der Stelle \lstinline|indic| wichtig. Dieser Wert wird dann anhand des zweiten Punktes (\lstinline|indic|), zum ersten Punkt (0) und zu vorherigen Punkt (\lstinline|indic-1|) berechnet. Sonst wird die normale Berechnung mit den Werten \lstinline|indic, indic+1, indic-1| ausgeführt.

	
# 	\lstinputlisting[basicstyle=\ttfamily\scriptsize,linerange={218,220,221,229,231,232,240-244}, caption={Ausschnitt 1 aus \protect\lstinline|update_sort_array| Funktion in DCE.py}, label = {cd:DCE_update_sort_array_A1.py}]{../Code/DCE/DCE.py}

# 	Da die K Werte nun berechnet wurden, müssen diese im \lstinline|sort_arr| aktualisiert werden. Dies geschieht in der Funktion \lstinline|update_sort_array| (s. Listings \ref{cd:DCE_update_sort_array_A1.py} - \ref{cd:DCE_update_sort_array_A4.py}), die nun näher erläutert wird. \\
# 	Die Funktion benötigt, das \lstinline|sort_arr|, den aktuellen Index \lstinline|indic|, sowie die zuvor berechneten K Werte für den vorherigen Punkt \lstinline|k_bef|, den aktuellen Punkt \lstinline|k_act| und das Polygon. \\
# 	\newpage
# 	Es werden zunächst zwei Boolean Variablen initialisiert, die anzeigen, ob ein Wert im \lstinline|sort_arr| gefunden wurde und überschrieben werden muss. Außerdem wird der erste Wert aus dem \lstinline|sort_arr| gelöscht. \todo{Zweimal den ersten Wert zu löschen ist doch eigentlich sinnfrei? Aber sonst schrumpft das sort Array nicht, weil immer zwei Elemente hinzugefügt werden und nur eins gelöscht wird...}\\
# 	Im nächsten Schritt wird dann mit einer Numpy Methode die entsprechende Stelle im \lstinline|sort_arr| gesucht an der die K Werte überschrieben werden müssen. Hier wird ebenfalls nach dem nachfolgenden Wert von \lstinline|indic| gesucht, der in der darauffolgenden IF Abfrage genutzt wird. Diese Abfrage fängt den Fall ab, dass \lstinline|indic| den Wert 0 hat oder der nächste Wert nicht existiert. Wenn dies der Fall ist, wird wieder der erste Wert des \lstinline|sort_arr| Arrays gelöscht, sonst wird der letzte Wert gelöscht.

# 	\lstinputlisting[basicstyle=\ttfamily\scriptsize,linerange={249,250,252-256,259,261-265,268-270},firstnumber=12, caption={Ausschnitt 2 aus \protect\lstinline|update_sort_array| Funktion in DCE.py}, label = {cd:DCE_update_sort_array_A2.py}]{../Code/DCE/DCE.py}

# 	Wenn weiterhin \lstinline|indic != 0| gilt, wird mit zwei aufeinanderfolgenden IF Abfragen der Wert der gesuchten Indizes im \lstinline|sort_arr| Array abgefragt. Da diese immer aus einem 2 dimensionales Array bestehen, kann mit einer Größenabfrage abgefragt werden, ob ein Wert gefunden wurde. Wenn die Größe den Wert 0 hat, bzw. kein Wert gefunden wurde, wird ein Numpy Array mit dem entsprechenden Index und K Wert erzeugt, welches anschließend mit dem \lstinline|sort_arr| verbunden wird. Dies passiert, damit immer für jeden Punkt im Polygon ein K Wert vorhanden ist, wenn dieser vorher entfernt wurde.


# 	\lstinputlisting[firstnumber=28, basicstyle=\ttfamily\scriptsize,linerange={273-280}, caption={Ausschnitt 3 aus \protect\lstinline|update_sort_array| Funktion in DCE.py}, label = {cd:DCE_update_sort_array_A3.py}]{../Code/DCE/DCE.py}

# 	In Ausschnitt 3 (s. Listing \ref{cd:DCE_update_sort_array_A3.py}) werden die K Werte im \lstinline|sort_arr| aktualisiert. Auch hier wird zunächst der Sonderfall betrachtet, wenn \lstinline|Indic = 0| ist, da nun der letzte Punkt (als vorheriger) und erste Punkt (als aktueller) im Array aktualisiert werden muss. Sonst wird abgefragt, ob ein Wert an das \lstinline|sort_arr| angehängt wurde, was ein Überschreiben des Wertes überflüssig macht. Wenn dies nicht der Fall ist, wird das entsprechende Element im Array mit dem neuberechneten K Wert überschrieben.

# 	\lstinputlisting[firstnumber=36, basicstyle=\ttfamily\scriptsize,linerange={289,292,293,304,306}, caption={Ausschnitt 4 aus \protect\lstinline|update_sort_array| Funktion in DCE.py}, label = {cd:DCE_update_sort_array_A4.py}]{../Code/DCE/DCE.py}

# 	Zuletzt werden die Indizes des \lstinline|sort_arr| neu nummeriert, da es sonst beim Löschen ein Wert außerhalb des Polygons angesteuert wird. \todo{ich weiß auch noch nicht so genau, warum das überhaupt der Fall ist. Er löscht den aktuellen Wert, aktualisiert den vorherigen und fügt den neuberechneten hinzu -> eigentlich muss es auch ohne Neunummerierung schrumpfen} Im letzten Schritt wird das Array wieder nach dem geringsten K Wert sortiert und daraufhin zurückgeben. \\
# 	Damit ist die While Schleife aus Listing \ref{cd:DCE_simplify_polygon_A2.py} fast beendet. Es wird in dieser die aktuelle Punktzahl mit der gewünschten verglichen und das Polygon wird im Erfolgsfall zurückgeben. Ansonsten beginnt die Schleife von vorne. \\
	# Nun wird die Berechnung des K Wertes beschrieben.

	# \lstinputlisting[basicstyle=\ttfamily\scriptsize,linerange={358-362,364,367-369,373,376}, caption={Ausschnitt aus \protect\lstinline|calc_k_for_all_points| Funktion in DCE.py}, label = {cd:DCE_calc_k_for_all_points.py}]{../Code/DCE/DCE.py}

	# Der K Wert wird in der folgenden Funktion \lstinline|calc_k_with_points| berechnet. Diese Methode basiert auf der Formel \ref{Equ_K_Bark} ( nach \citet{Latecki1999a})und ist dahingehend abgeändert worden, dass diese nicht mit Liniensegmenten, sondern mit drei Punkten berechnet werden kann. Die abgeänderte Formel lautet:
	# \begin{equation}
	# 	K(p,S_1,S_2) = \frac{\beta(p, S_1, S_2)l(p, S_1)l(p, S_2)}{l(p, S_1) + l(p, S_2)} 
	# 	\label{equ_K_DCE_points}
	# \end{equation}
	# Im Programmcode ist dies folgendermaßen implementiert (s. Listing \ref{cd:DCE_calc_k_with_points.py}). Es wird zunächst der Winkel $\beta$ berechnet, indem alle drei Punkte und das Polygon übergeben werden. Danach werden die beiden Distanzen zwischen $p, S_1$ und $p, S_2$ berechnet. Die Winkelberechnungsfunktion arbeitet mit NumPy und die Distanzberechnungsfunktion basiert auf Funktionen, die GeoPandas bietet.
	# \lstinputlisting[basicstyle=\ttfamily\scriptsize,linerange={406,418-420,422,423}, caption={Ausschnitt aus \protect\lstinline|calc_k_with_points| Funktion in DCE.py}, label = {cd:DCE_calc_k_with_points.py}]{../Code/DCE/DCE.py}
	# Diese drei Werte werden dann analog zur Formel \ref{equ_K_DCE_points} zum Wert K berechnet. Als letzten Schritt wird dieser Wert und der Winkel als Array zurückgegeben.
	
	# In Listing \ref{cd:DCE_angle_and_distance.py} ist zu sehen, dass die Winkelberechnungsfunktion mit dem Arcustangens und $\pi$ arbeitet. Dies basiert auf der Dokumentation von NumPy \citep{numpy_angle}. Da die Berechnung ein Array ausgibt, müssen alle Elemente aufsummiert werden, um einen Wert zu erhalten. Dieser Wert wird dann in Radiant umgerechnet und zurückgeben. \\
	# Die Distanzberechnung erfolgt mit einer Funktion, die GeoPandas bei \lstinline|Geopanda.Geoseries| Objekt bietet. Diese errechnet die Distanz zwischen den Punkten \lstinline|p1| und \lstinline|p2|. Danach wird diese zurückgegeben.
	# \lstinputlisting[basicstyle=\ttfamily\scriptsize,linerange={545,557-559,569,570,572,573,577,596,605-608}, caption={Ausschnitte aus \protect\lstinline|get_angle_two_lines| und \protect\lstinline|get_distance_between_two_points| Funktionen in DCE.py}, label = {cd:DCE_angle_and_distance.py}]{../Code/DCE/DCE.py}




# def testarray():
#     p = choosePolygon(1)
#     test_arr = [[4,6.325],[0,5.1235],[3,0.0789],[1,0.3256],[2, 10.125],[5,0.12358]]
#     len_bef = len(test_arr)
#     test_arr = np.asarray(test_arr)
#     sort_test_arr = test_arr[np.argsort(test_arr[:,1], kind="quicksort")]
#     print(sort_test_arr)
#     print("stop")
#     indic = int(sort_test_arr[0][0])


#     k_bef = 7
#     k_act = 12
#     test = update_sort_array_sec(sort_test_arr,indic,k_bef,k_act, p)
#     print(test)
#     print("laenge vor udpate: "+ str(len_bef) + "laenge nach update" + str(len(test)))
#     print("stop 2")
# #testarray()






# def insert_element(arr,indic ,elem):
#     indic_del = np.where(np.isin(arr[:,0], indic))
#     arr = np.delete(arr,indic_del,0)
#     new_k_value = np.array([indic, elem])
#     arr= np.concatenate((arr,[new_k_value]), axis = 0)
#     #arr = sort_arr_func(arr)

#     return arr

# def update_element(arr, indic, k_val):
#     #print("anfangsindic" + str(indic))
#     indic_del = np.where(np.isin(arr[:,0], indic))
#     # print(indic_del)

#     # print(arr[0][1])
#     indic_del = indic_del[0]
#     # print("indic")
#     # print(indic)
#     if indic_del.size == 0:
#         print("not found" + str(indic))
#        # print(arr)
#         new_val_arr = np.array([indic, k_val])
#         #print(new_val_arr)
#         arr = np.concatenate((arr, [new_val_arr]), axis=0)
#         #arr = np.append(arr, [new_val_arr], axis= 0)
#         # print("nach hinzufuegen")
#         # print(arr)
#         #print("stop")
#     else:
#         print("k in sort array wird an stelle " + str(indic_del[0]) + " geupdatet")
#         # print("arr vor update")
#         # print(arr)
#         # print(arr[2][0])
#         # print(arr[2][1])
#         #print(indic_del[0])
#         # print("___________________")
#         arr[indic_del[0]][1] = k_val
#         #print("arr nach update")
#         #print(arr)
#     #     print("_________________________")
#     # print(arr)

#     return arr





# def simplify_polygon_k_immer_neu(arr, fNoP, options):
#     DCE_Polygon = create_Polygon_from_array(arr)
#     NoP = get_number_of_points(DCE_Polygon)
#     indic_arr = []

#     while(get_number_of_points(DCE_Polygon) != fNoP):
#         k_val_arr = calc_k_for_all_points(DCE_Polygon)
#         sort_arr = np.asarray(k_val_arr, dtype="float64")
#         sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="quicksort")]
        

#         indic = int(sort_arr[0][0])
#         indic_arr.append(indic)
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)

#     print("__________________K IMMER NEU___________________")
#     #DCE_Polygon.plot()
#     #plt.show()
#     #print(indic_arr)
#     return polygon_to_pixels(DCE_Polygon)



# def sort_arr_func(sort_arr):
#     sort_by_num = sort_arr[np.argsort(sort_arr[:,0], kind="mergesort")]
#     for i in range(len(sort_by_num)):
#         sort_by_num[i][0]=i
#     sort_by_k =sort_by_num[np.argsort(sort_by_num[:,1], kind="mergesort")]
#     return sort_by_k



# def del_indic(arr, indic):
#     indic_del = np.where(np.isin(arr[:,0], indic))
#     arr = np.delete(arr, indic_del[0][0], axis = 0)
#     return arr





# def update_sort_array(sort_arr, indic, k_bef, k_act, p):
#     NoP_Poly = get_number_of_points(p)
#     overwritten_act = False
#     overwritten_bef = False
    

#     sort_arr = np.delete(sort_arr, 0, axis = 0)

#     sort_array_indic_bef = np.where(np.isin(sort_arr[:,0], indic-1))
#     #sort_array_indic_act = np.where(np.isin(sort_arr[:,0], indic))

#     new_val_arr = np.array([indic, k_act])
#     sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0)
 

#     # sort_array_indic_aft = np.where(np.isin(sort_arr[:,0], indic+1))
#     # if indic == 0 or sort_array_indic_aft[0].size == 0:
#     #     sort_arr = np.delete(sort_arr, 0, axis = 0)
#     # else:
#     #     sort_arr = np.delete(sort_arr, int(sort_array_indic_aft[0][0]), axis = 0)


#     #print("bef indic" + str(sort_array_indic_bef))
#    # print("act indic" + str(sort_array_indic_act))
#     # if indic !=0:
#     # if sort_array_indic_bef[0].size == 0:
#     #     #   print("hinzugefuegt indic" + str(indic-1))
#     #     overwritten_bef = True
#     #     new_val_arr = np.array([indic, k_bef])
#     #     sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0)
#     # else:
#     sort_array_indic_bef = int(sort_array_indic_bef[0][0])
#         #print(sort_array_indic_bef)

#     if sort_array_indic_act[0].size ==0:
#         print("hinzugefuegt indic" + str(indic))
#         overwritten_act = True
#         new_val_arr = np.array([indic, k_act])
#         sort_arr = np.concatenate((sort_arr, [new_val_arr]), axis =0)
#     else:
#         sort_array_indic_act = int(sort_array_indic_act[0][0])


#     # else:
#     #     sort_array_indic_bef = len(sort_arr)-1
#     #     sort_array_indic_act = 0
#     #overwritten_act = False
#     overwritten_bef = False
#     #sort_array_indic_act = int(sort_array_indic_act[0][0])
   
#     # print(indic)
#     print("bef: "+str(sort_array_indic_bef) + "act  " + str(sort_array_indic_act) +" indic " + str(indic))
#     if indic == 0:
#         sort_arr[(len(sort_arr)-1)][1] = k_bef
#         sort_arr[0][1] = k_act
#     else:
#         if overwritten_bef == False:
#             if indic-1 >= len(sort_arr):
#                 sort_array_indic_bef = len(sort_arr)-1
#             sort_arr[sort_array_indic_bef][1] = k_bef
#         if overwritten_act == False:
#             if indic >= len(sort_arr):
#                 sort_array_indic_act = len(sort_arr)-1
#             sort_arr[sort_array_indic_act][1] = k_act


#     #berechen letztes Element neu
#     #last_element = calc_k_with_points(p,len(sort_arr)-1,0, len(sort_arr)-2)
#     #print("last_element")
#     #print(last_element)

 
#     sort_by_num = sort_arr[np.argsort(sort_arr[:,0], kind="quicksort")]
#     #print("indic" + str(indic))
#     # dec_ind = np.where(np.isin(sort_by_num[:,0], indic))
#     # for dec_ind in range(len(sort_by_num)):
#     #     sort_by_num[dec_ind][0] = sort_by_num[dec_ind][0]-1
#     #print("vor neu nummierung")
#     #print(sort_by_num)
#     for i in range(len(sort_by_num)):
#        sort_by_num[i][0]=i
#  #   print("neusortiert")
#     #print(sort_by_num)
#     #print("stop")
# #
#     #sort_by_num[len(sort_by_num)-1][1] = last_element[0]

#     #print(sort_by_num)
#     # print(sort_by_num)
#     # print("stop")

#     sort_by_k =sort_by_num[np.argsort(sort_by_num[:,1], kind="quicksort")]
#     # print(sort_by_k)
#     return(sort_by_k)



# def simplify_polygon_fast(arr, fNoP, options):
#     DCE_Polygon = create_Polygon_from_array(arr)
#     NoP = get_number_of_points(DCE_Polygon)

#     k_val_arr = calc_k_for_all_points(DCE_Polygon)
#     sort_arr = np.asarray(k_val_arr, dtype="float64")
#     sort_arr = sort_arr[np.argsort(sort_arr[:,1], kind="quicksort")]


#     indic_gleich_NoPTemp = 0
#     indicM1_gleich_Null = 0
#     indicP1_gr_NoPTemp_bef = 0
#     indicP1_gr_NoPTemp_act = 0
#     indic_norm_bef = 0
#     indic_norm_act = 0
#     indic_arr = []

#     #print("erstes Sort Array")
#    # print(sort_arr)
#     while(len(sort_arr)>= fNoP):
#         indic = int(sort_arr[0][0])
#         indic_arr.append(indic)
     
#         NoP_before_delete_Polygon = get_number_of_points(DCE_Polygon)
#         NoP_before_delete_sortarray = len(sort_arr)
#         print("indic" + str(indic) + "punktanzahl poly: " + str(get_number_of_points(DCE_Polygon)) + "Laenge sort array" + str(len(sort_arr)))
#         DCE_Polygon = delete_point_from_polygon(DCE_Polygon, indic)
#         entfernter_Punkt = sort_arr[0]
#         #sort_arr = np.delete(sort_arr, 0, axis = 0)

    
#         NoP_temp = get_number_of_points(DCE_Polygon)

#         if indic-1 == 0:
#             k_bef = calc_k_with_points(DCE_Polygon, 0,1, (NoP_temp-1) )
#         else:
#             if indic+1 > NoP_temp:
#                 k_bef = calc_k_with_points(DCE_Polygon, indic-1, 0, indic) #RICHTIG??
#             else:
#                 k_bef = calc_k_with_points(DCE_Polygon, indic-1, indic, indic-2) #muss es nicht indic-1,indic, indic-2 heissen?
            
#         if indic+1 > NoP_temp:   
#             k_act = calc_k_with_points(DCE_Polygon,indic, 0, indic-1) #RICHTIG??
#         else:
#             k_act = calc_k_with_points(DCE_Polygon,indic, indic+1, indic-1)
              
       
   
#         sort_arr = update_sort_array(sort_arr,indic,k_bef[0], k_act[0],DCE_Polygon)
    
#         # print("sort_arr nach aktualisierung")
#         # print(sort_arr)
#         # print(calc_k_with_points(DCE_Polygon,4,0,3))
#         # print(" ")
#         # print("Reference:")
#         # print(calc_k_for_all_points(DCE_Polygon))
#         # print("Reference 2:")
#         # print(get_lowest_k(DCE_Polygon, options))
#         # print(get_number_of_points(DCE_Polygon))


#         # if len(sort_arr) != get_number_of_points(DCE_Polygon):
#         #     print("Punktanzahl Polygon vor Entfernung: "+ str(NoP_before_delete_Polygon) + "  IST Zahl: "+ str(get_number_of_points(DCE_Polygon)))
#         #     print("Punktanzahl array vor Entfernung: "+ str(NoP_before_delete_sortarray) + "  IST Zahl: "+ str(len(sort_arr)))
#         #     print("Fehler; Gesamtpunktanzahl ist verschieden")

#         if (get_number_of_points(DCE_Polygon) == fNoP):
#             print("Basisdaten:")
#             print(indic_arr)
#             DCE_Polygon.plot()
#             plt.show()
#             return polygon_to_pixels(DCE_Polygon)
#     #print(sort_arr)
#     # sort_arr = update_element(sort_arr, indic-1, k_bef[0])
#     # sort_arr = update_element(sort_arr, indic, k_act[0])


#     # print("sort_arr")
#     # print(sort_arr)
#     # DCE_Polygon.plot()
#     # plt.show()
#     print("indic_arr")
#     print(indic_arr)
#     return polygon_to_pixels(DCE_Polygon)






# def calc_k_for_all_points_coords(p):
#     NoP = get_number_of_points(p)
#     temp_k_val_arr = []
#     for i in range(NoP):
#         if i == 0:
          
#             temp = calc_k_with_points(p,i,1, (NoP-1))
#             coords = get_selected_point(p,i)
#             temp_k_val_arr.append([i,temp[0], coords])
#         else:
#             temp = calc_k_with_points(p,i,i+1,i-1)
#             coords = get_selected_point(p,i)
#             temp_k_val_arr.append([i,temp[0], coords])


#     return temp_k_val_arr