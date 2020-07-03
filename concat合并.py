import numpy as np
import pandas as pd

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)

res = pd.concat([df1,df2,df3],axis=0) # vertical concat,但此时索引没有改变为012012012
print(res)
res = pd.concat([df1,df2,df3],axis=1) # horizontal concat
print(res)
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True) # vertical concat,此时索引为0-8、
print(res)

print('--------------------------')

# join,['inner','outer']
# df1 df2的columns与索引都有重合
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
print(df1)
print(df2)

res = pd.concat([df1,df2]) # 这样做的话有些值会被nan填充，此时默认为join='outer'
print(res)
res = pd.concat([df1,df2],join='inner',ignore_index=True) # 'inner' 只会保留两者的交集
print(res)

# reindex_like 根据df1 index的形式join df1与df2
res = pd.concat([df1,df2.reindex_like(df1)],axis=1)
print(res)

print('----------')
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True) # append会增加一行
print(s1)
print('----------')
print(res)

res = df1.append([df2,df3]) # 把df2,df3向下加入到df1
print(res)

