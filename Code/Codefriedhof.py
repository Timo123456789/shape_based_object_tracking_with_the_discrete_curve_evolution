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