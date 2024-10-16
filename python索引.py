import numpy as np

A = np.arange(3,15).reshape((3,4))
B = np.arange(3,15)
"""
如下是类似于多维列表的索引方式
"""
print(B[3])
print(A[2,1])#h还是略有不同的
"""
 可以用冒号来代替一行或者一列的所有数字,也可用冒号来表示行到行，列到列
"""
print(A)
# print(A[1,1:4])
"""
可以用for循环来检索说有的行和列。注意对列进行索引操作时得先将矩阵进行转置
"""
for row in A:
    print(row)
for column in A.T:#想要遍历列，可以先转置
    print(column)

"""
如果要进行所有元素的索引，必须先对矩阵转化成类似列表的形式
"""
print(A.flatten())
for item in A.flat:
    print(item,end=' ')
