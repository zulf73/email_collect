
import re
import html
import urllib.parse
f = open('upennecon.html')
for line in f:
    m = re.findall(r"mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", line)
    for g in m:
        print(g)





