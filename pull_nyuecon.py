
import re
f = open('nyuecon.html')
for line in f:
	m = re.findall( r'mailto:(.+?)\"', line, re.MULTILINE)
	for g in m:
		print g




