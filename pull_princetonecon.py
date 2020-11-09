import re
import html
import urllib.parse
f = open('princetonecon.html')
for line in f:
    m = re.findall(r"mailto:(.+?)\'", line)
    for g in m:
        print(g.replace('&#64;','@'))
        




