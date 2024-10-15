"""
numpy简介：
主要是用于数组计算，包含
1.强大的N维数组对象ndarray
广播功能函数
整合基础语言代码的工具
线性代数，傅里叶变换，随机数生成（有什么特殊吗？）

另外安装的包：Scipy ， Matplotlib
"""

"""
ndarray特点: 存放同类型元素
初始化：numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度


np.zeros(x,y)生成x行y列的0矩阵，np.ones(x,y)同理
"""
import numpy as np
array = np.array([[1,2,3],[4,5,127],[7,8,9]],dtype = np.int16 )
array0 = np.ones((3,4),dtype = int)
# print(array)
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)
# print(array0)
a = np.arange(10,20,2)#numpy语法生成数列
a1 = np.arange(12).reshape((3,4))#一以数组形式生成数列
a2 = np.linspace(1,10,6).reshape((2,3))#将1~10平均分割成成x-1段生成列表，也可以reshape
print(a1)
print(a2)#