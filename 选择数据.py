import numpy as np
import pandas as pd

dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
print(df)

# 两种方法选择columns
print(df['a'])
print(df.a)

# 两种方法选择index
print(df[0:3])
print(df['20200102':'20200104'])

# select by label: loc，标签筛选
print(df.loc['20200102']) # 选择index 20200102
print(df.loc[:,['a','b']]) # 选择 columns a,b

# select by position: iloc， 数字筛选
print(df.iloc[[1,3,5],1:3]) # 1,3,5行1到3的元素

# Boolean indexing
print(df[df.a < 9]) # a小于9的值,但是同行里面其他列如b,c,d的值就算不小于9也会打印



