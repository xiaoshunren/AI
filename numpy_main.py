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