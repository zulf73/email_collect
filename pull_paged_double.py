
import re
import requests
#from bs4 import BeautifulSoup as soup
from collections import deque
from lxml import etree
def get_emails( url ):
	
	#print("Processing %s" % url)
    try:
        response = requests.get(url)
        new_emails = set(re.findall(r"mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
        return new_emails
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
        pass
	

def pull_double( url, indiv_prefix, indiv_prefix_end ):
    urls =  deque()
    response = requests.get(url)
    #soup = BeautifulSoup(response, "lxml") # lxml is just the parser for reading the html
    parent = etree.fromstring(response.text)
    m = parent.xpath('//a/@href')
    #m = lxml.html.find_rel_links( root, 'href') # this is the line that does what you want
    #m = re.findall( indiv_prefix_end + '(.+?)"', response.text, re.MULTILINE)
    for g in m:
        print(g)
        new_url = g
        urls.append( new_url)
    for q in urls:
	    ne = get_emails( q )
	    for e in ne:
		    print(e)

url = 'https://law.stanford.edu/directory/?tax_and_terms=1067'
indiv_prefix = 'https://law.stanford.edu/directory/'
indiv_prefix_end = 'directory/'

for page in range(1,5):
    current_url = url + "&page=" + str(page)
    print(current_url)
    pull_double( current_url, indiv_prefix, indiv_prefix_end)



