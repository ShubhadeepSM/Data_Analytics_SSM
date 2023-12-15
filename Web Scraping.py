#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[5]:


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage_resp = requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text


# In[6]:


soup = BeautifulSoup(webpage_resp, 'lxml')


# In[11]:


soup.find_all('h1')[0].text.strip()


# In[13]:


for i in soup.find_all('h2'):
    print(i.text.strip())


# In[14]:


len(soup.find_all('h2'))


# In[19]:


len(soup.find_all('div', class_= 'companyCardWrapper__companyRatingWrapper'))


# In[20]:


company = soup.find_all('div', class_='companyCardWrapper')


# In[21]:


len(company)


# In[58]:


name = []
rating = []
reviews = []
company_desc = []

for i in company:
    name.append((i.find('h2').text.strip()))
    rating.append(i.find('div', class_= 'companyCardWrapper__companyRatingWrapper').text.strip())
    reviews.append(i.find('span', class_= 'companyCardWrapper__ActionCount').text.strip())
    company_desc.append(i.find('div', class_= 'companyCardWrapper__interLinkingWrapper').text.strip())
    
df = {'Name':name, 'Rating':rating, 'No. of Reviews':reviews, 'Description':company_desc}
final_df = pd.DataFrame(df)


# In[59]:


final_df


# In[43]:


rating


# In[47]:


reviews


# In[60]:


final_df.shape


# In[68]:


total_final_df = pd.DataFrame()

for j in range(1,200):
    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage_resp = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage_resp, 'lxml')
    company = soup.find_all('div', class_='companyCardWrapper')
    name = []
    rating = []
    reviews = []
    company_desc = []

    for i in company:
        name.append((i.find('h2').text.strip()))
        rating.append(i.find('div', class_= 'companyCardWrapper__companyRatingWrapper').text.strip())
        reviews.append(i.find('span', class_= 'companyCardWrapper__ActionCount').text.strip())
        company_desc.append(i.find('div', class_= 'companyCardWrapper__interLinkingWrapper').text.strip())
    
    df = {'Name':name, 'Rating':rating, 'No. of Reviews':reviews, 'Description':company_desc}
    final_df = pd.DataFrame(df)

    total_final_df = pd.concat([total_final_df, final_df], ignore_index = True)


# In[70]:


total_final_df


# In[ ]:




