import numpy as np
import pandas as pd

dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])

# 选择后更改即可
df.iloc[2,2] = 1111
df.loc['20200101','b'] = 2222
df[df.a > 4] = 0 # 这样的话会对a>4的整行都设为0，包括b,c,d列
print(df)

df.b[df.a == 0] = -1 # 这样则只会改变b这一列
print(df)

# 加上新的一列
df['f'] = np.nan # 设为NAN
df['e'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20200101',periods=6)) # 新增一列并赋值
print(df)






