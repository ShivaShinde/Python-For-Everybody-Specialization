import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//comment')
    print len(counts)
    #numbers = tree.findall('.//count')
    jain = []
    for item in counts:
        jain.append(item.find('count').text)
    #print counts
    print jain
    jain1 = map(int, jain)
    print sum(jain1)
   