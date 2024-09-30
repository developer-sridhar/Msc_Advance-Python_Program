import numpy as np
a=np.array([[3,1],[2,2]])
w=np.linalg.eig(a)
print(w)

#OUTUT ?
# EigResult(eigenvalues=array([4., 1.]), eigenvectors=array([[ 0.70710678, -0.4472136 ],
#        [ 0.70710678,  0.89442719]]))

#Array([3.73205081,0.26794919]