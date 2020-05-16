import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
import scipy.linalg as sl

const = 10

def get_array(n):
	array = []
	a = np.random.randint(0, 10, size=(n))
	c = np.random.randint(0, 10, size=(n))
	f = np.random.randint(0, 10, size=(n))
	b = np.zeros((n))
	b = a + c + const
	a[0] = 0
	c[n - 1] = 0
	array = np.zeros((3,n))
	array[2, 0:-1] = a[1: ]
	array[1] = b
	array[0, 1: ] = c[ :-1]
	array = np.array(array)
	return a, b, c, f, array


def tridiagonal_ma(a, b, c, f, n):
	alpha = np.zeros(n + 1)
	beta = np.zeros(n + 1)
	for i in range(n):
		tmp_arg = a[i] * alpha[i] + b[i]
		alpha[i + 1] = -c[i] / tmp_arg
		beta[i + 1] = (f[i] - a[i] * beta[i]) / tmp_arg
	x = np.zeros(n + 1)
	for i in range(n, 0, -1):
		x[i - 1] = alpha[i] * x[i] + beta[i]
	return x

my_time = [0]
_time = [0]
n0 = n = 10000
step = 10000
start, finish = 0, 0
_start, _finish = 0, 0
while finish - start <= 1:
	a, b, c, f, A = get_array(n)
	start = time.time()
	tridiagonal_ma(a, b, c, f, n)
	finish = time.time()
	my_time.append(finish - start)
	_start = time.time()	
	sl.solve_banded((1, 1), A, f)
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
fig.savefig('hw1/sweep.png')
