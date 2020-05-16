import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.linalg as sl
import time

def inverse(A, f):
	n = len(f)
	x = [0] * n
	for _i in range(n, 0, -1):
		i = _i - 1
		x[i] = f[i]
		for j in range(i, n):
			x[i] -= A[i][j] * x[j]
	return x

def gauss(A, f):
	n = len(f)
	for k in range(n):
		tmp1 = A[k][k]
		for j in range(k + 1, n):
			A[k][j] /= tmp1
		f[k] /= tmp1
		A[k][k] = 1
		for i in range(k + 1, n):
			tmp2 = A[i][k]
			for j in range(k + 1, n):
				A[i][j] -= tmp2 * A[k][j]
			f[i] -= tmp2 * f[k]
			A[i][k] = 0
	return inverse(A, f)

my_time = [0]
_time = [0]
n0 = n = 10
step = 10
start, finish = 0, 0
_start, _finish = 0, 0
while finish - start <= 1:
	A = np.random.rand(n, n)
	f = np.random.rand(n)
	start = time.time()
	gauss(A, f)
	finish = time.time()
	my_time.append(finish - start)
	_start = time.time()
	np.linalg.solve(A, f)
	_finish = time.time()
	_time.append(_finish - _start)
	n += step
x = [y for y in range(n0, n + 1, step)]
fig = plt.figure()
plt.plot(x, my_time, label="My time")
plt.plot(x, _time, label="Numpy time")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend(bbox_to_anchor=(0.5, 0.5, 0.5, 0.5), loc='upper center')
plt.show()
fig.savefig('hw1/gauss.png')