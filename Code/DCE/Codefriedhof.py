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