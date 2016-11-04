#coding:utf-8
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101',periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(['bei','jing','chang','ping']),
                    'F':'foo'
                    })
df2 = df.copy()
df2['E'] = ['one','one','two','three','four','']
s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
df['F'] = s1
df.at[dates[0],'A'] = 0
df.iat[0,0] = 1
df.loc[:,'D'] = np.array([5]*len(df))

df2 = df.copy()
df2[df2>0] = -df2

df1 = df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E'] = 1

df1.dropna(how='any')
df1.fillna(value=5)
pd.isnull(df1)


s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
#df.sub(s,axis='index')
#df.apply(np.cumsum)
a = df.apply(lambda x:x.max()-x.min())

s = pd.Series(np.random.randint(0,7,size=10))

s = pd.Series(['A','B','C','Amaba',np.nan,'CABA','cat'])

df = pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3],df[3:7],df[7:]]
b = pd.concat(pieces)

left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right  = pd.DataFrame({'key':['foo','bar'],'rval':[4,5]})
c = pd.merge(left,right,on='key')

df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
s = df.iloc[3]


ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts = ts.cumsum()
ts.plot()
print('end-of-file')