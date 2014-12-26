Code2040APIChallenge
======================
This project hosts sorce codes to solve the Code2040 Challenge. 
For more details, visit http://challenge.code2040.org/

The stages are in separeted files. I solved it using python language 
but, as described in the specification, you can use any language 
to solve it. 

Files:

stage0.py -> In order to use it, you must create a respository on GitHub 
website. After that, you have to paste your new respository URL in the 
dictionary to be send to the endpoint. After execute it, the program 
prints your token (in a dictionary format), which will be your ID 
for the challenge. Save it! You will use it in the next steps. 

stage1.py -> It gets a string from the endpoint, reverses it and send
 to the endpoint. I wrote more than one method to solve it. Indeed, that's
 was one of the reasons I chose python: You have freedom to solve a problem 
 in many ways. Don't forget to use YOUR token!

stage2.py -> It gets a target word (needle) and a list of words (haystack) 
from endpoint. Our mission here is sending the position our needle was found
 to the endpoint.

stage3.py -> It gets a target prefix and a list of words from endpoint. 
Our goal is send a list of words that don't contain the given prefix.

stage4.py -> Maybe it's the most difficult task. The API will give us a dictionary,
which contains a datestamp and an interval. The value for datestamp is a 
string, formatted as an ISO 8601 datestamp. The value for interval is a 
number of seconds. Our goal is to add the interval to the date, then return 
the resulting date to the API.

seegrades.py -> See your grades. (Don't forget to put your token!)
