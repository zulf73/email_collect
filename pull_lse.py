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
		new_emails = set(re.findall(r"mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
		return new_emails
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
 		pass
	

urls =  deque()
for k in range(0,250):
    start_rank = k*10+1
    url_name = 'https://www.lse.ac.uk/People/Search-People?collection=lse-people&query&start_rank=%d' % start_rank
    urls.append( url_name )

for q in urls:
	ne = get_emails( q )
	for e in ne:
		print e





