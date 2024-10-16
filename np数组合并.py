import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
V = np.vstack((A,B))
print(V.shape) #verical stack,将两个矩阵进行竖直方向上的合并
H = np.hstack((A,B))
print(H.shape)

"""
如何将一个横向的数列转换为竖向的数列，即本来是一行的怎么转换成一列，
例子告诉我们T转置显然是不行的

需要一个加维数的操作
"""
print(A)#此时还是一维的数组
print(A[np.newaxis,:])#在列上加维度
print(A[:,np.newaxis])#在行上加维度
"""
多个数组横向或纵向的合并
"""
print(np.concatenate((A,B,B,A),axis = 1))
