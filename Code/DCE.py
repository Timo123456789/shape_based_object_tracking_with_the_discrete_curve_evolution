import numpy as np


def testdurchlauf():
    testpolygon = [[0,0],[2,0],[2,2],[3,4],[1,2]]
    #Alternativ Import einer Textdatei mit Punkten (gleiches Schema wie oben?)
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