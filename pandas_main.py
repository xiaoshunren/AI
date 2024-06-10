#Series的字符串表现形式为：索引在左边，值在右边。
import pandas as pd # type: ignore
import numpy as np # type: ignore
s = pd.Series([1,3,6,11,44,1])
print(s)
print('------------------------------------')

#DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）
#DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。
dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
print('------------------------------------')
print(df['b'])
print('------------------------------------')
print(df.dtypes)
print('------------------------------------')
print(df.index)
print('------------------------------------')
print(df.columns)
print('------------------------------------')
print(df.values)
print('------------------------------------')
df.describe()
print('------------------------------------')
print(df.T) #翻转数据
print('------------------------------------')
print(df.sort_index(axis=1, ascending=False)) #按照index排序
print('------------------------------------')
print(df.sort_values(by='a')) #按值排序
print('------------------------------------')
#选择数据
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print(df)
print('------------------------------------')