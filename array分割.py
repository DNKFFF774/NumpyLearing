import numpy as np

A = np.arange(3,15).reshape((3,4))

print(A)
"""
从横向分割
"""
print(np.split(A,4,axis = 1 ))
"""
操作发现这种方法只能进行均等分割，不能进行不等的分割
得用如下的方法
"""
# print(np.array_split(A,3,axis = 1))
# print(np.vsplit(A,3))#可以理解为分割线段沿着竖直方向前进
# print(np.hsplit(A,4))