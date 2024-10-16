import pandas as pd
import numpy as np

dates = pd.date_range('20240101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['aa','b','c','d'])
# print(df)
"""
按照行进行索引
select by index
"""
# print(df[0:2],'\n',df['20240105':'20240106'])
# print(df.loc['20240101'])#在对行名进行索引时，前面要加一个loc，和行名检索略有不同


"""
按照 列 进行索引
select by column
"""
# print(df['a'])
#  或者
# print(df.a)
""""
整体进行方形的检索
"""
# print(df.loc['20240103',:])
"""
select by position
"""
print(df.iloc[[1,3,5],2:4])

"""
mixed selection
ix索引在新版本取消
"""

"""
boolean indexing条件筛选
显然只能对列索引进行操作
只能对column进行筛选
"""
# print(df[df['aa']>8])
# print(df[df.loc['20240101']>8])错误