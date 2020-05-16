import scipy.linalg as sl
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
from math import sqrt

def seidel(A, f, n):
	eps = 0.000000001
	xnew = np.zeros(n)
	diff = 1
	while diff > eps:
		x = np.copy(xnew)
		xnew = np.zeros(n)
		for i in range(n):
			s = 0
			S = A[i]
			s = np.dot(S[ :i], xnew[ :i])
			s += np.dot(S[i + 1: ], x[i + 1: ])
			xnew[i] = (f[i] - s) / S[i]
		delta_x = xnew - x
		diff = sqrt(np.dot(delta_x, delta_x))
	return x

myTime, npTime = [0], [0]
n0 = n = 100
step = 100
finish, start = 0, 0
fn, st = 0, 0
while finish - start < 1:
	A = np.random.randint(0, 10, size=(n,n))
	f = np.random.randint(0, 10, size=(n))
	s = np.sum(np.abs(A), axis = 1)
	for i in range(n):
		A[i][i] = A[i][i] + s[i]
	start = time.time()
	seidel(A, f, n)
	finish = time.time()
	myTime.append(finish - start)
	st = time.time()
	sl.solve(A, f)
	fn = time.time()
	npTime.append(fn - st)
	n += step

x = [y for y in range(n0, n + 1, step)]
fig = plt.figure()
plt.plot(x, myTime, label="My time")
plt.plot(x, npTime, label="Numpy time")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend(bbox_to_anchor=(0.5, 0.5, 0.5, 0.5), loc='upper center')
plt.show()
fig.savefig('hw2/seidel.png')