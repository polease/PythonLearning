
# <codecell>

# In[3]:

from bs4 import BeautifulSoup


# In[4]:

import requests


# In[5]:

response = requests.get("https://en.wikipedia.org/wiki/Battle_of_Winterthur")


# In[6]:

len(response.text)


# In[7]:


soup = BeautifulSoup(response.text,'html.parser')


# In[8]:

soup.title


# In[9]:

soup.p


# In[10]:

soup.p.a


# In[ ]:

soup.p.find_all("a")


#%%
soup.find(id="mw-content-text").p.a.get("href")

# <codecell>


hello

# <markdowncell>

