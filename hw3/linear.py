import numpy as np

def makeLines(x, y):
	n = len(x) - 1
	coef = np.zeros(n)
	for i in range(n):
		coef[i] = (y[i + 1] - y[i]) / (x[i + 1] / x[i])
	return coef

def linearInterpolation(x, y ,z):
	n = len(x) - 1
	m = len(z)
	ans = np.zeros(n)
	coef = makeLines(x, y)
	for i in range(m):
		for j in range(n):
			if x[j] <= z[i]:
				ans[i] = coef[j] * (z[i] - x[j]) + y[j]
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

x, y, z = [], [], []
read_file("hw3/train.dat", x)
read_file("hw3/train.ans", y)
read_file("hw3/test.dat", z)
ans = linearInterpolation(x, y, z)
write_file("hw3/linear.ans", ans)