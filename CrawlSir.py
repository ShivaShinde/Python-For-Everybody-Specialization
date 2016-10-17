# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
list1=[]
for tag in tags:
   # Look at the parts of a tag
   #print 'URL:',tag.get('href', None)
   list1.append(int(tag.contents[0]))
   #print 'Attrs:',tag.attrs
print sum(list1)
