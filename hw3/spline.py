import numpy as np

def sweep(a, b, c, f):
	n = len(f)
	alpha = np.zeros(n + 1)
	beta = np.zeros(n + 1)
	for i in range(n):
		tmpArg = a[i] * alpha[i] + b[i]
		alpha[i + 1] = - c[i] / tmpArg
		beta[i + 1] = (f[i] - a[i] * beta[i]) / tmpArg
	x = np.zeros(n + 1)
	for i in range(n, 0, -1):
		x[i - 1] = alpha[i] * x[i] + beta[i]
	return x

def generateSpline(x, y):
	n = x.shape[0] - 1
	h = (x[n] - x[0]) / n
	a = np.array([0] + [1] * (n - 1) + [0])
	b = np.array([1] + [4] * (n - 1) + [1])
	c = np.array([0] + [1] * (n - 1) + [0])
	f = np.zeros(n + 1)
	for i in range(1, n):
		f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
	s = sweep(n + 1, a, b, c, f)
	for i in range(0, n):
		B[i] = s[i]
		A[i] = (B[i + 1] - B[i]) / (3 * h)
		C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
		D[i] = y[i]
	return A, B, C, D

def splineInterpolation(x, y, z):
	m = len(z)
	n = len(x) - 1
	ans = [0] * m
	A, B, C, D =  generateSpline(x, y)
	for i in range(m):
		for j in range(n):
			if x[j] <= z[i]:
				ans[i] = A[j] * (z[i] - x[j]) ** 3 + B[j] * (z[i] - x[j]) ** 2 + C[j] *(z[i] - x[j]) + D[j]
	return ans

def read_file(name, vec):
	file = open(name, 'r')
	for line in file:
		vec.append(float(line))    
	file.close()

def write_file(name, vec):
	m = len(vec)
	file = open(name, 'w')
	for i in range(m):
		file.write(str(v[i]))
		file.write(' ')
	file.close()

x, y, z = [], [], []
read_file("hw3/train.dat", x)
read_file("hw3/train.ans", y)
read_file("hw3/test.dat", z)
ans = splineInterpolation(x, y, z)
write_file("hw3/spline.ans", ans)
