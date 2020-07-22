
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
		#print(response.text)
		new_emails = set(re.findall(r'mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)\"', response.text, re.I))
		return new_emails
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
 		pass



#urls =  deque()
"""
for line in f:
	m = re.findall( r'facpages/(.+?)"', line, re.MULTILINE)
	for g in m:
		new_url = 'https://www.physics.harvard.edu/people/facpages/'  + g
		urls.append( new_url)
"""
q = 'https://economics.harvard.edu/people'
for page in range(1,30):
	ne = get_emails( q +'?page=' + str(page) )
 	for e in ne:
		print e





