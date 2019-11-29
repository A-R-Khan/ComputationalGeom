import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize
import random


def normalize(vec):
	return vec/np.linalg.norm(vec)

def random_factor(n):
	return (10 - (9./num_tries)*(n))

def inertia_factor(n):
	pass

def goal_factor(n):
	return (7./num_tries)*(n)

num_tries = 60
dist = 2

vec1 = dist*normalize(np.array([-5, 0]))

start = np.array([-15, -15])
goal = np.array([10, 10])

for i in range(1):
	vecs = []
	vecs.append(start)
	vecs.append(normalize(goal-start))
	tip = vecs[-2] + vecs[-1]

	for tries in range(num_tries):
		vec2 = dist*normalize(4*normalize(vecs[-1]-vecs[-2]) + goal_factor(tries)*normalize(goal-tip) + random_factor(tries)*normalize(np.random.random_sample(2) - np.array([0.5, 0.5])))
		tip = tip+vec2

		if -2 < tip[0] - start[0] < 2 and -2 < tip[1] - start[1] < 2:
			tip = tip-vec2
			continue
		else:
			vecs.append(vec2)


	tip = start
	for vec in range(1, len(vecs)):
		plt.quiver(tip[0], tip[1], vecs[vec][0], vecs[vec][1], angles='xy', scale_units='xy', scale=1, headlength = 0, headwidth = 0)
		tip = tip + vecs[vec]

plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.show()