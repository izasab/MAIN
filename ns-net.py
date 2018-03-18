from numpy import exp, array, random, dot




def sig(x):
	return 1 / (1 + exp(-x))

def sig_der(x):
	return x * (1 - x)



inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
outputs = array([[0, 1, 1, 0]]).T


random.seed(1)

weights = 2 * random.random((3, 1)) - 1


for i in xrange(100):
	
	out = sig(dot(inputs, weights))

	error = outputs - out

	adj = error * sig_der(out)



	weights += dot(inputs.T, adj)


	print weights
	print


print sig((dot(array([1, 0, 0]), weights)))





