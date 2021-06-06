import re
import requests
import sys
from bs4 import BeautifulSoup as soup
from collections import deque
#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)
headers = { 'User-Agent' : 'Mozilla/5.0'}
def get_emails( url ):
	#print("Processing %s" % url)
    try:
        response = requests.get(url, headers=headers)
        #print(response.text)
        findings = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
        new_emails = set(findings)
        #print(new_emails)
        return new_emails
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
        pass

if __name__ == '__main__':
    list = get_emails( sys.argv[1] )
    for a in list:
        print(a)




