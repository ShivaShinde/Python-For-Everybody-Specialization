# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
position = int(raw_input("Enter the position:"))
count = int(raw_input("Please give me a count:"))
list1 = []
k=0
def main(url, position, count):
    k=0
    if count == 0:
        return list1[k-1]
    else:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        k=0
        for tag in tags:
            list1.append(tag.get('href', None))
            k += 1
            if k==position:
                break
        count -= 1              
if __name__ == '__main__':
    main(url, position, count)    
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)
    main(list1[k-1],position, count)