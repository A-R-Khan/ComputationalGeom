import numpy as np
import random
from scipy.linalg import null_space

def normalize(vector):
	return vector/np.linalg.norm(vector)

def CostFunction(plane, point):
	pass

class Plane:

	def __init__(self, dim, points = None):
		self.dim = dim
		self.directions = normalize(np.random.random_sample(dim))
		self.constant = np.random.random()*3 + 2

		self.points = self.GeneratePoints() if points is None else points

		self.plane_vectors = self.GeneratePlaneVectors()

	def GeneratePoints(self):
		temp_pts = np.array([np.array([np.random.random() for _ in range(self.dim - 1)] + [0,]) for _2 in range(self.dim)])

		for point in temp_pts:
			point[self.dim - 1] = (self.constant - np.dot(point, self.directions)) / self.directions[self.dim - 1]

		return temp_pts

	def GeneratePlaneVectors(self):
		return np.array([normalize(self.points[i] - self.points[0]) for i in range(1, self.dim)])


class Point:
	def __init__(self, dim):
		self.dim = dim
		self.point = np.array([np.random.random()*random.choice([-1, 1]) for _ in range(3)]) 

def GenerateRandomNormal(dim):
	return normalize(np.array([np.random.normal() for i in range(dim)]))

P = Plane(100)

centroid = np.sum(P.points, axis = 0)/P.dim
print np.dot(P.directions, centroid)
print P.constant

