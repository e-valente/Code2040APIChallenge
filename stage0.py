#!/usr/bin/python
#Contact: emanuelvalente@gmail.com

import urllib2
import json

#Data to be send
ourdict = {'email': "emanuelvalente@gmail.com", \
	'github': "https://github.com/lbull/Code2040APIChallenge"}

#convert our data in JSON format
jdata = json.dumps(ourdict)

#Send it
response = urllib2.urlopen("http://challenge.code2040.org/api/register", jdata)

#get the content
page_content = response.read()

#print it (our token)
print(page_content)