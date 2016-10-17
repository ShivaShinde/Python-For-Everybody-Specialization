from __future__ import print_function
import requests
import urllib2, urllib
from BeautifulSoup import BeautifulSoup

wordlist = open('test.txt', 'a')

word = raw_input('Paste your word ')

url = 'http://services.aonaware.com/DictService/Default.aspx?action=define&dict=wn&query=%s' % word

# print url

html = urllib.urlopen(url).read()
# print html
soup = BeautifulSoup(html)
visible_text = soup.find('pre')(text=True)

print(visible_text, file=wordlist)