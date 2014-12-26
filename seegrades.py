#!/usr/bin/python
#Contact: emanuelvalente@gmail.com

import urllib2
import json, sys


if __name__ == '__main__':
	
	#Data to be send (to get our task)
	ourdict = {'token': "SqRw7EIYkX"}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)

	#Send it (get our haystack and needle)
	response = urllib2.urlopen("http://challenge.code2040.org/api/status", jdata)
	#get the content
	page_content = response.read().decode('utf-8')

	#json -> python dict
	ourdict = json.loads(page_content)
	ourdict = ourdict['result']

	#our grades
	for key in ourdict.keys():
		print("%s : %s" %(key, ourdict[key]))