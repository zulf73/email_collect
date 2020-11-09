#https://stackoverflow.com/questions/10820351/how-should-i-process-xlink-references-with-lxml-in-python
import io
import lxml.html
from lxml import etree
import requests
from lxml.html.soupparser import fromstring
import imgkit
import pytesseract

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
url = 'https://law.stanford.edu/directory/?tax_and_terms=1067'
response = requests.get( url,  headers=headers)

for k in range(1,5):
    c_url = 'https://law.stanford.edu/directory/?tax_and_terms=1067&page=' + str(k)
    imgkit.from_url( c_url, 'out.jpg')
    print(pytesseract.image_to_string('out.jpg'))


#root = fromstring( response.text )
#penv = root.xpath("//image")

#print(etree.tostring(root))
#for e in penv:
    #print(e)
    #child = e.get("{http://www.w3.org/1999/xlink}href")
#    print(etree.tostring(e))
#    print("###################################")
#    c = etree.parse(child).getroot()
#    parent.replace(e, c)
