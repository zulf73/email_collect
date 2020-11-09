import re
import html
import urllib.parse
f = open('torontoecon.html')
for line in f:
    m = re.findall(r"revealDisplay\('(.+?)', '(.+?)'\)", line)
    for g in m:
        print(g[0][::-1] + '@' + g[1][::-1])
        




