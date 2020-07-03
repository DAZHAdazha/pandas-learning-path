import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum() # 累加
# data.plot()
# plt.show()

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
        index=np.arange(1000),
        columns=list('abcd'))
data = data.cumsum()
print(data.head(3)) # 打印出前3个数据,默认前5个

# plt methods:
# 'bar','hist','box','kde','area','scatter','hexbin','pie'

# data.plot() # 4组数据，4根折线
# plt.show()

ax = data.plot.scatter(x='a',y='b',color='DarkBlue',label='Class 1')
data.plot.scatter(x='a',y='c',color='DarkGreen',label='Class 2',ax=ax) # 把两组数据打印到一起
plt.show()


