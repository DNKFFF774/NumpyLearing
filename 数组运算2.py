import numpy as np
A = np.arange(2,14).reshape((3,4))
# B = np.arange(2,26).reshape((2,3,4))

print(A)
print(np.clip(A,5,9))#进行一定范围内的取舍，可以舍去无用的数值
 # print(np.cumsum(B))

#注意numpy中的数组和一般的存储形式之间的差别，注意其中的各个元素其实是由空格分割而成的

#通过实例操作可以发现：一般的操作仅可以对二维数组进行相关额计算
#可以熟悉一下对数组做的所有运算，并且可以配上 axis = 0 来对列分别进行操作， axis = 1 即为对行进行操作
# print(np.ndim(A))
