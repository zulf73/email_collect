
import re
import requests
from bs4 import BeautifulSoup as soup
from collections import deque

#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)

def get_emails( url ):
	
	#print("Processing %s" % url)
	try:
    		response = requests.get(url)
		new_emails = set(re.findall(r"([a-z0-9\.\-+_]+ at [a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
		return new_emails
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
 		pass
	

f = open('tokyoecon.html')
urls =  deque()
for line in f:
	m = re.findall( r'href="(.+?\.html)"', line, re.MULTILINE)
	for g in m:
		new_url = 'http://www.e.u-tokyo.ac.jp/fservice/faculty/'  + g
		urls.append( new_url)

for q in urls:
    ne = get_emails( q )
    for e in ne:
        f = e.replace(" at ", "@")
        print f





