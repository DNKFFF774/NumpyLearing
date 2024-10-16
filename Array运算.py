import numpy as np
a = np.array([3,20,30,40])
b = np.arange(4).reshape((2,2))
a1 = np.array([[1,1],[2,2]])
c = a1*b
c2 = np.dot(a1,b)

#这个才是矩阵相乘的形式
c3 = a1.dot(b)

#也是矩阵乘法的两个不同形式
print(a1)
print(b)
# print(c)
print(c2)

#print(b<3)#可以逐个判断列表中元素的大小

#np.min np.max np.sum字面意思
print(np.sum(a1,axis = 1))#1是对行进行操作，0是对列进行操作

