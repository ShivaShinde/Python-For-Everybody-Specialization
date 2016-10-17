import json
import urllib

getURL = raw_input("Please enter URL")
if len(getURL) < 1: 
    print "Invalid URL sir"
print "Retrieving given URL:", getURL
pleaseCheck = urllib.urlopen(getURL)
#reads all the data, now we can print that data if we want to
pleaseRead = pleaseCheck.read()
#load as string, loads will load all the data as string into the info
info = json.loads(pleaseRead)
#empty list and a count variable to track the number of student counts
list1 = []
count1 = 0
#dictionary in list, again a dictionary in list, so FOR-LOOP in dictionary of FOR-LOOP in a list :)
for element in info:
    for item in info['comments']:
        list1.append(item["count"])
        count1 += 1
    break
#this is jus type conversion of list1
list2 = map(int, list1)
print "This is the sum professor:", sum(list2)
print "this is count:", count1