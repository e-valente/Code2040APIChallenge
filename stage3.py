#!/usr/bin/python
#Contact: emanuelvalente@gmail.com

import urllib2
import json, sys

#returns index where needle was found
#O(n)
def searchNeedle(needle, haystacklist):

	for i in range(len(ourlist)):
		if ourlist[i] == ourneedle:
			return i

	return -1 #if we dont find it

if __name__ == '__main__':

	#Data to be send (to get our task)
	ourdict = {'token': "SqRw7EIYkX"}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)

	#Send it (get our haystack and needle)
	response = urllib2.urlopen("http://challenge.code2040.org/api/prefix", jdata)
	#get the content
	page_content = response.read().decode('utf-8')

	#json -> python dict
	ourdict = json.loads(page_content)
	ourdict = ourdict['result']

	#setting our target
	words = ourdict['array']
	prefix = ourdict['prefix']

	#our array that does not contain
	#the the prefix in the beggining
	#of each word
	answer = []
	for word in words:
		if word.startswith(prefix) is False:
			answer.append(word)
			#print(word)


	#We will send our answer to the endpoint
	ourdict = {'token': "SqRw7EIYkX", 'array': answer}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)
	#Send it
	response = urllib2.urlopen("http://challenge.code2040.org/api/validateprefix", jdata)
	#get the content
	page_content = response.read()
	#print it (response)
	print(page_content)
