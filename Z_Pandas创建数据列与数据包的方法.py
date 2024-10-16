import pandas as pd
import numpy as np
s = pd.Series([1,2,5,np.nan,44,1])
print(s)
#
dates = pd.date_range('20240101',periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
"""
还可以指定列名使用字典的方式生成
"""
"""
奶奶的我已经被这pandas的数据整合功能给震惊到了
"""