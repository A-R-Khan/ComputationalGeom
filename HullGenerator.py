import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize
import random

DISTANCE = 4
INRT_FAC = 7
RAND_FAC = 3

def normalize(vec):
	return vec/np.linalg.norm(vec)


def isLeft( P0, P1, P2 ):
    return ( (P1[0] - P0[0]) * (P2[1] - P0[1]) - (P2[0] -  P0[0]) * (P1[1] - P0[1]) )

def wn_PnPoly( P, V):

    wn = 0

    for i in range(-1, len(V)):
        if V[i][1] <= P[1]:
            if V[i+1][1]  > P[1] :
                 if isLeft( V[i], V[i+1], P) > 0 :
                     wn+=1     
        else:               
            if V[i+1][1]  <= P[1] :  
                 if isLeft( V[i], V[i+1], P) < 0 :
                     wn-=1
    return wn

hull = []

def InsertNode(hull, node, expected_pos):
	e = expected_pos
	dist1 = np.linalg.norm(node - hull((e+1)%len(hull)))
	dist2 = np.linalg.norm(node - hull(e))
	dist3 = np.linalg.norm(node - hull(e-1))
	dist4 = np.linalg.norm(node - hull(e-2))

	d1 = dist1 + dist2
	d2 = dist2 + dist3
	d3 = dist3 + dist4

	d_min = min(d1, min(d2, d3))

	if d_min == d1:
		if e+1 == 0:
			hull.append(node)
		else:
			hull.insert(e, node)
	else if d_min == d2:
		if e == 0:
			hull.append(node)
		else:
			hull.insert(e, node)
	else if d_min == d3:
		pass


def GenerateNode(hull):
	hull_node = random.randrange(0, len(hull))
	del hull[hull_node]
	for i in range(2):
		new_node = hull_node + DISTANCE * (INRT_FAC * normalize(hull_node) + RAND_FAC * normalize(np.array([np.random.normal() for i in range(2)])))
		InsertNode(hull, new_node, hull_node)




				


