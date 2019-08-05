#!/usr/bin/env python
# coding: utf-8

# # pandas入门

# ## 1.pandas的数据结构介绍

# ### 1.1 Series

# #### Series 的构建,Series 类似一位数组的对象，它是由一组数据和一组与之相关的数据标签组成

# In[1]:


import pandas as pd
obj = pd.Series([4,7,-5,3])
obj


# In[2]:


obj.values


# In[3]:


obj.index


# In[4]:


obj2 = pd.Series([4,5,7,3],index = ['a','b','c','d'])
obj2


# In[68]:


import pandas as pd
obj = pd.Series([4,7,-5,3])
obj


# In[6]:


obj2.index


# #### Series 的索引

# #### 与普通的numpy数组相比，可以通过索引的方式选择series中的单个或者一组数值

# In[7]:


obj2['a']


# In[8]:


obj2['a'] = 5
obj2['a']


# In[9]:


obj2[['a','b','c']]


# #### Series的运算

# In[10]:


obj2[obj2>5]


# In[11]:


obj2*2


# In[12]:


import numpy as np
np.exp(obj2)


# #### obj可以看作是一个定长的有序字典，因为它是索引导数据值的一个映射

# In[13]:


'b' in obj2


# In[14]:


'e' in obj2


# #### 如果数据被放在一个python的字典中，可以通过这个字典来创建series

# In[15]:


sdata = {'first':1,'second':2,'third':3}
obj3 = pd.Series(sdata)
obj3


# #### 索引可以设定,并且挑选出符合索引的数值（nan表示缺失）

# In[16]:



states = ['hha','second']
obj4 = pd.Series(sdata,index = states)
obj4


# #### 检测缺失数字

# In[17]:


pd.isnull(obj4)


# In[18]:


pd.notnull(obj4)


# In[19]:


obj4.isnull()


# #### Series最重要的一个功能是：他在算数运算中会自动对齐不同索引的数据

# In[20]:


obj3


# In[21]:


obj4


# In[22]:


obj3+obj4


# #### Series对象本身及其都有一个name属性

# In[23]:


obj4.name = 'population'
obj4.index.name = 'state'
obj4


# In[24]:


obj4.index.name


# In[25]:


obj4['hha']


# ### 1.2.DataFrame 

# #### dataframe 是一个表格的数据结构，它含有一组有序的列，每列可以是不同的值类型。 可以被看作是由series组成的字典

# #### dataframe的构建（最常用的是直接传入一个等长列表或者numpy数组组成的字典）

# In[26]:


from pandas import DataFrame
data ={'state':['ohio','ohio','ohio','nevada','nevada'],
       'year':[2000,2001,2002,2001,2002],
       'pop':[1.5,1.7,3.6,2.4,2.9]
      }
frame = DataFrame(data)
frame


# #### 可以指定列序列，并且改变所有的行

# 

# In[27]:


DataFrame(data,columns = ['year','state','pop'])


# #### 和series一样，如果传入的列在数据中找不到，就会产生na数值

# In[28]:


frame2 = DataFrame(data,columns = ['year','state','pop','debt'],index = ['one','two','three','four','five'])
frame2


# In[29]:


frame2.columns


# #### 可将dataframe的列获取为一个series

# In[30]:


frame2['state']


# In[31]:


frame2.year


# #### 通过行数或者标签获得信息

# In[32]:


frame2.ix['three']


# #### 列也可以通过赋值的方式进行修改

# In[33]:


frame2['debt'] = np.arange(5.)
frame2


# In[34]:


val = pd.Series([-1.2,-1.5,-1.7],index = ['two','four','five'])
frame2['debt'] = val
frame2


# #### 为不存在的列赋值会创建一个新列

# In[35]:


frame2['eastern'] = frame2.state =='ohio'
frame2


# In[36]:


del frame2['pop']


# In[37]:


frame2.columns


# #### dataframe 另外一种构建方式（ 嵌套字典）

# In[38]:


pop = {'nevada':{2001:2.4,2002:2.9},
      'ohio':{2000:1.7,2002:3.6}}


# #### 如果将上述传给dataframe 那么就会被解释为：字典的键值作为列，内层键值作为行索引

# In[39]:


frame3 = DataFrame(pop)
frame3 


# 

# #### dataframe的转置

# In[40]:


frame3.T


# #### dataframe可以进行索引的显示指定

# In[41]:


DataFrame(pop,index = [2000,2001,2002,2003])


# In[42]:


frame3['ohio']


# In[43]:


frame3['ohio'][:1]


# #### [:-1]表示除去最后一行的其他所有行

# In[44]:


frame3['ohio'][:-1]


# In[45]:


pdata = {'ohio':frame3['ohio'][:-1],
         'nevada':frame3['nevada'][:2]
        }
DataFrame(pdata)


# #### 可以输入给dataframe构造器的数据

# ![jupyter](./1.png)

# #### 如果设置了dataframe的index和columns的name属性，那么这些信息也会被显示出来

# In[46]:


frame3.index.name = 'year';frame3.columns.name = 'state'
frame3


# ## 2.索引对象

# #### pandas的索引对象负责管理轴标签和其它元数据（比如：轴名称）

# In[47]:


import numpy as np
obj = pd.Series(np.arange(3),index = ['a','b','c'])
index = obj.index
index


# In[48]:


index[1:]


# #### index对象不可以进行修改，这个非常重要，保证了index对象在多个数据结构之间安全共享

# #### index[1]  = 'a'是错误的

# In[49]:


index = pd.Index(np.arange(3))
obj2 = pd.Series([1.5,-2.5,0],index = index)
obj2.index is index


# ![jupyter](./2.png)

# #### Index除了长得像数组，Index的功能也类似一个的固定大小的集合

# In[50]:


frame3


# In[51]:


'ohio' in frame3.columns


# In[52]:


2000 in frame3.index


# ![jupyter](./3.png)

# ## 3.基本功能

# ### 3.1重新索引，创建一个适应新索引的新对象

# In[53]:


obj = pd.Series([4.5,7.2,-5.3,3.6],index = ['a','b','c','d'])
obj


# In[54]:


obj2 = obj.reindex(['a','b','c','d','e'])
obj2


# In[55]:


obj2 = obj.reindex(['a','b','c','d','e'],fill_value = 0)
obj2


# In[56]:


obj3 = pd.Series(['blue','purple','yellow'],index = [0,2,4])
obj3.reindex(range(6),method = 'ffill')


# ![jupyter](./4.png)

# In[57]:


frame = pd.DataFrame (np.arange(9).reshape((3,3)),index = ['a','c','d'],columns = ['ohio','texas','california'])
frame


# In[58]:


frame2 = frame.reindex(['a','b','c','d'])
frame2


# In[59]:


states = ['texas','utah','california']
frame.reindex(columns = states)


# In[60]:


frame.reindex(index = ['a','b','c','d'],columns = states )


# ![jupyter](./5.png)

# ## 4.丢弃指定轴上的项

# In[61]:


obj = pd.Series(np.arange(5.),index = ['a','b','c','d','e'])
obj


# In[62]:


new_obj = obj.drop('c')
new_obj


# In[63]:


obj.drop(['d','c'])


# In[64]:


data = pd.DataFrame(np.arange(16).reshape((4,4)),
                  index = ['ohio','colorado','utah','new work'],
                  columns = ['one','two','three','gour'])
data


# In[65]:


data.drop(['ohio','colorado'])


# In[66]:


data.drop('two',axis = 1)


# In[67]:


data.drop(['two','gour'],axis = 1)


# ## 5.索引、选取和过滤

# In[ ]:





# In[ ]:





# In[ ]:




