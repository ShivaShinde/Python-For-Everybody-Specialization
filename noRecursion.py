import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
position = int(raw_input("Enter the position:"))
count = int(raw_input("Please give me a count:"))

def main(link, position, count_):
    for _ in xrange(count_):
        page = urllib.urlopen(link).read()
        soup = BeautifulSoup(page)
        tags = soup.findAll('a')
        link = tags[position-1].get('href', None)
    return link

if __name__ == '__main__':
    print main(url, position, count)
