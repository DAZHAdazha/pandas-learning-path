import numpy as np
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)
res = pd.merge(left,right,on='key') # on为选择在哪一个columns合并,合并和只有一个key
print(res)

# merging two df by key/keys.(may be used in database)
# conside two keys

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print('-----------------')
print(left)
print(right)
res = pd.merge(left,right,on=['key1','key2']) # 默认为inner
print(res)

# how = ['left', 'right', 'outer', 'inner']
res = pd.merge(left,right,on=['key1','key2'],how='outer') # outer,没有的数据用nan
print(res)

res = pd.merge(left,right,on=['key1','key2'],how='left') # left,基于left
print(res)

res = pd.merge(left,right,on=['key1','key2'],how='right') # right,基于right
print(res)

print('-------------------------')

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
# indicator='xxx'可以自定义该栏的名字
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True) # 会给出merge的细节
print(res)
print('----------------')

# merge by index ('k0,k1,k2')
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)
print(right)
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
print('----------------')

# overlapping 同样是k0的age两个数据集有重叠
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)

# 使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)

# merge的许多用法也可以用join实现
