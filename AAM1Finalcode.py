from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib
import csv

r = requests.get('https://www.census.gov/programs-surveys/popest.html')


# In[15]:


soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.find_all('a'):
   # print (link.get('href'))
links = soup.find_all('a')
print(len(links))


# In[24]:


sg = soup.findAll('a', attrs={'href': re.compile("^http")})
print(sg)


# In[25]:


print(len(sg))

