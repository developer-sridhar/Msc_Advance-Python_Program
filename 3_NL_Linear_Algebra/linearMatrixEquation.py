import numpy as np
arr1=np.array([[1,2],[3,5]])
arr2=np.array([1,2])
print("Result…",np.linalg.solve(arr1,arr2))

#OUTPUT
# Result… [-1.  1.]