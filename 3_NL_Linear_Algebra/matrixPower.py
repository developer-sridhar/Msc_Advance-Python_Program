import numpy as np
from numpy.linalg import matrix_power

a = np.array([2, 6])
b = np.array([3, 10])

print("Vector:")
print("a =", a) 

print("Vector:")
print("b =", b) 

print("\nInner product of vector a and b =")
print(np.inner(a, b))  

print("\nOuter product of vector a and b =\n")
outer_product = np.outer(a, b) 
print(outer_product)

print("\nMatrix Exponentiation")

i = np.array([[0, 1], [-1, 0]]) 
print(matrix_power(i, 3)) 


#OUTPUT
# Vector:
# a = [2 6]
# Vector:
# b = [ 3 10]

# Inner product of vector a and b =
# 66

# Outer product of vector a and b =

# [[ 6 20]
#  [18 60]]

# Matrix Exponentiation
# [[ 0 -1]
#  [ 1  0]]