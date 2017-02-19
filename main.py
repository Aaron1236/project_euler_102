#Aaron McKeown, 2/19/17
#ANSWER: 228

import matplotlib.pyplot as plt
import urllib.request
import pandas as pd
import numpy as np
import math

"""
Answer: 228
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed.

Consider the following two triangles:
A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)
It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing
the co-ordinates of one thousand "random" triangles, find the number of triangles for which
the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.

"""

def get_n_clean_n_pickle():
    x = urllib.request.urlopen('https://projecteuler.net/project/resources/p102_triangles.txt')
    df = pd.read_csv(x, header=None)
    df.to_pickle('triangle.pickle')

def tri_area(A_x, A_y, B_x, B_y, C_x, C_y):
    return .5 * abs(((A_x - C_x)*(B_y - A_y)) - ((A_x - B_x)*(C_y - A_y)))
    #print(area)

def area_calcs(row):
    df = pd.read_pickle('triangle.pickle')
    A_x = df[0][row]
    A_y = df[1][row]
    B_x = df[2][row]
    B_y = df[3][row]
    C_x = df[4][row]
    C_y = df[5][row]
    P_x = 0
    P_y = 0

    calc_one = tri_area(A_x, A_y, B_x, B_y, C_x, C_y)
    calc_two = tri_area(A_x, A_y, B_x, B_y, P_x, P_y)
    calc_three = tri_area(A_x, A_y, P_x, P_y, C_x, C_y)
    calc_four =  tri_area(P_x, P_y, B_x, B_y, C_x, C_y)
    #print(calc_one)
    return calc_one, calc_two + calc_three + calc_four


def is_area_equal(row):
    a, b = area_calcs(row)
    #print(int(a), '  ', int(b))
    if math.isclose(a, b):
        return 1
    else:
        return 0

j = 0
for i in range(1000):
    if is_area_equal(i) is 1:
        j += 1

print('The origin is within the triangle ', j, ' number of times.')
