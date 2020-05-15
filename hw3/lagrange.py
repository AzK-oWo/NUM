import numpy as np

def phi(i, z, x):
	n = len(x)
	p = 1
	for j in range(n):
		tmp = x[j]
		if x[i] != tmp:
			p *= (z - tmp) / (x[i] - tmp)
	return p

def lagrangeInterpolation(x, y, z):
	n = len(x)
	m = len(z)
	ans = [0] * m
	for i in range(m):
		for j in range(n):
			ans += y[i] * phi(i, z, x)
	return 

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
ans = lagrangeInterpolation(x, y, z)
write_file("hw3/lagrange.ans", ans)