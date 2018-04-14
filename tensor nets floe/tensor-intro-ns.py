

import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)


result = tf.multiply(x1, x2)



with tf.Session() as sess:
	output = sess.run(result)
	print(output)

print(output)



























#from __future__ import absolute_import, division, print_function

#import os
#import matplotlib.pyplot as plt

#import tensorflow as tf

## Initialize two constants
#x1 = tf.constant([1,2,3,4])
#x2 = tf.constant([5,6,7,8])

## Multiply
#result = tf.multiply(x1, x2)

## Print the result
#print("\n lewl \n")

## Intialize the Session
#sess = tf.Session()

## Print the result
#print(sess.run(result))


#print("\n lewl \n")

## Close the session
#sess.close()
