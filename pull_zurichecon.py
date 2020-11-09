
import re
import html
import urllib.parse
f = open('zurichecon.html')
for line in f:
    m = re.findall( r'eval\(unescape\((.+?)\)\)', line, re.MULTILINE)
    for g in m:
        #print(g)
        #print(html.unescape(g))
        text = urllib.parse.unquote(g)
        new_email = re.findall(r"mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", text)
        print(new_email[0])





