import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojsonjson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    #adding parameters to the URL of an API, which contains the JSON data 
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    #Opening and reading the contents in the given URL
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: 
        #"loads" load as string which loads the data into js in a string format!
        js = json.loads(str(data)) 
        print js
    except: 
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        #print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    #Trying to extract an attribute from a Dictionary in a list in a Dictionary :)
    location = js['results'][0]['place_id']
    print location
