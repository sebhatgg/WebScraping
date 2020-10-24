<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib
import csv

r = requests.get('https://www.census.gov/programs-surveys/popest.html')
<<<<<<< HEAD
=======
>>>>>>> df8f9a877bee4ddaf8e4389054b57f0c904484b1
soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.find_all('a'):
   # print (link.get('href'))
links = soup.find_all('a')
print(len(links))
<<<<<<< HEAD
# Only the ablsolute links
=======


# In[24]:

>>>>>>> df8f9a877bee4ddaf8e4389054b57f0c904484b1

sg = soup.findAll('a', attrs={'href': re.compile("^http")})
print(sg)

<<<<<<< HEAD
print(len(sg))

with open("aam1taskRev.csv",'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ')
    write.writerows(sg)
    csvfile.close()
=======

=======
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib
import csv

r = requests.get('https://www.census.gov/programs-surveys/popest.html')
<<<<<<< HEAD
=======

>>>>>>> df8f9a877bee4ddaf8e4389054b57f0c904484b1
soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.find_all('a'):
   # print (link.get('href'))
links = soup.find_all('a')
print(len(links))
<<<<<<< HEAD
# Only the ablsolute links
=======


# In[24]:

>>>>>>> df8f9a877bee4ddaf8e4389054b57f0c904484b1

sg = soup.findAll('a', attrs={'href': re.compile("^http")})
print(sg)

<<<<<<< HEAD
print(len(sg))

with open("aam1taskRev.csv",'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ')
    write.writerows(sg)
    csvfile.close()
=======

>>>>>>> df8f9a877bee4ddaf8e4389054b57f0c904484b1
>>>>>>> 20a01bf147f0cdd45f9229204b617d49c7b4c2c6
