from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib
import csv

r = requests.get('https://www.census.gov/programs-surveys/popest.html')
soup = BeautifulSoup(r.text, 'html.parser')
#for link in soup.find_all('a'):
   # print (link.get('href'))
links = soup.find_all('a')
print(len(links))
# Only the ablsolute links

sg = soup.findAll('a', attrs={'href': re.compile("^http")})
print(sg)

print(len(sg))

with open("aam1taskRev.csv",'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ')
    write.writerows(sg)
    csvfile.close()