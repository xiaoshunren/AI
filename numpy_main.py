import numpy as np # 基础值算法
# import matplotlib.pyplot as plt # 数据可视化
# import pandas as pd # 序列高级函数
# import scipy as sc # 科学计算


print('----------test--------------')

# 「np.array」任何可被解释为Numpy数组的逻辑结构

ary = np.array([1,2,3,4,5,6])
print(ary,type(ary))
print(ary.shape) # 维度


print('-----------维度改为2行3列-------------')

ary.shape = (2,3) # 维度改为2行3列
print(ary,ary.shape)
ary.shape = (6,)
print('------------------------')


print('-----------数组运算-------------')
# 数组运算
print(ary)
print(ary *3)
print(ary > 3)
print(ary + ary)
print('------------------------')


# 「np.arange」(起始值(0)终止值,步长(1))
a = np.arange(0, 5, 1)
print(a)

b = np.arange(0, 10, 2)
print(b)
print('------------------------')

b1 = np.arange(1,10)
print(b1)
print('------------------------')

# 「np.zeros」(数组元素个数，dtype='类型')
c = np.zeros(10)
print(c)
print('------------------------')

c1 = np.zeros(10,dtype='int32') #32进制→整数
print(c1,c1.dtype)
print('------------------------')

# np.ones(数组元数个数，dtype='类型')
d = np.ones(10)
print(d)
print('------------------------')

# 维度 2行3列
d1 = np.ones((2,3),dtype='float32') #  float32 → 1.0
print(d1,d1.shape,d1.dtype)
print('------------------------')

# 5个5/1
print(np.ones(5)/5)

# np.zeros_like()
# np.ones_like()
print(np.zeros_like(a))
print(np.ones_like(b))

print('------------------------')
print('------------------------')



print('----------数组的维度 --------------')
# 数组的维度 「np.ndarray.shape」

ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.shape)
print('------------------------')

# 二维数组

ary = np.array(
    [
        [1,2,3,4],
        [5,6,7,8]
    ]
)
print(type(ary),ary,ary.shape)
print('------------------------')


print('----------元素的类型--------------')
# 元素的类型 「np.ndarray.dtype」
ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.shape)

print('------------------------')
# 转换ary元素的类型
b = ary.astype(float)
print(type(b),b,b.dtype)
# 转换ary元素的类型
c = ary.astype(str)
print(type(c),c,c.dtype)
print('------------------------')

print('----------数组元素个数--------------')
# np.ndarray.size
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(ary.shape,ary.size,len(ary))


print('----------数组元素索引（下标)--------------')
# 数组对象[...,页号，行号，列号]
# 下标从0开始，到数组len-1结束

a = np.array([
              [[1,2],[3,4]],
              [[5,6],[7,8]]
            ]) 
print(a,a.shape)
print(a[0])
print(a[0][0])
print(a[0][0][0])

print('------------------------')

# 属性测试
print('------------属性测试------------')

# 一维数组里的8个元素
a = np.arange(1,9)
print(a,a.shape)

# 修改维度
a.shape =(2,4)
print(a,a.shape)
print(a.dtype)

# 修改数据类型
b = a.astype('float32')
print(b,b.dtype)
# size属性
print(b,'size:',b.size,'length:',len(b))
# 索引 下标index操作 三维数组
c = np.arange(1, 19)
c.shape =(3, 2, 3) #3页，2行，3列
print(c)
print('------------------------')
print(c[0]) # 拿到第1页
print('------------------------')
print(c[0][1]) # 拿到第1页第1行
print('------------------------')
print(c[0,1,0]) # 拿到数组中的4  位置在0页1行0列
print('------------------------')
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k]) # i页j行k列
print('------------------------')


print('----------知識ポイント補足--------------')
# argmin() 和 argmax() 两个函数分别对应着求矩阵中最小元素和最大元素的索引。
A = np.arange(2,14).reshape((3,4)) 
# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])
print(np.argmin(A))    # 0
print(np.argmax(A))    # 11
print(np.mean(A))        # 均值
print(np.median(A))       # 中位数
print('---------------------')
A = np.arange(12).reshape((3, 4))
print(A)
#纵向分割
print(np.split(A, 2, axis=1))
#横向分割
print(np.split(A, 3, axis=0))
#不等量分割
print(np.array_split(A, 3, axis=1)) # # 沿轴1将数组分成3个子数组 axis: 指定要分割的轴。默认值为 0。

print('---------数列合并------------')
A = np.array([1,1,1])
B = np.array([2,2,2])
         
print(np.vstack((A,B)))    # vertical stack本身属于一种上下合并，即对括号中的两个整体进行对应操作
D = np.hstack((A,B))       # horizontal stack D本身来源于A，B两个数列的左右合并，而且新生成的D

print(D) 
# [1,1,1,2,2,2]
print('---------------------')

 # 视图变维度(数据共享) reshape() ・ravel()

a = np.arange(1,9) 
print(a) # 数列1-8
print('---------------------')
b=a.reshape(2,4) # 视图变维 →　2行4列二维数组
print(b)
print('---------------------')
c=b.reshape(2,2,2) # 视图变维 →　2页2行2列三维数组
print(c)
print('---------------------')
d=c.ravel() # 视图变维 →　一维数组
print(d)
print('---------------------')

# 复制变维度(数据独立) flatten()
e = c.flatten() # 把三维数组变成一维显示
print(e)
print('---------------------')

# 数组切片操作
# 步长+:默认切 头到尾
# 步长-:默认切 尾到头
# 默认步长 1
# 数组对象[起始位置:终止位置:步长,......]

a = np.arange(1,10)
print(a) # 1 2 3 4 5 6 7 8
print(a[:3]) # 9 8 7 6 5 4 3 2 1
print(a[3:6])#  4 5 6 
print(a[6:]) # 7 8 9
print(a[::-1]) #  9 8 7 6 5 4 3 2 1
print(a[:-4:-1])# 9 8 7
print(a[-4:-7:-1])# 6 5 4
print(a[-7::-1])# 3 2 1
