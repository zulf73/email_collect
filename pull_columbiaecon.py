import re
import html
import urllib.parse
f = open('columbiaecon.html')
for line in f:
    m = re.findall(r"mailto:(.+&#64;.+?)'", line)
    for g in m:
        h=g.replace('&#64;','@')
        print(h)




