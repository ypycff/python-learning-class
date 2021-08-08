# NumPy is a library of numeric functions (matrices and other high-level maths).
# For an intro, see https://en.wikipedia.org/wiki/NumPy.

# Import the NumPy module. 
import numpy as np

# Create an ndarray (i.e. a NumPy data array) explicitly.
x = np.array([1, 2, 3])
print('\nx:\n%s' % x)

# Create an ndarray from a range (0..9 here).
y = np.arange(10)  
print('\ny:\n%s' % y)

# Create a 3x3 matrix.
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('\nOriginal a:\n%s' % a)
a = a.transpose()
print('\nTransposed a:\n%s' % a)

# Create another 3x3 matrix.
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print('\nb:\n%s' % b)
result = np.multiply(a,b)
print('\na multiplied by b:\n%s' % result)

# Create a 3x1 vector.
c =  np.array([1, 10, 100])
print('\nc:\n%s' % c)
result = np.dot(a, c)
print('\na multiplied by c:\n%s' % result)