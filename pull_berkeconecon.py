import re
import requests
from bs4 import BeautifulSoup as soup
from collections import deque
#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)

def get_emails( url ):
	#print("Processing %s" % url)
    try:
        response = requests.get( url )
        new_emails = set(re.findall(r"([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
        return new_emails
    except (requests.exceptions.InvalidSchema,requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
        pass
	

f = open('berkecon.html')
urls =  deque()
for line in f:
    m = re.findall( r'href="(.+?)"', line, re.MULTILINE)
    for g in m:
        #print g
        try:
            response = requests.get(g)
            if response.text:
                links = re.findall( r'href="(.+?)"', response.text, re.MULTILINE)
                for h in links:
                    urls.append( h )
        except (requests.exceptions.InvalidSchema,requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
    		pass


for q in urls:
    ne = get_emails( q )
    if ne:
        for e in ne:
            print e





