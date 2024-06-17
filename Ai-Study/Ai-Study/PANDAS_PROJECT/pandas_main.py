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
print(df['A'])
print('------------------------------------')
print(df.A)
print('------------------------------------')
#选择行
print(df[0:3])
print('------------------------------------')
#使用标签来选择数据 loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']]) 
print(df.loc['20130102',['A','B']])
print('------------------------------------')
#采用位置进行选择 iloc
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
print('------------------------------------')
#判断指令 (Boolean indexing) 进行选择
print(df[df.A>8])
print('------------------------------------')
# 创建数据
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print(df)
print('------------------------------------')
#利用索引或者标签确定需要修改值的位置
df.iloc[2,2] = 1111
df.loc['20130101','B'] = 2222
print(df)
print('------------------------------------')
#根据条件 如果现在的判断条件是这样, 我们想要更改B中的数, 而更改的位置是取决于 A 的. 对于A大于4的位置. 更改B在相应位置上的数为0.
df.B[df.A>4] = 0
print(df)
print('------------------------------------')
#批量处理
df['F'] = np.nan
print(df)
print('------------------------------------')
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print('------------------------------------')
#直接去掉有 NaN 的行或列, 可以使用 dropna
df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop 
    ) 
print('------------------------------------')
#将 NaN 的值用其他值代替, 比如代替成 0
df.fillna(value=0)
print('------------------------------------')
#判断是否有缺失数据 NaN, 为 True 表示缺失数据
df.isnull() 
print('------------------------------------')
