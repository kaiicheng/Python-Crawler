#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

request_url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E5%8D%A1%E6%A8%82%E6%AF%94&page=1&sort=sale/dc"
query_str_params = {
    'q': '卡樂比',
    'page': '1',
    'sort': 'sale/dc'
}

response = requests.get(request_url, params = query_str_params)


# In[2]:


# 常用屬性
response.status_code
# 200 合法且正常請求
# 404 錯誤的請求
# 403 正確辦不合法的請求(如：不認識你)


# In[3]:


# 顯示回信中的內容 (如：拆信、讀出來)
response.text


# In[4]:


# 顯示回信中的內容 (如：拆信、讀出來) (但和twxt不同，類似用中文、英文念)
response.content


# In[5]:


response.json


# In[6]:


response.json()


# In[7]:


# This code is equal to response.json().
import json
json.loads(response.text)


# In[8]:


calbee= response.json()
type(calbee)


# In[13]:


calbee


# In[15]:


calbee['prods']


# In[17]:


print(calbee['prods'])


# In[27]:


calbee['QTime']


# In[10]:


type(calbee['prods'])


# In[11]:


# The data of the first product.
calbee['prods'][0]


# In[12]:


# The data of the second product.
calbee['prods'][1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




