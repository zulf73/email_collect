
import re
import requests
from bs4 import BeautifulSoup as soup
from collections import deque
import time

#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)

def get_emails( url ):
	#print("Processing %s" % url)
    try:
        response = requests.get(url)
        new_emails = set(re.findall(r"([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
        return(new_emails)
    except (requests.exceptions.InvalidSchema,requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
        pass
	

url = 'https://economics.ucla.edu/faculty/ladder'
urls =  deque()
response = requests.get(url)
m = re.findall( r'href="(.+?)"', response.text, re.MULTILINE)
for g in m:
    new_url = g
    #print(new_url)
    urls.append( new_url )

for q in urls:
    time.sleep(1)
    ne = get_emails( q )
    if ne:
        for e in ne:
            print(e)





