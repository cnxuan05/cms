# -*- coding:utf-8 -*-
# matplotlib 使用方法
'''
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("x value")
plt.ylabel("y value")
plt.title("a simple example")
plt.legend
plt.show()
'''

import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

ts = pd.Series(random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
