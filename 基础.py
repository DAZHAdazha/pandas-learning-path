import numpy as np
import pandas as pd

# numpy 更类似于 array形式 而pandas更像字典

s= pd.Series([1,3,6,np.nan,44,1]) # np.nan = None
print(s)

# 时间
dates = pd.date_range('20200101',periods=6)
print(dates)

# np.random.randn(6,4) 随机生成6行4列的数据,每一行的值为dates的元素,每一列为columns里的元素
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

# 若不给index columns的默认形式
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

# 另一种使用dataframe形式, A,B,C各为一列，后面的值为每列数据
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
print(df2)
print(df2.dtypes) # 打印出每列的数据
print(df2.index) # 打印出序列index的值
print(df2.columns) #打印出columns的值
print(df2.values) # 打印出每一个value
print(df2.describe()) # 会打印出count,mean,min,max等值,但只会计算是数字的列,其他格式的列会忽略
print(df2.T)
print(df2.sort_index(axis=1,ascending=False)) # axis=1对columns排序axis=0对index排序,False=逆序
print(df2.sort_values(by='E')) # 根据column'E'的值来排序

