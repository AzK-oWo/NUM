import numpy as np
import time
import matplotlib.pyplot as plt
from random import randint

def cholesky(array, n):
	s = np.zeros((n, n))
	for i in range(1, n + 1):
		_i = i - 1
		s[_i][_i] = array[_i][_i]
		for j in range(1, i):
			_j = j - 1
			s[_i][_i] -= s[_j][_i] ** 2
		s[_i][_i] = s[_i][_i] ** (1 / 2)
		for j in range(i + 1, n + 1):
			_j = j - 1
			s[_i][_j] = array[_i][_j]
			for k in range(1, i):
				_k = k - 1
				s[_i][_j] -= s[_k][_i] * s[_k][_j]
			s[_i][_j] /= s[_i][_i]
	return s

my_time = [0]
_time = [0]
n0 = n = 50
step = 50
start, finish = 0, 0
_start, _finish = 0, 0
while finish - start <= 1:
	f = np.random.uniform(0, 100, (n))
	A = np.tril(np.random.rand(n, n))
	for i in range(n):
		A[i][i] = 100
	start = time.time()
	cholesky(A, n)
	finish = time.time()
	my_time.append(finish - start)
	_start = time.time()
	np.linalg.cholesky(A)
	_finish = time.time()
	_time.append(_finish - _start)
	n += step
x = [y for y in range(n0, n + 1, step)]
plt.plot(x, my_time, label="My time")
plt.plot(x, _time, label="Numpy time")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.5), loc=0, borderaxespad=0.)
plt.show()