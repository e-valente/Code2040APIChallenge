#!/usr/bin/python
#Contact: emanuelvalente@gmail.com

import urllib2
import json, sys, re, datetime

#returns an datetime.datetime objet
#notice there is an iso8601 lib to 
#parse it but is not a python offical package		
#so that's why we're using this method
def parseIsoToDateTime(isoDate):

	#where are using some string "hacks" here!
	mystr = isoDate.replace('T', ' ')
	mystr = mystr.replace('Z', ' ')
	mylist = re.split('[-:. ]', mystr)

	#str to int
	#*the last element is garbage
	mylist = [int(i) for i in mylist[:-1]]
	
	return datetime.datetime(*mylist)

if __name__ == '__main__':
	
	#Data to be send (to get our task)
	ourdict = {'token': "SqRw7EIYkX"}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)

	#Send it (get our haystack and needle)
	response = urllib2.urlopen("http://challenge.code2040.org/api/time", jdata)
	#get the content
	page_content = response.read().decode('utf-8')

	#json -> python dict
	ourdict = json.loads(page_content)
	ourdict = ourdict['result']

	#setting our target
	ourisodate = ourdict['datestamp']
	secondstoadd = ourdict['interval']

	#ourdate will be a datetime.datime object
	ourdate = parseIsoToDateTime(ourisodate)

	#yes, we can add seconds -> timedelta(min, secs)
	ourdate += datetime.timedelta(0, secondstoadd)
	
	#our answer
	answer = ourdate.isoformat()
	
	#We will send our answer to the endpoint
	ourdict = {'token': "SqRw7EIYkX", 'datestamp': answer}
	#convert our data in JSON format
	jdata = json.dumps(ourdict)
	#Send it
	response = urllib2.urlopen("http://challenge.code2040.org/api/validatetime", jdata)
	#get the content
	page_content = response.read()
	#print it (response)
	print(page_content)