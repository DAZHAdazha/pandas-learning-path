import numpy as np
import pandas as pd

dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

print(df.dropna(axis=0,how='any')) # 丢掉有nan的行 how默认为any,也可以为'all'
print(df.dropna(axis=1)) # 丢掉有nan的列

print(df.fillna(value=0)) # 将所有为nan的填充为0

print(df.isnull()) # 检测是否有数据缺失(为nan)
print(np.any(df.isnull())==True) # 若表太大可以用这种方法检测是否有数据缺失(为nan)



