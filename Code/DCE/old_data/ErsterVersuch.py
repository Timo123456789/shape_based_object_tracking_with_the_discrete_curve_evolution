# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:46:14 2023

@author: timol
"""
import numpy as np



def gen_pairwise_turn_angles(p):
    n = p.ndim
    high_arr_val = highest_value_from_ndim_array(p)
    O = np.zeros((high_arr_val[0], high_arr_val[1]))
    #O = np.array
    print("O leer")
    print(O)
    print("p")
    print(p)
  
    for i in np.ndenumerate(O):
      #  print("i in for",i)
        for j in np.ndenumerate(O):
          #  print("j in For",i)
            if i != j:
               # print("test i ungleich j")
              #  print(i)
                prev = p[i-1]
                if i == 0:
                    prev = p[n-1]
                v1 = p[i]-p[prev]
                v2 = p[j]-p[i]
                O[i][j] = positiveTurnAngleBetween(v1,v2)                 
    return O

def positiveTurnAngleBetween(v1,v2):
 
  b = np.arctan2(v2[1],v2[0])-np.arctan2(v1[1], v1[0])
  if b>= 0:
     # print("if",b)
      return b
      
  else:
     # print("ifelse", (b+(2*np.pi)) )
      return (b+(2*np.pi))


def highest_value_from_ndim_array(a):
    max_x = np.max(a[:,0])
    max_y = np.max(a[:,1])
    print(max_x, max_y)
    return [max_x, max_y]
  


p = np.array([[3,0],[0,2],[2,4]])
#print("test", highest_value_from_ndim_array(p))
print("Endergebnis", gen_pairwise_turn_angles(p))
