import numpy as np

A = np.arange(4)
print(A)

B = A
C = A.copy()
print(B)

A[0] = 11
print(B)
print(C) #deeep copy
"""
可以看到从C++角度来看，B是A的引用
"""
