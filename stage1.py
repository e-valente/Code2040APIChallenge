#!/usr/bin/python
#Contact: emanuelvalente@gmail.com

import urllib2
import json

def reverseString1(mystr):
	return mystr[::-1]

def reverseString2(mystr):
	return "".join((mystr[i-1] for i in xrange(len(mystr), 0, -1)))

def reverseString3(mystr):
	result_str = ""
	for i in xrange(len(mystr), 0, -1):
		result_str += mystr[i-1]
	return result_str	


if __name__ == '__main__':
	
	#Data to be send (to get the string)
	ourdict = {'token': "SqRw7EIYkX"}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)

	#Send it (get the string)
	response = urllib2.urlopen("http://challenge.code2040.org/api/getstring", jdata)
	#get the content
	page_content = response.read()
	#json -> python dict
	ourdict = json.loads(page_content)
	#our string
	mystring = ourdict['result']
	#reverse the string
	#As python is awesome, let's use the most 
	#elegant approach to solve our problem ;))
	result = reverseString1(mystring)

	#wrapping our result in a dictionary
	ourdict = {'token':"SqRw7EIYkX", 'string': result}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)
	#Send it our response
	response = urllib2.urlopen("http://challenge.code2040.org/api/validatestring", jdata)

	page_content = response.read()
	#print the result
	print(page_content)
