from numpy import exp, array, random, dot




def sig(x):
	return 1 / (1 + exp(-x))

def sig_der(x):
	return x * (1 - x)



inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])

outputs = array([[0, 1, 1, 0]]).T


random.seed(1)

weights = 2 * random.random((3, 1)) - 1

print inputs

for i in xrange(15):
	print i
	
	out = sig(dot(inputs, weights))
	print 'out: \n', out


	error = outputs - out
	print 'error: \n', error


	adj = error * sig_der(out)
	print 'adj: \n', adj


	weights += dot(inputs.T, adj)


	print '\n', weights
	
	

print '\n \n'
print sig((dot(array([1, 1, 0]), weights)))
print 
print sig((dot(array([0, 1, 1]), weights))) , '\n'


